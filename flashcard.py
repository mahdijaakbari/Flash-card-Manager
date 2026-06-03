class Flashcard:

    # Konstruktor der Karteikarte
    # Speichert Frage, Antwort und Kategorie
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer
        self.category = category

        # Anzahl der richtigen Antworten
        self.correct_answers = 0

        # Anzahl der falschen Antworten
        self.wrong_answers = 0

    # Erhöht die Anzahl der richtigen Antworten um 1
    def mark_correct(self):
        self.correct_answers += 1

    # Erhöht die Anzahl der falschen Antworten um 1
    def mark_wrong(self):
        self.wrong_answers += 1

    # Berechnet die Erfolgsquote der Karteikarte in Prozent
    def success_rate(self):
        total = self.correct_answers + self.wrong_answers

        # Verhindert eine Division durch Null
        if total == 0:
            return 0

        return (self.correct_answers / total) * 100

    # Wandelt das Objekt in ein Dictionary um
    # Wird für das Speichern als JSON verwendet
    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "category": self.category,
            "correct_answers": self.correct_answers,
            "wrong_answers": self.wrong_answers
        }

    # Erstellt ein Flashcard-Objekt aus einem Dictionary
    # Wird beim Laden von JSON-Daten verwendet
    @classmethod
    def from_dict(cls, data):
        if "question" not in data or "answer" not in data or "category" not in data:
            raise ValueError ("falshe flashcard data")
        card = cls(
            data["question"],
            data["answer"],
            data["category"]
        )

        # Übernimmt gespeicherte Statistikwerte
        card.correct_answers = data.get("correct_answers", 0)
        card.wrong_answers = data.get("wrong_answers", 0)

        return card