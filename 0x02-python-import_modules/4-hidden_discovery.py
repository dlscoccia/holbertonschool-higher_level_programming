#!/usr/bin/python3
import hidden_4
i = 0
for i in dir(hidden_4):
    if ("__" not in i):
        print(i)
