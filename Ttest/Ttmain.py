j = 0
print('Hello')
I = float('10.1')
S = 'tino'
print(I+1)
S = S.replace('in', 'onono')
print(S)
while j != -1:
    j = S.find('o')
    S = S[:j] + '!' + S[(j+1):]
    j = S.find('o')
print(S)
