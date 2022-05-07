#Treasure_Map
#Created by Cephas Cardozo
#Developed with 💖 using Python

#welcome_print
print("Welcome to the Treasure Map!")
print("Created by Cephas Cardozo")
print("Developed using Python")

#variables_lists
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1,row2,row3]

#print
print(f"{row1}\n{row2}\n{row3}")

#user_input
position = input("Where do you want to put the treasure?\n\nType here: ")

#variables
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[3-1]
selected_row[horizontal - 1] = "X"

#final_print
print(selected_row)