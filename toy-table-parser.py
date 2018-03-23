from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import re
import io


class vertex(object):

    def __init__(self, value):

        self.name = name
        self.children = []

    def add_child(self, child):

        assert isinstance(self, child), 'child is not a vertex!'

        child.root = self
        self.children.append(child)

    def



def extract_tables(fp):
    "Extract the text between table tags"
    with io.open(fp, 'r', encoding='utf8') as f:

        text = f.read()

        text = text.encode('utf8', 'ignore')
    tables = re.findall(r'<table(.*)</table>', text, re.DOTALL)
    # print('tables', tables)
    print(type(tables))
    for i in tables:
        print(i)


def extract_rows(table_text):




if __name__ == "__main__":

    extract_tables('example.html')
