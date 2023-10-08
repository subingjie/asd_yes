# 此处定义了一个链表的节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def iterateListNode(self, head: ListNode):
        # 定义一个数组，用于存储链表的值，最后返回数组
        result = []
        # 遍历链表，将链表的值存储到数组中
        while head:
            result.append(head.val)
            head = head.next
        
        return result

class Demo:
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    # 模拟有十个数据的链表来进行测试,数据最好无序
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next.next = ListNode(10)

    # 创建一个Solution类的实例
    solution = Solution()
    # 调用Solution类中的方法，将链表转换为数组
    result = solution.iterateListNode(head)
    # 打印结果
    print(result)
    
