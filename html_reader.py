from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import logging
import re
import io


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

UNPAIRED_TAGS = ['<br>', '<br />', '<hr>', '<basefont>', '<meta>', '<DOCTYPE>']


import string
printable = set(string.printable)


def html_to_printable(html_str):

    new_str = ''
    for char in html_str:
        if char in printable:
            new_str += char
    return new_str


def get_next_open_tag(string, start_index=0):
    cur_stack = []
    tag_stack = []
    tag_pairs = []
    for i, c in enumerate(string[start_index:]):

        if c == '<':
            cur_stack.append(['<', i])

        elif c == '>':
            start = cur_stack.pop()
            sdex = start[1]
            edex = i + 1
            assert len(cur_stack) == 0, '<> missmatch more < then >'
            tag = string[sdex: edex]
            if tag in UNPAIRED_TAGS:
                logger.info('skipping unpaired tag {}'.format(tag))
                continue

            tag_dat = [tag, (sdex, edex)]

            if '</' in tag:
                open_tag = tag_stack.pop()

                tag_contents = string[open_tag[1][-1]: sdex]
                tag_pairs.append([open_tag, tag_dat, tag_contents])
            else:
                tag_stack.append(tag_dat)
    print("tag_stack", tag_stack)
    assert len(tag_stack) == 0, 'Tag mismatch {}'.format(tag_stack)

    for t in tag_pairs:
        print(t)


class recipe(object):

    def __init__(self):

        self.name = ''
        self.description = ''
        self.children = []
        self.components = []

    def add_recipe(self):
        pass


def extract_tables(fp):
    "Extract the text between table tags"
    with io.open(fp, 'r', encoding='utf8') as f:
        text = f.read()
        text = html_to_printable(text)
    return re.findall(r'<table.*</table>', text, re.DOTALL)


def read_table(table_text):
    headers = re.findall(r'<th(.*)</th>', table_text, re.DOTALL)
    for heading in headers:
        print(heading)

    # logger.debug('headers {}'.format(headers))

    rows = re.findall(r'<tr(.*)</tr>', table_text, re.DOTALL)

    for row in rows:
        # print(row)
        get_next_open_tag(row)
    # logger.debug('rows: {}'.format(rows))



if __name__ == "__main__":

    tables = extract_tables('example.html')
    get_next_open_tag(tables[-1])
    # for table in tables.re:
    #     print(table[:200])

        # read_table(table)
        # break
