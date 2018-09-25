import os
import itertools


content_sign = '<content_here>'
posts_dir_name = 'content/blog'
index_file_name = 'index.html'
page_file_name = 'models/_page.html'
sections = ['contact', 'about']
sections_dir_name = 'models'


def make_page(content_lines, page, contents_start):
    content = []
    content += [i for i in page[:contents_start]]
    content += [i for i in content_lines]
    content += [i for i in page[contents_start+1:]]
    return(content)


page_file = open(page_file_name,'r')
page = page_file.readlines()
page_file.close()

contents_start = [n for (n,l) in enumerate(page) if content_sign in l][0]

posts_dir = os.listdir(posts_dir_name)
posts_dir.sort()
posts_dir = posts_dir[::-1]
posts = [posts_dir_name+'/'+i for i in posts_dir]
posts = [['<div class=post>']+open(i).readlines()+['</div>'] for i in posts]
posts = [i for i in itertools.chain.from_iterable(posts)]
posts = [i.replace('--','—') for i in posts]


index_file = open(index_file_name,'w')
index_file.writelines(make_page(posts,
                                page,
                                contents_start))

for section in sections:
    section_file = open(sections_dir_name+'/_'+(section+'.html' if not('.html' in section)
                                             else section),'r')
    section_lines = section_file.readlines()
    section_lines = [i.replace('--','—') for i in section_lines]
    section_file.close()

    section_file_name = section+'.html'
    section_file = open(section_file_name,'w')
    section_file.writelines(make_page(section_lines,
                                      page,
                                      contents_start))
    section_file.close()
