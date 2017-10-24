phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_list = plist[1:3]

print(new_list.extend([plist[5], plist[4], plist[7], plist[6]]))

new_phrase = ''.join(new_list)

print(plist)
print(new_phrase)
