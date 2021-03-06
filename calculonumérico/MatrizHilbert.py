import numpy as np

n=18
H=np.zeros((n,n))

for i in range(n):
  for j in range(n):
    H[i,j]=1/(i+j+1)

print(H)

x=np.array([1]*n)
print(x)

b=H@x
print(b)

x_sol=np.linalg.solve(H,b)
print(x_sol)

np.linalg.norm(x-x_sol)/np.linalg.norm(x)

d=len(H) 
for s in range (0, d-1):
  for t in range (s+1,d):
    m = H[t][s]/H[s][s]
    
    for j in range (s+1,d):
      H[t][j]=H[t][j]-(m*H[s][j])
    b[t]=(-m)*b[s]+b[t]
    H[t][s]=0


print(H)
b=H@x
print(b)
x_sol = np.linalg.solve(H, b)
print(x_sol)

def pivoteacao(s, H, b):
  d=len(H)
  elemento = H[s][s]
  linhadoelemento=s
  for p in range (s+1, d):
    if abs(H[p][s]) > abs(elemento):
      elemento = H[p][s]
      linhadoelemento = p
  
  if s == linhadoelemento:
    troca = False
  else:
    a=H[s]
    b=H[linhadoelemento]
    H[s]=b
    H[linhadoelemento]=a 
    c=b[s]
    e=b[linhadoelemento]
    b[linhadoelemento]=c
    b[s]=e
    troca = True
  return troca

d=len(H)
for s in range (0, d-1):
  for t in range (s+1,d):
    pivoteacao
    m = H[t][s]/H[s][s]
    print(H)
    
    for j in range (s+1,d):
      H[t][j]=H[t][j]-(m*H[s][j])
    b[t]=b[t]-(m)*b[s]
    H[t][s]=0

print(H)
b=H@x
print(b)
x_sol = np.linalg.solve(H, b)
print(x_sol)