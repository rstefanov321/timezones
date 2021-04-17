# ====================== Time zones output ==========================

# first, we import the necessary modules:
import datetime
import pytz

# make a dictionary of all the countries you want the user to choose from
# (can always be changed, exact strings taken from the "all_timezones" list)
countries = {0: "quit",
             1: "Europe/Paris",
             2: "Australia/Darwin",
             3: "Asia/Kolkata",
             4: "Asia/Jakarta",
             5: "Asia/Kabul",
             6: "Brazil/Acre",
             7: "Asia/Bangkok",
             8: "Asia/Brunei",
             9: "Asia/Chita",
             }

print()

# Providing the user with the options to choose from
print("Please choose a timezone: ")
for i in countries.keys():
    print(i, ": ", countries[i])

# setting the input
choice = int(input(": "))

# creating a for-loop to find the chosen timezone
for tz in countries:
    if 1 <= choice <= len(countries.keys()):  # setting the steps to complete if choice is valid
        chosen_zone = countries[choice]
        tz_to_display = pytz.timezone(chosen_zone)
        time_in_chosen = datetime.datetime.now(tz=tz_to_display)
        print("You chose: {}". format(countries[choice]))
        print("Here is the time in that part of the world: {} {}".format(time_in_chosen.strftime("%A %x %X %z")))

        print("-"*40)  # showing the local time

        local_time = datetime.datetime.now()
        print("Your local time is {}".format(local_time.strftime("%A %x %X %z")))

        print("-"*40)  # showing the UTC time.

        utc_time = datetime.datetime.utcnow()
        print("And the UTC time is {}.".format(utc_time.strftime("%A %x %X %z")))
        print()
        choice = int(input("Please choose a timezone or 0 to quit: "))

        print()
    elif choice == 0:
        print("You decided to quit, have a nice day!")
        print()
        break
    else:
        print("Please pick a number from 1 to {} or 0 to quit.".format(len(countries)-1))
        choice = int(input())




