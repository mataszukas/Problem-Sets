from emoji import emojize

def main():
    user_input = input("Input: ")
    print((f"Output: {emojize(user_input)}"))

if __name__ == '__main__':
    main()
