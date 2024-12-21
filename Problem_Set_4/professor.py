import random


def main():
    x = get_level()
    print(f"Score: {generate_integer(x)}")


def get_level():
    while True:
        try:
            print("Type -1 to quit")
            user_input = int(input("Level: "))
            if user_input == -1:
                return -1
            elif 0 < user_input < 4:
                return user_input
            else:
                continue
        except: 
            continue
    


def generate_integer(level):
    if level == -1:
        return 0
    score = 0
    total = 0
    while True:
        i = 0
        if total == 10:
            return score
            break
        if level == 1:
            number1 = random.randint(0, 9)
            number2 = random.randint(0, 9)
        elif level == 2:
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
        elif level == 3:
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)
        sum = number1 + number2
          
        while True:
            print("Type -1 to quit")
            user_input = int(input(f"{number1} + {number2} = "))
            if user_input == -1:
                return score
                break
            elif user_input == sum:
                score += 1
                total += 1
                break
            else:
                print(f"EEE")
                i += 1
                if i == 3:
                    print(f"{number1} + {number2} = {sum}")
                    total += 1
                    break
                else:
                    continue

                

if __name__ == "__main__":
    main()
