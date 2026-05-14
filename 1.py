#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit(0)

    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    print(sum(arr))
