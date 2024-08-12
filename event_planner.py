#Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2

venue_add_ons = "Audio System" if attendees > 1000 else "projector"
print(venue_add_ons)

# Task 3

food = input("Do you want a vegetarian meal?")
venue_food = "Vegetarian Delight Caterers" if food == "yes" else "Gourmet Meals Caterers"
print(venue_food)