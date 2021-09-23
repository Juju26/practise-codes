#length of line
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())

re=float((((x2-x1)**2)+((y2-y1)**2))**0.5)
print('%.2f',re)