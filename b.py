import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.bgcolor("black")
wn.title("Memory_Cards")

# Named the cards and used ChatGpt to set the positions but will be changed later on
card_values = ['Joker', 'King', 'Queen', 'Jack', 'Ace', 'Spades', 'Hearts', 'Diamond'] * 2
rand.shuffle(card_values)  # Shuffle the card values so they appear randomly

card_positions = [(-150, 150), (-50, 150), (50, 150), (150, 150),
                  (-150, 50), (-50, 50), (50, 50), (150, 50),
                  (-150, -50), (-50, -50), (50, -50), (150, -50),
                  (-150, -150), (-50, -150), (50, -150), (150, -150)]

# Initialize variables
cards_flip = []  # List to store indices of flipped cards
card_match = []  # List to store indices of matched cards

# The card itself (unflipped)
memorycard_turtle = trtl.Turtle()
memorycard_turtle.speed('fastest')
memorycard_turtle.hideturtle()
memorycard_turtle.shape("square")
memorycard_turtle.shapesize(stretch_wid=4, stretch_len=3)
memorycard_turtle.color("white")
memorycard_turtle.penup()

# Draw a card (either face-up or face-down)
def draw_card(x, y, value, hide=True):
    memorycard_turtle.goto(x, y)
    if hide:
        memorycard_turtle.fillcolor("white")
        memorycard_turtle.stamp()
    else:
        memorycard_turtle.fillcolor("black")
        memorycard_turtle.stamp()
        memorycard_turtle.write(value, font=("Times New Roman", 18, "bold"))

# Draw all cards initially (hidden)
def draw_all_memorycards():
    for i, (x, y) in enumerate(card_positions):
        draw_card(x, y, "", hide=True)

#cite (chatgpt)
    # Function to check for matches
def check_match():
    global cards_flip
    if len(cards_flip) == 2:
        i1, i2 = cards_flip
        if card_values[i1] == card_values[i2]:
            card_match.append(i1)
            card_match.append(i2)
        else:
            # If cards don't match, hide them again
            memorycard_turtle.goto(card_positions[i1][0], card_positions[i1][1])
            memorycard_turtle.fillcolor("white")
            memorycard_turtle.stamp()
            memorycard_turtle.goto(card_positions[i2][0], card_positions[i2][1])
            memorycard_turtle.fillcolor("white")
            memorycard_turtle.stamp()
#End cite
        cards_flip = []  # Reset flipped cards list

    # Check if all cards have been matched
    if len(card_match) == len(card_values):
        draw_end_game()

# Function to handle the click event (flip a card)
def flip_card(x, y):
    global cards_flip

# Cited chatgpt:
    # Find the index of the card clicked
    card_index = -1
    for i, (cx, cy) in enumerate(card_positions):
        if abs(cx - x) < 50 and abs(cy - y) < 50:
            card_index = i
            break
# End Cite

    if card_index == -1 or card_index in card_match or card_index in cards_flip:
        return  # Do nothing if the card is already flipped or matched

    # Flip the card
    cards_flip.append(card_index)
    draw_card(card_positions[card_index][0], card_positions[card_index][1], card_values[card_index], hide=False)

    # Check for match if two cards have been flipped
    if len(cards_flip) == 2:
        wn.ontimer(check_match,  210)  # Wait before checking for match


# Function to display the game over message
def draw_end_game():
    memorycard_turtle.goto(0, 0)
    memorycard_turtle.color("black")

# Add event listener for mouse click
wn.onclick(flip_card)


# Draw all cards at the start (hidden)
draw_all_memorycards()

# Start the game loop
wn.mainloop()
