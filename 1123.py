# Python Assignment #5 

# 과제 32
set1 = {1, 3, 5, 7, 9}
set2 = {3, 5, 7, 9, 11}
print("합집합: ", set1.union(set2))
print("교집합: ", set1.intersection(set2))

# 33
set1 = {2, 4, 6, 8, 10}
set2 = {4, 6, 8, 10, 12}
print("차집합: ", set1.difference(set2))
print("대칭차집합: ", set1.symmetric_difference(set2))

# 34
fav_num = {3, 5, 7, 9, 11}
fav_num.update({100})
print(fav_num)

# 35
a = {100, 200, 300, 400, 500}
b = {400, 500, 600, 700, 800}

intersection_result = a & b
print("교집합:", intersection_result)

difference_result = a - b
print("차집합:", difference_result)

symmetric_difference_result = a ^ b
print("대칭차집합:", symmetric_difference_result)

# (35 연습)
# x = a.copy()
# x.intersection_update(b)
# print("intersection_update:", x)

# y = a.copy()
# y.difference_update(b)
# print("difference_update:", y)

# z = a.copy()
# z.symmetric_difference_update(b)
# print("symmetric_difference_update:", z)

# 36
a = {100, 200, 300, 400, 500}
b = {100, 200, 300, 400, 500}
if a.issuperset(b):
    print("상위")
if a.issubset(b):
    print("부분")
if a == b:
    print("동시")

# 37
fav_num = {1, 3, 5, 7, 9}
fav_num.add(1000)
fav_num.pop()
print(fav_num)

# 38
multiples = {x for x in range(1, 101) if (x % 3 == 0 and x % 5 == 0)}
print(multiples)