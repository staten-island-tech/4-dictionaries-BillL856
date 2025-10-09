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