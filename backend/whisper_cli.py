import argparse
import os
import sys
import re
from faster_whisper import WhisperModel

def main():
    parser = argparse.ArgumentParser(description="Transcribe a .wav file to a .txt file using faster-whisper.")
    parser.add_argument("input_path", help="Path to the input .wav file")
    parser.add_argument("--output_path", help="Path to the output .txt file")

    args = parser.parse_args()

    # Attempt to find NVIDIA DLL paths
    
    prefix_path = sys.prefix
    script_dir = os.path.dirname(os.path.abspath(__file__))
    venv_path = os.path.join(script_dir, "env")
    base_paths = []
    if prefix_path:
        base_paths.append(os.path.join(prefix_path, "Lib", "site-packages", "nvidia"))
    if os.path.exists(venv_path):
        base_paths.append(os.path.join(venv_path, "Lib", "site-packages", "nvidia"))
    for base in base_paths:
        for sub_dir in ["cublas", "cuda_nvrtc", "cudnn", "cuda_runtime"]:
            dll_path = os.path.abspath(os.path.join(base, sub_dir, "bin"))
            if os.path.exists(dll_path):
                os.add_dll_directory(dll_path)
                # Also add to PATH as a fallback, as some loaders ignore add_dll_directory
                os.environ["PATH"] = dll_path + os.pathsep + os.environ.get("PATH", "")
                print(f"Added DLL directory and PATH: {dll_path}")

    try:
        print("Attempting to load model on CUDA...")
        model = WhisperModel("base", device="cuda", compute_type="int8")
        print("Model loaded successfully on CUDA.")
    except Exception as e:
        print(f"CUDA initialization failed: {e}")
        print("Falling back to CPU...")
        # Using float32 for CPU as int8 might not be supported on all CPUs depending on the backend
        model = WhisperModel("base", device="cpu", compute_type="float32")
        print("Model loaded successfully on CPU.")

    # Perform transcription
    segments, info = model.transcribe(args.input_path, beam_size=5)
    
    print(f"Transcribing using model: {info.language} ({info.language_probability:.2f})")
    
    full_text = []
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        full_text.append(segment.text)

    # Output handling
    output_filename = args.output_path
    if not output_filename:
        base, _ = os.path.splitext(args.input_path)
        output_filename = f"{base}.txt"

    # Write the transcription to a file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(" ".join(full_text))

    print(f"Transcription complete. Saved to: {output_filename}")

if __name__ == "__main__":
    main()
