import unittest

from flashcard import Flashcard
from repetition import RepetitionSystem


# Testet die Klasse RepetitionSystem
# Diese Klasse prüft die Wiederholungslogik der Karteikarten
class TestRepetitionSystem(unittest.TestCase):

    # Wird vor jedem Test ausgeführt
    # Erstellt drei Beispielkarten für die Tests
    def setUp(self):
        self.card1 = Flashcard(
            "Python?",
            "Language",
            "Programming"
        )

        self.card2 = Flashcard(
            "2+2",
            "4",
            "Math"
        )

        self.card3 = Flashcard(
            "Berlin?",
            "Capital",
            "Geography"
        )

    # Testet, ob neue Karten eine hohe Priorität bekommen
    # Neue Karten haben noch keine richtigen oder falschen Antworten
    def test_new_card_priority(self):
        priority = (
            RepetitionSystem.calculate_priority(
                self.card1
            )
        )

        self.assertEqual(
            priority,
            10
        )

    # Testet Karten mit hoher Fehlerquote
    # Viele falsche Antworten sollen zu einer hohen Priorität führen
    def test_high_error_rate_priority(self):
        self.card1.correct_answers = 2
        self.card1.wrong_answers = 8

        priority = (
            RepetitionSystem.calculate_priority(
                self.card1
            )
        )

        self.assertGreater(
            priority,
            8
        )

    # Testet Karten mit niedriger Fehlerquote
    # Viele richtige Antworten sollen zu einer niedrigen Priorität führen
    def test_low_error_rate_priority(self):
        self.card1.correct_answers = 9
        self.card1.wrong_answers = 1

        priority = (
            RepetitionSystem.calculate_priority(
                self.card1
            )
        )

        self.assertLess(
            priority,
            3
        )

    # Testet die Sortierung der Karten nach Priorität
    # Die Karte mit mehr falschen Antworten soll zuerst erscheinen
    def test_sort_cards(self):
        self.card1.correct_answers = 8
        self.card1.wrong_answers = 2

        self.card2.correct_answers = 2
        self.card2.wrong_answers = 8

        cards = [
            self.card1,
            self.card2
        ]

        sorted_cards = (
            RepetitionSystem.sort_cards(
                cards
            )
        )

        self.assertEqual(
            sorted_cards[0],
            self.card2
        )


# Startet die Tests, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    unittest.main()