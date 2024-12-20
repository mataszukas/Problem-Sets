def main():
    # x = int(input("Enter fuel level 'x': "))
    # y = int(input("Enter fuel tank size 'y': "))
    calculate()
    
def calculate():
    while True:
        try:
            user_input = input("Fraction: ").strip().split("/")
            x = int(user_input[0])
            y = int(user_input[1])
            if (x > y and y > 0):
                print("Fuel level cannot be more than fuel tank")
                continue
            elif (x < 0 or y < 0):   
                print("Number cannot be negative")
                continue
            level = round(x/y * 100, 0)
            if 1 < level < 99: 
                print(f"{level:.0f}%")
                break
            elif 0 <= level <= 1:
                print("E")
                break
            elif level >= 99:    
                print("F")
                break
        except ZeroDivisionError:
            print("Please enter a number 'y' above 0")
            continue
        except ValueError:
            print("Please write fraction again with numbers above 0 and '/' separator")
            continue
           
if __name__ == "__main__":
    main()