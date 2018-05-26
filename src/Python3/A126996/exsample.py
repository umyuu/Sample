# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
text = u'すもももももももものうち'
tokenizer = Tokenizer(mmap=True)
token_filters = [POSKeepFilter('名詞'), TokenCountFilter(att='base_form')]
a = Analyzer(tokenizer=tokenizer, token_filters = token_filters)
for k, v in a.analyze(text):
    print('%s: %d' % (k, v))


