# Proposal

## Why

The current `DictationForm` allows for text input but lacks a native microphone recording interface. Adding this allows users to dictate their input directly, improving accessibility and ease of use. Recording the audio allows the system to process and provide transcriptions based on the complete recording.

## What Changes

- Modify `DictationForm.tsx` to include a microphone button.
- Add state management for recording status (idle, recording, stopped).
- Implement a media recording hook/logic to capture audio from the microphone.
- Add visual feedback (e.g., a pulsing icon or label) when recording is active.
- Implement a mechanism to submit the complete recording to the existing fetch endpoint once stopped.

## Capabilities

### New Capabilities
- `voice-input`: Provides the capability to capture audio from the user's microphone and submit the recording for transcription.

### Modified Capabilities

## Impact

- `frontend/src/DictationForm/DictationForm.tsx`
- State management within the frontend component.
- Browser APIs (MediaRecorder).
- Network requests (single submission).
