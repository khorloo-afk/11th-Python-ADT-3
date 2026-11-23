# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = []
HeadPointer = 0
TailPointer = -1

def IsEmpty():
    return HeadPointer > TailPointer

def IsFull():
    return TailPointer == 7


# Exercise 2
def Enqueue(Item):
    global TailPointer
    if IsFull():
        return False
    TailPointer += 1
    Queue[TailPointer] = Item
    return True
# Exercise 3
def Dequeue():
    global HeadPointer
    if IsEmpty():
        return -1
    removed_item = Queue[HeadPointer]
    HeadPointer += 1
    return removed_item

# Exercise 4
def Peek():
    if IsEmpty():
        return -1
    return Queue[HeadPointer]

def ShowQueue():
    if IsEmpty():
        return ""
    items = []
    for i in range(HeadPointer, TailPointer + 1):
        items.append(str(Queue[i]))
    return " ".join(items)

# Exercise 5
def Canteen(Commands):

