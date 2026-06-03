import unittest

from flashcard import Flashcard


class TestFlashcard(unittest.TestCase):

    def setUp(self):
        self.card = Flashcard(
            "What is Python?",
            "Programming language",
            "Programming"
        )

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

    def test_mark_correct(self):
        self.card.mark_correct()

        self.assertEqual(
            self.card.correct_answers,
            1
        )

    def test_mark_wrong(self):
        self.card.mark_wrong()

        self.assertEqual(
            self.card.wrong_answers,
            1
        )

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


if __name__ == "main":
    unittest.main()