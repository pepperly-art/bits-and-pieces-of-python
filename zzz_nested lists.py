# that one successful thing that took me 3 days
# I'm saving this for posterity
# because I hate lists!
# oh my god

strings = ['abcqwe', 'def', 'ghiq']
new_strings =[]

longest_word = max(strings, key=len) # abcqwe

for word in range(len(strings)): # counts 0, 1, 2
#    print(f"{word} - {strings[word]}")
    new_word = strings[word]
    while len(new_word) < len(longest_word):
        new_word = new_word + ' '
#    print(new_word)
    new_strings.append(new_word)

#print(new_strings)

for k in range(len(longest_word)): # k = 0-5
#    print(f"{k} is k")
    chara = ''
    for i in range(len(new_strings)): # i = 0-2
        chara = chara + new_strings[i][k]
    print(chara)

# ==== failed attempts === #

# len(l)) = 6
#for i in range(len(strings)):
#    charas = ''
#    m = len(l) - 1
#    while len(strings[i]) < m:
#        strings[i] = strings[i] + ' '
#    for k in range(len(strings[i])):
#        print(strings[k][i])
#    print(charas)

#for i in range(len(l)):
#    charas = ""
#    while len(strings[i]) < len(l):
#        string[i] = string[i] + " "
#    for k in range(len(strings[i])):
#        charas = charas + strings[k][i]
#    print(charas)
    