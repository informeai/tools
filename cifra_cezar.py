

def encrypt(texto, hot):
    e = ''
    for t in texto:
        i = ord(t) + hot
        e += chr(i)
    return e

def decrypt(texto, hot):
    e = ''
    for t in texto:
        i = ord(t) - hot
        e += chr(i)
    return e


if __name__ == '__main__':
    e = encrypt('Wellington Salgado Gadelha 27/02/1984', 13)
    print(e)

    d = decrypt('dryyv{t|{-`nytnq|-Tnqryun-?D<=?<>FEA', 13)
    print(d)