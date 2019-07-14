#!/bin/python3

from os import listdir, mkdir
from os.path import exists, isfile, isdir, relpath, dirname, join, splitext
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
    html = markdown2.markdown(mdt, extras=['metadata', 'break-on-newline',
                                           'smarty-pants','cuddled-lists',
                                           'numbering', 'footnotes',
                                           'fenced-code-blocks',
                                           'wiki-tables'])
    # more extras:
    # https://github.com/trentm/python-markdown2/wiki/Extras

    meta = html.metadata

    html = str(html)

    title = ''.join(['<a id=\'post_title\' href="', path, '">'])
    if 'date' in meta.keys():  title = "".join([title, meta['date'], ' - '])
    if 'title' in meta.keys(): title = "".join([title, meta['title']])
    title = "".join([title, '</a>'])

    html = "\n".join([title, '<div class="inner">\n', html, '\n\n</div>\n\n'])
    return(html)

def make_page(content, page_file_path, _split_layout):
    root_relpath = join(relpath('.', dirname(page_file_path)),'')
    if root_relpath == './':
        root_relpath = ''
    split_layout = [ layout_half.replace(relpath_sign, root_relpath)
                            for layout_half in _split_layout ]
    page = ''.join([split_layout[0],
                    content,
                    split_layout[1]])
    return(page)

def make_page_from_posts(posts, page_file_path, _split_layout=['','']):
    '''
    makes an html page from
    '''
    content = '\n'.join([ posts[post] for post in sorted(posts, reverse=True) ])

    page = make_page(content, page_file_path, _split_layout)
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
        dir_path  =  path
        page_file_path = ''.join([dir_path,'.html'])
        page_file_path = 'index.html'

        if not exists(path):
            mkdir(path)

        posts = {}
        for _post_file_name in listdir(_dir_path):
            _post_file_path = join(_dir_path, _post_file_name)
            post_file_name = ''.join([splitext(_post_file_name)[0], '.html'])
            post_file_path = join(dir_path, post_file_name)

            with open(_post_file_path, 'r') as _post_file:
                _post = _post_file.read()
                post  = md_to_html(_post, post_file_path)
                posts[post_file_name] = post
                _post_file.close()

            with open(post_file_path,'w') as post_page_file:
                post = md_to_html(_post, post_file_name)
                post_page = make_page(post, post_file_path, _split_layout)
                post_page_file.write(post_page)
                post_page_file.close()

        with open(page_file_path, 'w') as page_file:
            page = make_page_from_posts(posts, page_file_path, _split_layout)
            page_file.write(page)
            page_file.close()

    elif isfile(_path):
        _page_file_path = _path
        page_file_name  = ''.join([splitext(subpath)[0], '.html'])
        page_file_path  = join(content_dir_path, page_file_name)

        with open(_page_file_path, 'r') as _page_file:
            _page = _page_file.read()
            page  = md_to_html(_page, page_file_name)
            _page_file.close()

        with open(page_file_path, 'w') as page_file:
            page = make_page(page, page_file_path, _split_layout)
            page_file.write(page)
            page_file.close()
