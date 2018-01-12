# set
some_list = ['1', '1', 'a', 'da', 'da', 1, 54, 21]
# 1. 使用set获取重复的数据
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# 2. 交集 ：intersection
valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown','blue'}

print(input_set.intersection(valid))
# 3. 差集
print(input_set.difference(valid))
