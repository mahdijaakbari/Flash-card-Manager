from flashcard import Flashcard
from manager import FlashcardManager
from storage import Storage
from cardstatistics import Statistics
from repetition import RepetitionSystem

import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


# Zentrale Instanz des Managers
# Hier werden alle Karteikarten während der Programmlaufzeit verwaltet
manager = FlashcardManager()

# Datei, in der die Karteikarten dauerhaft gespeichert werden
FILENAME = "data/cards.json"


# Lädt alle gespeicherten Karteikarten aus der JSON-Datei
# und fügt sie dem Manager hinzu
def load_cards():
    cards = Storage.load_from_file(FILENAME)

    for card in cards:
        manager.add_card(card)


# Speichert alle aktuellen Karteikarten in der JSON-Datei
# Falls der Ordner data noch nicht existiert, wird er erstellt
def save_cards():
    os.makedirs("data", exist_ok=True)

    Storage.save_to_file(
        manager.get_all_cards(),
        FILENAME
    )


# Zentriert ein Fenster auf dem Bildschirm
# Dadurch erscheint jedes Fenster optisch besser positioniert
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


# Erstellt ein neues Fenster mit einer Tabelle
# Diese Funktion wird für "Show All Cards" und Kategorien benutzt
def create_table_window(title, cards):
    window = tk.Toplevel()
    window.title(title)
    center_window(window, 900, 450)

    # Überschrift des Fensters
    header = tk.Label(
        window,
        text=title,
        font=("Arial", 18, "bold")
    )
    header.pack(pady=10)

    # Spalten der Tabelle
    columns = (
        "question",
        "answer",
        "category",
        "correct",
        "wrong",
        "success"
    )

    # Erstellt die Tabelle
    table = ttk.Treeview(
        window,
        columns=columns,
        show="headings",
        height=14
    )

    # Namen der Spalten
    table.heading("question", text="Question")
    table.heading("answer", text="Answer")
    table.heading("category", text="Category")
    table.heading("correct", text="Correct")
    table.heading("wrong", text="Wrong")
    table.heading("success", text="Success Rate")

    # Breite und Ausrichtung der Spalten
    table.column("question", width=230)
    table.column("answer", width=230)
    table.column("category", width=130)
    table.column("correct", width=80, anchor="center")
    table.column("wrong", width=80, anchor="center")
    table.column("success", width=120, anchor="center")

    # Fügt alle Karteikarten in die Tabelle ein
    for card in cards:
        table.insert(
            "",
            "end",
            values=(
                card.question,
                card.answer,
                card.category,
                card.correct_answers,
                card.wrong_answers,
                f"{card.success_rate():.2f}%"
            )
        )

    table.pack(expand=True, fill="both", padx=15, pady=10)

    # Button zum Schließen des Fensters
    close_button = tk.Button(
        window,
        text="Close",
        width=15,
        command=window.destroy
    )
    close_button.pack(pady=10)


