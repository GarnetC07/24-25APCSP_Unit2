import turtle as trtl
import random as rand

# Initialize the screen
wn = trtl.Screen()
wn.bgcolor("white")
wn.title("Memory Card Game")

# Cards and variables
card_values = ["A", "B", "C", "D", "E", "F", "G", "H"] * 2  # 2 sets of 8 cards
rand.shuffle(card_values)  # Shuffle cards to randomize their positions

# Create lists to track the state of each card
flipped_cards = []  # Cards that have been flipped
matched_cards = []  # Cards that have been matched

# Card positions (4x4 grid layout) - create exactly 16 positions
card_positions = [
    (-250, 150), (-150, 150), (-50, 150), (50, 150),
    (-250, 50), (-150, 50), (-50, 50), (50, 50),
    (-250, -50), (-150, -50), (-50, -50), (50, -50),
    (-250, -150), (-150, -150), (-50, -150), (50, -150)
]

# Setup the turtle for drawing
card_turtle = trtl.Turtle()
card_turtle.shape("square")
card_turtle.shapesize(stretch_wid=4, stretch_len=4)
card_turtle.color("lightgray")
card_turtle.speed(0)
card_turtle.penup()

# Function to draw a card at a specific position
def draw_card(x, y, value, hide=True):
    card_turtle.goto(x, y)
    if hide:
        card_turtle.fillcolor("lightgray")  # Show hidden state
        card_turtle.stamp()
    else:
        card_turtle.fillcolor("white")  # Show flipped state
        card_turtle.stamp()
        card_turtle.write(value, font=("Arial", 16, "normal"))

# Function to draw all cards initially (hidden)
def draw_all_cards():
    for i, (x, y) in enumerate(card_positions):
        value = card_values[i]
        draw_card(x, y, value, hide=True)

# Function to check if the two flipped cards match
def check_for_match():
    global flipped_cards, matched_cards
    if len(flipped_cards) == 2:  # Only check if two cards are flipped
        i1, i2 = flipped_cards
        if card_values[i1] == card_values[i2]:
            matched_cards.append(i1)  # Add matched card indices to the matched list
            matched_cards.append(i2)
        flipped_cards = []  # Reset the flipped cards list

# Function to handle the click event (flip a card)
def flip_card(x, y):
    # Find the index of the card clicked
    card_index = -1
    for i, (cx, cy) in enumerate(card_positions):
        if abs(cx - x) < 50 and abs(cy - y) < 50:
            card_index = i
            break

    if card_index == -1 or card_index in flipped_cards or card_index in matched_cards:
        return  # Do nothing if the card is already flipped or matched

    # Flip the card
    flipped_cards.append(card_index)
    draw_card(card_positions[card_index][0], card_positions[card_index][1], card_values[card_index], hide=False)

    # Check for match if two cards have been flipped
    if len(flipped_cards) == 2:
        wn.ontimer(check_for_match, 500)  # Wait before checking for match

    # End game if all cards are matched
    if len(matched_cards) == len(card_values):
        draw_end_game()

# Function to display the game over message
def draw_end_game():
    card_turtle.goto(0, 0)
    card_turtle.color("black")
    card_turtle.write("You win!", align="center", font=("Arial", 30, "bold"))

# Add event listener for mouse click
wn.onclick(flip_card)

# Draw all cards at the start (hidden)
draw_all_cards()

# Start the game loop
wn.mainloop()
