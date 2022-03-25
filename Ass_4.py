data: list = ["laptop", "wireless mouse", "wireless keyboard", "headphone"]
# Pointers for not using pop() method
# start_pointer: int = 0
# end_pointer: int = len(data) - 1


def display(data_structure: int):
    global start_pointer, end_pointer
    if data_structure == 1:
        print("\nCurrent Stack")
        for i in range(len(data) - 1, -1, -1):
            print(data[i])
        return
    print("\nCurrent Queue")
    print(*data)


# def display(data_structure: int):
#     global start_pointer, end_pointer
#     if data_structure == 1:
#         print("\nCurrent Stack")
#         for i in range(end_pointer, start_pointer - 1, -1):
#             print(data[i])
#         return
#     print("\nCurrent Queue")
#     for i in range(start_pointer, end_pointer + 1):
#         print(data[i], end="    ")
#     print()


def showWelcomeMenu():
    print("Which data structure you want to use?")
    print("1.\tStack")
    print("2.\tQueue")
    print("3.\tExit")
    print("Enter your choice:", end="\t")


def showDataStructureMenu(data_structure: int):
    print("Which operation you want to perform?")
    print(f"1.\t{'Push' if data_structure == 1 else 'Enqueue'}")
    print(f"2.\t{'Pop' if data_structure == 1 else 'Dequeue'}")
    print("3.\tDisplay")
    print("4.\tGo back")
    print("Enter your choice:", end="\t")


def insert(data_structure: int):
    # global end_pointer    # uncomment to use pointers
    if data_structure == 1:
        data.append(input("What you want to push to the stack?\n"))
        print("Data pushed!")
    else:
        data.append(input("What you want to enqueue to the queue?\n"))
        print("Data inserted!")
    # end_pointer += 1      # uncomment to use pointers
    display(data_structure)


def delete(data_structure: int):
    if len(data) == 0:
        print(f'{"Stack" if data_structure == 1 else "Queue"} is empty')
        return
    if data_structure == 1:
        data.pop()
        print("Data popped!")
    else:
        data.pop(0)
        print("Queue dequeued!")
    display(data_structure)


# def deleteWithPointers(data_structure: int):
#     if data_structure == 1:
#         global end_pointer
#         end_pointer -= 1
#         print("Data popped!")
#     else:
#         global start_pointer
#         start_pointer += 1
#         print("Queue dequeued!")
#     display(data_structure)


while True:
    showWelcomeMenu()
    data_structure: int = int(input())

    if data_structure == 1 or data_structure == 2:
        while True:
            showDataStructureMenu(data_structure)
            operation: int = int(input())

            if operation == 1:
                insert(data_structure)
            elif operation == 2:
                delete(data_structure)
            elif operation == 3:
                display(data_structure)
            elif operation == 4:
                break
            else:
                print("Invalid operation.")
    
    elif data_structure == 3:
        print("Closing the application!")
        break
