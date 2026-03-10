import tkinter as tk
from tkinter import ttk
import re
from collections import Counter

def summarize():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        return

    sentences = re.split(r'(?<=[.!?])\s+', text)

    words = re.findall(r'\w+', text.lower())

    freq = Counter(words)

    # sentence scores
    scores = {}
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            scores[sentence] = scores.get(sentence, 0) + freq[word]

    # choose only 40% of sentences
    summary_length = max(1, int(len(sentences) * 0.4))

    top_sentences = sorted(scores, key=scores.get, reverse=True)[:summary_length]

    # for original order
    summary = []
    for s in sentences:
        if s in top_sentences:
            summary.append(s)

    result = " ".join(summary)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


root = tk.Tk()
root.title("Simple Text Summarizer")
root.geometry("700x500")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Enter Text").pack(anchor="w")

input_text = tk.Text(frame, height=12)
input_text.pack(fill="both", expand=True)

ttk.Button(frame, text="Summarize", command=summarize).pack(pady=10)

ttk.Label(frame, text="Summary").pack(anchor="w")

output_text = tk.Text(frame, height=8)
output_text.pack(fill="both", expand=True)

root.mainloop()