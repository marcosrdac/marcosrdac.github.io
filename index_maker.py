import os
import itertools

signal_text = 'FILL BODY'

layout_file = open('layout.html','r')
layout = layout_file.readlines()
layout_file.close()

posts_start = [n for n,l in enumerate(layout) if signal_text in l][0]

posts_dir = 'posts'
files_list = os.listdir(posts_dir)
files_list.sort()
files_list = files_list[::-1]
files_list = [posts_dir+'/'+i for i in files_list]
posts = [open(i).readlines()+['  ','  <br>'] for i in files_list]

html_page = []
html_page += [i for i in layout[:posts_start]]
html_page += [i for i in itertools.chain.from_iterable(posts)]
html_page += [i for i in layout[posts_start+1:]]

page = open('index.html','w')
page.writelines(html_page)
