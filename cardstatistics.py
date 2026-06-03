class Statistics:

    # Gibt die Gesamtanzahl aller Karteikarten zurück
    @staticmethod
    def total_cards(cards):
        return len(cards)

    # Zählt die Anzahl der Karten pro Kategorie
    # Das Ergebnis wird als Dictionary zurückgegeben
    @staticmethod
    def cards_per_category(cards):
        result = {}

        for card in cards:
            category = card.category

            # Erstellt einen neuen Eintrag
            # falls die Kategorie noch nicht existiert
            if category not in result:
                result[category] = 0

            # Erhöht den Zähler der Kategorie um 1
            result[category] += 1

        return result

    # Berechnet die gesamte Erfolgsquote aller Karteikarten
    @staticmethod
    def overall_success_rate(cards):
        total_correct = 0
        total_answers = 0

        for card in cards:
            total_correct += card.correct_answers

            total_answers += (
                card.correct_answers +
                card.wrong_answers
            )

        # Verhindert eine Division durch Null
        if total_answers == 0:
            return 0

        return (total_correct / total_answers) * 100

    # Berechnet die Erfolgsquote für jede Kategorie
    # Das Ergebnis wird als Dictionary zurückgegeben
    @staticmethod
    def success_rate_per_category(cards):
        result = {}

        for card in cards:
            category = card.category

            # Erstellt einen neuen Eintrag für die Kategorie,
            # falls die Kategorie noch nicht existiert
            if category not in result:
                result[category] = {
                    "correct": 0,
                    "total": 0
                }

            # Addiert die richtigen Antworten der Kategorie
            result[category]["correct"] += card.correct_answers

            # Addiert alle Antworten der Kategorie
            result[category]["total"] += (
                card.correct_answers + card.wrong_answers
            )

        success_rates = {}

        for category, values in result.items():

            # Verhindert eine Division durch Null
            if values["total"] == 0:
                success_rates[category] = 0
            else:
                success_rates[category] = (
                    values["correct"] / values["total"]
                ) * 100

        return success_rates

    # Erstellt eine Liste mit schwierigen Karteikarten
    # Eine Karte gilt als schwierig
    # wenn mehr falsche als richtige Antworten vorliegen
    @staticmethod
    def difficult_cards(cards):
        difficult = []

        for card in cards:
            if card.wrong_answers > card.correct_answers:
                difficult.append(card)

        return difficult