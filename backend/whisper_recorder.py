import sys
import time
import pyaudio
import numpy as np
import wave

class Recorder:
    def __init__(self, channels=1, rate=16000, chunk=1024):
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False
        self.frames = []

    def open_stream(self):
        if self.stream is None:
            self.stream = self.p.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.chunk)

    def start(self):
        self.open_stream()
        self.is_recording = True
        self.frames = []
        print(f"Recording...")

    def stop(self):
        self.is_recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        return self.frames

    def record(self, duration=None):
        self.start()
        start_time = time.time()

        while self.is_recording:
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            self.frames.append(data)

            if duration is not None and (time.time() - start_time) >= duration:
                self.stop()
                break

        return self.frames

    def save(self, frames, output_path):
        try:
            audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
            max_peak = np.max(np.abs(audio_data))
            if max_peak > 0:
                target_peak = 32767 * 0.891
                if max_peak > target_peak:
                    audio_data = (audio_data * (target_peak / max_peak)).astype(np.int16)
                print(f"Normalized peak: {np.max(np.abs(audio_data))}")

            with wave.open(output_path, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
                wf.setframerate(self.rate)
                wf.writeframes(audio_data.tobytes())
            
            with wave.open(output_path, 'rb') as wf:
                print(f"Verified metadata - Channels: {wf.getnchannels()}, Sample Width: {wf.getsampwidth()}, Frame Rate: {wf.getframerate()}")
            
            print(f"Recording finished. Saved to {output_path}")
        except PermissionError:
            print(f"Error: Permission denied when writing to {output_path}.", file=sys.stderr)
            sys.exit(1)
        except (OSError, RuntimeError) as e:
            print(f"Error: Could not write recording to {output_path}. ({e})", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred during saving: {e}", file=sys.stderr)
            sys.exit(1)

    def close(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
