import sys

def add_result()->None:
    n_=input().split()
    n=int(n_[0])
    vec=[]
    p=[]
    sum=0
    for i in range(n):
        _temp=input().split()
        temp=int(_temp[0])
        sum+=temp
        vec.append(temp)
        p.append(sum)
    while(True):
        data=input().split()
        a,b=int(data[0]),int(data[1])
        if(a!=0):
            print(p[b]-p[a-1])
        else:
            print(p[b])

if __name__ =="__main__":
    add_result()
