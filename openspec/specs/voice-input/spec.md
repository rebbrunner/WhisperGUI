# voice-input Specification

## Purpose

Provides the capability to capture audio from the user's microphone and send a complete recording to the transcription service for processing.

## Requirements

### Requirement: Microphone Access
The system SHALL request and receive permission to access the user's microphone browser-side when the user interacts with the dictation interface.

#### Scenario: User grants microphone permission
- **WHEN** the user clicks the microphone button
- **THEN** the browser prompts for microphone access and the user accepts

#### Scenario: User denies microphone permission
- **WHEN** the user clicks the microphone button
- **THEN** the system notifies the user that microphone access is required for dictation

### Requirement: Audio Recording and Submission
The system SHALL capture audio from the microphone and submit the complete recording to the transcription endpoint once the recording is stopped.

#### Scenario: Active recording
- **WHEN** the user is speaking during an active recording session
- **THEN** the system captures the audio data

#### Scenario: Stop recording and submit
- **WHEN** the user clicks the microphone button a second time during a recording session
- **THEN** the system stops capturing audio and submits the final recording to the backend

### Requirement: Visual Recording Indicator
The system SHALL provide a clear visual indicator to the user when the microphone is actively recording.

#### Scenario: Recording indicator visibility
- **WHEN** the recording status is active
- **THEN** the microphone button or a nearby indicator displays a pulsing or active state animation
