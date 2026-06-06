import unittest

from flashcard import Flashcard


# Testklasse für die Klasse Flashcard
# Hier werden die wichtigsten Funktionen einer Lernkarte geprüft
class TestFlashcard(unittest.TestCase):

    # Diese Methode wird vor jedem einzelnen Test ausgeführt
    # Dadurch hat jeder Test eine neue und unveränderte Karteikarte
    def setUp(self):
        self.card = Flashcard(
            "What is Python?",
            "Programming language",
            "Programming"
        )

    # Testet, ob eine Karteikarte richtig erstellt wird
    def test_create_flashcard(self):
        self.assertEqual(
            self.card.question,
            "What is Python?"
        )

        self.assertEqual(
            self.card.answer,
            "Programming language"
        )

        self.assertEqual(
            self.card.category,
            "Programming"
        )

    # Testet, ob eine richtige Antwort gezählt wird
    def test_mark_correct(self):
        self.card.mark_correct()

        self.assertEqual(
            self.card.correct_answers,
            1
        )

    # Testet, ob eine falsche Antwort gezählt wird
    def test_mark_wrong(self):
        self.card.mark_wrong()

        self.assertEqual(
            self.card.wrong_answers,
            1
        )

    # Testet, ob eine Karteikarte in ein Dictionary umgewandelt wird
    # Diese Funktion wird später beim Speichern als JSON gebraucht
    def test_to_dict(self):
        data = self.card.to_dict()

        self.assertEqual(
            data["question"],
            "What is Python?"
        )

        self.assertEqual(
            data["answer"],
            "Programming language"
        )

    # Testet, ob aus einem Dictionary wieder eine Karteikarte erstellt wird
    # Diese Funktion wird später beim Laden aus JSON gebraucht
    def test_from_dict(self):
        data = {
            "question": "Capital of Germany?",
            "answer": "Berlin",
            "category": "Geography",
            "correct_answers": 3,
            "wrong_answers": 1
        }

        card = Flashcard.from_dict(data)

        self.assertEqual(
            card.question,
            "Capital of Germany?"
        )

        self.assertEqual(
            card.answer,
            "Berlin"
        )

        self.assertEqual(
            card.correct_answers,
            3
        )

        self.assertEqual(
            card.wrong_answers,
            1
        )


# Startet die Tests, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    unittest.main()