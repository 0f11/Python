"""Simple game of blackjack."""
from textwrap import dedent

import requests


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value, suit, code):
        self.code = code
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.code


class Hand:
    """Simple class for holding hand information."""

    def __init__(self):
        self.score = 0
        self.cards = []

    def add_card(self, card):
        if card == int:
            self.cards.append(card)
            self.score += int(card)
        if card == 'Jack' or 'Queen' or 'King':
            self.cards.append(10)
            self.score += 10
        if card == 'Ace' and self.score <= 10:
            self.cards.append(11)
            self.score += 11
        if card == 'Ace' and self.score > 10:
            self.cards.append(1)
            self.score += 1


class Deck:
    """Deck of cards. Provided via api over the network."""

    def __init__(self, shuffle=False):
        """
        Tell api to create a new deck.

        :param shuffle: if shuffle option is true, make new shuffled deck.
        """
        if shuffle == False:
            requests.get("https://deckofcardsapi.com/api/deck/new").json()
            self.deck_id = requests.get("https://deckofcardsapi.com/api/deck/new").json()['deck_id']

        if shuffle == True:
            requests.get("https://deckofcardsapi.com/api/deck/new/shuffle").json()
            self.deck_id = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle").json()['deck_id']
            self.is_shuffled = True

    def shuffle(self):
        """
        Shuffle the deck.
        """
        requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/shuffle")

    def draw(self):
        """
        Draw card from the deck.

        :return: card instance.
        """
        new_card = requests.get(f'https://deckofcardsapi.com/api/deck/{self.deck_id}/draw').json()['cards']
        Card.code = new_card['code']
        Card.suit = new_card['suit']
        Card.value = new_card['value']

        return Card


class BlackjackController:
    """Blackjack controller. For controlling the game and data flow between view and database."""

    def __init__(self, deck: Deck, view: 'BlackjackView'):
        """
        Start new blackjack game.

        :param deck: deck to draw cards from.
        :param view: view to communicate with.
        """
        deck.shuffle(deck.deck_id)





class BlackjackView:
    """Minimalistic UI/view for the blackjack game."""

    def ask_next_move(self, state: dict) -> str:
        """
        Get next move from the player.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :return: parsed command that user has choses. String "H" for hit and "S" for stand
        """
        self.display_state(state)
        while True:
            action = input("Choose your next move hit(H) or stand(S) > ")
            if action.upper() in ["H", "S"]:
                return action.upper()
            print("Invalid command!")

    def player_lost(self, state):
        """
        Display player lost dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You lost")

    def player_won(self, state):
        """
        Display player won dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You won")

    def display_state(self, state, final=False):
        """
        Display state of the game for the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :param final: boolean if the given state is final state. True if game has been lost or won.
        """
        dealer_score = state["dealer"].score if final else "??"
        dealer_cards = state["dealer"].cards
        if not final:
            dealer_cards_hidden_last = [c.__repr__() for c in dealer_cards[:-1]] + ["??"]
            dealer_cards = f"[{','.join(dealer_cards_hidden_last)}]"

        player_score = state["player"].score
        player_cards = state["player"].cards
        print(dedent(
            f"""
            {"Dealer score":<15}: {dealer_score}
            {"Dealer hand":<15}: {dealer_cards}

            {"Your score":<15}: {player_score}
            {"Your hand":<15}: {player_cards}
            """
        ))


if __name__ == '__main__':
    BlackjackController(Deck(), BlackjackView())  # start the game.
