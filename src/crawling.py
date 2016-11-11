import requests
import textwrap
import re
from os import listdir, path
from BeautifulSoup import BeautifulSoup

base_url = 'https://leetcode.com'
list_url = '/problemset/algorithms'
root_dir = './temp/'

# Get the problem list
parsed = BeautifulSoup(requests.get(base_url + list_url).content)
table = parsed.find('table', attrs = {'id': 'problemList'})
problems = []
for row in table.findAll('tr'):
    if row.findAll('td'):
        pid = str(row.findAll('td')[1].text)
        pid = (3 - len(pid)) * '0' + pid
        title = str(row.find('a').text)
        url = base_url + str(row.find('a').get('href'))
        problems.append((pid, title, url))

# Get local file list
file_list = {}
for p in filter(lambda x: x.startswith('P-'), listdir(root_dir)):
    pid = re.search('^P-(\d+)-', p).groups()[0]
    file_list[pid] = path.join(root_dir, p)

# Iterate each problem
for pid, title, url in problems:
    try:
        p = BeautifulSoup(requests.get(url).content)
        t = p.find('div', attrs = {'class': 'question-content'})

        # Problem description
        des = ''.join(line.text.encode('ascii', 'ignore') + '\n' for line in \
            t.findAll('p') if line.text).strip(' \n')

        # Wrap text
        des = ''.join(line + '\n' for line in textwrap.wrap(des, 70)).strip('\n')

        # Problem tags
        tags = ''.join(str(tag.text) + ', ' for tag in \
            t.find('span', attrs = {'class': 'hidebutton'}).findAll('a')).strip(', ')

        # Format strings
        string = '\'\'\'\nP-%s - %s\n\n%s\n\nTags: %s\n\'\'\'\n' % (pid, title, des, tags)

        # Write to file
        if pid in file_list:
            with open(file_list[pid], 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(string + '\n' + content)
            print 'Problem #%s Processed' % pid
        else:
            print 'Problem #%s Not Exist' % pid

    except:
        print 'Problem #%s Skipped' % pid
