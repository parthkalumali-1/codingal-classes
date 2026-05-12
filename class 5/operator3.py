#Is / Is Not
print("------x--------")
x = 10
print(x, type(x))
print(id(x))

y = 20
print("------y--------")
print(y, type(y))
print(id(y))

print(x is y)

# Member in, Not in
name = 'Parth'
print('a' in name)
print('z' in name)

list1 = [1, 12, 23, 95, 36, 71]
print(1 in list1)
print(999 in list1)

print(1 not in list1)
print(999 not in list1)

# 10 ---> 1010
# 2 ---> 10
# 3 ---> 11
# A ----> 65 --->

# bitwise operation: &, |, ~
# 1 & 1 --> 1
# 1 & 0 --> 0
# 0 & 1 --> 0
# 0 & 0 --> 0

print(5 & 3)
print(5 | 3)
print(2 | 3)
print(8 << 2)