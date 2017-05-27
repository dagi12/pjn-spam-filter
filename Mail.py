#!/usr/bin/python3.5
import re
from string import punctuation


# 0 temat
# 1 nadawca
# 2 odbiorca
# 3 data
# 5 treść


class Mail:
    title = ""
    sender = ""
    receiver = ""
    content = ""
    is_junk = False
    is_junk_predicted = False
    word_count = 0
    sign_count = 0

    def __init__(self, row, is_junk=False):
        self.title = row[0]
        self.sender = row[1]
        self.receiver = row[2]
        self.content = row[5]
        self.sign_count = len(row[5])
        self.word_count = len(re.compile(r'[{}]'.format(punctuation)).sub(' ', self.content).split())
        self.is_junk = is_junk
