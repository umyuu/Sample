# -*- coding: utf-8 -*-
from collections import Counter
score  = Counter()
outs = {'strike': (3, 'out!'), 'ball': (4, 'fourball!')}

for _ in range(int(input())):
    a = input()
    score[a] += 1
    end_count, msg = outs[a]
    if score[a] == end_count:
        print(msg)
        break

    print(a + '!')