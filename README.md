Date Parser
===========

This is a simple program written for the contest Coding for Grub held on Nov. 18. For details about the contest refer to https://github.com/davejagoda/CodingForGrub. My program outputs most of the answer in the wrong format but it still got the second prize....

This program uses Python's built-in function dateutil.parser.parse which takes a string and try to parse it into a datetime object. It enumerates over all possible substrings so it is a relatively slow program.

The program which generates the final result is "new.py". "parser.py" uses bing translate api to handle language problem but the final data is only in English (lol).
