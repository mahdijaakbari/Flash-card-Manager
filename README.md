# Lernkarten-Trainer

Name: Mahdija Akbari, Simla Karadeniz, Tim Treibert, Sareh Sheidaei, Mouod Nikmanesh  
Gruppe: BCSM206 - Team C9

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![Storage](https://img.shields.io/badge/Storage-JSON-orange)
![Tests](https://img.shields.io/badge/Tests-44%20passed-brightgreen)
![Status](https://img.shields.io/badge/Status-Student%20Project-purple)

---

## 1. Einleitung

### Ziel der Arbeit

Ziel dieser Arbeit ist die Entwicklung eines einfachen **Lernkarten-Trainers in Python**.

Mit dem Programm können Lernkarten erstellt, gespeichert, geladen, bearbeitet und gelöscht werden. Außerdem kann eine Lernsession durchgeführt werden. Nach jeder Karte wird gespeichert, ob die Antwort richtig oder falsch war.

Eine Lernkarte besteht aus:

- Frage
- Antwort
- Kategorie
- Anzahl richtiger Antworten
- Anzahl falscher Antworten

Ein weiterer Schwerpunkt der Arbeit ist das systematische Testen des Programms. Dafür wurden automatisierte Tests mit `unittest` erstellt.

---

## 2. Anforderungen und Entwurf

### Wichtigste Funktionen

Das Programm bietet folgende Funktionen:

- Neue Lernkarten hinzufügen
- Alle Lernkarten anzeigen
- Lernkarten bearbeiten
- Lernkarten löschen
- Lernkarten nach Kategorie anzeigen
- Lernsession durchführen
- Richtige und falsche Antworten speichern
- Wiederholungslogik verwenden
- Statistiken anzeigen
- Daten dauerhaft in einer JSON-Datei speichern

Das Programm besitzt zusätzlich eine einfache grafische Benutzeroberfläche mit `tkinter`. Dadurch kann der Benutzer das Programm mit Buttons bedienen, ohne Zahlen im Terminal eingeben zu müssen.

---

### Entwurf der Benutzeroberfläche

Die Benutzeroberfläche wurde mit `tkinter` umgesetzt. Sie besteht aus einem Hauptfenster mit mehreren Buttons. Jeder Button startet eine bestimmte Funktion des Lernkarten-Trainers.

Im Hauptmenü gibt es folgende Optionen:

- Add Card
- Show All Cards
- Edit Card
- Delete Card
- Show Cards by Category
- Study Session
- Show Statistics
- Save and Exit

Dadurch ist die Bedienung übersichtlich und einfach.

---

### Vorschau der Oberfläche

#### Hauptmenü

Das Hauptmenü zeigt alle wichtigen Funktionen des Programms. Der Benutzer kann jede Funktion direkt mit einem Button starten.

![](https://codi.ide3.de/uploads/8d53e431-894e-4c20-8b9d-c20574a3a045.PNG)

---

#### Karte hinzufügen

Über dieses Fenster kann eine neue Lernkarte mit Frage, Antwort und Kategorie erstellt werden.

![](https://codi.ide3.de/uploads/0fcbb396-17eb-479c-9577-10bec7e58c0b.PNG)

---

#### Alle Karten anzeigen

Alle gespeicherten Lernkarten werden übersichtlich in einer Tabelle angezeigt.

![](https://codi.ide3.de/uploads/74fafac6-72d3-4337-a4ff-2e4bf2fdf112.PNG)

---

#### Karten nach Kategorie anzeigen

Der Benutzer kann eine Kategorie eingeben und nur die passenden Lernkarten anzeigen lassen.

![](https://codi.ide3.de/uploads/c690b1b5-d8d0-4228-bd4f-ffd496eafdae.PNG)

---

#### Lernsession

In der Lernsession wird zuerst die Frage angezeigt. Danach kann der Benutzer die Antwort anzeigen lassen und entscheiden, ob seine Antwort richtig oder falsch war.

![](https://codi.ide3.de/uploads/d69f82e3-8fe0-4e80-9398-8d573db6aa30.PNG)

---

#### Statistiken

Das Statistikfenster zeigt wichtige Informationen über den Lernfortschritt, zum Beispiel die Anzahl der Karten, Erfolgsquoten und schwierige Karten.

![](https://codi.ide3.de/uploads/b58f9e39-da54-45bb-aeb2-c138f6ff264a.PNG)

---

### Gewählte Wiederholungslogik

Die Wiederholungslogik basiert auf einer einfachen Priorität.

Neue Karten bekommen eine hohe Priorität, weil sie noch nicht gelernt wurden.

Bei bereits beantworteten Karten wird die Fehlerquote berechnet:

```text
Fehlerquote = falsche Antworten / alle Antworten
```

Je höher die Fehlerquote ist, desto höher ist die Priorität der Karte. Dadurch werden schwierige Karten häufiger angezeigt. Karten mit vielen richtigen Antworten bekommen eine niedrigere Priorität.

Diese Logik befindet sich in der Datei `repetition.py`.

---

### Speicherformat

Die Lernkarten werden im JSON-Format gespeichert.

Die Speicherdatei befindet sich im Ordner:

```text
data/cards.json
```

Eine Lernkarte wird zum Beispiel so gespeichert:

```json
{
    "question": "Was ist Python?",
    "answer": "Eine Programmiersprache",
    "category": "Programmierung",
    "correct_answers": 2,
    "wrong_answers": 1
}
```

Das JSON-Format wurde gewählt, weil es einfach lesbar ist und gut zu Python-Dictionaries passt.

---

## 3. Implementierung

### Überblick über die technische Umsetzung

Das Projekt wurde in mehrere Python-Dateien aufgeteilt:

```text
main.py
flashcard.py
manager.py
storage.py
cardstatistics.py
repetition.py
```

Die Datei `main.py` startet das Programm und enthält die grafische Oberfläche.

Die Datei `flashcard.py` enthält die Klasse `Flashcard`. Diese Klasse beschreibt eine einzelne Lernkarte mit Frage, Antwort, Kategorie und Statistikwerten.

Die Datei `manager.py` enthält die Klasse `FlashcardManager`. Diese Klasse verwaltet alle Lernkarten, zum Beispiel Hinzufügen, Löschen, Suchen und Bearbeiten.

Die Datei `storage.py` enthält die Klasse `Storage`. Diese Klasse speichert und lädt die Karten aus der JSON-Datei.

Die Datei `cardstatistics.py` enthält die Klasse `Statistics`. Diese Klasse berechnet Statistiken wie Anzahl der Karten, Erfolgsquote und schwierige Karten.

Die Datei `repetition.py` enthält die Klasse `RepetitionSystem`. Diese Klasse berechnet die Priorität der Karten für die Lernsession.

---

### Projektstruktur

```text
project/
│
├── main.py
├── flashcard.py
├── manager.py
├── storage.py
├── cardstatistics.py
├── repetition.py
├── requirements.txt
├── README.md
│
├── data/
│   └── cards.json
│
├── picture/
│   ├── add_card.png
│   ├── all_cards.png
│   ├── category_cards.png
│   ├── menu.png
│   ├── statistics.png
│   └── study.png
│
└── tests/
    ├── test_flashcard.py
    ├── test_manager.py
    ├── test_project.py
    ├── test_repetition.py
    ├── test_statistics.py
    └── test_storage.py
```

---

### Beschreibung der wichtigsten Dateien

#### `flashcard.py`

Diese Datei enthält die Klasse `Flashcard`.

Wichtige Methoden:

- `mark_correct()`
- `mark_wrong()`
- `success_rate()`
- `to_dict()`
- `from_dict()`

---

#### `manager.py`

Diese Datei enthält die Klasse `FlashcardManager`.

Wichtige Methoden:

- `add_card()`
- `remove_card()`
- `edit_card()`
- `find_card()`
- `get_all_cards()`
- `get_cards_by_category()`

---

#### `storage.py`

Diese Datei enthält die Klasse `Storage`.

Wichtige Methoden:

- `save_to_file()`
- `load_from_file()`

Fehlerhafte oder nicht vorhandene Dateien werden abgefangen, damit das Programm nicht abstürzt.

---

#### `cardstatistics.py`

Diese Datei enthält die Klasse `Statistics`.

Beispiele für berechnete Statistiken:

- Gesamtanzahl aller Karten
- Anzahl der Karten pro Kategorie
- Erfolgsquote insgesamt
- Erfolgsquote pro Kategorie
- Schwierige Karten

---

#### `repetition.py`

Diese Datei enthält die Klasse `RepetitionSystem`.

Sie berechnet die Priorität der Karten. Karten mit hoher Fehlerquote bekommen eine höhere Priorität.

---

### Besondere Entwurfsentscheidungen

Eine wichtige Entscheidung war, das Programm in mehrere Klassen aufzuteilen. Dadurch ist der Code übersichtlicher und einfacher zu testen.

Außerdem wurde `tkinter` für die grafische Oberfläche verwendet. Der Vorteil ist, dass `tkinter` bereits in Python enthalten ist. Deshalb werden keine externen Bibliotheken benötigt.

Für die Speicherung wurde JSON verwendet, weil dieses Format einfach, verständlich und gut testbar ist.

Die Fehlerbehandlung beim Laden fehlerhafter oder nicht vorhandener Dateien wurde so umgesetzt, dass das Programm nicht abstürzt. Stattdessen wird eine leere Liste zurückgegeben.

---

## 4. Teststrategie

### Welche Testarten wurden verwendet?

Für das Projekt wurden automatisierte Unit-Tests mit `unittest` verwendet.

`unittest` ist eine Standardbibliothek von Python. Deshalb musste keine zusätzliche Bibliothek installiert werden.

Die Tests befinden sich im Ordner `tests/`:

```text
tests/
├── test_flashcard.py
├── test_manager.py
├── test_project.py
├── test_repetition.py
├── test_statistics.py
└── test_storage.py
```

Die Tests können mit einem einzigen Befehl gestartet werden:

```bash
python -m unittest discover -s tests
```

Jede Testdatei prüft einen bestimmten Teil des Programms.

---

### Getestete Dateien und Funktionen

#### `test_flashcard.py`

Diese Datei testet die Klasse `Flashcard`.

Getestet wurden:

- Erstellen einer Lernkarte
- Speichern von Frage, Antwort und Kategorie
- Markieren einer richtigen Antwort
- Markieren einer falschen Antwort
- Umwandlung einer Karte in ein Dictionary
- Erstellen einer Karte aus einem Dictionary

Beispiel:

```python
def test_mark_correct(self):
    self.card.mark_correct()

    self.assertEqual(
        self.card.correct_answers,
        1
    )
```

Dieser Test prüft, ob die Anzahl der richtigen Antworten korrekt erhöht wird.

---

#### `test_manager.py`

Diese Datei testet die Klasse `FlashcardManager`.

Getestet wurden:

- Hinzufügen einer Karte
- Entfernen einer vorhandenen Karte
- Entfernen einer nicht vorhandenen Karte
- Suchen einer Karte
- Suchen einer nicht vorhandenen Karte
- Anzeigen von Karten nach Kategorie
- Bearbeiten einer Karte
- Bearbeiten einer nicht vorhandenen Karte

Beispiel:

```python
def test_remove_nonexistent_card(self):
    result = self.manager.remove_card(
        "Unknown"
    )

    self.assertFalse(result)
```

Dieser Test prüft, ob das Programm korrekt reagiert, wenn eine Karte gelöscht werden soll, die nicht existiert.

---

#### `test_storage.py`

Diese Datei testet die Klasse `Storage`.

Getestet wurden:

- Speichern und Laden von Karten
- Laden einer nicht vorhandenen Datei
- Laden einer fehlerhaften JSON-Datei
- Speichern und Laden einer leeren Liste

Beispiel:

```python
def test_load_nonexistent_file(self):
    cards = Storage.load_from_file(
        "does_not_exist.json"
    )

    self.assertEqual(cards, [])
```

Dieser Test prüft, ob das Programm beim Laden einer nicht vorhandenen Datei nicht abstürzt.

---

#### `test_statistics.py`

Diese Datei testet die Klasse `Statistics`.

Getestet wurden:

- Gesamtanzahl aller Karten
- Anzahl der Karten pro Kategorie
- Gesamte Erfolgsquote
- Erfolgsquote bei leerer Kartensammlung
- Erfolgsquote pro Kategorie
- Liste schwieriger Karten

Beispiel:

```python
def test_success_rate_empty_cards(self):
    rate = Statistics.overall_success_rate(
        []
    )

    self.assertEqual(
        rate,
        0
    )
```

Dieser Test prüft, ob bei einer leeren Kartensammlung keine Division durch Null entsteht.

---

#### `test_repetition.py`

Diese Datei testet die Klasse `RepetitionSystem`.

Getestet wurden:

- Priorität neuer Karten
- Priorität bei hoher Fehlerquote
- Priorität bei niedriger Fehlerquote
- Sortierung der Karten nach Priorität

Beispiel:

```python
def test_high_error_rate_priority(self):
    self.card1.correct_answers = 2
    self.card1.wrong_answers = 8

    priority = (
        RepetitionSystem.calculate_priority(
            self.card1
        )
    )

    self.assertGreater(
        priority,
        8
    )
```

Dieser Test prüft, ob eine Karte mit vielen falschen Antworten eine hohe Priorität bekommt.

---

#### `test_project.py`

Diese Datei enthält zusätzliche zusammenfassende Tests für mehrere wichtige Projektteile.

Sie prüft unter anderem:

- Flashcard-Funktionen
- Manager-Funktionen
- Speicherfunktionen
- Statistikfunktionen
- Wiederholungslogik

Diese Datei dient als zusätzlicher Gesamttest für das Projekt.

---

### Welche Randfälle wurden berücksichtigt?

Neben normalen Funktionen wurden auch Randfälle getestet.

Getestete Randfälle:

- Leere Kartensammlung
- Erfolgsquote ohne Antworten
- Laden einer nicht vorhandenen Datei
- Laden einer fehlerhaften JSON-Datei
- Speichern und Laden einer leeren Liste
- Entfernen einer nicht vorhandenen Karte
- Bearbeiten einer nicht vorhandenen Karte
- Sortierung von Karten mit unterschiedlicher Fehlerquote

Diese Tests sind wichtig, damit das Programm stabil bleibt und nicht abstürzt.

---

### Test der Benutzeroberfläche

Die grafische Benutzeroberfläche wurde zusätzlich manuell getestet.

Da GUI-Tests mit `tkinter` aufwendiger sind, wurde für das Interface ein händisch ausgeführter Test dokumentiert. Dabei wurden die wichtigsten Bedienabläufe der Oberfläche geprüft.

| Funktion | Testbeschreibung | Erwartetes Ergebnis | Ergebnis |
|---|---|---|---|
| Add Card | Eine neue Lernkarte wird über das Formular hinzugefügt. | Die Karte wird gespeichert und kann angezeigt werden. | Erfolgreich |
| Show All Cards | Der Button wird angeklickt. | Alle Karten erscheinen in einer Tabelle. | Erfolgreich |
| Show Cards by Category | Eine Kategorie wird eingegeben. | Nur Karten dieser Kategorie werden angezeigt. | Erfolgreich |
| Study Session | Eine Karte wird abgefragt und als richtig oder falsch markiert. | Die Werte `correct_answers` oder `wrong_answers` werden aktualisiert. | Erfolgreich |
| Show Statistics | Der Statistik-Button wird angeklickt. | Statistikfenster mit Kartenanzahl, Erfolgsquote und schwierigen Karten erscheint. | Erfolgreich |

Damit wurde überprüft, dass die grafische Oberfläche korrekt mit den vorhandenen Programmfunktionen verbunden ist.

---


---

## 5. Ergebnisse

### Aktueller Funktionsumfang

Das Programm kann aktuell:

- Lernkarten hinzufügen
- Lernkarten anzeigen
- Lernkarten bearbeiten
- Lernkarten löschen
- Karten nach Kategorie anzeigen
- Lernsession starten
- Antworten als richtig oder falsch markieren
- Statistiken anzeigen
- Daten in einer JSON-Datei speichern
- Daten aus einer JSON-Datei laden
- Karten nach Wiederholungspriorität sortieren

Die grafische Oberfläche zeigt die wichtigsten Funktionen über Buttons an.

---

### Testergebnisse

Die automatisierten Tests wurden mit folgendem Befehl gestartet:
![](https://codi.ide3.de/uploads/eb209654-3a89-42b9-9666-f378453561f2.png)

```bash
python -m unittest discover -s tests
```

Das Ergebnis war erfolgreich:

```text
Ran 44 tests in 0.033s

OK
```

Das bedeutet, dass alle 44 automatisierten Tests erfolgreich ausgeführt wurden. Die Aufgabenstellung fordert mindestens 15 automatisierte Tests. Mit 44 Tests wird diese Anforderung erfüllt.

Damit funktionieren die getesteten Klassen und Methoden korrekt.

---

### Bekannte Fehler oder offene Punkte

Aktuell sind keine kritischen Fehler bekannt.

Mögliche Verbesserungen für die Zukunft wären:

- Suchfunktion für Lernkarten
- Automatisches Speichern nach jeder Änderung
- Besseres Design der grafischen Oberfläche
- Export als CSV-Datei
- Mehr Einstellungen für die Lernsession
- Möglichkeit, Karten direkt in der Tabelle zu bearbeiten

---


## 6. Ergänzende Dokumentation der Benutzeroberfläche

Die Benutzeroberfläche wurde im Bericht durch mehrere Screenshots dokumentiert.  
Die Screenshots zeigen die wichtigsten Bedienbereiche des Programms:

- Hauptmenü
- Karte hinzufügen
- Alle Karten anzeigen
- Karten nach Kategorie anzeigen
- Lernsession
- Statistiken

Zusätzlich wurde die Benutzeroberfläche manuell getestet. Dabei wurde geprüft, ob die Buttons korrekt funktionieren und ob die Eingaben des Benutzers richtig verarbeitet werden.

Ein zusätzliches Video wurde nicht erstellt, da die Funktionsweise der Oberfläche durch Screenshots und den manuellen GUI-Test ausreichend dokumentiert ist.

---
## 7. Reflexion des KI-Einsatzes

Für dieses Projekt wurde ChatGPT als KI-Werkzeug verwendet.

Die KI wurde für folgende Aufgaben eingesetzt:

- Ideensammlung
- Refactoring
- Generierung von Testfällen
- Erstellung und Verbesserung der grafischen Oberfläche


---
## 8. Fazit

Der Lernkarten-Trainer ist ein kleines, aber vollständiges Python-Projekt.

Das Programm erfüllt die wichtigsten Anforderungen. Es kann Lernkarten verwalten, speichern, laden, abfragen und Statistiken anzeigen.

Besonders wichtig war nicht nur die Programmierung, sondern auch das Testen. Mit 44 automatisierten Tests wurde überprüft, ob die zentralen Funktionen korrekt arbeiten.

Beim nächsten Mal würde ich früher mit den Tests beginnen und die Benutzeroberfläche noch moderner gestalten.