#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello Python!')
print('2020-07-29')
msg = "明月几时有"
print(msg.decode('utf-8'))


s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
# error code
# name = input('please enter your name: ')
# print('hello,', name)

arr = ['aaa', 'bbb', 'ccc']
arr.insert(3, 'ddd')  # 插入元素
for i in xrange(0, len(arr)):
    print(arr[i])

arr.pop(3)  # 删除元素

for i in arr:
    print(i)

print(arr)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print("sum:", sum)

print(list(range(5)))
info = "偶数"
print(info.decode('utf-8'))
for i in xrange(0, len(list(range(10)))):
    if i % 2 == 0:
        print(i)

tup = ('aaa', 'bbb', '123', '456', ['ccc', '789'], 'ddd')
print(tup)
print(len(tup))
for i in xrange(0, len(tup)):
    if len(tup[i]) == 2:
        for j in xrange(0, len(tup[i])):
            print(tup[i][j])
    else:
        print(tup[i])

# 0--99
n = 0
while n < 100:
    print(n)

    n = n + 1
