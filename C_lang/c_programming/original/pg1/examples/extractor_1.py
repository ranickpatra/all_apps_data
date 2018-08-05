import bs4 as bs
import shutil
import os

image_url = 'https://raw.githubusercontent.com/ranickpatra/all_apps_data/master/C_lang/modified/images'

hd = '''
<!DOCTYPE html>
<html>

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">


  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>

  <script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>


  <link rel="stylesheet" href="./style/style1.css">
  <link rel="stylesheet" href="./style/style2.css">


</head>

<body>

  <div class="container">
'''

fd = '''
  </div>
</body>
</html>
'''

src = 'examples/'
dest = 'modified/'

file_list = []
image_path_lst = []

with open('content_fnames.txt', 'r') as f:
    for l in f.readlines():
        l = l.strip()
        file_list.append(l)


for f_name in  file_list:

    print(f_name)

    with open(src + f_name, 'r') as f:
        soup = bs.BeautifulSoup(f, "lxml")


    cont = None
    for main_content in soup.findAll('section', 'main-content'):
        for _ in main_content.findAll('h1'):
            title = _.text
            _.decompose()

        for _ in main_content.findAll('div', 'page-short-description'):
            desc = _.text
            _.decompose()

        for _ in main_content.findAll('div', 'content-bottom'):
            _.decompose()

        for _ in main_content.findAll('div', {"class":"content"}):
            _.decompose()
            break

        for _ in main_content.findAll('iframe'):
            _.decompose()

        for img in main_content.findAll('img'):
            image_path_lst.append(img['src'].replace('./', src))

        for a in main_content.findAll('a'):
            a.replaceWithChildren()

        cont = main_content

    with open('modified/'+f_name, 'w') as f:
        cont = str(cont)
        replace_what = './'+f_name.replace('.html', '_files')
        cont = cont.replace(replace_what, image_url)
        f.write(hd + '<h2 class="page_title"><strong>' + title + '</strong></h2><br><p>' + desc + '</p><br>' + cont + fd)

    #break


if not os.path.exists('modified/images/'):
    os.makedirs('modified/images/')


for g in image_path_lst:
    f_name = g[g.rindex('/')+1:]
    shutil.copy(g, 'modified/images/'+f_name)
