# 算法记录|DAY 1 数组

## 数组理论基础

**数组定义**：数组是存放在连续内存空间上相同类型数据的集合

**数组特点**：

* 数组下标从0开始
* 数组的内存空间都是连续的

不同编程语言内存管理是不一样的：

*  如在C++中，二维数组是连续分布的
* 在java中，二维数组可能是如下排列<img src="E:\大四下\课外学习\Python\笔记\DAY1 2025.4.9\image-20250409183640430.png" alt="image-20250409183640430" style="zoom:25%;" />

## 704. 二分查找

### 左闭右闭

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r  = mid - 1
            else:
                l = mid + 1
        return -1
```

关键点：

* while的判断条件为 `while(left<=right)`,使用<=而非<,是因为left==right是有意义的
* `if(nums[middle]>target)`right要赋值为middle-1,是因为当前nums[middle]一定不是target，而后右区间都是要检查的

### 左闭右开

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        result=-1
        while(left<right):
            middle=left+(right-left)//2
            if(target<nums[middle]):
                right=middle
            elif(target>nums[middle]):
                left=middle+1
            else:
                result=middle
                break
        return result
```

关键点：

* while ，这里使用 < ,因为left == right在区间[left, right)是没有意义的
* `if(nums[middle]>target)`right要赋值为middle,因为是左闭右开，下一个区间不会去比较nums[middle]

## 27.移除元素

### 暴力解法

略，通过双循环实现

时间复杂度O（n^2）,空间复杂度O（1）

### 快慢指针

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIndex,k=0,0
        for fastIndex in range(len(nums)):
            if(nums[fastIndex]!= val):
                nums[slowIndex]=nums[fastIndex]
                slowIndex+=1
                k+=1
        return k
```

**双指针法**：通过一个快指针和一个慢指针，在一个for循环下完成两个for循环的工作

* 快指针：顺序遍历每个元素
* 慢指针：指向新数组下标的位置，不是每个循环都移动

时间复杂度O（n），空间复杂度O（1）

### 库函数

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        counts=nums.count(val)
        for i in range(counts):
            nums.remove(val)
        return len(nums)
```

调用Python库函数实现

时间复杂度也许是O（n）?

### 相向双指针法

```python
#27.移除元素 相向双指针法
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left,right=0,len(nums)-1
        while(left<=right):
            while(left<=right and nums[left]!=val):
                left+=1
            while(left<=right and nums[right]==val):
                right-=1
            if(left<right):
                nums[left]=nums[right]
                left+=1
                right-=1
        return right+1
```

通过前后一个左指针一个右指针，双向夹逼

当左指针发现val时，右指针向左寻找第一个非val元素与之交换。

时间复杂度为O（n）

## 977.有序数组的平方

```python
#977.有序数组的平方
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        count=len(nums)
        left,right,k = 0,count-1,count-1
        new=[0]*count
        for i in range(count):
            nums[i]*=nums[i]
        while(k>=0):
            if(nums[left]<nums[right]):
                new[k]=nums[right]
                right-=1
            else:
                new[k]=nums[left]
                left+=1
            k-=1
        return new
```

**核心**：由于原数组本来有序，最大元素必然在两头，因此可优化排序时间为O（n）,快排为O（nlogn）

## Python语法补充

1. `def search(self, num:List[int], target:int)->int:` 

   1. var:type: 表示参数的类型，如此处的nums: List[int]
   2. def f( )->type:表示该函数的返回值为type类型

2. List相关函数及其方法

   1. 相关函数

      1. `cmp(list1,list2)` 3.0版本已经消失
      2. `len(list)` 返回列表元素个数
      3. `max(list)` 返回列表元素最大值
      4. `min(list)` 返回列表元素最小值
      5. `list(seq)` 将元组转化为列表

   2. List自身包含的方法

      1. `list.append(obj)`在列表末尾添加新元素

      2. `list.count(obj)`统计某个元素在列表中出现的次数

      3. `list.extend(seq)`在列表末尾一次性追加另一个序列多个值

      4. `list.index(obj)`在列表中找出某个值第一个匹配项的索引位置

      5. `list.insert(index,obj)`将新元素插入指定位置上

      6. `list.pop([index=-1])`默认返回并删除最后一个（即index==-1）元素，也可指定返回删除某一位置，如l`ist1.pop(1)`就是弹出list1第二个元素

      7. `list.remove(obj)`移除列表中某个指的第一个匹配项

      8. `list.reverse()`反转列表中元素

      9. `list.sort(key=None, reverse=False)`

         1. cmp参数在Python3中已被移除

         2. key:指定为一个函数，选取列表中指定元素来排序

            ```python
            #!/usr/bin/python
            # -*- coding: UTF-8 -*-
             
            # 获取列表的第二个元素
            def takeSecond(elem):
                return elem[1]
             
            # 列表
            random = [(2, 2), (3, 4), (4, 1), (1, 3)]
             
            # 指定第二个元素排序
            random.sort(key=takeSecond)
             
            # 输出类别
            print('排序列表：')
            print(random)
            ```

            ```
            排序列表：
            [(4, 1), (2, 2), (1, 3), (3, 4)]
            ```

         3. reverse:排序规则，默认为升序即`reverse = False`,`reverse = True`表示为降序

3. 在Python中，`//`表示为整数除法，它会执行除法运算，向下取整为最接近的整数

   ```python
   left = 1
   right = 10
   middle = left + (right - left) // 2
   # middle = 1 + (10 - 1) // 2
   # middle = 1 + 9 // 2
   # middle = 1 + 4  # 因为整数除法 9 // 2 的结果是 4
   # middle = 5
   ```

4. python中的逻辑运算符，and,or,not

5. git代码管理（基础上传）

   1. `git init`把这个目录编程Git可以管理的仓库
   2. `git add` 后可加单一文件名，也可加`.`把当前目录所有文件add
   3. `git commit -m "comment"`把文件提交到仓库
   4. `git remote add origin .....`关联远程仓库
   5. `git push -u origin master`把本地所有内容推送到远程库上