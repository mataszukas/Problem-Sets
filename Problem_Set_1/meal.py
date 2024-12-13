def define_time(format_type, am_pm=None, time=None):
    pass
    if format_type == "12":
        while True:
                time = input("What time is it? (-1 to exit) ")
                if time == "-1":
                    return None, None
                time = time.split(":")
                if len(time) == 2 and len(time[1]) == 2:       
                    am_pm = input("What time of day is it? 1 - AM, 2 - PM: (-1 to exit) ").strip()
                    if am_pm == "-1":    
                        return None, None
                    elif am_pm == "1" or am_pm == "2":
                        return time, am_pm
                    else:
                        print("Invalid time and/or time of day. Try again")
                else:
                    print("Invalid input. Try again")
    elif format_type == "24":
        while True:
            time = input("What time is it? (-1 to exit) ")
            if time == "-1":
                return None, None
            time = time.split(":")    
            if len(time) == 2 and len(time[1]) == 2: 
                return time, None
            else:
                print ("Invalid input. Try again")
    elif format == "-1":
        return None, None
    else:
        print("Invalid format")

def convert(time, am_pm=None):
    pass
    while True:
        try:
            if am_pm is None:
                hour = float(time[0])
                minute = float(time[1])
                if 0 <= hour < 24 and 0 <= minute < 60:
                    total = hour + minute / 60
                    return total
                elif hour > 24 or 0 > minute > 60:
                    print("Invalid time format. Type hours between 0 and 24, minutes 0 to 60.")
                    time = input("What time is it? (-1 to exit) ").split(":")
                    continue
            elif am_pm != None:
                hour = float(time[0])
                minute = float(time[1])
                if 1 <= hour < 13 and 0 <= minute < 60:
                    total = hour + minute / 60
                    return total
                else:
                    print("Invalid time format. Type hours between 1 and 13, minutes 0 to 60.")
                    time = input("What time is it? (-1 to exit) ").split(":")
                    continue
            else:
                return None
        except ValueError:
            print("Input error (invalid time). Try again.")
            time = input("What time is it? (-1 to exit) ").split(":")
    
def check_meal_time(total, am_pm=None):
    pass
    if am_pm == "1":

        if 7 <= total <= 8:
            print("breakfast time")
        else:
            return None
    elif am_pm == "2":
                
        if 12 <= total <= 13:
            print("lunch time")
        elif 6 <= total <= 7:
            print("dinner time")
        else:
            return None
    elif am_pm == None:
            if 7 <= total <= 8:
                print("breakfast")
            elif 12 <= total <= 13:
                print("lunch")
            elif 18 <= total <= 19:
                print("dinner")
            else: 
                return None 
      
def main():
    while True:
        format = input("What is the time format? Type 12 for 12hour, or 24 for 24hour (-1 to exit): ").strip()
        if format == "-1":
            break
        elif format == "12" or format == "24":
            time, am_pm = define_time(format)
            if time is None:
                break
            total_time = convert(time, am_pm)
            if total_time is not None:
                check_meal_time(total_time, am_pm)   
        else:
            print("Invalid format. Try again")
            
if __name__ == "__main__":
    main()
