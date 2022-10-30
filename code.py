f1 = open('input.txt')
n = f1.read()
f1.close()
r = []
r = n.split()
a = int(r[0]) // 10
b = int(r[0]) % 10
f2 = open('output.txt','w')
f2.write(f"{a} {b}")
f2.close()
