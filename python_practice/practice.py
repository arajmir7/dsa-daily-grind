class Solution:
    def calculator():
        print("Select operator")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Division")

        choice=input("Select a choice: ")

        a = float(input("Enter fisrt number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result: ", a+b)
        elif choice == "2":
            print("Result: ", a-b)
        elif choice == "3":
            print("Result: ", a*b)
        elif choice == "4":
            if b != 0:
                print("Result: ", a/b)
            else:
                print("Error Cannot divided by zero")
        else:
            print("Invalid Choice")
    calculator()

