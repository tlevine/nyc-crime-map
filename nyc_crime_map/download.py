#!/usr/bin/env python3
import logging

import vlermv
import requests

logger = logging.getLogger(__name__)
DIR = os.path.expanduser('~/.nyc-crime-map')
@vlermv.archive(parent_directory = DIR)
def page(table_id, select, pageToken = None):
    '''
    Args: A pageToken or None
    Returns: The next pageToken or None
    '''
    r = table_features(table_id, select)

@vlermv.archive(parent_directory = DIR)
def table_features_tailpage(table_id, select, pageToken):
    return _table_features(table_id, select, pageToken)

@vlermv.archive(parent_directory = DIR)
def table_features_firstpage(table_id, select):
    return _table_features(table_id, select, None)

def _table_features(table_id, select, pageToken, where = None, maxResults = 1000,
                    KEY = 'AIzaSyDW3Wvk6xWLlLI6Bfu29DuDaseX-g18_mo'):
    url = 'https://www.googleapis.com/mapsengine/v1/tables/%s/features/' % table_id

    params = {
        'key': KEY,
        'version': 'published',
        'maxResults': maxResults,
        'select': select,
    }
    if where:
        params['where'] = where
    if pageToken:
        params['pageToken'] = pageToken

    headers = {
        'User-Agent': 'http://thomaslevine.com/!/nyc-crime-map/',
        'Referer':  'http://maps.nyc.gov/crime/',
    }
    return requests.get(url, headers = headers, params = params)
