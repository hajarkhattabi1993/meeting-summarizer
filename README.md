# Meeting Summarizer 🎤

## What It Does
A local LLM system that automatically summarizes meetings 
and sends the summary to Outlook via email.

## Architecture
Audio/Text Input → Whisper → Chunker → Mistral → Parser → ChromaDB → SMTP → Outlook

## Tech Stack
- Ollama + Mistral (local LLM)
- Whisper (speech to text)
- ChromaDB (vector database)
- FastAPI (API layer)
- SMTP (email)

## How To Run
1. Clone the repo
2. Create virtual environment: python -m venv venv
3. Activate: source venv/Scripts/activate
4. Install dependencies: pip install -r requirements.txt
5. Run: python main.py

## Project Structure
- src/ - all source code
- api/ - FastAPI endpoints
- tests/ - test files
- data/ - sample meeting transcripts
- logs/ - log files
- reports/ - performance reports