import tkinter as tk
import random

# Create the Card class to represent a playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Create the Deck class to represent a deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

# Create the Hand class to represent a player's hand
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    
    def add_card(self, card):
        self.cards.append(card)
        # Yup, Ace only has the value of 1 in this variation of Blackjack
        if card.rank == "Ace":
            self.value += 1
        elif card.rank in ["Jack", "Queen", "King"]:
            self.value += 10
        else:
            self.value += int(card.rank)
    
    def __str__(self):
        hand_string = ""
        for card in self.cards:
            hand_string += str(card) + "\n"
        return hand_string

# Create the Blackjack class to represent the game
class Blackjack:
    def __init__(self, window):
        # Create the deck and shuffle it
        self.deck = Deck()
        self.deck.shuffle()
        
        # Create the player's and dealer's hands
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        # Deal the initial cards
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        
        # Check if any player has achieved blackjack
        if self.player_hand.value == 21:
            self.end_game("You win!")
        if self.dealer_hand.value == 21:
            self.end_game("You lose!")

        # Create the GUI elements
        self.window = window
        self.player_label = tk.Label(window, text=str(self.player_hand))
        self.player_label.pack()
        self.player_value_label = tk.Label(window, text=f"Player Value: {self.player_hand.value}\n\n")
        self.player_value_label.pack()
        self.dealer_label = tk.Label(window, text=str(self.dealer_hand))
        self.dealer_label.pack()
        self.dealer_value_label = tk.Label(window, text=f"Dealer Value: {self.dealer_hand.value}")
        self.dealer_value_label.pack()
        self.hit_button = tk.Button(window, text="Hit", width=20, height=2, command=self.hit)
        self.hit_button.pack()
        self.stand_button = tk.Button(window, text="Stand", width=20, height=2, command=self.stand)
        self.stand_button.pack()
        self.replay_button = tk.Button(window, text="Replay", width=20, height=2, command=self.replay)
        
    def hit(self):
        # Add a card to the player's hand and update the GUI
        self.player_hand.add_card(self.deck.deal())
        self.player_label.config(text=str(self.player_hand))
        self.player_value_label.config(text=f"Player Value: {self.player_hand.value}\n\n")

        # check if the player has Blackjack
        if self.player_hand.value == 21:
            self.end_game("You win!")
        
        # Check if the player has busted
        if self.player_hand.value > 21:
            self.player_value_label.config(text=f"Player Value: {self.player_hand.value}\n\n")
            self.end_game("You busted!")
    
    def stand(self):
        # Reveal the dealer's hole card and update the GUI
        self.dealer_label.config(text=str(self.dealer_hand))
        
        # Keep hitting until the dealer has at least 17 points
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_label.config(text=str(self.dealer_hand))
            self.dealer_value_label.config(text=f"Dealer Value: {self.dealer_hand.value}")
        
        # Check if the dealer has busted
        if self.dealer_hand.value > 21:
            self.dealer_value_label.config(text=f"Dealer Value: {self.dealer_hand.value}")
            self.end_game("Dealer busted!")
        
        # Compare the player's and dealer's hands to determine the winner
        elif self.player_hand.value > self.dealer_hand.value:
            self.dealer_value_label.config(text=f"Dealer Value: {self.dealer_hand.value}")
            self.end_game("You win!")
        elif self.player_hand.value < self.dealer_hand.value:
            self.dealer_value_label.config(text=f"Dealer Value: {self.dealer_hand.value}")
            self.end_game("You lose!")
        else:
            self.dealer_value_label.config(text=f"Dealer Value: {self.dealer_hand.value}")
            self.end_game("It's a tie!")
    
    def end_game(self, message):
        # Display the final result and enable the replay button
        self.player_label.config(text=message)
        self.hit_button.config(state="disabled")
        self.stand_button.config(state="disabled")
        self.replay_button.pack()
    
    def replay(self):
        # Reset the game
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
    
        # Update the GUI
        self.player_label.config(text=str(self.player_hand))
        self.player_value_label.config(text=f"Player Value: {self.player_hand.value}\n\n")
        self.dealer_label.config(text=str(self.dealer_hand))
        self.dealer_value_label.config(text=f"Dealer Value: {self.dealer_hand.value}")
        self.hit_button.pack()
        self.hit_button.config(state="normal")
        self.stand_button.pack()
        self.stand_button.config(state="normal")
        self.replay_button.pack_forget()

        

# Create the main window and start the game
window = tk.Tk()
window.title("Blackjack")
game = Blackjack(window)

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the coordinates for the center of the screen
x = (screen_width/2) - (500/2)
y = (screen_height/2) - (300/2)

# Use the geometry() method to set the size and position of the window
window.geometry("300x300+%d+%d" % (x, y))

window.mainloop()