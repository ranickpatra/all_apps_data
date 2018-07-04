import json
import re

files_lst = {}


def create_db(super_class, file_name, host):
    files_lst[super_class] = {}
    with open(file_name, 'r') as f:
        last = ''
        for line in f.readlines():
            line = line.replace('\n', '')

            if line[0] == '#':
                files_lst[super_class][line[1:]] = []
                last = line[1:]
                continue

            line = line.split('->')
            files_lst[super_class][last].append({'url':host + line[0].replace(' ', '%20').replace('&', '%26'), 'title':line[1]})



def create_db_ds(super_class, file_name, host):
    files_lst[super_class] = {}
    with open(file_name, 'r') as f:
        last = ''
        for line in f.readlines():
            line = line.replace('\n', '')
            if not line.split('/')[0] in files_lst[super_class]:
                files_lst[super_class][line.split('/')[0]] = []
            line = re.split('/|->', line)
            files_lst[super_class][line[0]].append({'url':host+line[0].replace(' ', '%20').replace('&', '%26')+'/'+line[1].replace(' ', '%20').replace('&', '%26'), 'title':line[2]})




create_db(super_class='advance', file_name='advance.txt', host='https://raw.githubusercontent.com/ranickpatra/all_apps_data/master/C_lang/modified/')
create_db(super_class='basic', file_name='basic.txt', host='https://raw.githubusercontent.com/ranickpatra/all_apps_data/master/C_lang/modified/')
create_db(super_class='example', file_name='example.txt', host='https://raw.githubusercontent.com/ranickpatra/all_apps_data/master/C_lang/modified/')
create_db_ds(super_class='ds', file_name='content_ds.txt', host='https://raw.githubusercontent.com/ranickpatra/all_apps_data/master/C_lang/ds/modified/')

with open('database.json', 'w') as f:
    f.write(json.dumps(files_lst, sort_keys=True, indent=4))
    #f.write(json.dumps(files_lst))
