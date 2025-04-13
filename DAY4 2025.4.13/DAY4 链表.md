#DAY4 |链表

## 24. 两两交换链表中的节点

![image-20250413213629359](E:\大四下\课外学习\Python\笔记\DAY4 2025.4.13\image-20250413213629359.png)

具体操作逻辑如上，本题主要就是理清操作逻辑，代码逻辑如下

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead=ListNode(val=-1,next=head)
        cur=dummyhead
        while(cur.next!=None and cur.next.next!=None):
            temp1=cur.next
            temp2=cur.next.next.next
            cur.next=cur.next.next
            cur.next.next=temp1
            cur.next.next.next=temp2
            cur=cur.next.next
        return dummyhead.next
```

递归实现如下

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        pre=head
        cur=head.next
        next=head.next.next
        cur.next=pre
        pre.next=self.swapPairs(head=next)
        return cur
```

时间复杂度：O(n) 空间复杂度O（1）

##  19.删除链表的倒数第N个节点

双指针的应用，设置两个指针，fast和slow指针，让fast先走n+1步，再让slow走，直到fast走到None(链表尽头，不过双向链表是不是没有尽头)，由于fast和slow指针始终相隔n+1各元素，因此slow指针下一个指向的便是待删除元素

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead=ListNode(val=-1,next=head)
        fast,slow=dummyhead,dummyhead
        while(fast!=None and n+1):
            n-=1
            fast=fast.next
        while(fast!=None):
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummyhead.next
```

时间复杂度O(n),空间复杂度O(1)

## 面试题 02.07. 链表相交

```python
#面试题 02.07. 链表相交
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA=headA
        curB=headB
        sizeA,sizeB=0,0
        while(curA):
            sizeA+=1
            curA=curA.next
        while(curB):
            sizeB+=1
            curB=curB.next
        curA,curB=headA,headB
        if(sizeA<sizeB):
            sizeA,sizeB=sizeB,sizeA
            curA,curB=curB,curA
        gap=sizeA-sizeB
        for _ in range(gap):
            curA=curA.next
        while(curA):
            if(curA==curB):
                return curA
            curA=curA.next
            curB=curB.next
        return None
```

时间复杂度为O（n+m）,思路就是将链表向右侧对齐

```python
#面试题 02.07. 链表相交 非常有意思的等比例法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if(not headA or not headB):
            return
        pointerA=headA
        pointerB=headB
        while(pointerA!=pointerB):
            pointerA=pointerA.next if pointerA else headB
            pointerB=pointerB.next if pointerB else headA
        return pointerA
```

非常巧妙的思路，简要解释为如下

aaaaaabbb

bbbaaaaaa

通过比例实现了自动右对齐

## 142.环形链表II

本体的思路是设置快慢指针，快指针每回合走两步，慢指针每回合走一步，从相对速度来看，快指针相当于每回合相对慢指针走一步，所以如果存在环，快慢指针一定在环上相交

对此可以数学建模：

数学证明详细见[代码随想录 (programmercarl.com)](https://programmercarl.com/0142.环形链表II.html#思路)

![image-20250414014333103](E:\大四下\课外学习\Python\笔记\DAY4 2025.4.13\image-20250414014333103.png)

本题主要还是一个数学证明

头节点到环形入口处距离记为x,环形入口处到相遇点距离为y，相遇点到入口处为z

有$$(x+y)*2=x+y+n*(y+z)$$

可化简为$x=(n-1)*(y+z)+z$

当n为1时，为$x=z$,

所以从相交点处产生指针index1,从原点处产生index2他们一定会在入口点相遇，即使n不是1，也就最多是index1多转几圈

```python
# 142.环形链表II
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow=head,head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(fast==slow):
                index1=fast
                index2=head
                while(index1!=index2):
                    index1=index1.next
                    index2=index2.next
                return index1
        return None
```

python特有的集合法....

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited=set()
        while head:
            if head not in visited:
                visited.add(head)
                head=head.next
            else:
                return head
        return None
```

