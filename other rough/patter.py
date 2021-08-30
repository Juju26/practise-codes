"""
    x
    x x       
x x x x x          5           
    x x
    x

      x
      x x 
      x x x     
x x x x x x x       7
      x x x 
      x x 
      x 
"""
n=4
for i in range(0,n):
    
    if i==n//2:
        for k in range(n):
            print("x",end=" ")
    
    elif i==(n//2)+1 or i==(n//2)-1:
        for j in range(n):
            if j==(n//2) or j==(n//2)+1:
                print("x",end=" ")
            elif j==(n//2):
                print("x")
            else:
                print(" ",end=" ")
    elif i==0 or i==n-1:
        for j in range(n):
            if j==(n//2):
                print("x",end="")
            else:
                print(" ",end=" ")
    print()


