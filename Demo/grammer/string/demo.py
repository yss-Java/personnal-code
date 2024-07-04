import re
# a="abc123+-*"
# b=re.findall('abc',a)
# print(b)

s = "a123456b"
rule = "a[0-9][1-6][1-6][1-6][1-6][1-6]b"	#这里暂时先用这种麻烦点的方法，后面有更容易的，不用敲这么多[1-6]
l = re.findall(rule,s)
print(l)
s = "abcabcaccaac"
rule = "a[a,b,c]c"  # rule = "a[a-z0-9][a-z0-9][a-z0-9][a-z0-9]c"
l = re.findall(rule, s)
print(l)
print(re.findall("caa[a，^]", "caa^bcabcaabc"))
print(re.findall("caa[^,a]", "caa^bcabcaabc"))
print(re.findall("^abca", "abcabcabc"))
print(re.findall("abc$", "accabcabc"))
print(re.findall("c\d\d\da", "abc123abc"))
print(re.findall("\^abc", "^abc^abc"))
print(re.findall("\s\s", "a     c"))
print(re.findall("\w\w\w", "abc12_"))
print(re.findall("\w{2}", "abc12_"))
print(re.findall("010-\d*", "010-123456789"))
print(re.findall("010-\d+", "010-123456789"))
print(re.findall(".", "010\n?!"))
print(re.findall("010-\d?", "010-123456789"))
print(re.findall("010-\d*", "010-123456789"))
print(re.findall("010-\d*?", "010-123456789"))
print(re.findall("010-\d{3,5}", "010-123456789"))
print(re.findall("010-\d{3,5}?", "010-123456789"))

