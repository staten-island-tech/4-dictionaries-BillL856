def lang(x):
    t=0
    s=0
    for char in x:
        if char== "t" or char=="T":
            t+=1
        elif char== "s" or char=="S":
            s+=1
    if t>s:
        print("english")
    else:
        print("french")
lang("I like to eat apple")

def spaces(n,y,t):
    both=0
    for i in range(n):
        if (y[i]=="C" and t[i]=="C"):
            both+=1
    return both
print(spaces(5, "CCC..", "C.C.C"))

def MC(n,s,a):
    correct=0
    for i in range(n):
        if s[i]==a[i]:
            correct+=1

""" def pw(x):
    upper=0
    lower=0
    digits=0
    if len(x)>6 and len(X)<12:
        for char in x:
            if char.isdigit():
                lower+=1
        if upper>3 and lower>2 and digits>1:
 """
            
def wizard(o,n,duels):
    owner=o
    number_of_owners=1
    for i in range(n):
        if duels[1][i]:
            if duels[1]==owner:
                owner=duels[0]
                number_of_owners+=1