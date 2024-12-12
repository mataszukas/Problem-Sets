def convert(time, am_pm=None):
    try:
        hour = float(time[0])
        minute = float(time[1])
        if 0 <= hour < 24 and 0 <= minute < 60:
            total = hour + minute / 60
            return total
        elif am_pm != None:
            if 1 <= hour < 13 and 0 <= minute < 60:
                total = hour + minute / 60
                return total
            else:
                return None
        else:
            return None
    except ValueError:
        print("Input error (invalid time)")
        return None
    

def check_meal_time(total, am_pm=None):
    
    if am_pm == 1:
        if 7 <= total <= 8:
            print("breakfast")
        else:
            return None
        
    elif am_pm == 2:
            
        if total >= 12 :
            print("lunch")
        elif 6 <= total <= 7:
            print("dinner")
        else:
            return None
        
    else:
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

        if format == "12":
            
            time = input("What time is it? (-1 to exit) ")
            if time == "-1":
                break
            else:
                time = time.split(":")
                
            am_pm = input("What time of day is it? 1 - AM, 2 - PM: (-1 to exit) ").strip()
            if am_pm == "-1":    
                break
            elif len(time) == 2 and len(time[1]) == 2 and [am_pm == 1 or am_pm == 2]:
                total_time = convert(time)
                if total_time is not None:
                    check_meal_time(total_time, am_pm)
                else:
                    None
            else:
                print("Invalid time and/or time of day")

        elif format == "24":
            time = input("What time is it? ").split(":")
            total_time = convert(time)
            if total_time is not None:
                check_meal_time(total_time)
            else:
                print("Invalid time")
        elif format == "-1":
            break
        else:
            print("Invalid format")



if __name__ == "__main__":
    main()
