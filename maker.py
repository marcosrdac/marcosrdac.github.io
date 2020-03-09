#!/usr/bin/env python
# Program: Site compiler
# Author:  Marcos Reinan de Assis Conceição (@marcosrdac)
# GitHub:  marcosrdac
# E-mail:  marcosrdac+site@gmail.com
#
# How to use it:
#   put this inside a directory
#   create a "_content" folder to put markdown contents:
#     - pure page as an only file;
#     - blog-like page as a folder of markdown posts.
#   these posts may have titles and dates, you can do that by preceding the
#     markdown code with
#       ---
#       date:  07/22/2019
#       title: Your post/page title here
#       type:  post
#       ---
#     where type is something experimental. Obs.: metadata is not mandatory.
#   create an HTML layout with root references given by "<!-- root path --!>"
#     and "<!-- content here --!>" as the place to put page contents.
#   create a CSS file that uses a#logo and a#post_title as logo text and
#     title post text.
#   put those files in "style" folder.
#   all these structures I'm talking about are already made in my site example:
#     https://github.com/marcosrdac/marcosrdac.github.io
# then, just run this file

from os import listdir, mkdir
from os.path import exists, isfile, isdir, relpath, dirname, join, splitext
import re
import markdown2


# definitions
basic_layout_file_path  = 'style/basic_layout.html' # Basic layout used

content_sign = '<!-- content here --!>'  # HTML sign to put contents
relpath_sign = '<!-- root path --!>'     # HTML sign for root path

index_page_name = 'blog'            # page chosen to be main

_content_dir_path = '_content'           # input markdown folder
content_dir_path  = 'content'            # output HTML folder

pics_dir_path = 'pictures'


# function definitions
def md_to_html(mdt, path='#top', root_relpath=None):
    '''
    Creates HTML text from markdown text. HTML title is an a#post_title.
    '''
    if not root_relpath:
        root_relpath=''

    # modify pictures postition
    pics_relpath = join(root_relpath, pics_dir_path)
    mdt = re.sub('\!\[(.*)\]\((.*)\)',
                 ''.join([r'![\1](',
                           pics_relpath,
                          r'/\2)']),
                 mdt)

    html = markdown2.markdown(mdt, extras=['metadata',
                                           #'break-on-newline',
                                           'smarty-pants',
                                           'numbering',
                                           'tables',
                                           'footnotes',
                                           'fenced-code-blocks',
                                           'wiki-tables'])
    # more extras:
    # https://github.com/trentm/python-markdown2/wiki/Extras

    meta = html.metadata
    if 'type' in meta.keys():
        if meta['type'] in ['poem', 'poetry']:
            html = markdown2.markdown(mdt, extras=['metadata',
                                                   'break-on-newline',
                                                   'smarty-pants',
                                                   'numbering',
                                                   'footnotes',
                                                   'fenced-code-blocks',
                                                   'wiki-tables'])


    html = str(html)

    title = ''.join(['<a id=\'post_title\' href="', path, '">'])
    if 'date' in meta.keys():  title = "".join([title, meta['date'], ' - '])
    if 'title' in meta.keys(): title = "".join([title, meta['title']])
    title = ''.join([title, '</a>'])
    html  = '\n'.join([title, '<div class="inner">\n', html, '\n\n</div>\n\n'])

    if 'draft' in  meta.keys():
        if meta['draft'] in ['true', 'True', 'yes']:
            html = ''
    return(html)


def make_page(content, page_file_path, _split_layout):
    '''
    Given HTML marked content (1 - content), a layout (3 - _split_layout) and a
    place (2 - page_file_path), this function creates an entire HTML page for
    the content, in order for it to be put at page_file_path.
    '''
    root_relpath = join(relpath('.', dirname(page_file_path)),'')
    if root_relpath == './':
        root_relpath = ''
    split_layout = [ layout_half.replace(relpath_sign, root_relpath)
                            for layout_half in _split_layout ]
    page = ''.join([split_layout[0],
                    content,
                    split_layout[1]])
    return(page)


