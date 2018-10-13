f=open("train.json","r")
g=f.read()
print(type(g))
import ast
x=ast.literal_eval(g)
# y=str(x["anger"])
y=str(x["boredom"])#do this for all categories
y=y[1:-1]
sent=y.split(",")
ch="\""
for s in sent:
    #print(s[1],s[-1])
    if s[1]=="\'":
        s=s[2:]
    if s[-1]=="\'":
        s=s[:-1]
    if s[1]!=ch:
        
        s=ch+s
    if s[-1]!=ch:
        s=s+ch
    
    print("training_data.append({\"class\":\"boredom\", \"sentence\":"+s+"})")
