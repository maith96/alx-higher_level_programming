#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len = len(sys.argv)
    if len < 2:
        print('0 argument.', end = '\n')
    else:
        print('{} arguments:'.format(len - 1))
        for i in range(1, (len)):
            print('{}: {}'.format(i, sys.argv[i]))
