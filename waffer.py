points = 174 
points = 174 # use this input when submitting your answer

#set prize to default vale of none
prize = None

#use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <=180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

#use the truth value of prize to assign result to the correct message
if prize: 
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)