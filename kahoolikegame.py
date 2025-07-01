import random

# Willkommensnachricht
print("Dieser Teil richtet sich an den Lehrer")

# Anzahl der Fragen und Spieler (Anzahl der Fragen soll mindestens die Anzahl der Spieler)
# Anzahl der Spieler soll mindestens 1 sein
while True:
    Anzahl_der_Fragen = int(input("Wie viele Fragen würden Sie stellen? "))
    if Anzahl_der_Fragen <= 0:
        print("Stellen Sie bitte genug Fragen.")
        continue
    else:
        while True:
            Anzahl_der_Spieler = int(input("Wie viele sind Sie? "))
            if Anzahl_der_Spieler >= 1:
                break
            else:
                print("Bitte geben Sie eine gültige Anzahl von Spielern ein.")
                continue

        if Anzahl_der_Fragen >= Anzahl_der_Spieler:
            break
        else:
            print("Die Anzahl der Fragen sollte mindestens so groß wie die Anzahl der Spieler sein.")
            continue

# Überprüfung, ob jeder Spieler mindestens eine Frage hat
while Anzahl_der_Fragen < Anzahl_der_Spieler:
    print("Stellen Sie bitte genug Fragen, damit jeder Spieler mindestens eine Frage hat.")
    Anzahl_der_Fragen = int(input("Wie viele Fragen würden Sie stellen? "))

# Die Namen der Spieler werden abgefragt
Alle_Namen_der_Spieler = []
for i in range(Anzahl_der_Spieler):
    die_Name = input(f"Wie heißt der {i+1}. Spieler? ")
    Alle_Namen_der_Spieler.append(die_Name)

# Der Lehrer gibt Fragen und Antworten ein
Alle_Fragen = []
Alle_Lösungen = []
for i in range(Anzahl_der_Fragen):
    die_Frage = input(f"Bitte geben Sie die {i+1}. Frage ein: ")
    die_Lösung = input(f"Bitte geben Sie die Lösung für die {i+1}. Frage ein: ")
    Alle_Fragen.append(die_Frage)
    Alle_Lösungen.append(die_Lösung)

# Das beginn des Spiels
print("\nDas Spiel beginnt jetzt!\nHerzlich willkommen bei unserem Spiel 😍\nDrücken Sie die Eingabetaste, um zu beginnen")
input("")

# Es wird eine zufällige Frage an jedem Spieler gestellt
richrige_Lösungen_Liste = {name: 0 for name in Alle_Namen_der_Spieler}

for i in range(Anzahl_der_Fragen):
    for name in Alle_Namen_der_Spieler:
        if Alle_Fragen:
            zufällige_Frage = random.choice(Alle_Fragen)
            index_der_Frage = Alle_Fragen.index(zufällige_Frage)
            Alle_Fragen.remove(zufällige_Frage)
            aktuelle_Antwort = input(f"{name}, hier ist deine Frage: {zufällige_Frage}\nAntwort: ")
            richtige_antwort = Alle_Lösungen[index_der_Frage]
            if aktuelle_Antwort.lower() == richtige_antwort.lower():
                print("Richtig 🔥")
                richrige_Lösungen_Liste[name] += 1
            else:
                print("Falsch 🙁")

# Die Ergebnisse werden gegeben
print("\nDas Spiel ist vorbei! Hier sind die Ergebnisse:\n")
for name, punkte in richrige_Lösungen_Liste.items():
    print(f"{name}, du hast {punkte} Fragen von {Anzahl_der_Fragen // Anzahl_der_Spieler} richtig gelöst.")