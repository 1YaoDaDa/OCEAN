# creat function: equal to strip
# the following code not work, how to do that...??
print('请输入您想要从首尾去除的字符或其它参数：')
text = input()
import re
myfun = re.compile(r'text')
print('请输入一行字符串：')
selfString = str(input())
mo = myfun.sub('',selfString)
print(mo)
