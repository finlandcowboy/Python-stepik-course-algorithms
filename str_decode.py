text = input()
a = list(text)
letters = []
for letter in a:
    if letter not in letters:
        letters.append(letter)


coded_let = []
code = '0'
for i in range(len(letters)):
    if len(letters) == 1:
        coded_let.append(code)
        break
    if i == len(letters)-1:
        code = code[:-1]
        
        coded_let.append(code)
    code = '1' + code
    
    
dec_str =""
for i in a:
    if i in letters:
        dec_str = dec_str + str(coded_let[letters.index(i)])


print(len(letters),len(dec_str))

for k in range(len(letters)):
    print(letters[k],": ",coded_let[k],sep='')
    
print(dec_str)
    