## 课外补充

### Python的格式化输出——print()

python中有三种输出方法：表达式语句，print()函数，和使用文件对象的write

`print(*objects,sep='',end='/n',file=sys.stdout,flush=False)`

* objects:表示一次可输出多个对象，输出多个对象时，需要用`，`分隔

* sep:输出时用来间隔多个对象，默认是一个空格

* end:用来设定以什么结尾，默认是换行符\n

* file:要写入的文件对象

* flush: 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新

  ```python
  >>>print(1)  
  1  
  >>> print("Hello World")  
  Hello World  
   
  >>> a = 1
  >>> b = 'runoob'
  >>> print(a,b)
  1 runoob
   
  >>> print("aaa""bbb")
  aaabbb
  >>> print("aaa","bbb")
  aaa bbb
  >>> 
   
  >>> print("www","runoob","com",sep=".")  # 设置间隔符
  www.runoob.com
  ```

  使用flush产生一个Loading的效果：

  ```python
  import time
  
  print("---RUNOOB EXAMPLE ： Loading 效果---")
  
  print("Loading",end = "")
  for i in range(20):
      print(".",end = '',flush = True)
      time.sleep(0.5)
  ```

输出美化

* str.format():使得输出格式更为多样

* str(),repr():将输出的值转化为字符串

  * str():返回一个用户易读的表达形式

  * repr():返回一个解释器易读的表达形式

  * 在对象的定义中，可以用`__str()__` `__repr()__`方式重载定义

    ```python
    class MyClass:
    def __repr__(self):
    return "MyClass(param1='value1', param2='value2')"
    
    def __str__(self):
    return "MyClass with value1 and value2"
    
    obj = MyClass()
    print(repr(obj)) # 输出: MyClass(param1='value1', param2='value2')
    print(str(obj)) # 输出: MyClass with value1 and value2
    ```

* str类的常用方法：

  * `str.rjust() `:让字符串靠右，并在左填充空格，同理有`ljust()` 和 `center(）`,类似的还有`zill(n)`他会在字符左端填充0，直到总占位n,实例如下：

    ```python
    >>> for x in range(1, 11):
    ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    ...     # 注意前一行 'end' 的使用
    ...     print(repr(x*x*x).rjust(4))
    ...
     1   1    1
     2   4    8
     3   9   27
    .....
    >>> '12'.zfill(5)
    '00012'
    >>> '-3.14'.zfill(7)
    '-003.14'
    >>> '3.14159265359'.zfill(5)
    '3.14159265359'
    ```

  * `str.format()`:

    * 在未命名字符串中参数时，会按照顺序，将{}中的内容，被format()中的参数替代

      ```python
      >>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
      菜鸟教程网址： "www.runoob.com!"
      ```

    * 数字也可以用于指向传入对象在format()中的位置，从0开始

      ```python
      >>> print('{0} 和 {1}'.format('Google', 'Runoob'))
      Google 和 Runoob
      >>> print('{1} 和 {0}'.format('Google', 'Runoob'))
      Runoob 和 Google
      ```

    * 如果使用了关键字参数，则他们的值会指向对应关键字。关键字规则和数字规则可以混用

      ```python
      >>> print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
      菜鸟教程网址： www.runoob.com
      
      >>> print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
      站点列表 Google, Runoob, 和 Taobao。
      ```

    * 在原字符处的{}，不同标识代表不同的解读方法：`!a` 使用ascii(),`!s` 使用str(),`!s`使用repr()

      ```python
      >>> import math
      >>> print('常量 PI 的值近似为： {}。'.format(math.pi))
      常量 PI 的值近似为： 3.141592653589793。
      >>> print('常量 PI 的值近似为： {!r}。'.format(math.pi))
      常量 PI 的值近似为： 3.141592653589793。
      ```

    * 可选项`:`可以跟`.+数字+f`表示保留到小数点后位数

      ```python
      >>> import math
      >>> print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
      常量 PI 的值近似为 3.142。
      ```

    * 可在：传入整数，或整数+d,表示域至少的宽度，用于美化表格

      ```python
      >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
      >>> for name, number in table.items():
      ...     print('{0:10} ==> {1:10d}'.format(name, number))
      ... 
      Google     ==>          1
      Runoob     ==>          2
      Taobao     ==>          3
      ```

    * 可以通过字典，用[],访问键值

      ```python
      >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
      >>> print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
      Runoob: 2; Google: 1; Taobao: 3
      ```

  * 旧字符串格式化

    ```python
    >>> import math
    >>> print('常量 PI 的值近似为：%5.3f。' % math.pi)
    常量 PI 的值近似为：3.142。
    ```

