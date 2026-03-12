# 📝 Text Summarizer GUI

A simple desktop NLP application that summarizes long text into concise summaries using Natural Language Processing.

---

## 🚀 Download Application

You can download the ready-to-run Windows application here:

⬇️ **Download the EXE**

[Download Text Summarizer](https://github.com/yourusername/text-summarizer/releases/download/v1.0/summarizer.exe)

No Python installation required.

---

## 🎯 Objective

To create a simple and user-friendly desktop application with a graphical interface that summarizes long passages of text into shorter concise summaries using NLP techniques.

---

## ⚙️ Technologies Used

- Python
- Tkinter (GUI)
- Natural Language Processing
- Hugging Face Transformers

---

## 🧠 Logic Used

### GUI Framework
The application interface is built using Tkinter. It provides:

- Input text area
- Summarize button
- Output summary box

### NLP Model
The summarization is powered by the **t5-small** model from Hugging Face Transformers.

### Summarization Pipeline
The Transformers pipeline handles:

- Tokenization
- Model inference
- Text generation

---

## ▶️ How to Run From Source

Clone the repository:

```
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
```

Install dependencies:

```
pip install tk transformers torch
```

Run the application:

```
python summarizer_app.py
```

---

## 📊 Output

The generated summary appears in the **Concise Summary** box inside the application GUI.

---

## 📌 Author

Manish Kushvaha
