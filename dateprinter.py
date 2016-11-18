def main():
    date = input("Enter date mm/dd/yyyy")
    print(date_printer(date))



def date_printer(date):
    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
              "December"]

    month_list = months[int(date[0])]

    date_list = date.split("/")
    date_format = month_list + " " + date_list[1] +', ' + date_list[2]


    return date_format

main()
