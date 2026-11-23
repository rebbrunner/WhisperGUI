# Proposal

## Why

The current transcription and recording logic is tightly coupled within two standalone scripts (`whisper_cli.py` and `whisper_recorder.py`). This makes it difficult to chain operations (e.g., recording followed by transcription) or to use these components in different contexts without duplicating code. Refactoring them into modular classes will improve maintainability, testability, and allow for easier integration into a unified application flow.

## What Changes

- Refactor `backend/whisper_recorder.py` to encapsulate recording logic into a `Recorder` class.
- Refactor `backend/whisper_cli.py` to encapsulate transcription logic into a `Transcriber` class.
- Create a new `backend/main.py` (or similar) to act as a master orchestrator that instantiates both classes and chains their operations.
- Maintain the existing CLI functionality for both scripts to ensure backward compatibility.

## Capabilities

### New Capabilities
- None

### Modified Capabilities
- None

## Impact

- `backend/whisper_cli.py`: Refactored to a class-based structure.
- `backend/whisper_recorder.py`: Refactored to a class-based structure.
- New `backend/main.py`: New entry point for the full recording-to-transcription pipeline.
