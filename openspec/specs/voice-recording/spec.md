# voice-recording Specification

## Purpose

Provides a CLI-based voice recording utility that prepares audio for high-quality transcription by ensuring proper normalization and sample rate.

## Requirements

### Requirement: CLI Voice Recording
The system SHALL provide a command-line interface to record audio from the default microphone device.
#### Scenario: Successful manual recording
- **WHEN** user starts recording via CLI and stops after desired duration
- **THEN** a .wav file is saved to the specified path

### Requirement: Audio Pre-cleaning
The system SHALL automatically process the recorded .wav file to ensure it is optimized for Whisper models.
#### Scenario: Normalization and sample rate adjustment
- **WHEN** a recording is completed
- **THEN** the system SHALL ensure the output file is 16kHz mono and normalized to -1dBFS

### Requirement: Error Handling
The system SHALL report errors if the microphone is unavailable or if the output path is unwritable.
#### Scenario: Microphone unavailable
- **WHEN** recording is started but no microphone is detected
- **THEN** the system SHALL output an error message to stderr and exit with non-zero status
