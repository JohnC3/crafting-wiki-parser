from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import re


def extract_tables(fp):
    "Extract the text between table tags"
    with open(fp, 'rb') as f:

        text = f.read()
        print(text[:44])
        text = text.decode()
    tables = re.findall(r'<table(.*)</table>', text, re.DOTALL)
    # print('tables', tables)
    print(type(tables))
    for i in tables:
        print(i)



if __name__ == "__main__":

    extract_tables('example.html')
