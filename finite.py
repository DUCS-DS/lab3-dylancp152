from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    length = 0
    current = lst.head
    while current:
        current = current.next
        length += 1
    return length


def llprint(lst):
    """print a finite linked list"""
    current = lst.head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print("Null")

if __name__ == "__main__":

    LinkedList = LList()
    values = [1,2,4,8,16,32,64,128,256,512]
    for val in values:
        append(LinkedList, Node(val))
    llprint(LinkedList)