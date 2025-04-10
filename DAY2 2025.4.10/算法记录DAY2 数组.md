# 算法记录|DAY2 数组

## 209.长度最小的子数组

### 滑动窗口解法

```python
#209.长度最小的子数组 滑动窗口
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result=float('inf')
        sum,left=0,0
        for right in range(len(nums)):
            sum+=nums[right]
            while(sum>=target):
                Sublen=right-left+1
                result = Sublen if Sublen<result else result
                sum-=nums[left]
                left+=1
        result = result if result != float('inf') else 0
        return int(result)
```

* 通过右指针先移动，左指针跟进，时间复杂度为O（n）
* 本质是满足了单调性，即左右指针只会往一个方向走不会回头，收缩本质去掉不需要的元素
* 滑动窗口有负数时无法成功，此时无论收缩还是扩张，里面的值可能增大或减小，不像之前收缩一定变小
* 和双指针不同，双指针最多只把数组遍历一遍，会漏掉很多情况

### 暴力解法

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result=float('inf')
        size=len(nums)
        for left in range(size):
            sum=0
            for right in range(left,size):
                sum+=nums[right]
                if(sum>=target):
                    Sublen=right-left+1
                    result = Sublen if Sublen<result else result
                    break
        result = result if result != float('inf') else 0
        return int(result)
```

时间复杂度为O（n^2）,超时无法通过案例

## 59.螺旋矩阵

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for _ in range(n)] #待填n*n矩阵
        loop=n//2
        offset=1
        count=1
        startx,starty=0,0
        while(loop):
            loop-=1
            i,j=startx,starty
            while(j<n-offset):
                matrix[i][j]=count
                count+=1
                j+=1
            while(i<n-offset):
                matrix[i][j]=count
                count+=1
                i+=1
            while(j>starty):
                matrix[i][j]=count
                count+=1
                j-=1
            while(i>startx):
                matrix[i][j]=count
                count+=1
                i-=1
            offset+=1
            startx+=1
            starty+=1
        if(n%2):
            matrix[n//2][n//2]=n*n
        return matrix
        
```

###明确循环不变量

* 回忆二分查找，遵循循环不变量原则，明确各个编辑条件在各个循环中的变化
* 如此时所有都满足左闭右开区间

## 58.区间和

```python
def add_result()->None:
    n=int(input())
    p=[]
    sum=0
    for i in range(n):
        temp=int(input())
        sum+=temp
        p.append(sum)
    while(True):
        try:
            data=input().split()
        except:
            break
        a,b=int(data[0]),int(data[1])
        if(a!=0):
            print(p[b]-p[a-1])
        else:
            print(p[b])

if __name__ =="__main__":
    add_result()
```

在写这部分时，一开始没有写`try...except..`导致程序死循环，无法通过测试样例

### 构建前缀和数组

以空间换时间，使得时间复杂度由暴力求解的O（m*n）降低到O（1）(构建前缀和数组的时间为O（n）)

## 44.开发商购买土地

```python
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
```

将方向行和方向列的和求出来，利用上题区间和的思想，再以O（n+m),得到最优划分（单构建前缀和需要O（mn）时间），已经优于O（n^3）

## 知识补充

### 1.Python内置函数 map(),filter(),reduce()

* `map(function,iterable1,iterable2,...)`：以iterable参数列表中每一个元素作为参数，调用function。并返回function 函数返回值列表（其实返回的时一个迭代器，需要list()转化为列表）。常与lambda匿名函数一同使用

  ```python
  >>> def square(x) :         # 计算平方数
  ...     return x ** 2
  ... 
  >>> map(square, [1,2,3,4,5])    # 计算列表各个元素的平方
  <map object at 0x100d3d550>     # 返回迭代器
  >>> list(map(square, [1,2,3,4,5]))   # 使用 list() 转换为列表
  [1, 4, 9, 16, 25]
  >>> list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   # 使用 lambda 匿名函数
  [1, 4, 9, 16, 25]
  >>>
  ```

* `filter(function,iterable)`：接受两个参数，第一个为函数，第二个为列表，将列表每个元素放入函数中判断，返回Trur or False,最后将返回True的元素放在新列表中。返回值为一个迭代器对象

  ```python
  #!/usr/bin/python3
   
  import math
  def is_sqr(x):
      return math.sqrt(x) % 1 == 0
   
  tmplist = filter(is_sqr, range(1, 101))
  newlist = list(tmplist)
  print(newlist)
  ```

  过滤出1到100中平方根是整数的数

* `reduce(function, iterable)`,先将数据集合1、2个元素进行操作，得到的结果再与第三个元素用function运算。返回值为函数计算结果

  * 例如

    ```python
    #!/usr/bin/python
    from functools import reduce
    
    def add(x, y) :            # 两数相加
        return x + y
    sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
    sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
    print(sum1)
    print(sum2)
    ```

    结果都是15

  * **注意：**Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：

    ```
    from functools import reduce
    ```

