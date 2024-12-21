def main():
    names = []
    while True:
        try:
            user_input = input("Name: ").capitalize()
            if user_input:
                names.append(user_input) #add name to names list
            else:
                continue
        except EOFError:
            print(f"Adieu, adieu, to ", end="")
            pass #for debug
            if len(names) == 1:
                print(f"{names[0]}")
            elif len(names) == 2:
                print(f"{names[0]} and {names[1]}")
            else:
                for i in range(len(names) - 1):
                    print(f"{names[i]}, ", end="") #while i is < len(names)
                print(f"and {names[-1]}") #when the end of list is reached
            break

if __name__ == '__main__':
    main()
