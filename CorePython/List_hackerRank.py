n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        print(cmd)
        eval("l."+cmd)
    else:
        print(l)
