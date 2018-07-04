import os
import bs4 as bs


fname = []

for f_name in os.listdir('modified'):
    if '.html' in f_name :
        fname.append(f_name)


for f_name in fname:
    with open('modified/'+f_name) as f:
        soup = bs.BeautifulSoup(f, "lxml")

        title = ""
        for tt in soup.findAll('h2', 'page_title'):
            title = tt.text

        with open('content.txt', 'a') as f1:
            f1.writelines(f_name+"->"+title+"\n")
