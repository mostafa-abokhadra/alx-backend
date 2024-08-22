#!/usr/bin/env python3
dic = [{"key1": "keyOne"}]
for dict in dic:
    if "key1" in dict:
        print("in")
print(dic[0]['key1'])
