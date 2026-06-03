import unittest

from flashcard import Flashcard
from cardstatistics import Statistics


# Testet die Klasse Statistics
# Diese Klasse prüft die Berechnung verschiedener Statistiken
class TestStatistics(unittest.TestCase):

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
            "Capital of Germany?",
            "Berlin",
            "Geography"
        )

    # Testet die Gesamtanzahl aller Karteikarten
    def test_total_cards(self):
        cards = [
            self.card1,
            self.card2,
            self.card3
        ]

        self.assertEqual(
            Statistics.total_cards(cards),
            3
        )

    # Testet die Anzahl der Karten pro Kategorie
    def test_cards_per_category(self):
        cards = [
            self.card1,
            self.card2,
            self.card1
        ]

        result = Statistics.cards_per_category(
            cards
        )

        self.assertEqual(
            result["Programming"],
            2
        )

        self.assertEqual(
            result["Math"],
            1
        )

    # Testet die gesamte Erfolgsquote aller Karten
    def test_overall_success_rate(self):
        self.card1.correct_answers = 8
        self.card1.wrong_answers = 2

        self.card2.correct_answers = 4
        self.card2.wrong_answers = 1

        cards = [
            self.card1,
            self.card2
        ]

        rate = Statistics.overall_success_rate(
            cards
        )

        self.assertEqual(
            rate,
            80.0
        )

    # Testet die Erfolgsquote bei leerer Kartensammlung
    # Dadurch wird eine Division durch Null verhindert
    def test_success_rate_empty_cards(self):
        rate = Statistics.overall_success_rate(
            []
        )

        self.assertEqual(
            rate,
            0
        )

    # Testet die Erfolgsquote pro Kategorie
    def test_success_rate_per_category(self):
        self.card1.correct_answers = 8
        self.card1.wrong_answers = 2

        self.card2.correct_answers = 4
        self.card2.wrong_answers = 1

        cards = [
            self.card1,
            self.card2
        ]

        result = Statistics.success_rate_per_category(
            cards
        )

        self.assertEqual(
            result["Programming"],
            80.0
        )

        self.assertEqual(
            result["Math"],
            80.0
        )

    # Testet die Liste schwieriger Karteikarten
    # Eine Karte gilt als schwierig, wenn sie mehr falsche als richtige Antworten hat
    def test_difficult_cards(self):
        self.card1.correct_answers = 2
        self.card1.wrong_answers = 5

        self.card2.correct_answers = 4
        self.card2.wrong_answers = 1

        cards = [
            self.card1,
            self.card2
        ]

        difficult = Statistics.difficult_cards(
            cards
        )

        self.assertEqual(
            len(difficult),
            1
        )

        self.assertEqual(
            difficult[0].question,
            "Python?"
        )


# Startet die Tests, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    unittest.main()