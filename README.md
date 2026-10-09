# PasswortGenerator von IT-Janz

Ein lokaler Passwortgenerator mit grafischer Oberfläche, geschrieben in Python und Tkinter. Länge und verfügbare Zeichengruppen lassen sich anpassen.

**Kostenlos und frei nutzbar:** Unter der [MIT-Lizenz](LICENSE) darf jede Person das Projekt privat oder kommerziell verwenden, verändern und weitergeben. Lizenz- und Urheberrechtshinweise müssen erhalten bleiben.

## Voraussetzungen

- Python 3.10 oder neuer
- Tkinter und eine grafische Desktop-Umgebung
- Keine zusätzlichen Python-Pakete und kein Benutzerkonto

Ob Tkinter verfügbar ist, lässt sich mit `python -m tkinter` prüfen. Falls es fehlt, die Tkinter-Unterstützung der verwendeten Python-Installation ergänzen. Auf manchen Systemen heißt der Python-Befehl `python3` oder `py`.

## Herunterladen und starten

1. Über **Code → Download ZIP** das gesamte Repository herunterladen und entpacken.
2. Im entpackten Ordner ein Terminal öffnen.
3. Die Anwendung starten:

   ```sh
   python PassGen.py
   ```

`PassGen.py` und `password_generator.py` müssen im selben Ordner liegen. Alternativ kann das Repository mit Git geklont werden:

```sh
git clone https://github.com/MJnms1980/PasswortGenerator.git
cd PasswortGenerator
python PassGen.py
```

## Bedienung

1. Eine Länge zwischen 8 und 128 Zeichen wählen; voreingestellt sind 16.
2. Großbuchstaben, Kleinbuchstaben, Ziffern und/oder eigene Sonderzeichen auswählen.
3. Auf **Passwort generieren** klicken.
4. Das Passwort im Ausgabefeld markieren und kopieren.

Die aktivierten Zeichengruppen bilden den verfügbaren Zeichenvorrat. Nicht jede Gruppe ist zwingend in jedem Ergebnis enthalten. Falls ein Dienst bestimmte Gruppen verlangt, das Ergebnis prüfen und gegebenenfalls neu erzeugen.

## Sicherheit und Grenzen

- Die Erzeugung verwendet Python `secrets` für kryptografisch geeignete Zufallszahlen.
- Die Anwendung speichert erzeugte Passwörter nicht in Dateien und überträgt sie nicht an einen Server. Der Website-Link öffnet nur bei einem Klick deinen Browser.
- Die angezeigte Einschätzung prüft lediglich Länge und Zeichenarten. Sie erkennt keine bekannten oder wiederverwendeten Passwörter und ist keine Sicherheitsgarantie.
- Ein großer Zeichenvorrat und längere Passwörter bieten mehr Möglichkeiten als kurze Passwörter aus wenigen Zeichen. Für jedes Konto ein eigenes Passwort verwenden.
- Kopierte Passwörter können in der Zwischenablage oder deren Verlauf verbleiben. Für dauerhafte Aufbewahrung einen Passwortmanager verwenden.

Sicherheitsprobleme bitte über den in [SECURITY.md](SECURITY.md) beschriebenen privaten Meldeweg melden.

## Mitarbeit und Tests

Fehlerberichte, Verbesserungsvorschläge und Pull Requests sind willkommen. Siehe [CONTRIBUTING.md](CONTRIBUTING.md).

Die Erzeugungslogik lässt sich ohne grafische Oberfläche testen:

```sh
python -m unittest discover -s tests -v
```

## Lizenz und Kontakt

[MIT-Lizenz](LICENSE), Copyright © 2026 IT-Janz. Die Software wird ohne Gewährleistung bereitgestellt; maßgeblich ist der Lizenztext. Es gibt keine Pflicht zur unveränderten Anzeige des IT-Janz-Logos oder zur Veröffentlichung eigener Änderungen.

Entwickelt von [IT-Janz](https://www.it-janz.de).
