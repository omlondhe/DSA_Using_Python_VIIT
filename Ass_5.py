print("Enter any string:")
string: str = input()

while (string.__len__() < 2):
    print("String must be at least 2 characters long!")
    string: str = input()
    
while (True):
    print("What operation you want to perform?")
    print("1.\tConcatenation")
    print("2.\tScanning")
    print("3.\tSubstring")
    print("4.\tTranslation")
    print("5.\tVerification")
    print("6.\tExit")

    choice = int(input("Enter your choice:\t "))
    
    # Concatenation
    if choice == 1:
        string2: str = input("Enter a string:\t")
        while string2.__len__() < 2:
            string2: str = input("String must be at least 2 characters long!\nEnter a string:\t")
        print(string + string2)

    # Scanning
    elif choice == 2:
        result: dict = {}
        for letter in string:
            if result.__contains__(letter):
                result[letter] += 1
            else:
                result.__setitem__(letter, 1)
        for key, value in result.items():
            print(f"{key}: {value}")
    
    # Substring
    elif choice == 3:
        left: int = int(input(f"Enter left index (0 - {string.__len__() - 1}):\t"))
        while (left < 0 or left >= string.__len__()):
            left: int = int(input(f"Enter left index (0 - {string.__len__() - 1}):\t"))
        right: int = int(input(f"Enter right index ({left} - {string.__len__() - 1}):\t"))
        while (right < left or right >= string.__len__()):
            right: int = int(input(f"Enter right index ({left} - {string.__len__() - 1}):\t"))    
        print(string[left:right])

    # Translation
    elif choice == 4:
        to_change: str = input("Which letter you want to translate?\t")
        while (to_change.__len__() < 0 or to_change.__len__() > 1):
            to_change: str = input("Which letter you want to translate?\t")
        to_change_to: str = input("To which letter you want to translate?\t")
        while (to_change_to.__len__() < 0 or to_change_to.__len__() > 1):
            to_change_to: str = input("To which letter you want to translate?\t")
        print(string.translate(string.maketrans(to_change, to_change_to)))

    # Verification
    elif choice == 5:
        string2: str = input("Enter a string to verify:\t")
        if string == string2:
            print("Verified")
        else:
            print("Not verified")

    # Exit
    elif choice == 6:
        exit()

    else :
        print("Enter a correct correct option.")