###2.Python中的迭代器与生成器

1. 迭代器

   1. 两种基本方法，`iter()`和`next()`

      * `iter()`:可以用字符串、列表、元组对象创建迭代器

        ```python
        >>> list=[1,2,3,4]
        >>> it = iter(list)    # 创建迭代器对象
        >>> print (next(it))   # 输出迭代器的下一个元素
        1
        >>> print (next(it))
        2
        >>>
        ```

        

      * 迭代器对象可以用for语言进行遍历,遍历返回其中元素

        ```python
        #!/usr/bin/python3
         
        list=[1,2,3,4]
        it = iter(list)    # 创建迭代器对象
        for x in it:
            print (x, end=" ")
        ```

        

      * 也可以使用`next()`进行遍历

        ```
        #!/usr/bin/python3
         
        import sys         # 引入 sys 模块
         
        list=[1,2,3,4]
        it = iter(list)    # 创建迭代器对象
         
        while True:
            try:
                print (next(it))
            except StopIteration:
                sys.exit()
        ```

   2. 创建一个类作为迭代器

      1. 把类作为迭代器需要实现两种方法`__iter__()` `__next__()` 

      2. `__iter__()` ：返回一个迭代器对象（即返回类对象），这个对象实现了`__next__()` ，并勇敢Stoplteration异常标识迭代的完成

      3. `__next__()` （Python 2 里是 next()）：会返回下一个迭代器对象

         ```python
         class MyNumbers:
           def __iter__(self):
             self.a = 1
             return self
          
           def __next__(self):
             x = self.a
             self.a += 1
             return x
          
         myclass = MyNumbers()
         myiter = iter(myclass)
          
         print(next(myiter))
         print(next(myiter))
         print(next(myiter))
         print(next(myiter))
         print(next(myiter))
         ```

         输出结果为

         ```
         1
         2
         3
         4
         5
         ```

   3. `Stoplteration`异常用于标识迭代的完成，可在`__next__()` 方法中设置`Stoplteration`异常，来结束迭代，例如如下在迭代20次后停止执行：

      ```python
      class MyNumbers:
        def __iter__(self):
          self.a = 1
          return self
       
        def __next__(self):
          if self.a <= 20:
            x = self.a
            self.a += 1
            return x
          else:
            raise StopIteration
       
      myclass = MyNumbers()
      myiter = iter(myclass)
       
      for x in myiter:
        print(x)
      ```

2. 生成器

   1. 定义：使用了yeild关键词的函数，称为生成器（generator）

   2. 遇到yeild时，函数会暂停执行，并返回yeild后的表达式的值作为迭代返回，每次调用生成器的 **next()** 方法或使用 **for** 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 **yield** 语句

      ```python
      def countdown(n):
          while n > 0:
              yield n
              n -= 1
       
      # 创建生成器对象
      generator = countdown(5)
       
      # 通过迭代生成器获取值
      print(next(generator))  # 输出: 5
      print(next(generator))  # 输出: 4
      print(next(generator))  # 输出: 3
       
      # 使用 for 循环迭代生成器
      for value in generator:
          print(value)  # 输出: 2 1
      ```

### 3.Python无穷大与无穷小

1. 

```python
>>> float('inf') # 正无穷
inf
>>> float('-inf') # 负无穷
-inf
```

**inf 均可以写成 Inf**

2. 有些操作时未定义的并会返回一个 NaN 结果:

   ```python
   >>> a = float('inf')
   >>> a/a
   nan
   >>> b = float('-inf')
   >>> a + b
   nan
   ```

###4.Python退出命令行

使用`exit()`回车，或者使用`quit()`回车

### 5.Python三目运算符

exp1 if contion else exp2 如`max = a if a>b else b`

### 6.Python3 range()函数用法

1. python3 range()返回的是一个可迭代对象，而不是列表元素，不会打印列表。而list(),tuple()函数是对象迭代器，可以把range()返回元素组成列表或元组

2. 基础语法

   ```python
   range(stop)
   range(start, stop[, step])
   #表示step参数是可选项
   ```

   * start:默认从0开始，range(5),等价于`range(0,5)`
   * stop:计数到stop结束，但不包含stop,如range(5),迭代返回[0,1,2,3,4]
   * step:步长，默认为一，可设置为负数，表示反向

   ```python
   for number in range(6, 1, -1):
       print(number)
   ```

   输出结果为：

   ```
   6
   5
   4
   3
   2
   ```

3. 可以下方式迭代生成列表

   ```python
   >>> numbers = list(range(1, 6))
   >>> numbers
   [1, 2, 3, 4, 5]
   ```

