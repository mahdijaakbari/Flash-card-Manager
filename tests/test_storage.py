import unittest
import os

from flashcard import Flashcard
from storage import Storage


# Testet die Klasse Storage
# Diese Klasse prüft das Speichern und Laden von Karteikarten in JSON-Dateien
class TestStorage(unittest.TestCase):

    # Wird vor jedem Test ausgeführt
    # Erstellt einen Dateinamen und eine Beispielkarte
    def setUp(self):
        self.filename = "test_cards.json"

        self.card = Flashcard(
            "What is Python?",
            "Programming language",
            "Programming"
        )

    # Wird nach jedem Test ausgeführt
    # Löscht die Testdatei, falls sie erstellt wurde
    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    # Testet, ob eine Karte gespeichert und wieder geladen werden kann
    def test_save_and_load_cards(self):
        Storage.save_to_file(
            [self.card],
            self.filename
        )

        loaded_cards = Storage.load_from_file(
            self.filename
        )

        self.assertEqual(
            len(loaded_cards),
            1
        )

        self.assertEqual(
            loaded_cards[0].question,
            "What is Python?"
        )

        self.assertEqual(
            loaded_cards[0].answer,
            "Programming language"
        )

        self.assertEqual(
            loaded_cards[0].category,
            "Programming"
        )

    # Testet das Laden einer Datei, die nicht existiert
    # Das Programm soll dabei nicht abstürzen
    def test_load_nonexistent_file(self):
        cards = Storage.load_from_file(
            "does_not_exist.json"
        )

        self.assertEqual(cards, [])

    # Testet das Laden einer fehlerhaften JSON-Datei
    # Das Programm soll eine leere Liste zurückgeben
    def test_load_invalid_json(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write("{ invalid json }")

        cards = Storage.load_from_file(
            self.filename
        )

        self.assertEqual(cards, [])

    # Testet das Speichern und Laden einer leeren Liste
    def test_save_empty_list(self):
        Storage.save_to_file(
            [],
            self.filename
        )

        loaded_cards = Storage.load_from_file(
            self.filename
        )

        self.assertEqual(
            loaded_cards,
            []
        )


# Startet die Tests, wenn diese Datei direkt ausgeführt wird
if __name__ == "__main__":
    unittest.main()