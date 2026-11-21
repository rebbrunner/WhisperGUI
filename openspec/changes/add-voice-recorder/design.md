# Design

## Context

See proposal.md for the motivation. The goal is to provide a standard way to record voice for transcription into the Whisper pipeline.

## Goals / Non-Goals

**Goals:**
- Provide a CLI tool that records from the default system microphone.
- Automatically normalize the output to 16kHz mono.
- Ensure the output is a standard `.wav` file compatible with `faster-whisper`.

**Non-Goals:**
- Real-time transcription (this is for recording first).
- High-fidelity studio-grade noise reduction (we will focus on normalization/sample rate).
- Support for multiple simultaneous inputs.

## Decisions

- **Library choice**: Use `PyAudio` for audio capture as it is standard for Python and handles standard host APIs well.
- **Sample Rate**: Standardize on 16,000 Hz. While `faster-whisper` can handle higher, 16k is optimal for many use cases and reduces file size.
- **Normalization**: Apply peak normalization to -1dBFS to ensure consistent input volume for Whisper.
- **CLI Structure**: Use `argparse` to provide clear `-o` (output) and `-d` (duration) flags, with an optional `--stop` flag or manual interrupt.

## Risks / Trade-offs

- [Risk] Portability of `PyAudio` across different OSs (e.g., Linux vs Windows). → [Mitigation] Rely on standard `portaudio` drivers.
- [Risk] Blocking the main thread during recording. → [Mitigation] Use a simple loop for recording; for long durations, we could move to a separate thread but for a CLI tool, a blocking loop is acceptable.

## Open Questions

- Do we need to support specific bit depths other than 16-bit? (Defaulting to 16-bit).