### Python 读取键盘输入

`input([prompt])`:先输出prompt,后接受一个标准输入数据

`input([prompt]).split(str="",num=string.count(str))`:可将输入的字符串分割

```python
#!/usr/bin/python
#输入三角形的三边长
a,b,c = (input("请输入三角形三边的长：").split())
a= int(a)
b= int(b)
c= int(c)

#计算三角形的半周长p
p=(a+b+c)/2

#计算三角形的面积s
s=(p*(p-a)*(p-b)*(p-c))**0.5

#输出三角形的面积
print("三角形面积为：",format(s,'.2f'))
```

### Python 打开文件

`open(filename,mode)`:返回一个file对象

* filename:包含要访问的文件的字符串值

* mode:决定了文件的打卡方式

  * r :只读打开，文件指针放文件开头

  * rd ：以二进制只读打开，文件指针放在开头

  * r+: 打开用于读写，放在文件开头

  * rb+:二进制打开文件读写，指针放在开头

  * w:打开文件用于写入，文件存在则打开文件，清除原有内容，从头写，若不存在则创建按

  * wb:同上，但以二进制形式打开

  * w+:打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

  * wb+:同上，但是二进制打开

  * a:打开文件用于追加，若文件存在，则从尾部开始追加，不会删除。若不存在则创建

  * ab:同上，二进制打开

  * a+: 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

  * ab+:同上，二进制

    ```python
    #!/usr/bin/python3
    
    # 打开一个文件
    f = open("/tmp/foo.txt", "w")
    
    f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
    
    # 关闭打开的文件
    f.close()
    
    
    #此时打开foo.txt如下
    $ cat /tmp/foo.txt 
    Python 是一个非常好的语言。
    是的，的确非常好!!
    ```

### Python 文件对象的方法

以下默认通过open()创建了一个f的文件对象

* `f.read([size])`: 读取文件内容，如果写了size,将读取一定数目，然后作为字符串或字节对象返回

  * size,被忽略或为负时，所有内容都会被读取并返回

    ```python
    #!/usr/bin/python3
    
    # 打开一个文件
    f = open("/tmp/foo.txt", "r")
    
    str = f.read()
    print(str)
    
    # 关闭打开的文件
    f.close()
    
    结果为：
    Python 是一个非常好的语言。
    是的，的确非常好!!
    ```

* `f.readline([size])`会从文件中读取单独的一行,指定size时，返回指定大小的字节数，负数或未指定全部返回,上述例子就会返回：

  ```python
  Python 是一个非常好的语言。
  ```

