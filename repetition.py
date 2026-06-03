class RepetitionSystem:

    # Berechnet die Priorität einer Karteikarte
    # Höhere Priorität bedeutet häufigere Wiederholung
    @staticmethod
    def calculate_priority(card):

        # Gesamtanzahl aller beantworteten Fragen
        total_answers = (
            card.correct_answers +
            card.wrong_answers
        )

        # Neue Karten (ohne Antworten) bekommen höchste Priorität
        if total_answers == 0:
            return 10

        # Fehlerquote der Karte berechnen
        error_rate = (
            card.wrong_answers / total_answers
        )

        # Priorität basiert auf Fehlerquote:
        # je mehr Fehler, desto höher die Priorität
        priority = 1 + (error_rate * 10)

        return priority

    # Sortiert eine Liste von Karten nach Priorität
    # Karten mit höherer Priorität kommen zuerst
    @staticmethod
    def sort_cards(cards):
        return sorted(
            cards,
            key=RepetitionSystem.calculate_priority,
            reverse=True
        )