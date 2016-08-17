1 '''
 2 Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
 3
 4 A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
 5
 6 For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
 7
 8 Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
 9
10 Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
11 '''
12
13 from combinatorics import selections
14
15 code = tuple(int(c) for c in open('cipher1.txt').read().split(','))
16
17 def decrypt(code, password):
18     l = len(password)
19     return tuple(c ^ password[i % l] for i, c in enumerate(code))
20
21 def text(code): return ''.join(chr(c) for c in code)
22
23 n = 0
24 for password in selections(tuple((ord(c) for c in list('abcdefghijklmnopqrstuvwxyz'))), 3):
25     c = decrypt(code, password)
26     t = text(c)
27     if t.find(' the ') > 0:
28         print sum(c)
29         break