def convert(letters):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    plain = []
    index = -1
    for ch in letters:
        for i in range(len(alphabet)):
            if ch == alphabet[i]:
                plain.append(i)
    return plain

def deconvert(num):
    deconv = ""
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

    for i in range(len(num)):
        for r in range(len(alphabet)):
            if num[i] == r:
                deconv = deconv + (alphabet[r])

    return deconv

def moduloN(a,N):
    if a < N:
        ans = a
    else:
        ans = a%N
    return ans

def cipher(plain,b,a):
    p = convert(plain)
    b = moduloN(b,26)
    c = ''

    for i in range(len(p)):
        c = c + str(a*p[i] + b)

    return c

def decipher(cipher,b,a):
    p = []
    
    for i in range(len(cipher)):
        p.append((cipher[i] - moduloN(b,26))/a)

    return deconvert(p)
    
        

def password(text):
    c = cipher(text,4940394,25)
    if c == "445479129":
        return True
    else:
        return False
        
    
    
print(decipher(cipher("asdf",346,25),346,25))
##ciph = cipher("asdf", 4940394, 25)
##print(ciph)
##deciph = decipher(ciph,4940394,25)
##print(deciph)

#print(password("asdf"))
