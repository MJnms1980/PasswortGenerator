import tkinter as tk
from tkinter import messagebox
import random
import re
import webbrowser

def calculate_strength(pw: str) -> str:
    length = len(pw)
    has_upper = bool(re.search(r'[A-Z]', pw))
    has_lower = bool(re.search(r'[a-z]', pw))
    has_digits = bool(re.search(r'\d', pw))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', pw))

    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digits: score += 1
    if has_special: score += 1

    if score <= 2:
        return "Sehr schwach"
    elif score == 3:
        return "Schwach"
    elif score == 4:
        return "Mittel"
    elif score == 5:
        return "Stark"
    else:
        return "Sehr stark"

def update_strength_display(event=None):
    pw = output_text.get("1.0", tk.END).strip()
    if pw:
        strength = calculate_strength(pw)
        strength_label.config(text=f"geschätzte Passwortqualität: {strength}")
    else:
        strength_label.config(text="geschätzte Passwortqualität: ")

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl für die Länge eingeben.")
        return

    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_digits = var_digits.get()
    use_special = var_special.get()
    special_chars = special_entry.get()

    chars = ""
    if use_upper:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lower:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if use_digits:
        chars += "0123456789"
    if use_special:
        chars += special_chars

    if not chars:
        messagebox.showwarning("Achtung", "Bitte mindestens eine Zeichengruppe auswählen.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, password)
    update_strength_display()

def open_link(event):
    webbrowser.open_new("https://www.it-janz.de")

# GUI-Fenster
root = tk.Tk()
root.title("Passwortgenerator v1.0 by IT-Janz")
root.geometry("500x500")
root.resizable(False, False)

# Variablen
length_var = tk.StringVar(value="12")
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

# Widgets
tk.Label(root, text="Passwortlänge:").pack(anchor="w", padx=20, pady=(20, 0))
tk.Entry(root, textvariable=length_var, width=5).pack(anchor="w", padx=20)

tk.Checkbutton(root, text="Großbuchstaben (A-Z)", variable=var_upper).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Kleinbuchstaben (a-z)", variable=var_lower).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Zahlen (0-9)", variable=var_digits).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Sonderzeichen", variable=var_special).pack(anchor="w", padx=20)

tk.Label(root, text="Sonderzeichen definieren:").pack(anchor="w", padx=20, pady=(10, 0))
special_entry = tk.Entry(root)
special_entry.insert(0, "!@#$%&*+-=?")
special_entry.pack(anchor="w", padx=20)

tk.Button(root, text="Passwort generieren", command=generate_password).pack(pady=15)

tk.Label(root, text="Passwort (markieren und kopieren z.B. mit Strg+C):").pack(anchor="w", padx=20, pady=(10, 0))

output_text = tk.Text(root, height=2, width=45, font=("Courier",20))
output_text.pack(padx=20)
output_text.config(wrap="none")
output_text.bind("<KeyRelease>", update_strength_display)

strength_label = tk.Label(root, text="geschätzte Passwortqualität: ", font=("Arial", 16, "italic"))
strength_label.pack(anchor="w", padx=20, pady=(5, 10))

# Klickbarer Link
link_label = tk.Label(root, text="Bereitgestellt von https://www.it-janz.de", fg="blue", cursor="hand2")
link_label.pack(side="bottom", pady=10)
link_label.bind("<Button-1>", open_link)

# Start
root.mainloop()