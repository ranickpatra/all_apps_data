import os
import bs4 as bs


with open('content.txt', 'w') as f:
    for f_name in os.listdir('content'):
        for files in os.listdir('content/'+f_name):
            if '.html' in files :
                with open('content/'+f_name+'/'+files, 'r') as html_f:
                    soup = bs.BeautifulSoup(html_f, 'lxml')
                    for temp in soup.findAll('div', 'middle-col'):
                        soup = temp
                    title = ''
                    for temp in soup.findAll("h1"):
                        title = temp.text

                f.write(f_name+'/'+files + '->'+title+'\n')
