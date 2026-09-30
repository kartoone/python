# Ticket sales authorization program
# This program will determine if a person is authorized to purchase tickets for a movie based on their age and the movie's rating.  
# Rules are as follows:
# 0 - G - General Audiences: All ages admitted.
# 1 - PG - Parental Guidance: Some material may not be suitable for children.
# 2 - PG-13 - Any child under 13 must be accompanied by a parent or adult guardian.
# 3 - R - Restricted: Under 17 requires accompanying parent or adult guardian.

print("0 - G - General Audiences: All ages admitted.")
print("1 - PG - Parental Guidance: Some material may not be suitable for children.")
print("2 - PG-13 - Any child under 13 must be accompanied by a parent or adult guardian.")
print("3 - R - Restricted: Under 17 requires accompanying parent or adult guardian.")
rating = int(input("Enter the movie rating (0-3): "))

if rating < 0 or rating > 3:
    print("Invalid rating. Please enter a number between 0 and 3.")
else:
    if rating < 2:
        print("You are authorized to purchase tickets for this movie.")
    else:
        age = int(input("Enter your age: "))
        if rating == 2 and age < 13:
            print("You are not authorized to purchase tickets for this movie without a parent or adult guardian.")
        elif rating == 3 and age < 17:
            print("You are not authorized to purchase tickets for this movie without a parent or adult guardian.")
        else:
            print("You are authorized to purchase tickets for this movie.")
