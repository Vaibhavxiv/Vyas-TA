# 📚 Vyas Teaching Assistant

A **course-specific AI teaching assistant** for the Sigma Web Development course. This system converts course videos into searchable transcripts, generates embeddings, and allows users to ask natural language questions to get **human-like answers** with video references and timestamps.

---

## Features

- Converts video tutorials into MP3 audio (`process_video.py`)  
- Transcribes audio and segments into chunks with timestamps (`chunks.py`)  
- Generates embeddings for semantic search (`embeddings.py`)  
- Answers user queries using GPT-4o-mini with context from relevant video chunks (`response.py`)  
- Streamlit web interface for easy interaction (`app.py`)  

---
## How It Works

- Videos → Audio extraction (process_video.py)
- Audio → Transcription + segmentation (chunks.py)
- Transcription → Embeddings (embeddings.py)
- Query → Find relevant chunks → GPT-4o-mini (response.py)
- Display results in Streamlit frontend (app.py)

---

## Folder Structure
```

├─ videos/                 # Original course video files
├─ audios/                 # Extracted MP3 audio files
├─ jsons/                  # Transcribed JSON files with chunks
├─ process_video.py        # Converts videos to audio
├─ chunks.py               # Transcribes audio into chunks
├─ embeddings.py           # Generates embeddings for chunks
├─ response.py             # Handles query answering
├─ app.py                  # Streamlit frontend
└─ embeddings.joblib       # Saved embeddings (after running embeddings.py)

```

---

## Installation

### 1. Clone the repository:

```
git clone https://github.com/yourusername/vyas-teaching-assistant.git
cd vyas-teaching-assistant
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
Dependencies include:

- whisper
- openai
- pandas
- joblib
- scikit-learn
- numpy
- streamlit

### 3. Convert videos to audio
```
python process_video.py
```
### 4. Transcribe audio into JSON chunk
```
python chunks.py
```
### 5. Generate embeddings for chunks
```
python embeddings.py
```
### 6. Start Streamlit assistant
```
pyhton app.py
```

