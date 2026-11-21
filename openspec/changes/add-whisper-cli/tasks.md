# Tasks

## 1. Setup & Dependencies

- [ ] 1.1 Create `whisper_cli.py` file and verify it's present in the root directory.
- [ ] 1.2 Verify that `faster-whisper` is available in the current environment.
- [ ] 1.3 Create a sample `.wav` file and a test output directory to use for verification.

## 2. Core CLI Implementation

- [ ] 2.1 Implement argument parsing for input path and output path using `argparse`.
- [ ] 2.2 Implement the `faster-whisper` model loading and transcription logic.
- [ ] 2.3 Implement output file writing logic and verify the transcription is saved to the `.txt` file.
- [ ] 2.4 Implement error handling for missing files or invalid formats and verify descriptive error messages are shown.

## 3. Verification & Testing

- [ ] 3.1 Run the CLI with a sample `.wav` file and verify the `.txt` output matches the expected transcription.
- [ ] 3.2 Run the CLI with an invalid file type and verify the correct error message is displayed.
- [ ] 3.3 Verify that the default output filename is correctly generated when no output path is provided.

## Workflow follow-up

- Archive the change after the project's review requirements are satisfied.
- Verify the archived result.
