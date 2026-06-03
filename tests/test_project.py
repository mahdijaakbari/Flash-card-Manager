import os
import tempfile
import unittest

from flashcard import Flashcard
from manager import FlashcardManager
from storage import Storage
from cardstatistics import Statistics
from repetition import RepetitionSystem


# Testet die Klasse Flashcard
# Diese Klasse prüft das Erstellen, Bewerten und Umwandeln von Karteikarten
class TestFlashcard(unittest.TestCase):

    # Testet, ob eine Karteikarte richtig erstellt wird
    def test_create_flashcard(self):
        card = Flashcard("Question", "Answer", "Category")

        self.assertEqual(card.question, "Question")
        self.assertEqual(card.answer, "Answer")
        self.assertEqual(card.category, "Category")
        self.assertEqual(card.correct_answers, 0)
        self.assertEqual(card.wrong_answers, 0)

    # Testet, ob eine richtige Antwort gezählt wird
    def test_mark_correct(self):
        card = Flashcard("Q", "A", "C")
        card.mark_correct()

        self.assertEqual(card.correct_answers, 1)

    # Testet, ob eine falsche Antwort gezählt wird
    def test_mark_wrong(self):
        card = Flashcard("Q", "A", "C")
        card.mark_wrong()

        self.assertEqual(card.wrong_answers, 1)

    # Testet die Erfolgsquote bei keiner Antwort
    # Dadurch wird eine Division durch Null verhindert
    def test_success_rate_zero_answers(self):
        card = Flashcard("Q", "A", "C")

        self.assertEqual(card.success_rate(), 0)

    # Testet die Erfolgsquote bei richtigen und falschen Antworten
    def test_success_rate_with_answers(self):
        card = Flashcard("Q", "A", "C")
        card.mark_correct()
        card.mark_wrong()

        self.assertEqual(card.success_rate(), 50)

    # Testet die Umwandlung einer Karteikarte in ein Dictionary
    def test_to_dict(self):
        card = Flashcard("Q", "A", "C")
        data = card.to_dict()

        self.assertEqual(data["question"], "Q")
        self.assertEqual(data["answer"], "A")
        self.assertEqual(data["category"], "C")
        self.assertEqual(data["correct_answers"], 0)
        self.assertEqual(data["wrong_answers"], 0)

    # Testet das Erstellen einer Karteikarte aus einem Dictionary
    def test_from_dict(self):
        data = {
            "question": "Q",
            "answer": "A",
            "category": "C",
            "correct_answers": 2,
            "wrong_answers": 1
        }

        card = Flashcard.from_dict(data)

        self.assertEqual(card.question, "Q")
        self.assertEqual(card.answer, "A")
        self.assertEqual(card.category, "C")
        self.assertEqual(card.correct_answers, 2)
        self.assertEqual(card.wrong_answers, 1)


# Testet die Klasse FlashcardManager
# Diese Klasse prüft das Hinzufügen, Löschen, Suchen und Bearbeiten von Karten
class TestFlashcardManager(unittest.TestCase):

    # Testet das Hinzufügen einer Karte
    def test_add_card(self):
        manager = FlashcardManager()
        card = Flashcard("Q", "A", "C")

        manager.add_card(card)

        self.assertEqual(len(manager.get_all_cards()), 1)

    # Testet das erfolgreiche Entfernen einer Karte
    def test_remove_card_success(self):
        manager = FlashcardManager()
        card = Flashcard("Q", "A", "C")

        manager.add_card(card)
        result = manager.remove_card("Q")

        self.assertTrue(result)
        self.assertEqual(len(manager.get_all_cards()), 0)

    # Testet das Entfernen einer Karte, die nicht existiert
    def test_remove_card_not_found(self):
        manager = FlashcardManager()

        result = manager.remove_card("Unknown")

        self.assertFalse(result)

    # Testet das Suchen einer Karte anhand der Frage
    def test_find_card(self):
        manager = FlashcardManager()
        card = Flashcard("Q", "A", "C")

        manager.add_card(card)
        found = manager.find_card("Q")

        self.assertEqual(found, card)

    # Testet das Anzeigen von Karten einer bestimmten Kategorie
    def test_get_cards_by_category(self):
        manager = FlashcardManager()
        card1 = Flashcard("Q1", "A1", "German")
        card2 = Flashcard("Q2", "A2", "Sport")

        manager.add_card(card1)
        manager.add_card(card2)

        result = manager.get_cards_by_category("German")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].category, "German")

    # Testet das Bearbeiten einer Karte
    def test_edit_card(self):
        manager = FlashcardManager()
        card = Flashcard("Old Q", "Old A", "Old C")

        manager.add_card(card)

        result = manager.edit_card(
            "Old Q",
            "New Q",
            "New A",
            "New C"
        )

        self.assertTrue(result)
        self.assertEqual(card.question, "New Q")
        self.assertEqual(card.answer, "New A")
        self.assertEqual(card.category, "New C")


