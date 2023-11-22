# 1.	在谍战影视剧中，经常能看到破解密码的环节，往往需要通过密码本，破译密码。下面请你来设计一个密码本(26个英文字符及常用符号” ”,”.”,”’”)，输入密文，根据密码本破解密文，生成原文。
password_book = {}
for i in range(26):
    letter = chr(ord('a') + i)
    password_book[letter] = chr(ord('z') - i)
password_book[' '] = ' '
password_book["'"] = "'"
password_book['.'] = '.'


def decrypt_message(text, password_book):
    plaintext = ""
    for char in text:
        if char in password_book:
            plaintext += password_book[char]
        else:
            plaintext += char
    return plaintext


print("原文是：", decrypt_message(input("请输入密文："), password_book))