def make_page_from_posts(posts, page_file_path="", _split_layout=['','']):
    '''
    Given HTML marked content posts as a dictionary (1 - posts), a layout
    (3 - _split_layout) and a place (2 - page_file_path), this function creates
    an entire HTML page for the the concatenated posts, in order for it to be put at
    page_file_path.
    '''
    content = '\n'.join([ posts[post] for post in sorted(posts, reverse=True) ])

    page = make_page(content, page_file_path, _split_layout)
    return(page)


# creates content_dir_path if it does not exist
if not exists(content_dir_path):
    mkdir(content_dir_path)

# opens basic layout file
# one day it will be more general
with open(basic_layout_file_path,'r') as layout_file:
    _split_layout  = layout_file.read().split(content_sign) # list
    layout_file.close()

# creates contents:
for subpath in listdir(_content_dir_path):  # subpath is a path inside _content
    _path = join(_content_dir_path, subpath)  # path in _content from root
    path  = join(content_dir_path,  subpath)  # path in content  from root

    # if path in _content is directory
    # then we are going to create a page for every post in this directory,
    # a main page to contain all of the posts and its remake to serve as index
    # page, if this path was chosen to be the index (it is defined at the top
    # of this code)
    if isdir(_path):
        _dir_path = _path  # just changing names for me to think faster
        dir_path  =  path  # just changing names for me to think faster
        page_file_path = ''.join([dir_path,'.html'])  # main page full path

        # if path does not exist in contents_dir
        if not exists(path):
            mkdir(path)  # create it

        _posts = {}  # markdown posts
        for _post_file_name in listdir(_dir_path):
            # other post variables
            _post_file_path = join(_dir_path, _post_file_name)
            post_file_name = ''.join([splitext(_post_file_name)[0], '.html'])
            post_file_path = join(dir_path, post_file_name)
            root_relpath = join(relpath('.', dirname(post_file_path)),'')
            if root_relpath == './':
                root_relpath = ''

            # reading and saving markdown posts into _posts as a dictionary
            with open(_post_file_path, 'r') as _post_file:
                _post = _post_file.read()
                _posts[post_file_name] = _post
                _post_file.close()

            # creating individual post pages
            with open(post_file_path, 'w') as post_page_file:
                post = md_to_html(_post, post_file_name, root_relpath)  # name: inside fold.
                post_page = make_page(post, post_file_path, _split_layout)
                post_page_file.write(post_page)
                post_page_file.close()

        # creating main posts page
        with open(page_file_path, 'w') as page_file:
            posts = {}
            for _post_file_name in _posts.keys():
                post_file_subpath     = join(subpath,
                                             ''.join([splitext(_post_file_name)[0],'.html']) )
                posts[_post_file_name] = md_to_html(_posts[_post_file_name],
                                                    post_file_subpath,
                                                    root_relpath)

            page = make_page_from_posts(posts, page_file_path, _split_layout)
            page_file.write(page)
            page_file.close()

        # generating index if directory is set to be the index file
        if splitext(subpath)[0] == index_page_name:
            for _post_file_name in _posts.keys():    # just like above
                post_file_path     = join(dir_path, _post_file_name)
                posts[_post_file_name] = md_to_html(_posts[_post_file_name],
                                                           post_file_path)
            page = make_page_from_posts(posts, 'index.html', _split_layout)


    # else, if we are not talking about a directory
    elif isfile(_path):
        _page_file_path = _path
        page_file_name  = ''.join([splitext(subpath)[0], '.html'])
        page_file_path  = join(content_dir_path, page_file_name)
        root_relpath = join(relpath('.', dirname(page_file_path)),'')
        if root_relpath == './':
            root_relpath = ''

        # read page's markdown content
        with open(_page_file_path, 'r') as _page_file:
            _page = _page_file.read()
            _page_file.close()

        # create and save page into content folder
        with open(page_file_path, 'w') as page_file:
            page = md_to_html(_page, page_file_name, root_relpath)
            page = make_page(page, page_file_path, _split_layout)
            page_file.write(page)
            page_file.close()

        # generating index if page is set to be the index file
        if splitext(subpath)[0] == index_page_name:
            page  = md_to_html(_page, page_file_path)
            page = make_page(page, 'index.html', _split_layout)

    # saving index page created in one of both last cases
    if splitext(subpath)[0] == index_page_name:
        with open('index.html', 'w') as page_file:
            page_file.write(page)
            page_file.close()
