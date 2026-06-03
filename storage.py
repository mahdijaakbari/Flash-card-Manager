import json
from flashcard import Flashcard


class Storage:

    # Speichert alle Karteikarten in einer JSON-Datei
    @staticmethod
    def save_to_file(cards, filename):

        # Wandelt alle Flashcard-Objekte in Dictionaries um
        data = [card.to_dict() for card in cards]

        # Öffnet die Datei im Schreibmodus und speichert die Daten
        # UTF-8 ist wichtig für deutsche Sonderzeichen wie ä, ö, ü und ß
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # Lädt Karteikarten aus einer JSON-Datei
    @staticmethod
    def load_from_file(filename):
        try:

            # Öffnet die Datei im Lesemodus
            # UTF-8 verhindert falsche Zeichen wie ÃŸ oder Ã¼
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Prüft, ob die Datei eine Liste enthält
            if not isinstance(data, list):
                print("Invalid file format.")
                return []

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

        # Fehlerbehandlung für unvollständige oder falsche Daten
        except (KeyError, TypeError, ValueError):
            print("Invalid flashcard data.")
            return []