# Öffnet ein Fenster zum Hinzufügen einer neuen Karteikarte
def add_card():
    window = tk.Toplevel()
    window.title("Add Card")
    center_window(window, 400, 300)
    window.resizable(False, False)

    # Überschrift
    tk.Label(
        window,
        text="Add New Card",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Formularbereich
    form = tk.Frame(window)
    form.pack(pady=10)

    # Eingabefeld für die Frage
    tk.Label(form, text="Question:", anchor="w").grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    question_entry = tk.Entry(form, width=35)
    question_entry.grid(row=0, column=1, pady=5)

    # Eingabefeld für die Antwort
    tk.Label(form, text="Answer:", anchor="w").grid(
        row=1,
        column=0,
        sticky="w",
        pady=5
    )

    answer_entry = tk.Entry(form, width=35)
    answer_entry.grid(row=1, column=1, pady=5)

    # Eingabefeld für die Kategorie
    tk.Label(form, text="Category:", anchor="w").grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    category_entry = tk.Entry(form, width=35)
    category_entry.grid(row=2, column=1, pady=5)

    # Speichert die neue Karteikarte
    def save_new_card():
        question = question_entry.get().strip()
        answer = answer_entry.get().strip()
        category = category_entry.get().strip()

        # Prüft, ob alle Felder ausgefüllt wurden
        if question == "" or answer == "" or category == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return

        card = Flashcard(question, answer, category)
        manager.add_card(card)

        messagebox.showinfo("Success", "Card added successfully.")
        window.destroy()

    # Button zum Speichern der Karte
    tk.Button(
        window,
        text="Save Card",
        width=20,
        command=save_new_card
    ).pack(pady=15)


# Zeigt alle gespeicherten Karteikarten in einer Tabelle an
def show_cards():
    cards = manager.get_all_cards()

    # Falls keine Karten vorhanden sind
    if not cards:
        messagebox.showinfo("Cards", "No cards available.")
        return

    create_table_window("All Cards", cards)


# Öffnet ein Fenster zum Bearbeiten einer Karteikarte
def edit_card():
    cards = manager.get_all_cards()

    # Bearbeiten ist nur möglich, wenn Karten existieren
    if not cards:
        messagebox.showinfo("Edit Card", "No cards available.")
        return

    window = tk.Toplevel()
    window.title("Edit Card")
    center_window(window, 900, 500)

    tk.Label(
        window,
        text="Select a card to edit",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Tabelle mit allen Karten
    columns = ("question", "answer", "category")
    table = ttk.Treeview(window, columns=columns, show="headings", height=10)

    table.heading("question", text="Question")
    table.heading("answer", text="Answer")
    table.heading("category", text="Category")

    table.column("question", width=300)
    table.column("answer", width=300)
    table.column("category", width=150)

    for card in cards:
        table.insert(
            "",
            "end",
            values=(card.question, card.answer, card.category)
        )

    table.pack(fill="both", expand=True, padx=15, pady=10)

    # Formular zum Bearbeiten der ausgewählten Karte
    form = tk.Frame(window)
    form.pack(pady=10)

    tk.Label(form, text="Question:").grid(
        row=0,
        column=0,
        pady=5,
        sticky="w"
    )

    question_entry = tk.Entry(form, width=45)
    question_entry.grid(row=0, column=1, pady=5)

    tk.Label(form, text="Answer:").grid(
        row=1,
        column=0,
        pady=5,
        sticky="w"
    )

    answer_entry = tk.Entry(form, width=45)
    answer_entry.grid(row=1, column=1, pady=5)

    tk.Label(form, text="Category:").grid(
        row=2,
        column=0,
        pady=5,
        sticky="w"
    )

    category_entry = tk.Entry(form, width=45)
    category_entry.grid(row=2, column=1, pady=5)

    # Speichert die ursprüngliche Frage der ausgewählten Karte
    selected_old_question = {"value": None}

    # Wird ausgeführt, wenn der Benutzer eine Karte auswählt
    def select_card(event):
        selected = table.focus()

        if not selected:
            return

        values = table.item(selected, "values")

        selected_old_question["value"] = values[0]

        # Alte Eingaben löschen
        question_entry.delete(0, tk.END)
        answer_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

        # Daten der ausgewählten Karte in die Felder einfügen
        question_entry.insert(0, values[0])
        answer_entry.insert(0, values[1])
        category_entry.insert(0, values[2])

    table.bind("<<TreeviewSelect>>", select_card)

    # Speichert die Änderungen an der Karteikarte
    def save_changes():
        if selected_old_question["value"] is None:
            messagebox.showerror("Error", "Please select a card first.")
            return

        new_question = question_entry.get().strip()
        new_answer = answer_entry.get().strip()
        new_category = category_entry.get().strip()

        if new_question == "" or new_answer == "" or new_category == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return

        manager.edit_card(
            selected_old_question["value"],
            new_question,
            new_answer,
            new_category
        )

        messagebox.showinfo("Success", "Card edited successfully.")
        window.destroy()

    tk.Button(
        window,
        text="Save Changes",
        width=20,
        command=save_changes
    ).pack(pady=10)


# Öffnet ein Fenster zum Löschen einer Karteikarte
def delete_card():
    cards = manager.get_all_cards()

    if not cards:
        messagebox.showinfo("Delete Card", "No cards available.")
        return

    window = tk.Toplevel()
    window.title("Delete Card")
    center_window(window, 800, 400)

    tk.Label(
        window,
        text="Select a card to delete",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Tabelle mit allen Karten
    columns = ("question", "answer", "category")
    table = ttk.Treeview(window, columns=columns, show="headings", height=12)

    table.heading("question", text="Question")
    table.heading("answer", text="Answer")
    table.heading("category", text="Category")

    table.column("question", width=300)
    table.column("answer", width=300)
    table.column("category", width=130)

    for card in cards:
        table.insert(
            "",
            "end",
            values=(card.question, card.answer, card.category)
        )

    table.pack(fill="both", expand=True, padx=15, pady=10)

    # Löscht die ausgewählte Karte
    def delete_selected():
        selected = table.focus()

        if not selected:
            messagebox.showerror("Error", "Please select a card first.")
            return

        values = table.item(selected, "values")
        question = values[0]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Do you really want to delete this card?\n\n{question}"
        )

        if confirm:
            manager.remove_card(question)
            table.delete(selected)
            messagebox.showinfo("Success", "Card deleted successfully.")

    tk.Button(
        window,
        text="Delete Selected Card",
        width=25,
        command=delete_selected
    ).pack(pady=10)


# Zeigt nur die Karten einer bestimmten Kategorie an
def show_cards_by_category():
    category = simpledialog.askstring("Category", "Enter category:")

    if not category:
        return

    cards = manager.get_cards_by_category(category)

    if not cards:
        messagebox.showinfo("Category", "No cards found in this category.")
        return

    create_table_window(f"Cards in Category: {category}", cards)


# Startet eine Lernsession
# Die Karten werden vorher nach Priorität sortiert
def study_session():
    cards = RepetitionSystem.sort_cards(
        manager.get_all_cards()
    )

    if not cards:
        messagebox.showinfo("Study Session", "No cards available.")
        return

    # Speichert den aktuellen Fortschritt der Lernsession
    session = {
        "index": 0,
        "cards": cards
    }

    window = tk.Toplevel()
    window.title("Study Session")
    center_window(window, 600, 380)
    window.resizable(False, False)

    title_label = tk.Label(
        window,
        text="Study Session",
        font=("Arial", 18, "bold")
    )
    title_label.pack(pady=10)

    progress_label = tk.Label(window, text="", font=("Arial", 11))
    progress_label.pack(pady=5)

    question_label = tk.Label(
        window,
        text="",
        font=("Arial", 14),
        wraplength=520,
        justify="center"
    )
    question_label.pack(pady=25)

    answer_label = tk.Label(
        window,
        text="",
        font=("Arial", 12),
        wraplength=520,
        justify="center"
    )
    answer_label.pack(pady=10)

    # Lädt die aktuelle Karte der Lernsession
    def load_current_card():
        index = session["index"]

        # Wenn alle Karten gelernt wurden, wird die Session beendet
        if index >= len(session["cards"]):
            messagebox.showinfo("Study Session", "Study session finished.")
            window.destroy()
            return

        card = session["cards"][index]

        progress_label.config(
            text=f"Card {index + 1} of {len(session['cards'])}"
        )

        question_label.config(text=f"Question:\n{card.question}")
        answer_label.config(text="Click 'Show Answer' to see the answer.")

    # Zeigt die Antwort der aktuellen Karte
    def show_answer():
        card = session["cards"][session["index"]]
        answer_label.config(text=f"Answer:\n{card.answer}")

    # Bewertet die aktuelle Karte als richtig
    def mark_correct():
        card = session["cards"][session["index"]]
        card.mark_correct()

        session["index"] += 1
        load_current_card()

    # Bewertet die aktuelle Karte als falsch
    def mark_wrong():
        card = session["cards"][session["index"]]
        card.mark_wrong()

        session["index"] += 1
        load_current_card()

    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Show Answer",
        width=15,
        command=show_answer
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Correct",
        width=15,
        command=mark_correct
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        button_frame,
        text="Wrong",
        width=15,
        command=mark_wrong
    ).grid(row=0, column=2, padx=5)

    load_current_card()


# Zeigt Statistiken in einem eigenen Fenster an
def show_statistics():
    cards = manager.get_all_cards()

    window = tk.Toplevel()
    window.title("Statistics")
    center_window(window, 700, 500)

    tk.Label(
        window,
        text="Statistics",
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    top_frame = tk.Frame(window)
    top_frame.pack(pady=10)

    total_cards = Statistics.total_cards(cards)
    overall_rate = Statistics.overall_success_rate(cards)

    # Anzeige der Gesamtanzahl der Karten
    tk.Label(
        top_frame,
        text=f"Total Cards\n{total_cards}",
        font=("Arial", 14),
        width=20,
        relief="groove",
        pady=10
    ).grid(row=0, column=0, padx=10)

    # Anzeige der gesamten Erfolgsquote
    tk.Label(
        top_frame,
        text=f"Overall Success Rate\n{overall_rate:.2f}%",
        font=("Arial", 14),
        width=25,
        relief="groove",
        pady=10
    ).grid(row=0, column=1, padx=10)

    # Notebook erzeugt mehrere Tabs für verschiedene Statistiken
    notebook = ttk.Notebook(window)
    notebook.pack(expand=True, fill="both", padx=15, pady=10)

    category_frame = tk.Frame(notebook)
    success_frame = tk.Frame(notebook)
    difficult_frame = tk.Frame(notebook)

    notebook.add(category_frame, text="Cards per Category")
    notebook.add(success_frame, text="Success per Category")
    notebook.add(difficult_frame, text="Difficult Cards")

    # Tabelle für die Anzahl der Karten pro Kategorie
    category_table = ttk.Treeview(
        category_frame,
        columns=("category", "count"),
        show="headings"
    )

    category_table.heading("category", text="Category")
    category_table.heading("count", text="Number of Cards")

    category_table.column("category", width=300)
    category_table.column("count", width=150, anchor="center")

    for category, count in Statistics.cards_per_category(cards).items():
        category_table.insert("", "end", values=(category, count))

    category_table.pack(expand=True, fill="both", padx=10, pady=10)

    # Tabelle für die Erfolgsquote pro Kategorie
    success_table = ttk.Treeview(
        success_frame,
        columns=("category", "rate"),
        show="headings"
    )

    success_table.heading("category", text="Category")
    success_table.heading("rate", text="Success Rate")

    success_table.column("category", width=300)
    success_table.column("rate", width=150, anchor="center")

    for category, rate in Statistics.success_rate_per_category(cards).items():
        success_table.insert("", "end", values=(category, f"{rate:.2f}%"))

    success_table.pack(expand=True, fill="both", padx=10, pady=10)

    # Tabelle für schwierige Karteikarten
    difficult_table = ttk.Treeview(
        difficult_frame,
        columns=("question", "category", "correct", "wrong"),
        show="headings"
    )

    difficult_table.heading("question", text="Question")
    difficult_table.heading("category", text="Category")
    difficult_table.heading("correct", text="Correct")
    difficult_table.heading("wrong", text="Wrong")

    difficult_table.column("question", width=350)
    difficult_table.column("category", width=150)
    difficult_table.column("correct", width=80, anchor="center")
    difficult_table.column("wrong", width=80, anchor="center")

    for card in Statistics.difficult_cards(cards):
        difficult_table.insert(
            "",
            "end",
            values=(
                card.question,
                card.category,
                card.correct_answers,
                card.wrong_answers
            )
        )

    difficult_table.pack(expand=True, fill="both", padx=10, pady=10)


# Speichert alle Karten und beendet das Programm
def save_and_exit(root):
    save_cards()
    messagebox.showinfo("Saved", "Cards saved successfully, Bye Bye.")
    root.destroy()


# Erstellt das Hauptfenster des Programms
def create_gui():
    load_cards()

    root = tk.Tk()
    root.title("Flashcard Trainer")
    center_window(root, 480, 620)
    root.resizable(False, False)

    # Einfaches Design für die Tabellen
    style = ttk.Style()
    style.theme_use("clam")

    # Haupttitel
    title = tk.Label(
        root,
        text="Flashcard Trainer",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    # Untertitel
    subtitle = tk.Label(
        root,
        text="Learning cards management system",
        font=("Arial", 11)
    )
    subtitle.pack(pady=5)

    # Bereich für die Buttons
    frame = tk.Frame(root)
    frame.pack(pady=25)

    # Liste aller Hauptfunktionen des Programms
    buttons = [
        ("Add Card", add_card),
        ("Show All Cards", show_cards),
        ("Edit Card", edit_card),
        ("Delete Card", delete_card),
        ("Show Cards by Category", show_cards_by_category),
        ("Study Session", study_session),
        ("Show Statistics", show_statistics),
        ("Save and Exit", lambda: save_and_exit(root))
    ]

    # Erstellt für jede Funktion einen Button
    for text, command in buttons:
        button = tk.Button(
            frame,
            text=text,
            command=command,
            width=32,
            height=2,
            font=("Arial", 11)
        )
        button.pack(pady=6)

    root.mainloop()


# Startpunkt des Programms
# Wenn main.py ausgeführt wird, startet die grafische Oberfläche
if __name__ == "__main__":
    create_gui()