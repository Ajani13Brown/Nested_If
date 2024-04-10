#Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))

if attendees > 100: venue = "large hall"
else: venue = "conference room"

print(venue)

#Task 2: Catering Choices

order=input("would you like to a vegetarian option? ")

print('I would recommend our Veggie Delight Caterers') if order == "yes" else print('in that case i would recommend Gourmet Meals Caterers')

