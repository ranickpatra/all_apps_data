import os


with open('content_f_maps.txt', 'w') as f:
    for f_name in os.listdir('content'):
        for files in os.listdir('content/'+f_name):
            if '.html' in files :
                f.write(f_name+'#'+files + '\n')
