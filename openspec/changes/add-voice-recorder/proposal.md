# Proposal

## Why

Current workflows for recording voice for Whisper transcription often require third-party GUI tools or complex command-line chains to ensure the correct audio format, sample rate, and normalization. A dedicated CLI utility simplifies this by providing a consistent way to record and "pre-clean" audio specifically for `faster-whisper` requirements.

## What Changes

- Create a new CLI command `whisper-recorder` (or a subcommand if applicable).
- Implement microphone recording functionality using `PyAudio` or `sounddevice`.
- Add an automated "cleaning" step that ensures the output `.wav` file is properly normalized and uses the recommended sample rate (e.g., 16kHz) for efficient Whisper transcription.
- Provide simple command-line arguments for output file path and recording duration/manual stop.

## Capabilities

### New Capabilities
- `voice-recording`: A capability to capture, format, and prepare audio input for transcription.

### Modified Capabilities
- None

## Impact

- New dependency: `PyAudio` or `sounddevice`.
- New CLI entry point.
- Better data quality for the transcription pipeline.
