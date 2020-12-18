s = "sasr_aaoowrztextaaaaeztezyuuiiduoi"
nl=[]
v = ['a','A','e','E','i','I','o','O','u','U']
for i in range(len(s)-1):
    if s[i] in v:
        if s[i-1] in v or s[i+1] in v:
            nl.append(s[i])
            if s[i+1] not in v:
                print(" ".join(nl))
                nl=[]