import random
import time

# Define the cards using a list of dictionaries
card_deck = [
    {"Name": "Diablo", "Health": 100, "Attack": 90, "Defense": 60},
    {"Name": "Medusa", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Jester", "Health": 120, "Attack": 60, "Defense": 90},
    {"Name": "Troll", "Health": 150, "Attack": 40, "Defense": 94},
    {"Name": "Specter", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Mist", "Health": 100, "Attack": 75, "Defense": 65},
    {"Name": "Savage", "Health": 100, "Attack": 90, "Defense": 50},
    {"Name": "Marauder", "Health": 100, "Attack": 85, "Defense": 50},
    {"Name": "Wimp", "Health": 110, "Attack": 40, "Defense": 85},
    {"Name": "Sorcerer", "Health": 100, "Attack": 70, "Defense": 55}
]


# Function to print card details
def print_card(card):
    print(f"Name: {card['Name']}")
    print(f"Health: {card['Health']}")
    print(f"Attack: {card['Attack']}")
    print(f"Defense: {card['Defense']}\n")


# Function to simulate a round of combat
def fight(player_deck, opponent_deck):
    # Randomly select a card for the opponent
    opponent_card = random.choice(opponent_deck)
    print("Opponent's card:")
    print_card(opponent_card)

    # Show player's cards
    print("Your cards:")
    for card in player_deck:
        print_card(card)
        time.sleep(1)  # Pause for visibility

    # Player selects a card to fight
    player_choice = int(input("Choose a card by index (0-indexed) to fight: ")) % len(player_deck)
    player_card = player_deck[player_choice]

    print("You have chosen:")
    print_card(player_card)

    # Combat logic
    damage = max(player_card['Attack'] - opponent_card['Defense'], 0)
    opponent_card['Health'] -= damage
    opponent_card['Defense'] = max(opponent_card['Defense'] - player_card['Attack'], 0)

    print(f"{player_card['Name']} attacks {opponent_card['Name']}!")
    if opponent_card['Health'] <= 0:
        print(f"{opponent_card['Name']} is defeated!")
        opponent_deck.remove(opponent_card)
    else:
        print(
            f"{opponent_card['Name']} now has {opponent_card['Health']} Health and {opponent_card['Defense']} Defense left.")

    # Pause before opponent's turn
    time.sleep(3)
    print("Opponent's turn...")

    # Opponent's attack (simplified logic for demonstration)
    if opponent_deck:
        opponent_choice = random.choice(opponent_deck)
        damage = max(opponent_choice['Attack'] - player_card['Defense'], 0)
        player_card['Health'] -= damage
        player_card['Defense'] = max(player_card['Defense'] - opponent_choice['Attack'], 0)

        print(f"{opponent_choice['Name']} attacks {player_card['Name']}!")
        if player_card['Health'] <= 0:
            print(f"{player_card['Name']} is defeated!")
            player_deck.remove(player_card)
        else:
            print(
                f"{player_card['Name']} now has {player_card['Health']} Health and {player_card['Defense']} Defense left.")


# Initialize decks
deck_size = 5
player_deck = random.sample(card_deck, deck_size)
opponent_deck = random.sample(card_deck, deck_size)

# Game loop
while player_deck and opponent_deck:
    fight(player_deck, opponent_deck)

# Determine the winner
if not opponent_deck:
    print("Congratulations! You are the winner!")
else:
    print("Sorry, the opponent has won.")