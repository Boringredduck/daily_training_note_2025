# 算法笔记|DAY3

## 链表

* 链表的类型：通过指针串联在一起的线性结构，每一个节点由数据域和指针域（存放指向下一个节点的指针）组成，入口节点，或链表的头结点为head
  * 单链表
  * 双链表：每一个节点有两个指针域，一个指向上一个节点，一个指向下一个节点
  * 循环链表：链表首位相连
* 链表的存储方式
  * 链表在内存中不是连续分布的
* 链表的操作
  * 删除节点：将该节点的前项的指针，指向下一项，Python中内存会自动回收
  * 添加节点：前项的指针指向它
  * 性能分析：插入删除时间复杂度都为O（1），但有一个查询过程，时间复杂度为O（n）

## 203.移除链表元素

###引入虚拟头节点，避免删除头节点时的特殊操作

```python
# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyhead=ListNode(0,head)
        cur=dummyhead
        while(cur.next!=None):
            if(cur.next.val == val ):
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummyhead.next
```

### 递归解决

```python
#递归实现 203.移除链表元素
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if(head==None):
            return
        if(head.val==val):
            new_head=self.removeElements(head=head.next,val=val)
            return new_head
        else:
            head.next=self.removeElements(head=head.next,val=val)
            return head
```

逻辑是：如果匹配删除项目，则返回下一个非删除项

如果是非删除项，直接返回

相较于前一种方法，由于涉及函数的递归调用，空间复杂度为O（n）

两种方法的时间复杂度都是O（n）

## 707.设计链表

### 单链表实现

```python
#设计链表,单链表
class MyLinkedList:
    class ListNode:
        def __init__(self,val=0,next=None):
            self.val=val
            self.next=next
            
    def __init__(self):
        self.dummyhead=self.ListNode(val=-1)
        self.count=0

    def get(self, index: int) -> int:
        if(index<0 or index>(self.count-1)):
            return -1
        cur=self.dummyhead.next
        while(index):
            index-=1
            cur=cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        self.dummyhead.next=ListNode(val=val,next=self.dummyhead.next)
        self.count+=1

    def addAtTail(self, val: int) -> None:
        cur=self.dummyhead
        while(cur.next):
            cur=cur.next
        cur.next=ListNode(val=val)
        self.count+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if(index>self.count):
            return
        if(index<0):
            index=0
        cur=self.dummyhead
        while(index):
            index-=1
            cur=cur.next
        cur.next=ListNode(val=val,next=cur.next)
        self.count+=1

    def deleteAtIndex(self, index: int) -> None:
        if(index>(self.count-1) or index<0):
            return
        cur=self.dummyhead
        while(index):
            index-=1
            cur=cur.next
        cur.next=cur.next.next
        self.count-=1
```

### 双链表法

找的index一定时，可从中间开始



## 206.反转链表

### 从前到后

都是利用双指针的思路，从前向后，将next指针一个个倒转

#### 双指针

```python
#206.反转列表 双指针
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        cur=head
        while(cur):
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre
```

#### 递归

```python
#206.反转列表 递归
class Solution:
    def reverse(self,pre:Optional[ListNode],cur:Optional[ListNode])->Optional[ListNode]:
        if(cur==None):
            return pre
        temp=cur.next
        cur.next=pre
        return self.reverse(cur,temp)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(pre=None,cur=head)
```

###从后到前的递归

为什么从前到后需要双指针但是从后向前不需要？

个人感觉是因为但单链表无法记录自己的前一项，因此需要两个指针。

而从后向前递归返回时，栈中自然记录了前一项的信息，所以不需要双指针。

本来想说双向链表，但是好像不存在这样的问题，只要更换头节点即可

```python
#206.反转列表 从后到前
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return
        if(head.next==None):
            return head
        last=self.reverseList(head=head.next)
        head.next.next=head
        head.next=None
        return last


```



## 零散知识补充

###  1.大模型下载

​	通过huggingface-cli下载模型

```shell
pip install -U huggingface_hub#安装依赖
huggingface-cli download model_name --local-dir dir_name #基本方法-下载模型
huggingface-cli down --repo-type dataset dataset_name --local-dir dir_name #基本方法下载数据集
```

### 2.Python中的Optional类

​	`from typing import Optional`

Optional类表示标记的函数的参数或返回值，或可以是指定的对象，也可以是空None

**注意**：Optional类型提示只能用在参数或返回值上，不能用在变量声明上。