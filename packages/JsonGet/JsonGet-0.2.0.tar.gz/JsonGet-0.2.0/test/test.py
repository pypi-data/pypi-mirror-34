from JsonGet import JsonGet as js


test = js.JsonGet()
str = 'aaabbaaa'
res = test.js_substr(str, condition='former', reference='b')
print(res)
