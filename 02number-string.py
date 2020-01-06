#搭配教學網址
#https://youtu.be/bLRa4TZ99aY
"""
# 數字運算
#
x=3+6
print(x)
x=2**6 # 次方
print(x)
x=6%2 # 除數
print(x)

x=2+3
print(x) #5
#方法1
#x=x+1  # x=x+1 將變數中的數字+1
#print(x) #6
#方法2
x+=1    # x=x+1 將變數中的數字+1
print(x)
"""
##字串運算
# s="Hell\"o" #\跳脫 #雙引號就可以在字串中被顯示
# Hell"o
#print(s)

"""
s="Hello"+"word" #字串 串接
print(s)
#Helloword

s="Hello" "word" #空白 字串
print(s)
#Helloword
"""
#表達很多行的字
"""
s="Hello\nword" #\n 代表換行
print(s)
#Hello
#word
"""
#寫多行文字
#s="""Hello
#Word""" #三個雙引號 python特殊用法 代表換行
#print(s)
#

# 乘法 顯示多個 Hello
#s="Hello"*3+"World"
#print(s)
#HelloHelloHelloWorld

#字串的字元編號 從 0 1 2 3 4 
#s="Hello"
#print(s[0]) #得到第一個字串 得到H
#print(s[2]) #得到第3個字串 得到L

#s="Hello"
#print(s[1:4]) #得到2 3 4個字串 ell  包含開頭，不包含結尾

#只給開頭 忽略結尾
s="Hello"
print(s[1:]) #取得1 後面所有的東西#忽略結尾


#只給結尾
s="Hello"
print(s[:4]) #不要結尾的前面所有字
