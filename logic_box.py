
print("Welcome to the Pattern & Number Logic Box!")

while True:
    print()
    print("Please select an option:")
    print("1-Generate a Pattern ")
    print("2-Analyze a range of numbers")
    print("3-Exit")

    choice = input("Enter your choice : ")

    match choice:
        case "1":
            print()
            print("Please select a pattern type:")
            print()
            print("1. Square Pattern")
            print("2. Star Triangle")
            print("3. Number Triangle")
            

            choice = int(input("\nEnter your choice : "))
            r = int(input("Enter the number of rows for the pattern: "))

    
            match choice:
                case 1:
                    print()
                    print("Square Pattern:")
                    for i in range(1, r+1):
                        for j in range(1, r+1):
                            print("*", end=" ")
                        print()
                    

                case 2:
                    print()
                    print("Star Triangle:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            print("*", end=" ")
                        print()

                    
                case 3:
                    print()
                    print("Number Repeat Triangle:")
                    for i in range(1, r+1):
                        for j in range(1, i+1):
                            print(i, end=" ")
                        print()
                    
               

                case _:
                    print("Invalid  choice.")

            
        case "2":
          
            print()
            start = int(input("Enter the starting number : "))
            end = int(input("Enter the ending number : "))
            print()

            sum = 0

            for num in range(start, end + 1):
                print(f"Number {num} is: ", "even" if num % 2 == 0 else "odd")
                sum += num
            
            print(f"\nSum of all numbers from {start} to {end}: {sum}")
            
            
        case "3":
            break


        case _:
            print("Invalid choice")



print("  Thank you for using the Logic Box!")

