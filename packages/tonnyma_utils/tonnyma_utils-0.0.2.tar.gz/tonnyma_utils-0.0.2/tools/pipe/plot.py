#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pandas as pd
from matplotlib import pyplot as plt
if __name__ == '__main__':
    if not sys.stdin.isatty():
        # print ''.join(sys.stdin.read())
        s = sys.stdin
        df = pd.read_csv(s)
        df.plot()
        # plt.title(sys.argv[1])
        plt.show()

    else:
        print sys.argv[1:]
