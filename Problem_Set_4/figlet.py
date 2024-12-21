from pyfiglet import Figlet
import random
import sys

def main():
    
    figlet = Figlet()
    fonts = figlet.getFonts()
    
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        set_font = sys.argv[2]
        figlet.setFont(font=set_font)
        user_input = input("Input: ")
        print(f"Output:\n{figlet.renderText(user_input)}")
        return
    elif len(sys.argv) == 1:
        user_input = input("Input: ")
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)
        print(f"Output:\n{figlet.renderText(user_input)}")
        return
    else:
        print("Invalid usage")
        sys.exit(1)

if __name__ == '__main__':
    main()
