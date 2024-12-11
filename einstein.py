def calculation(mass):

    int_mass = int(mass) #convert input from string to int
    c = 300000000 #speed of light
    E = int_mass * (c ** 2) #E=mc2
    return E #returns energy result

def main():

    user_input = input("m: ") #user inputs mass
    result = calculation(user_input) #send input mass to calculation
    print("E:", result) #prints results

main()