# Testet die Klasse Storage
# Diese Klasse prüft das Speichern und Laden von JSON-Dateien
class TestStorage(unittest.TestCase):

    # Testet, ob Karten gespeichert und wieder geladen werden können
    def test_save_and_load_file(self):
        card = Flashcard("Q", "A", "C")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp:
            filename = temp.name

        try:
            Storage.save_to_file([card], filename)
            loaded_cards = Storage.load_from_file(filename)

            self.assertEqual(len(loaded_cards), 1)
            self.assertEqual(loaded_cards[0].question, "Q")
            self.assertEqual(loaded_cards[0].answer, "A")
            self.assertEqual(loaded_cards[0].category, "C")

        finally:
            os.remove(filename)

    # Testet das Laden einer nicht vorhandenen Datei
    def test_load_missing_file(self):
        cards = Storage.load_from_file("file_that_does_not_exist.json")

        self.assertEqual(cards, [])

    # Testet das Laden einer fehlerhaften JSON-Datei
    def test_load_invalid_json_file(self):
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".json",
            mode="w"
        ) as temp:
            temp.write("invalid json")
            filename = temp.name

        try:
            cards = Storage.load_from_file(filename)

            self.assertEqual(cards, [])

        finally:
            os.remove(filename)


# Testet die Klasse Statistics
# Diese Klasse prüft die Berechnung von Statistiken
class TestStatistics(unittest.TestCase):

    # Testet die Gesamtanzahl der Karten
    def test_total_cards(self):
        cards = [
            Flashcard("Q1", "A1", "C1"),
            Flashcard("Q2", "A2", "C2")
        ]

        self.assertEqual(Statistics.total_cards(cards), 2)

    # Testet die Anzahl der Karten pro Kategorie
    def test_cards_per_category(self):
        cards = [
            Flashcard("Q1", "A1", "German"),
            Flashcard("Q2", "A2", "German"),
            Flashcard("Q3", "A3", "Sport")
        ]

        result = Statistics.cards_per_category(cards)

        self.assertEqual(result["German"], 2)
        self.assertEqual(result["Sport"], 1)

    # Testet die Erfolgsquote bei leerer Kartensammlung
    def test_overall_success_rate_zero(self):
        cards = []

        self.assertEqual(Statistics.overall_success_rate(cards), 0)

    # Testet die gesamte Erfolgsquote
    def test_overall_success_rate(self):
        card = Flashcard("Q", "A", "C")
        card.mark_correct()
        card.mark_wrong()

        result = Statistics.overall_success_rate([card])

        self.assertEqual(result, 50)

    # Testet die Erfolgsquote pro Kategorie
    def test_success_rate_per_category(self):
        card1 = Flashcard("Q1", "A1", "German")
        card1.mark_correct()

        card2 = Flashcard("Q2", "A2", "German")
        card2.mark_wrong()

        result = Statistics.success_rate_per_category([card1, card2])

        self.assertEqual(result["German"], 50)

    # Testet die Liste schwieriger Karten
    def test_difficult_cards(self):
        card = Flashcard("Q", "A", "C")
        card.mark_wrong()

        result = Statistics.difficult_cards([card])

        self.assertEqual(len(result), 1)


# Testet die Klasse RepetitionSystem
# Diese Klasse prüft die Wiederholungslogik
class TestRepetitionSystem(unittest.TestCase):

    # Testet, ob neue Karten eine hohe Priorität bekommen
    def test_new_card_priority(self):
        card = Flashcard("Q", "A", "C")

        self.assertEqual(RepetitionSystem.calculate_priority(card), 10)

    # Testet, ob falsch beantwortete Karten eine höhere Priorität bekommen
    def test_wrong_card_has_high_priority(self):
        card = Flashcard("Q", "A", "C")
        card.mark_wrong()

        self.assertGreater(RepetitionSystem.calculate_priority(card), 10)

    # Testet, ob Karten nach Priorität sortiert werden
    def test_sort_cards_by_priority(self):
        easy = Flashcard("Easy", "A", "C")
        easy.mark_correct()

        hard = Flashcard("Hard", "A", "C")
        hard.mark_wrong()

        cards = RepetitionSystem.sort_cards([easy, hard])

        self.assertEqual(cards[0].question, "Hard")


# Startet die Tests, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    unittest.main()