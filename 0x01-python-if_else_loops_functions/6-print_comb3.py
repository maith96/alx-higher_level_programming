#!/usr/bin/python3
print(', '.join(f'{i}{j}' for i in range(0, 10) for j in range(0,10) if j > i and j != i))
           