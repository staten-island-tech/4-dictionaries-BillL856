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

def spaces(y,t):
    cc = 0
    postion=[]
    for i in range (len(y)):
        if y[i]=="C" and t[i]=="C":
            cc+=1
            postion.append(i)
    
spaces("CCC..",".C.C.")