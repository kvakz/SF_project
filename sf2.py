def f_read(f):
    t = open(f,'r',encoding='utf-8')
    s=''
    for j in t:
        s+=j
    return s
        
def freq(s):
    c = ''
    for i in range(128):
        c+=chr(i)
    c += 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ—«»…'
    x=[]
    for i in c:
        if i in s:
            x.append([i,s.count(i)])
    x.sort(key=lambda x:x[1], reverse = True)
    return x


def sf(z, p):
    sl = 0
    sr = 0
    i = 0
    t = len(z)
    x = []
    y = []

    if len(z) == 1:
        d[z[0][0]] = p
    else:
        sl += z[0][1]
        x = [z[0]]
        t -= 1
        while t != 0:
            while sl >= sr and t > 0:
                i += 1
                sr += z[i][1]
                y += [z[i]]
                t -= 1
            while sr >= sl and t > 0:
                i += 1
                sl += z[i][1]
                x += [z[i]]
                t -= 1
        sf(x, p + '0')
        sf(y, p + '1')

def coding(d,q):
    s=''
    for i in range(len(q)):
        s+=d[q[i]]
    t = len(s)%8
    s+='0'*((8-t)%8)
    L = ''
    for i in range(0,len(s)-7,8):
        L+=chr(int(s[i:i+8],2))
    return L

def decoding(d2,L,o):
    s = ''
    for c in L:
        t=bin(ord(c))[2:]
        t='0'*((8-len(t)%8)%8)+t
        s+=t
    i=j=0
    p = ''
    while o>0:
        k=d2.get(s[j:i+1])
        if k != None:
            o-=1
            p+=k
            j=i+1
        i+=1
    return p

def writingtof(d2,o,L):
    with open('resultdic.txt','w',encoding='utf-8') as file1:
        file1.write('Количество символов в исходном тексте: '+ str(o) +'\n'+'Словарь для раскодирования: '+ str(d2))
    with open('resultSF.txt','w',encoding='utf-8') as file2:
        file2.write('Полученный результат кодирования:'+'\n'+L)


q = f_read('text.txt')
o = len(q)
z = freq(q)
d = {}
sf(z,'')
d2 = dict(zip(d.values(),d.keys()))
L = coding(d,q)
print(L)
p = decoding(d2,L,o)
print(p)
writingtof(d2,o,L)
