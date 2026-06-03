import unittest

from flashcard import Flashcard
from manager import FlashcardManager


# Testet die Klasse FlashcardManager
# Diese Klasse prüft das Verwalten von Karteikarten
class TestFlashcardManager(unittest.TestCase):

    # Wird vor jedem Test ausgeführt
    # Erstellt einen neuen Manager und zwei Beispielkarten
    def setUp(self):
        self.manager = FlashcardManager()

        self.card1 = Flashcard(
            "What is Python?",
            "Programming language",
            "Programming"
        )

        self.card2 = Flashcard(
            "2 + 2",
            "4",
            "Math"
        )

    # Testet das Hinzufügen einer Karte
    def test_add_card(self):
        self.manager.add_card(self.card1)

        self.assertEqual(
            self.manager.total_cards(),
            1
        )

    # Testet das Entfernen einer vorhandenen Karte
    def test_remove_card(self):
        self.manager.add_card(self.card1)

        result = self.manager.remove_card(
            "What is Python?"
        )

        self.assertTrue(result)

        self.assertEqual(
            self.manager.total_cards(),
            0
        )

    # Testet das Entfernen einer nicht vorhandenen Karte
    # In diesem Fall soll False zurückgegeben werden
    def test_remove_nonexistent_card(self):
        result = self.manager.remove_card(
            "Unknown"
        )

        self.assertFalse(result)

    # Testet das Suchen einer vorhandenen Karte
    def test_find_card(self):
        self.manager.add_card(self.card1)

        card = self.manager.find_card(
            "What is Python?"
        )

        self.assertEqual(
            card.answer,
            "Programming language"
        )

    # Testet das Suchen einer nicht vorhandenen Karte
    # In diesem Fall soll None zurückgegeben werden
    def test_find_nonexistent_card(self):
        card = self.manager.find_card(
            "Unknown"
        )

        self.assertIsNone(card)

    # Testet das Anzeigen von Karten einer bestimmten Kategorie
    def test_get_cards_by_category(self):
        self.manager.add_card(self.card1)
        self.manager.add_card(self.card2)

        programming_cards = (
            self.manager.get_cards_by_category(
                "Programming"
            )
        )

        self.assertEqual(
            len(programming_cards),
            1
        )

        self.assertEqual(
            programming_cards[0].question,
            "What is Python?"
        )

    # Testet das Bearbeiten einer vorhandenen Karte
    def test_edit_card(self):
        self.manager.add_card(self.card1)

        result = self.manager.edit_card(
            "What is Python?",
            "What is Java?",
            "Programming language",
            "Programming"
        )

        self.assertTrue(result)

        edited_card = self.manager.find_card(
            "What is Java?"
        )

        self.assertIsNotNone(edited_card)

        self.assertEqual(
            edited_card.answer,
            "Programming language"
        )

    # Testet das Bearbeiten einer nicht vorhandenen Karte
    # In diesem Fall soll False zurückgegeben werden
    def test_edit_nonexistent_card(self):
        result = self.manager.edit_card(
            "Unknown",
            "New Question",
            "New Answer",
            "New Category"
        )

        self.assertFalse(result)


# Startet die Tests, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    unittest.main()