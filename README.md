# Text-Summarizer

# Project Title:Text Summarizer GUI

# Objective:
To create a simple and user-friendly desktop application with a Graphical User Interface (GUI) that summarizes long passages of text into a shorter, concise version using a pre-trained Natural Language Processing (NLP) model.

# Logic Used:

GUI Framework: The application's interface is built using Tkinter, Python's standard library for creating GUIs. It provides an input box for user text, an output box for the result, and a button to trigger the process.

NLP Model: The core summarization logic is handled by the Hugging Face Transformers library. It uses a pre-trained, state-of-the-art model (t5-small) designed for text-to-text tasks.

Summarization Pipeline: A pipeline from the Transformers library abstracts the complex steps of tokenization, model inference, and decoding. It takes the raw text as input and efficiently generates the summarized text.

# How to Run:

Open a terminal or command prompt in the project folder.

Install the necessary libraries: pip install tk transformers torch

Run the application using the command: python summarizer_app.py

Paste your text into the input text area and click the "Summarize" button.

# Files:

summarizer_app.py → The main Python script that contains all the code for the GUI and the summarization functionality.

# Dataset:
This project does not use a local dataset file. Instead, it leverages the t5-small model from the Hugging Face model hub, which has been pre-trained on a vast corpus of text data to learn how to effectively summarize.

# Output Format:
The generated summary is displayed in the read-only "Concise Summary" text box within the application's GUI.
