# Design

## Context

The current implementation of transcription and recording is split into two standalone scripts, `whisper_cli.py` and `whisper_recorder.py`. This prevents easy chaining of the two processes (recording then transcribing) without manual intervention or duplicate logic. We need a modular class-based structure to allow for shared state, easier configuration, and a unified orchestration layer.

## Goals / Non-Goals

**Goals:**
- Encapsulate recording logic into a `Recorder` class.
- Encapsulate transcription logic into a `Transcriber` class.
- Create a master orchestration script that can run the full pipeline: Recording -> Transcription.
- Maintain backward compatibility for the existing CLI usage of both scripts.

**Non-Goals:**
- Changing the underlying audio recording or transcription libraries/algorithms.
- Creating a GUI for these actions (the focus is on the backend logic).

## Decisions

**1. Class Structure for Recorder**
- Decision: Move recording logic into a `Recorder` class.
- Rationale: Allows for consistent configuration of PyAudio parameters and a clean interface for starting/stopping recordings and saving files.
- Alternatives: Keeping it as a series of functions, but a class is better for managing state (like the stream object).

**2. Class Structure for Transcriber**
- Decision: Move transcription logic into a `Transcriber` class.
- Rationale: Encapsulates model loading, CUDA/CPU selection logic, and the transcription loop.
- Alternatives: Moving all logic to a single massive class, but separating `Recorder` and `Transcriber` keeps concerns distinct.

**3. Entry Point Strategy**
- Decision: Keep the original `if __name__ == "__main__":` blocks in both files but refactor the internal logic to call the new classes.
- Rationale: Ensures that existing workflows (invoking the scripts directly) do not break.
- Alternatives: Removing the entry points and forcing everything through a new script, which would break existing automation/shortcuts.

**4. Orchestration**
- Decision: Create `backend/main.py` as the primary entry point for the unified flow.
- Rationale: Provides a clean place to import both classes and execute the pipeline in a readable manner.

## Risks / Trade-offs

- [Risk] Potential for circular imports if classes are not structured correctly. → [Mitigation] Keep the classes in their own files and only import them in the orchestration script.
- [Risk] CUDA initialization might behave differently when called from a class method. → [Mitigation] Ensure the DLL path logic remains robust and is executed during `Transcriber` initialization.

## Open Questions

- Should we add a configuration file (e.g., YAML/JSON) to manage parameters like `model_size` or `sample_rate` for both classes? (Optional for now).
