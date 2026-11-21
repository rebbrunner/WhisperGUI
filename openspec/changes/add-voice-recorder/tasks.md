# Tasks

## 1. Environment and Scaffolding

- [ ] 1.1 Install `PyAudio` and `sounddevice` dependencies and verify they are available in the environment.
- [ ] 1.2 Create the `whisper-recorder` CLI entry point and verify the command is recognized.

## 2. Core Recording Implementation

- [ ] 2.1 Implement the audio capture loop using `PyAudio` and verify it can capture audio from the default device.
- [ ] 2.2 Implement the manual stop and duration logic and verify it correctly terminates the recording.
- [ ] 2.3 Implement the `.wav` file generation and verify the output file is created with the correct path.

## 3. Audio Pre-cleaning and Optimization

- [ ] 3.1 Implement the normalization step (-1dBFS) and verify it works on a sample recording.
- [ ] 3.2 Implement the sample rate conversion to 16kHz mono and verify the output file metadata.
- [ ] 3.3 Integrate the pre-cleaning steps into the final file save and verify the final `.wav` file is ready for Whisper.

## 4. Testing and Verification

- [ ] 4.1 Run a full recording test from start to finish and verify the final file meets all requirements (16kHz, mono, normalized).
- [ ] 4.2 Verify error handling for missing microphone or unwritable paths.

## Workflow follow-up

- Archive the change after the project's review requirements are satisfied.
- Verify the archived result.
