def SpeakWhatYouSee(n):
    n = str(n)
    le = len(n)
    c = 0
    a = 0
    i = 0
    s =''
    v =[]
    while i !=le:
        if c>1 and i in (i-1,i-1+a):
            continue
        c = 0
        for j in range(i,le):
            if n[i] == n[j]:
                c += 1 
                a +=1
            if j != le-1 and n[i] != n[j+1]:
                s =s+str(c)+n[i]
                break  
            if j == le-1:
                s = s+str(c)+n[i]
                break
        i += a
        a = 0
    return s


def callfun(m,l):
    arr = []
    w = m
    while l!=0:
        m = w
        w = SpeakWhatYouSee(m)
        arr.append(w)
        l -= 1
    return arr
print(callfun(1,7))