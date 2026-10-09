"""Passworterzeugung ohne grafische Oberfläche."""

import secrets

MIN_LENGTH = 8
MAX_LENGTH = 128


def create_password(length: int, characters: str) -> str:
    """Ziehe jedes Zeichen unabhängig aus dem gewählten Zeichenvorrat."""
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(f"Bitte eine Passwortlänge von {MIN_LENGTH} bis {MAX_LENGTH} wählen.")
    if not characters:
        raise ValueError("Bitte mindestens eine nicht leere Zeichengruppe auswählen.")
    # Doppelte benutzerdefinierte Zeichen sollen nicht häufiger gezogen werden.
    alphabet = ''.join(dict.fromkeys(characters))
    return ''.join(secrets.choice(alphabet) for _ in range(length))