* `f.readlines([size])`:读取所有行，并按行分割，返回由按行分割组成的列表

  ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo.txt", "r")
  
  str = f.readlines()
  print(str)
  
  # 关闭打开的文件
  f.close()
  
  ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']
  ```

  * 另外，利用for循环迭代时，也会按行读取

    ```python
    #!/usr/bin/python3
    
    # 打开一个文件
    f = open("/tmp/foo.txt", "r")
    
    for line in f:
        print(line, end='')
    
    # 关闭打开的文件
    f.close()
    
    输出：
    Python 是一个非常好的语言。
    是的，的确非常好!!
    ```

* `f.write(string)`:将string写入文件中，返回写入的字符数。string必须是字符类型，否则得先用str()转换

* `f.tell()`：返回当前文件指针，相较于文件开头的偏移量（及文件指针的位置），返回一个整数

* `f.seek()`

  * `f.seek(offset[, from_what=0])`:改变文件指针当前位置

  * offset，表示相较于`from_what`的偏移量

  * from_what:如果是0表示开头,1表示从当前位置往后，2表示从结尾开始（此时offset应该为负，表示从后往前）

    ```python
    >>> f = open('/tmp/foo.txt', 'rb+')
    >>> f.write(b'0123456789abcdef')
    16
    >>> f.seek(5)     # 移动到文件的第六个字节
    5
    >>> f.read(1)
    b'5'
    >>> f.seek(-3, 2) # 移动到文件的倒数第三字节
    13
    >>> f.read(1)
    b'd'
    ```

* `f.close()`:关闭文件释放资源

### Python pickle模块

* pickle序列化，能将程序中运行的对象保存在文件中去，永久存储

* pickle反序列化，从文件中创建上一次程序保存的对象

* 序列化：`pickle.dump(obj,file[,protocol])`，将对象obj写入.pkl的文件对象中

  ```python
  #!/usr/bin/python3
  import pickle
  
  # 使用pickle模块将数据对象保存到文件
  data1 = {'a': [1, 2.0, 3, 4+6j],
           'b': ('string', u'Unicode string'),
           'c': None}
  
  selfref_list = [1, 2, 3]
  selfref_list.append(selfref_list)
  
  output = open('data.pkl', 'wb')
  
  # Pickle dictionary using protocol 0.
  pickle.dump(data1, output)
  
  # Pickle the list using the highest protocol available.
  pickle.dump(selfref_list, output, -1)
  
  output.close()
  ```

* 反序列化：`pickle.load(file)`对file以读的形式打开，返回可读的文件对象

  ```python
  #!/usr/bin/python3
  import pprint, pickle
  
  #使用pickle模块从文件中重构python对象
  pkl_file = open('data.pkl', 'rb')
  
  data1 = pickle.load(pkl_file)
  pprint.pprint(data1)
  
  data2 = pickle.load(pkl_file)
  pprint.pprint(data2)
  
  pkl_file.close()
  ```

### Python中交换两数值

`a,b=b,a`

### Python集合

* 无序不重复序列，可进行集合运算，可用{}，用`，`分割创造集合，也可用set()函数

```python
set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合
```

* 集合运算包括：

  * -：差集

  * |：并

  * &：交

  * a^b:不同时包含ab

* 类似列表推导式，支持集合推导式（用{}框住的推导式）

  ```python
  >>> a = {x for x in 'abracadabra' if x not in 'abc'}
  >>> a
  {'r', 'd'}
  ```

* 基本方法

  * 添加元素：s.add(x),如果元素已存在，则不进行任何操作。

    * 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等s.update( x )

      ```python
      >>> thisset = set(("Google", "Runoob", "Taobao"))
      >>> thisset.update({1,3})
      >>> print(thisset)
      {1, 3, 'Google', 'Taobao', 'Runoob'}
      >>> thisset.update([1,4],[5,6])  
      >>> print(thisset)
      {1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
      >>>
      ```

  * 移除元素：s.remove(x),如果x不存在，会发生错误

    * 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。s.discard(x)
    * s.pop()随机删除集合中一个元素（set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除）

  * 计算元素集合个数：len(s)

    ```python
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> len(thisset)
    3
    ```

  * 清空集合 s.clear()

  * **判断元素是否在集合中** `x in b`,存在返回True，不存在返回False

    ```python
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> "Runoob" in thisset
    True
    >>> "Facebook" in thisset
    False
    >>>
    ```

**注意**：a={},这样声明的a类型是dict，不是set,需要a={value1,value2...}，声明空集合需要a=set()

