"""
Name: Yan Duan
Email: dementrock@gmail.com
"""

import sys
import urllib
from urllib import urlencode, urlopen
import re
from datetime import datetime
from dateutil.parser import parse
from time import sleep


def parse_end(content):
    for index in range(len(content) - 1, -1, -1):
        if content[index] != ' ':
            return content[:index + 1]
    return ''

def parse_beginning(content):
    for index in range(0, len(content)):
        if content[index] != ' ':
            return content[index:]
    return ''

def parse_date(content):
    if content.endswith('00:00:00'):
        return content[:-9]
    return content



def try_result(content, start, length, word_list):
    partial_sentence = ' '.join(word_list[start:start+length])
    result = partial_sentence
    if result.startswith('on') \
    or result.startswith('at') \
    or result.startswith('in') \
    or result.startswith('until'):
        return None
    try:
        date = parse(result)
        first_word = word_list[start]
        last_word = word_list[start+length-1]
        start_pos = content.find(first_word)
        end_pos = content.find(last_word) + len(last_word)
        return parse_end(content[:start_pos]) + '|' + parse_date(str(date)) + '|' + parse_beginning(content[end_pos:])
    except Exception as e:
        return None

def parsedate(content):

    word_list = re.split('[ !\?\(\)\[\]]', content)
    word_list = [w for w in word_list if w]
    
    for length in range(len(word_list), 0, -1):
        for start in range(0, len(word_list) - length + 1):
            result = try_result(content, start, length, word_list)
            if result:
                return result

def main():
    try:
        file_name = sys.argv[1]
    except Exception:
        file_name = 'datesentences.txt'
    file_content = open(file_name).read().split('\n')
    for content in file_content:
        if content:
            try:
                print parsedate(content)
            except Exception:
                print None

if __name__ == '__main__':
    main()
