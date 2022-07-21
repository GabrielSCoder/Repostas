string = input("Digite uma cadeia de caracteres: ")

string = list(string)
string= string[::-1]
rev = ''
for i in string:
    rev += i

print(rev)