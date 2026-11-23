# Whisper GUI

- **author:** Rebecca Brunner
- **date:** 20th November 2026

## Description

Fullstack transcription application meant to run entirely on localhost forw now (until I port recorder into react frontend).  Backend uses faster-whisper to accept speech and transcribe back into audio.  Endpoints served on FastAPI include record start (temp) record stop (temp), transcribe.

Frontend user interface includes a button which toggled on begins recorder, toggled off stops recorder.  Process button triggers transcribe op, which returns text that then displays in the text box in the user interface.
