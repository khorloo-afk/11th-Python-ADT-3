# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = []
HeadPointer = 0
TailPointer = -1

def IsEmpty():
    global Queue, Headpointer, Tailpointer
    if HeadPointer == -1 or Headpointer > Tailpointer:
        return -1


def IsFull():
    global Queue, Headpointer, Tailpointer
    if HeadPointer == -1 or Headpointer > Tailpointer:
        return 0


# Exercise 2
def Enqueue(Item):
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 5:
         return False
    if NumberItems == 0:
        HeadPointer = 0
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
        if TailPointer == 5:
            TailPointer = 0
    Queue[TailPointer] = Data
    NumberItems = NumberItems + 1
    return True

# Exercise 3
def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
         return -1
    DataToReturn = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1
    if HeadPointer == 5:
        HeadPointer = 0
    NumberItems = NumberItems - 1
    if NumberItems == 0:
        HeadPointer = -1
        TailPointer = -1
    return DataToReturn

# Exercise 4
def Peek():
     global Queue, Headpointer
     return Queue[Headpointer]


def ShowQueue():
    # Write your code here
    pass


# Exercise 5
def Canteen(Commands):
    # Write your code here
    pass
