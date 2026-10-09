# Mitarbeit an PasswortGenerator

Beiträge von allen Interessierten sind willkommen: Fehlerberichte, Dokumentation, Übersetzungen, Verbesserungsvorschläge und Code.

## Fehler und Vorschläge

Zunächst nach einem bestehenden [Issue](https://github.com/MJnms1980/PasswortGenerator/issues) suchen. Bei Fehlern Umgebung, Version, Reproduktionsschritte und erwartetes Verhalten angeben. Screenshots und Beispiele vor dem Hochladen anonymisieren. Sicherheitslücken nach [SECURITY.md](SECURITY.md) vertraulich melden.

Größere Änderungen am besten zunächst in einem Issue besprechen, damit Ziel und Umfang klar sind.

## Änderungen beitragen

1. Das Repository forken und lokal klonen.
2. Einen Arbeitszweig erstellen, etwa `fix/kurze-beschreibung`.
3. Eine klar abgegrenzte Änderung umsetzen und die betroffene Dokumentation aktualisieren.
4. Die Änderung prüfen und die Ergebnisse im Pull Request beschreiben.
5. Einen Pull Request gegen `main` öffnen und auf Rückfragen eingehen.

Keine produktiven Zugangsdaten, Kundendaten oder privaten Dokumente beitragen. Neue Abhängigkeiten und deren Lizenzen im Pull Request erklären. Für Beiträge müssen die notwendigen Rechte vorliegen; beigetragener Code soll unter der bestehenden [MIT-Lizenz](LICENSE) nutzbar sein.

## Prüfen

Python 3.10 oder neuer verwenden. Die Erzeugungslogik mit `python -m unittest discover -s tests -v` prüfen. Bei Änderungen an der Oberfläche zusätzlich Start, Längeneingabe, Zeichengruppen und Kopieren manuell auf einer Desktop-Umgebung testen.

Bitte tatsächlich ausgeführte Prüfungen und bekannte Grenzen im Pull Request nennen. Ein bestandener Syntaxcheck ersetzt keine Funktionsprüfung.

## Umgang miteinander

Sachlich und respektvoll kommunizieren. Beiträge werden geprüft; eine Annahme oder bestimmte Bearbeitungszeit ist nicht zugesichert.
