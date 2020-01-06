# 20191225-1226
# 取得資料 串接 取代 連續刪除
# len
# Tuple  資料不能變動
# List
# 巢狀列表

#有序可變動列表 List
"""
grades=[12,60,15,70,90]
print(grades)
#print(grades[0]) #取第一個值 12

#概念1 取代 列表值 
#grades[0]=55 #把55放到列表中的第一個位置
#print(grades)

#
grades=[12,60,15,70,90]
print(grades[1:4]) #123 不包含4
#[12,60,15,70]

grades[1:4]=[] #整個刪除 123 的列表
print(grades)
"""
"""
grades=[12,60,15,70,90]
grades=grades+[12,33]
print(grades)

length=len(grades) ##去得列表的長度 5
print(length)

#### 巢狀列表 ####
data=[[3,4,5],[6,7,8]]
print(data[0][0]) #第1層 的 第一個元素 3
print(data[1][0]) #第2層 的 第一個元素 6

data=[3,4,5]
print(data[0:2])

data=[[3,4,5],[6,7,8]]
data[0][0:2]=[5,5,5] 
# 取第一層 第一二個數字 3 4 不包含最後一個數  
# 取代成 [5,5,5] 
print(data[0])

grades=[12,60,15,70,90]
print(grades)
print(grades[1:4])

"""

#有序 不可變動列表 Tuple
#list 格式
list_ex=[3,4,5]
list_ex[0]=5
print(list_ex)

#tuple 格式
tuple_example=(3,4,5)
#tuple_example[0]=5 # 錯誤: Tuple  的資料不可以變動
print(tuple_example)
