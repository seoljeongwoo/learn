S = input()
tag ,result = False, ''
new_string =''
for i in range(len(S)):
    if tag == True:
        result += S[i]
        if S[i] == '>':
            tag = False
    else:
        if S[i] == '<':
            if len(new_string) !=0:
                result += new_string[::-1]
                new_string = ''

            result += S[i]
            tag = True
        elif S[i] == ' ':
            if len(new_string) != 0:
                result += new_string[::-1]
                new_string = ''

            result += S[i]
        else:
            new_string += S[i]
if len(new_string) != 0:
    result += new_string[::-1]
print(result)