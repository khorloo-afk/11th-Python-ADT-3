# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = [-1, -1, -1, -1, -1, -1, -1, -1]
HeadPointer = 0
TailPointer = -1


def IsEmpty():
    return HeadPointer > TailPointer


def IsFull():
    return TailPointer == 7


# Exercise 2
def Enqueue(Item):
    global Queue, HeadPointer, TailPointer

    if IsFull():
        return False

    TailPointer = TailPointer + 1
    Queue[TailPointer] = Item

    return True
    
# Exercise 3
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if IsEmpty():
        return -1

    Item = Queue[HeadPointer]
    HeadPointer = HeadPointer + 1

    return Item
# Exercise 4
def Peek():
    if IsEmpty():
        return -1

    return Queue[HeadPointer]
def ShowQueue():
    if IsEmpty():
        return ""

    Result = ""

    for i in range(HeadPointer, TailPointer + 1):
        Result = Result + str(Queue[i])

        if i < TailPointer:
            Result = Result + " "

    return Result

# Exercise 5
def Canteen(Commands):
    global Queue, HeadPointer, TailPointer

    Queue = [-1, -1, -1, -1, -1, -1, -1, -1]
    HeadPointer = 0
    TailPointer = -1

    Served = []

    for Command in Commands:

        if Command == "serve":
            Student = Dequeue()

            if Student != -1:
                Served.append(Student)

        else:
            Parts = Command.split(" ")
            Name = Parts[1]

            Enqueue(Name)

    return Served
