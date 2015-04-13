import requests
import re
import ast
from os import listdir, path
from BeautifulSoup import BeautifulSoup

base_url = 'https://leetcode.com'
list_url = '/problemset/algorithms'
src_dir = '../src/'
root_dir = '.'

# Get the tag list
tag_list = []
parsed = BeautifulSoup(requests.get(base_url + list_url).content)
for item in parsed.findAll('a', attrs = {'class': 'list-group-item'}):
    if item.get('href').startswith('/tag'):
        title = item.findChild('small').text.encode('ascii', 'ignore').strip()
        url = base_url + str(item.get('href'))
        tag_list.append((title, url))

# Get local file list
file_list = {}
for p in filter(lambda x: x.startswith('P-'), listdir(src_dir)):
    pid = re.search('^P-(\d+)-', p).groups()[0]
    file_list[pid] = path.join(src_dir, p)

# Iterate the tag list
# For each tag, create a MD file and add all the problems under this tag
data_re = re.compile('data: (.*),\n  \}\);\n', re.DOTALL | re.MULTILINE)
title_re = re.compile('>(.*)</a>')

with open('Table-by-tag.md', 'w') as t:
    t.write('# Leet-Code Problems\n')
    for title, tag_url in sorted(tag_list, key = lambda x: x[0]):
        fname = title.replace(' ', '-') + '.md'
        t.write('- ### [%s](./%s)\n' % (title, fname))
        with open(fname, 'w') as f:
            f.write('# %s\n' % (title, ))
            html = requests.get(tag_url).content
            plist = ast.literal_eval(data_re.search(html).group(1))
            for p in sorted(plist, key = lambda x:int(x['id'])):
                pid = (3 - len(p['id'])) * '0' + p['id']
                title = title_re.search(p['title']).group(1)
                url = file_list[pid] if pid in file_list else ''
                md_str = '- %s [%s](%s)\n' % (pid, title, url)
                f.write(md_str)
