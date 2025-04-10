def buy()->None:
    #初始化矩阵
    nums=input().split()
    n,m=int(nums[0]),int(nums[1])
    matrix=[]
    sums=0
    for i in range(n):
        temp=input().split()
        for j in range(m):
            temp[j]=int(temp[j])
        sums+=sum(temp)
        matrix.append(temp)

    horizontal=[0]*n#求行的前缀和
    for i in range(n):
        horizontal[i]=sum(matrix[i])
    vertical=[0]*m #求列的前缀和
    for j in range(m):
        for i in range(n):
            vertical[j]+=matrix[i][j]
    #依次划分行列，比较最小区分
    result = float('inf')
    subhorizon=0
    for i in range(n):
        subhorizon+=horizontal[i]
        result=min(result,abs(sums-subhorizon-subhorizon))
    subvertical=0
    for i in range(m):
        subvertical+=vertical[i]
        result=min(result,abs(sums-subvertical-subvertical))
    result=int(result)
    print(result)

if __name__ == "__main__":
    buy()

        
        
    
    
