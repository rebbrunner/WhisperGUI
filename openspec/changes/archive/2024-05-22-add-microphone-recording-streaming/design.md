# Design

## Context

The `DictationForm.tsx` currently only supports text input. This design enables microphone recording and submission of a complete recording to the backend. See proposal.md for the motivation.

## Goals / Non-Goals

**Goals:**
- Add a microphone button to `DictationForm.tsx`.
- Implement a `MediaRecorder` hook to manage recording state.
- Capture a full audio recording and submit it via a single `POST` request.
- Provide a pulsing visual indicator when recording is active.

**Non-Goals:**
- Adding real-time transcription display (this is part of the backend's response handling).
- Supporting multiple simultaneous recording streams.

## Decisions

**Decision 1: Use MediaRecorder API**
- Rationale: It is the standard web API for capturing audio/video. It handles the complexity of managing the underlying media stream.
- Alternatives: Web Audio API (more control but significantly more complex for this use case).

**Decision 2: Single Upload of Final Recording**
- Rationale: The backend currently only supports a final `.wav` file and does not support incremental chunk processing.
- Alternatives: Chunked Streaming (Requires backend changes).

**Decision 3: CSS Animation for Visual Feedback**
- Rationale: A simple CSS animation on the microphone icon provides immediate visual feedback without heavy React re-renders.

## Risks / Trade-offs

- [Risk] Browser support for specific `MediaRecorder` MIME types. → Mitigation: Use `audio/webm;codecs=opus` as a primary target.
- [Risk] Large file upload latency. → Mitigation: Ensure the connection is stable and the recording duration is kept reasonable.

## Open Questions

- Does the current fetch endpoint support the expected MIME types for the submitted recording? (Assuming yes for now).
