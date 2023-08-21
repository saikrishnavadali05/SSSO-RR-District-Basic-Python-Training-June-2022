#import multiply

s=input()
if(s[0]=='a'):
    l=s[4:len(s)].split(",")
    l=[int(x) for x in l]
if(s[0]=='m'):
    l=s[9:len(s)].split(",")
    l=[int(x) for x in l]
for i in l:
    if(i%2!=0):
        l.remove(i)
if len(l)<4:
    print("Given input size is less than 4")
    quit()
if(l==[]):
    print("No even numbers in input")
    quit()
if(s[0]=='m'):
    from multiply import mul
    mul(l)
else:
    from add import ad
    ad(l)





