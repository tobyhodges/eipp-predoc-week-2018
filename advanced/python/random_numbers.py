#! /usr/bin/env python

import random
import sys

for i in range(10000):
    sys.stdout.write(f'{random.randint(-500,500)}\n')
