import os


with open('content_fnames.txt', 'w') as f:
    for f_name in os.listdir('examples'):
        if '.html' in f_name :
            f.write(f_name + '\n')
