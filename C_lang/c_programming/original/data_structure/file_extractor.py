import os
import shutil
import bs4 as bs

file_names = []
src = 'content/'
dest = 'modified/'
image_url = 'https://raw.githubusercontent.com/ranickpatra/all_apps_data/master/C_lang/ds/modified/images'


h_cont = '''
<!DOCTYPE html>
<html>

<head>
  <title>Introduction to C</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">


  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>

  <script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"></script>


  <link rel="stylesheet" href="../style/style1.css">
  <link rel="stylesheet" href="../style/style2.css">


</head>

<body>

  <div class="container">

'''

f_cont = '''

  </div>

</body>

</html>


'''


with open('content_f_maps.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        file_names.append(line.split('#'))


def check_for_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


for files in file_names:
    check_for_dir(dest+files[0])
    print(files[1])
    images = []
    with open(src+files[0]+'/'+files[1], 'r') as f:
        soup = bs.BeautifulSoup(f,'lxml')
        for body_cnt in soup.findAll('div', 'middle-col'):
            soup = body_cnt
        for temp in soup.findAll('div', 'pre-btn'):
            temp.decompose()
        for temp in soup.findAll('div', 'nxt-btn'):
            temp.decompose()
        for temp in soup.findAll('div', 'topgooglead'):
            temp.decompose()
        for temp in soup.findAll('div', 'clearer'):
            temp.decompose()
        for temp in soup.findAll('div', 'print-btn'):
            temp.decompose()


        for img in soup.findAll('img'):
            images.append(img['src'].replace('./', ''))




        soup = str(soup)
        replace_what = './'+files[1].replace('.html', '_files')
        soup = soup.replace(replace_what, image_url)
        with open(dest+files[0]+'/'+files[1], 'w') as f1:
            f1.write(h_cont+soup+f_cont)

        for img in images:
            shutil.copy(src+files[0]+'/'+img, dest+'images')




    #break
