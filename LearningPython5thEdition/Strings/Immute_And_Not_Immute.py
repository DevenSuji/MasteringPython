# S = 'shrubbery'
# L = list(S) # Expand to a list
# print(L)
# L[1] = 'c' # Change it in place
# L[2] = 'n' # Change it in place
# print(''.join(L)) # Join with empty delimiter

B = bytearray(b'spam')
print(B.decode())
B.extend(b'eggs')
print(B.decode())

dir(B.decode())

s = 'spam'
dir(s)