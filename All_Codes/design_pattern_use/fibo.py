n1 = 0
n2 = 1
n = 9
count = 0

while count <= n:
    
    print(n1,end=' , ')
    
    nth = n1 + n2
    
    n1 = n2
    n2 = nth
    
    count += 1
