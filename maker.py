#!/bin/python3

import os
import re
import markdown2

content_sign = '<!-- contents here --!>'
posts_dir_name = '_content/blog/'
output_posts_dir_name = 'content/blog/'
index_file_name = 'index.html'
layout_file_name = 'style/layout.html'
sections_dir_name = '_content/'
output_sections_dir_name = 'content/'


with open(layout_file_name,'r') as layout_file:
    layout = layout_file.read()
    layout_file.close()
    layout = layout.split(content_sign)

def get_relative_path_up(path):
    return('../' * path.count('/'))

def md_to_html(markdown_post):
    ignored_tags = [ ''.join(['<',i,j,'>']) for i in ['','/']
                            for j in ['center', 'div','h1', 'h2', 'h3', 'h4', 'h5', 'h6'] ]
    ignored_tags.append('<div lang="latex">')

    # achando texto entre --- e ---
    meta_match = re.match(r'^-{3}(.*)-{3}', markdown_post, re.S)
    # retirando quebras de linhas das strings, separando por linhas
    meta_strings = meta_match.groups()[0].splitlines()[1:]
    # separing keys and values
    meta_ = [re.search(':', i,re.S).start() for i in meta_strings]
    meta_ = [(i[:meta_[n]], i[meta_[n]+2:]) for (n,i) in enumerate(meta_strings)]
    # creating dictionary
    meta = dict(meta_)

    post = markdown_post[meta_match.end()+2:].splitlines()
    post = [ '</p>\n<h1>'+i[2:]+'</h1>\n<p>' if (i!='' and i[0]=='#') else i for i in post ]
    post = [ i+'<br>' if all(not(j in i) for j in ignored_tags) else i for i in post ]
    post = '\n'.join(post)
    post = '<div class="inner">\n<p>\n'+post+'\n</p>\n</div>\n\n'
    title = ' '.join([meta['date'],meta['title']])
    title = '<h1 class="bgemph">'+title+'</h1>\n\n'
    return(title+post)

def md_to_html(markdown_post):
    ignored_tags = [ ''.join(['<',i,j,'>']) for i in ['','/']
                            for j in ['center', 'div','h1', 'h2', 'h3', 'h4', 'h5', 'h6'] ]
    ignored_tags.append('<div lang="latex">')

    # achando texto entre --- e ---
    meta_match = re.match(r'^-{3}(.*)-{3}', markdown_post, re.S)
    # retirando quebras de linhas das strings, separando por linhas
    meta_strings = meta_match.groups()[0].splitlines()[1:]
    # separing keys and values
    meta_ = [re.search(':', i,re.S).start() for i in meta_strings]
    meta_ = [(i[:meta_[n]], i[meta_[n]+2:]) for (n,i) in enumerate(meta_strings)]
    # creating dictionary
    meta = dict(meta_)

    post = markdown_post[meta_match.end()+2:].splitlines()
    post = [ '</p>\n<h1>'+i[2:]+'</h1>\n<p>' if (i!='' and i[0]=='#') else i for i in post ]
    post = [ i+'<br>' if all(not(j in i) for j in ignored_tags) else i for i in post ]
    post = '\n'.join(post)
    post = '<div class="inner">\n<p>\n'+post+'\n</p>\n</div>\n\n'
    title = ' '.join([meta['date'],meta['title']])
    title = '<h1 class="bgemph">'+title+'</h1>\n\n'
    return(title+post)

def make_page(content_dir, layout):
    posts = [ md_to_html(open(i).read()) for i in content_dir ]
    posts = [ i.replace('--', '—') for i in posts ]
    index = layout[0]+''.join(posts)+layout[1]
    return(index)


# blog
content_dir_name = posts_dir_name
flat_ls = [ content_dir_name+i for i in os.listdir(content_dir_name) ]
content_dir = [ i for i in flat_ls if os.path.isfile(i) if '.md' in i  ]
content_dir.sort(reverse=True)

_layout = [ i.replace('{relative_path_up}',
                get_relative_path_up(index_file_name))
                for i in layout ]

page_file = open(index_file_name,'w')
page_file.write(make_page(content_dir, _layout))
page_file.close()

# pages
content_dir_name = sections_dir_name

pages = [ i[:-3] for i in os.listdir(content_dir_name)
                if os.path.isfile(content_dir_name+i)
                    if '.md' in i ]
content_dir = [ content_dir_name+i for i in pages ]

_layout = [ i.replace('{relative_path_up}',
                get_relative_path_up(content_dir[0]))
                for i in layout ]

for i, page in enumerate(pages):
    page_file = open(output_sections_dir_name+page+'.html','w')
    page_file.write(make_page([content_dir[i]+'.md'], _layout))
    page_file.close()
