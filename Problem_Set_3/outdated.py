def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    organize()

def organize():
    while True:
        try:
            date = input("Date: ")
            if '/' in date:
                date = date.split('/')
                if len(date) != 3:
                    continue
                elif len(date[0]) !=2 or len(date[1]) !=2:
                    continue
                elif int(date[0]) < 1 or int(date[0]) > 12:
                    continue
                elif int(date[1]) < 1 or int(date[1]) > 31:
                    continue
                else:
                    print(f"{date[2]}-{date[0]}-{date[1]}")
                    break
            elif ',' in date:
                date = date.strip().split(',')
                date0 = date[0].split(' ')
                year = date[1].strip()
                month = date0[0].lower().capitalize()
                day = int(date0[1])
                if len(date) != 2 and len(date0) != 2:
                    continue
                elif day < 1 or day > 31:
                    continue
                for index, i in enumerate(months):
                    if month in i:
                        print(f"{year}-{(index+1):02}-{day:02}")
                    else:
                        continue
                break
            else:
                continue
        except EOFError:
            break
        except:
            continue
            
  
main()