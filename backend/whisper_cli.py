import argparse
import os
import sys
import re
from faster_whisper import WhisperModel

class Transcriber:
    def __init__(self, cache_path, model_size="base", device="cuda", compute_type="int8"):
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type
        self.model = None
        self.cache_path = cache_path
        self._setup_dll_paths()
        self.load_model()

    def _setup_dll_paths(self):
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

    def load_model(self):
        try:
            print(f"Attempting to load model {self.model_size} on {self.device}...")
            self.model = WhisperModel(
                self.model_size, 
                device=self.device, 
                compute_type=self.compute_type,
                download_root=self.cache_path
            )
            print(f"Model loaded successfully on {self.device}.")
        except Exception as e:
            print(f"CUDA initialization failed: {e}")
            print("Falling back to CPU...")
            # Using float32 for CPU as int8 might not be supported on all CPUs depending on the backend
            self.model = WhisperModel(
                self.model_size, 
                device="cpu", 
                compute_type="float32"
            )
            print("Model loaded successfully on CPU.")

    def transcribe(self, input_path, output_path=None, beam_size=5):
        segments, info = self.model.transcribe(input_path, beam_size=beam_size)
        print(f"Transcribing using model: {info.language} ({info.language_probability:.2f})")
        
        full_text = []
        for segment in segments:
            print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
            full_text.append(segment.text)
        
        result = " ".join(full_text)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Transcription complete. Saved to: {output_path}")
        
        return result
