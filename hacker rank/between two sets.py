'''
problem link: https://www.hackerrank.com/challenges/between-two-sets/problem

For all those guys like me who found this question difficult to understand, 
here's the simple explanation i got after searching for decades.

1. Find LCM of the first array a. 
2.Find GCD / HCF of the second array b.
3.Find all the multiples of LCM up to GCD, which divides the GCD evenly.

For Example: Here, In the given sample Input, 
The LCM of array a would be 4 and the GCD of the array b would be 16. 
Now, Find all Multiples of 4,(like 4,8,12,16,...) upto 16, such that, 
(16%multiple_of_4_here) should be 0. 
Here, 16%4=0 -----> count=1 (suppose this variable.) 
16%8=0 -----> count=2 
16%12!=0 ---> count=2 
16%16=0 ---> count=3.

Thus, The answer is 3. Hope this helped you.
'''
def getTotalX(a, b):
    # Write your code here
    def gcd(x,y):
        if y==0:
            return x
        else:
            return gcd(y,x%y)
    def lcm(x,y):
        return x*y//gcd(x,y)
    
    #a-->lcm      lca 
    f1=a[0]
    f2=a[1]
    lca=lcm(f1,f2)
    for i in range(2,len(a)):
        lca=lcm(lca,a[i])
    #b ---> gcd   gcb
    gcb=b[0]
    for i in b[1:]:
        gcb=gcd(gcb,i)
    
    mu=lca
    ll=lca
    i=1
    op=[]
    while ll<=gcb:
        ll=mu*i 
        if gcb%ll==0:
            op.append(ll) 
        i+=1
    return len(op)

    
            

first_multiple_input =[2,3] #input().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr =[2,4]  #list(map(int, input().rstrip().split()))
brr =[16,32,96]  #list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)
print(total)