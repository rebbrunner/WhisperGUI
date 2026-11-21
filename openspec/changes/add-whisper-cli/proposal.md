# Proposal

## Why

Provide a simple command-line interface for users to transcribe pre-recorded .wav files into text format using the faster-whisper engine. This enables quick, headless transcription without needing the full GUI.

## What Changes

- Create a new CLI tool (e.g., `whisper_cli.py`).
- Implement logic to load a `.wav` file and run it through `faster-whisper`.
- Add command-line arguments for input file path and output text file path.
- Handle transcription errors and save the final transcription to a `.txt` file.

## Capabilities

### New Capabilities
- `whisper-cli`: A new CLI interface for processing audio files and generating transcriptions.

### Modified Capabilities
- None

## Impact

- New standalone script.
- Dependency on `faster-whisper` (already installed).
- No changes to existing GUI components.
