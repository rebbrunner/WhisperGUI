import sys
import threading
from whisper_recorder import Recorder
from whisper_cli import Transcriber

def main():
    # Example configuration
    output_audio_path = "test_recording.wav"
    output_text_path = "test_transcription.txt"

    print(f"--- Starting Dynamic Recording Pipeline ---")

    # 1. Initialize Recorder
    recorder = Recorder(channels=1, rate=16000, chunk=1024)

    try:
        # 2. Start Recording in a background thread
        print(f"Recording started. Type 'stop' and press Enter to finish.")
        
        def record_task():
            recorder.record()

        recording_thread = threading.Thread(target=record_task)
        recording_thread.start()

        # Listen for "stop" command
        while True:
            user_input = input("Enter 'stop' to finish: ").strip().lower()
            if user_input == "stop":
                recorder.stop()
                break

        recording_thread.join()

        # 3. Save the recorded frames
        print(f"Saving recording to {output_audio_path}...")
        recorder.save(recorder.frames, output_audio_path)
        print("Recording saved successfully.")

        # 4. Initialize Transcriber
        print(f"Step 2: Initializing Transcriber...")
        transcriber = Transcriber(model_size="base", device="cuda", compute_type="int8")

        # 5. Transcribe Audio
        print(f"Step 3: Transcribing {output_audio_path}...")
        transcriber.transcribe(output_audio_path, output_path=output_text_path)
        print("Transcription successful.")

        print(f"--- Pipeline Completed Successfully ---")
        print(f"Final results: {output_audio_path}, {output_text_path}")

    except Exception as e:
        print(f"Pipeline failed: {e}")
        sys.exit(1)
    finally:
        recorder.close()

if __name__ == "__main__":
    main()
