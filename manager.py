from flashcard import Flashcard


class FlashcardManager:

    # Konstruktor des Managers
    # Erstellt eine leere Liste für alle Karteikarten
    def __init__(self):
        self.cards = []

    # Fügt eine neue Karteikarte zur Sammlung hinzu
    def add_card(self, card):
        self.cards.append(card)

    # Entfernt eine Karteikarte anhand der Frage
    # Gibt True zurück, wenn die Karte gefunden wurde
    def remove_card(self, question):
        for card in self.cards:
            if card.question == question:
                self.cards.remove(card)
                return True

        return False

    # Gibt alle gespeicherten Karteikarten zurück
    def get_all_cards(self):
        return self.cards

    # Gibt alle Karten einer bestimmten Kategorie zurück
    def get_cards_by_category(self, category):
        return [
            card for card in self.cards
            if card.category == category
        ]

    # Sucht eine Karteikarte anhand der Frage
    # Gibt die Karte zurück, falls sie gefunden wird
    def find_card(self, question):
        for card in self.cards:
            if card.question == question:
                return card

        return None
    def edit_card (self, old_question, new_question=None, new_answer=None, new_category=None):
        card = self.find_card(old_question)
        if card is None:
            return False
        if new_question  is not None:
            card.question= new_question

        if new_answer  is not None:
            card.answer= new_answer

        if new_category  is not None:
            card.category= new_category
        return True


    # Liefert die Gesamtanzahl aller Karteikarten
    def total_cards(self):
        return len(self.cards)