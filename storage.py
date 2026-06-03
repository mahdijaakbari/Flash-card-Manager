import json
from flashcard import Flashcard
import os

class Storage:

    # Speichert alle Karteikarten in einer JSON-Datei
    @staticmethod
    def save_to_file(cards, filename):

        # Wandelt alle Flashcard-Objekte in Dictionaries um
        data = [card.to_dict() for card in cards]

        # Öffnet die Datei im Schreibmodus und speichert die Daten
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    # Lädt Karteikarten aus einer JSON-Datei
    @staticmethod
    def load_from_file(filename):
        try:

            # Öffnet die Datei im Lesemodus.
            with open(filename, "r") as file:
                data = json.load(file)

            # Erstellt Flashcard-Objekte aus den geladenen Daten
            return [
                Flashcard.from_dict(card_data)
                for card_data in data
            ]

        # Fehlerbehandlung für nicht vorhandene Dateien
        except FileNotFoundError:
            print("File not found.")
            return []

        # Fehlerbehandlung für ungültige JSON-Dateien
        except json.JSONDecodeError:
            print("Invalid JSON file.")
            return []