### 7.Python中的数字函数

* 可以直接使用的数字函数

  * `abs(x)`返回数字的绝对值，如abs(-10)返回10，可以是整数，浮点数，复数。输入数字什么类型，返回什么类型

  * `max(x,y,z,...)`：返回给定参数的最大值，参数可为列表（也可以为字符串，按序返回最大字母本身），x,y,z为数值表达式

  * `min(x,y,z,...)`:同上返回最小值

  * `pow(x,y[,z])`此为内置pow方法，计算x的y次方，若z存在，再对结果取模，结果等效于pow(x,y) %z

  * `round(x[,n])`返回x数字表达式，四舍五入的结果，n表示从小数点位数，默认为0

    ```python
    print ("round(56.659,1) : ", round(56.659,1))
    输出：
    round(56.659,1) :  56.7
    ```

* 需要通过import math静态调用的函数`math.f()`调用

  * `math.ceil(x)`返回数字的上入整数，如math.ceil(4.1) 返回 5

  * `math.floor(x)`返回数字的下舍整数，小于等于，如math.floor(-1.2)返回，-2

  * `math.exp(x)`方法返回x的指数,e^x。float

  * `math.log(x)`返回x的自然对数，x>0

  * `math.log10(x)`返回10基数的对数，x>0

  * `math.fabs()`以浮点形式返回数字绝对值，如 math.fabs(-10) 返回10.0，与abs()区别在：

    * abs()是内置函数
    * 且fabs() 函数只对浮点型跟整型数值有效，不能处理复数

  * `math.modf(x)`返回x的整数部分与小数部分，两部分符号与x相同，整数部分用浮点数表示

    ```python
    print ("math.modf(100.12) : ", math.modf(100.12))
    输出结果为：
    math.modf(100.12) :  (0.12000000000000455, 100.0)
    ```

  * `math.pow(x,y)`求x的y次方，可内置，方法略有不同

  * `math.sqrt(x)`返回数字x的平方根

### 8.Python中的随机数函数 

大部分函数需要引入`import random`模块，然后通过random静态对象调用该方法

* `random.choice(seq)`从列表，元组，字符串中随机抽取一项并返回，可使用迭代器如`random.choice(range(100))`

* `random.randrange([start,]stop[,step])`相当于从一个`range([start,]stop[,step])`随机抽一个即`random.choice(range([start,]stop[,step]))`

* `random.random()`:返回由均匀分布随机生成的一个实数，在半开区间[0,1)内

* `random.seed([x])`在seed确定时，random()生成的随机数会是同一个

  ```python
  #!/usr/bin/python3
  import random
  
  random.seed()
  print ("使用默认种子生成随机数：", random.random())
  print ("使用默认种子生成随机数：", random.random())
  
  random.seed(10)
  print ("使用整数 10 种子生成随机数：", random.random())
  random.seed(10)
  print ("使用整数 10 种子生成随机数：", random.random())
  
  random.seed("hello",2)
  print ("使用字符串种子生成随机数：", random.random())
  
  输出为
  使用默认种子生成随机数： 0.7908102856355441
  使用默认种子生成随机数： 0.81038961519195
  使用整数 10 种子生成随机数： 0.5714025946899135
  使用整数 10 种子生成随机数： 0.5714025946899135
  使用字符串种子生成随机数： 0.3537754404730722
  ```

* `random.shuffle(lst)`将列表中所有元素随机排序，返回None,输入必须是列表，会直接作用于原本的lst,但shuffle具有破坏性，要用seed随机生成同一个随机列表需要中间赋值（详细自查）

* `random.uniform(x,y)`随机生成一个浮点数，在[x,y]（或[y,x],x,y无强制大小要求）内

### 9.Python中的三角函数与数学常量

都需要引入`import math`模块，用`math.f()`静态调用

1. 三角函数：
   1. acos(x),asin(x),atan(x),atan(x,y):反正切
   2. cos(x),sin(x),tan(x):三角函数
   3. degrees(x):弧度转化为角度
   4. radians(x):角度转化为弧度
2. 数学常量
   1. pi,e

### 10.Python单下划线

表示临时或无意义的变量，或者解释器最近一个表达式的结果，如

```python
>>> 20 + 3
23
>>> _
23
>>> print(_)
23

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]
```

可以通过如下操作，生成一个3*3的列表

```python
[[0]*3for _ in range(3)]
```

其中`[0]*3`生成`[0,0,0]`,for list in range(n),则将list重复n次

### 11.Python Type()函数

​	拥有命名和取名两个功能，分别对应一个参数和三个参数时

### 12.Python sum() 函数

### 13.查看并导出git记录

`git log`:查看git历史提交记录

`git log > ./log.txt`:导出到当前目录下的 log.txt
