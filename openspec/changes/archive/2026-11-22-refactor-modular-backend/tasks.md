# Tasks

## 1. Refactor Recorder

- [x] 1.1 Create `Recorder` class in `backend/whisper_recorder.py` and verify it can be instantiated with correct PyAudio parameters.
- [x] 1.2 Move recording logic (stream opening, loop, saving) into `Recorder.record()` method and verify it produces a valid `.wav` file.
- [x] 1.3 Update `main()` in `whisper_recorder.py` to use the `Recorder` class and verify existing CLI command still works.

## 2. Refactor Transcriber

- [x] 2.1 Create `Transcriber` class in `backend/whisper_cli.py` and verify it correctly handles DLL path setup.
- [x] 2.2 Move transcription logic (model loading, transcription loop, writing output) into `Transcriber.transcribe()` method and verify it produces a correct `.txt` file.
- [x] 2.3 Update `main()` in `whisper_cli.py` to use the `Transcriber` class and verify existing CLI command still works.

## 3. Integration Orchestrator

- [x] 3.1 Create `backend/main.py` and implement a sample pipeline that uses both `Recorder` and `Transcriber` classes and verify it completes a full recording-to-transcription cycle.
- [x] 3.2 Verify that the new classes do not have circular dependencies and are correctly imported in `main.py`.

## Workflow follow-up

- Archive the change after the project's review requirements are satisfied.
- Verify the archived result.
