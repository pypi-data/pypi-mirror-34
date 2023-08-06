# -*- coding: utf-8 -*-

# Copyright (c) 2014-2017 CoNWeT Lab., Universidad Politécnica de Madrid

# This file is part of CKAN BAE Publisher Extension.

# CKAN BAE Publisher Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN BAE Publisher Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN BAE Publisher Extension.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import base64
import ckan.lib.base as base
import ckan.lib.helpers as helpers
import ckan.model as model
import ckan.plugins as plugins
import logging
import os
import requests

from ckanext.baepublisher.store_connector import StoreConnector, StoreException
from ckan.common import request
from pylons import config

log = logging.getLogger(__name__)

__dir__ = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(__dir__, '../assets/logo-ckan.png')
VERIFY_SSL = not bool(os.environ.get('OAUTHLIB_INSECURE_TRANSPORT'))

with open(filepath, 'rb') as f:
    LOGO_CKAN_B64 = base64.b64encode(f.read())


class PublishControllerUI(base.BaseController):

    def __init__(self, name=None):
        self._store_connector = StoreConnector(config)
        self.store_url = self._store_connector.store_url

    def _sort_categories(self, categories):
        list_of_categories = []
        cat_relatives = {}
        categories_sorted = sorted(categories, key=lambda x: int(x['id']))
        if not len(categories_sorted):
            return list_of_categories, cat_relatives
        list_of_categories.append(categories_sorted[0])
        cat_relatives[categories_sorted[0]['id']] = {'href': categories_sorted[0]['href'],
                                                     'id': categories_sorted[0]['id']}
        categories_sorted.pop(0)

        # Im sorry for this double loop, ill try to optimize this
        for tag in categories_sorted:
            if tag['isRoot']:
                list_of_categories.append(tag)
                cat_relatives[tag['id']] = {'href': tag['href'],
                                            'id': tag['id']}
                continue
            for item in list_of_categories:
                if tag['parentId'] == item['id']:
                    list_of_categories.insert(list_of_categories.index(item) + 1, tag)
                    cat_relatives[tag['id']] = {'href': tag['href'],
                                                'id': tag['id'],
                                                'parentId': tag.get('parentId', '')}
                    break
        return list_of_categories, cat_relatives

    # This function is intended to make get requests to the api
    def _get_content(self, content):
        c = plugins.toolkit.c
        filters = {
            'lifecycleStatus': 'Launched'
        }
        if content == 'catalog':
            filters['relatedParty.id'] = c.user
        response = requests.get(
            '{0}/DSProductCatalog/api/catalogManagement/v2/{1}'.format(
                self.store_url, content), params=filters, verify=VERIFY_SSL)
        # Checking that the request finished successfully
        try:
            response.raise_for_status()
        except Exception:
            log.warn('{} couldnt be loaded'.format(content))
            c.errors['{}'.format(
                content)] = ['{} couldnt be loaded'.format(content)]
        return response.json()

    def publish(self, id, offering_info=None, errors=None):

        c = plugins.toolkit.c
        tk = plugins.toolkit
        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'auth_user_obj': c.userobj,
                   }

        # Check that the user is able to update the dataset.
        # Otherwise, he/she won't be able to publish the offering
        try:
            tk.check_access('package_update', context, {'id': id})
        except tk.NotAuthorized:
            log.warn(
                'User %s not authorized to publish %s in the FIWARE Store' % (
                    c.user, id))
            tk.abort(
                401, tk._('User %s not authorized to publish %s') % (
                    c.user, id))

        # Get the dataset and set template variables
        # It's assumed that the user can view a package if he/she can update it

        dataset = tk.get_action('package_show')(context, {'id': id})
        c.pkg_dict = dataset
        c.errors = {}

        self._list_of_categories, self._cat_relatives = self._sort_categories(self._get_content('category'))
        self._list_of_catalogs = self._get_content('catalog')

        # Get categories in the expected format of the form select field
        def _getList(param):
            requiredFields = ['id', 'name']
            result = []
            for i in param:
                result.append({x: i[x] for x in requiredFields})
            for elem in result:
                elem['text'] = elem.pop('name')
                elem['value'] = elem.pop('id')
            return result

        c.offering = {
            'categories': _getList(self._list_of_categories),
            'catalogs': _getList(self._list_of_catalogs)
        }
        # when the data is provided
        if request.POST:
            offering_info = {
                'pkg_id': request.POST.get('pkg_id', ''),
                'name': request.POST.get('name', ''),
                'description': request.POST.get('description', ''),
                'version': self._store_connector.validate_version(request.POST.get('version', '')),
                'is_open': 'open' in request.POST,
                'license_title': request.POST.get('license_title', ''),
                'license_description': request.POST.get('license_description', ''),
                'role': request.POST.get('role', '')
            }
            categories = request.POST.getall('categories')
            tempList = []

            # Insert all parents in the set until there are no more new parents
            for cat in categories:
                tempList.append(self._cat_relatives[cat])
                tempCat = self._cat_relatives[cat]
                while 'parentId' in tempCat and tempCat['parentId']:
                    tempList.append(self._cat_relatives[tempCat['parentId']])
                    tempCat = self._cat_relatives[tempCat['parentId']]

            for cat in tempList:
                if 'parentId' in cat:
                    del cat['parentId']

            tempList = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in tempList)]
            offering_info['categories'] = tempList

            offering_info['catalog'] = request.POST.get('catalogs')
            # Read image
            # 'image_upload' == '' if the user has not set a file
            image_field = request.POST.get('image_upload', '')

            if image_field != '':
                offering_info['image_base64'] = base64.b64encode(
                    image_field.file.read())
            else:
                offering_info['image_base64'] = LOGO_CKAN_B64

            # Convert price into float (it's given as string)
            price = request.POST.get('price', '')
            if price == '':
                offering_info['price'] = 0.0
            else:
                try:
                    offering_info['price'] = float(price)
                except Exception:
                    offering_info['price'] = price
                    log.warn('%r is not a valid price' % price)
                    c.errors['Price'] = ['"%s" is not a valid number' % price]

            # Set offering. In this way, we recover the values introduced previosly
            # and the user does not have to introduce them again
            c.offering = offering_info
            # Check that all the required fields are provided
            required_fields = ['pkg_id', 'name', 'version']
            for field in required_fields:
                if not offering_info[field]:
                    log.warn('Field %r was not provided' % field)
                    c.errors[field.capitalize()] = ['This field is required to publish the offering']

            # Private datasets cannot be offered as open offerings
            if dataset['private'] is True and offering_info['is_open']:
                log.warn(
                    'User tried to create an open offering for a private dataset')
                c.errors['Open'] = ['Private Datasets cannot be offered as Open Offerings']

            # Public datasets cannot be offered with price
            if ('price' in offering_info and dataset['private'] is False and
                    offering_info['price'] != 0.0 and 'Price' not in c.errors):
                log.warn(
                    'User tried to create a paid offering for a public dataset')
                c.errors['Price'] = ['You cannot set a price to a dataset that is public since everyone can access it']
            if not c.errors:
                try:
                    offering_url = self._store_connector.create_offering(
                        dataset, offering_info)
                    helpers.flash_success(
                        tk._(
                            'Offering <a href="%s" target="_blank">%s</a> published correctly.' % (
                                offering_url, offering_info['name'])),
                        allow_html=True)

                    # FIX: When a redirection is performed, the success message is not shown
                    # response.status_int = 302
                    # response.location = '/dataset/%s' % id
                except StoreException as e:
                    c.errors['Store'] = [e.message]
            else:
                c.offering['catalogs'] = _getList(self._list_of_catalogs)
                c.offering['categories'] = _getList(self._list_of_categories)
        return tk.render('package/publish.html')
