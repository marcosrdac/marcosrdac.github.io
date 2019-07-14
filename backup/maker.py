#!/bin/python3

from os import listdir, mkdir
from os.path import exists, isdir, relpath, dirname, join, splitext
import re
import markdown2


# definitions
basic_layout_file_path  = 'style/basic_layout.html'

content_sign = '<!-- content here --!>'
relpath_sign = '<!-- relative path --!>'

index_file_path = 'index.html'

_content_dir_path = '_content'
content_dir_path  = 'content'


# function definitions
def md_to_html(mdt, path='#top'):
    html = markdown2.markdown(mdt, extras=['metadata', 'break-on-newline'])
    meta = html.metadata

    html = str(html)

    title = ''.join(['<a id=\'post_title\' href="', path, '">'])
    if 'date' in meta.keys():  title = "".join([title, meta['date'], ' - '])
    if 'title' in meta.keys(): title = "".join([title, meta['title']])
    title = "".join([title, '</a>'])

    html = "\n".join([title, '<div class="inner">\n', html, '\n\n</div>\n\n'])
    return(html)

def make_page(content, page_path, _split_layout):
    split_layout = [ layout_half.replace(relpath_sign,
                                         relpath('.', dirname(page_path)))
                            for layout_half in _split_layout ]
    print(split_layout[0])
    page = ''.join([split_layout[0],
                    content,
                    split_layout[1]])
    return(page)

def get_directory__posts(_page_dir, page_dir='', autoref=False):
    _posts = {}
    for _post_file_name in listdir(_page_dir):
        _post_file_path = join(_page_dir, _post_file_name)
        post_file_name = ''.join([splitext(_post_file_name)[0], '.html'])
        post_file_path = join(page_dir, post_file_name)
        with open(_post_file_path, 'r') as _post_file:
            _post = _post_file.read()
            _posts[_post_file_name] = _post
            _post_file.close()
    return(_posts)

def get_directory_posts(_page_dir, page_dir='', autoref=False):
    posts = {}
    for _post_file_name in listdir(_page_dir):
        _post_file_path = join(_page_dir, _post_file_name)
        post_file_name = ''.join([splitext(_post_file_name)[0], '.html'])
        post_file_path = join(page_dir, post_file_name)
        with open(_post_file_path, 'r') as _post_file:
            _post = _post_file.read()
            if autoref:
                posts[_post_file_name] = md_to_html(_post, '#post_title')
            else:
                posts[_post_file_name] = md_to_html(_post, post_file_path)
            _post_file.close()
    return(posts)

def make_page_from_posts(posts, page_path, _split_layout=['','']):
    '''
    makes an html page from
    '''
    content = '\n'.join([ posts[post] for post in sorted(posts, reverse=True) ])

    page = make_page(content, page_path, _split_layout)
    return(page)


if not exists(content_dir_path):
    mkdir(content_dir_path)

with open(basic_layout_file_path,'r') as layout_file:
    _split_layout  = layout_file.read().split(content_sign) # list
    layout_file.close()


for subpath in listdir(_content_dir_path):
    _path = join(_content_dir_path, subpath)
    path  = join(content_dir_path,  subpath)

    if isdir(_path):
        _dir_path = _path
        dir_path = path
        page_path = 'index.html'

        _posts = get_directory_posts(_dir_path, dir_path)
        posts = get_directory_posts(_dir_path, dir_path)

        page = make_page_from_posts(posts, page_path, _split_layout)

        page_file = open(page_path,'w')
        page_file.write(page)
        page_file.close()

        if not exists(path):
            mkdir(path)


        posts = get_directory_posts(_dir_path, dir_path, autoref=True)

        for post_file_name in posts.keys():
            post_file_path = join(relpath('.'),
                                  join(dir_path,''.join([splitext(post_file_name)[0],
                                                         '.html'])))
            page = make_page(posts[post_file_name], post_file_path, _split_layout)

            page_file = open(post_file_path,'w')
            page_file.write(page)
            page_file.close()
