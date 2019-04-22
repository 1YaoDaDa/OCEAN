# 编写一个函数，检查字符串是否匹配模式xxx-xxx-xxxx，x代表0～9数字。返回值为ture和false
# 因为被检查的字符串可能是任意长度，如“my phne num is xx-xxx-xxxx”，这时需要遍历字符串中的内容，依次取12个字符给text，交给定义函数判断.
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
            if text[7] != '-':
                return False
            for i in range(8,11):
                if not text[i].isdecimal():
                    return False
    return True
print('411-444-5424 is a phone number:')
print(isPhoneNumber('411-444-5424'))
print('moshi moshi is a phone number:')
print(isPhoneNumber('moshi moshi'))
message = 'what you say 4120-23-3333,no ,it is 412-023-3333'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number found: ' + chunk)
print('done')
