# -*- coding: utf-8 -*-

import json
import os
import sys

import requests

def abort(msg):
    print 'Error!: {0}'.format(msg)
    sys.exit(1)

def ustr2filename(ustr):
    """ Windows で有効なファイル名に変換する. """

    ret = ustr

    # ファイル名として使えない文字を除外.
    invalid_chars = u'\\/:*?"<>|'
    for invalid_char in invalid_chars:
        ret = ret.replace(invalid_char, u'')

    # ターミナルのエンコーディングでエンコード.
    ret = ret.encode(sys.stdout.encoding)

    return ret

def get(url, params, headers):
    r = requests.get(url, params=params, proxies=proxies, headers=headers)
    return r

def post(url, data_dict, headers_dict):
    r = requests.post(url, data=json.dumps(data_dict),
                      proxies=proxies, headers=headers_dict)
    return r

def print_response(r, title=''):
    c = r.status_code
    h = r.headers
    print '{0} Response={1}, Detail={2}'.format(title, c, h)

def assert_response(r, title=''):
    c = r.status_code
    h = r.headers
    if c<200 or c>299:
        abort('{0} Response={1}, Detail={2}'.format(title, c, h))

class Article:
    def __init__(self, d):
        self._title      = d['title']
        self._html_body  = d['rendered_body']
        self._md_body    = d['body']
        self._tags       = d['tags']
        self._created_at = d['created_at']
        self._updated_at = d['updated_at']
        self._url        = d['url']

        user = d['user']
        self._userid   = user['id']
        self._username = user['name']

    def save_as_markdown(self):

        title = ustr2filename(self._title)
        body  = self._md_body.encode('utf8')

        filename = '{0}.md'.format(title)
        fullpath = os.path.join(MYDIR, filename)
        with open(fullpath, 'w') as f:
            f.write(body)

    def list2file(filepath, ls):
        with open(filepath, 'w') as f:
            f.writelines(['%s\n' % line for line in ls] )

MYDIR = os.path.abspath(os.path.dirname(__file__))

proxies = {
    "http": os.getenv('HTTP_PROXY'),
    "https": os.getenv('HTTPS_PROXY'),
}
token = os.getenv('QIITA_ACCESS_TOKEN')
headers = {
    'content-type'  : 'application/json',
    'charset'       : 'utf-8',
    'Authorization' : 'Bearer {0}'.format(token)
}

# 認証ユーザの投稿一覧
url = 'https://qiita.com/api/v2/authenticated_user/items'
params = {
    'page'     : 1,
    'per_page' : 100,
}
r = get(url, params, headers)
assert_response(r)
print_response(r)

items = r.json()
print '{0} entries.'.format(len(items))
for i,item in enumerate(items):
    print '[{0}/{1}] saving...'.format(i+1, len(items))
    article = Article(item)
    article.save_as_markdown()
