import argparse
import sys
import time
import pyaudio
import numpy as np
import wave

def save_recording(frames, output_path, channels, rate, format_name, p):
    try:
        # Convert frames to numpy array
        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

        # Peak normalization to -1dBFS
        max_peak = np.max(np.abs(audio_data))
        if max_peak > 0:
            # -1dBFS is approximately 0.891 peak amplitude for 16-bit
            target_peak = 32767 * 0.891
            if max_peak > target_peak:
                audio_data = (audio_data * (target_peak / max_peak)).astype(np.int16)
            print(f"Normalized peak: {np.max(np.abs(audio_data))}")

        with wave.open(output_path, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(format_name))
            wf.setframerate(rate)
            wf.writeframes(audio_data.tobytes())
        
        # Verify output file metadata
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

def main():
    parser = argparse.ArgumentParser(description="Whisper Voice Recorder")
    parser.add_argument("-o", "--output", required=True, help="Output .wav file path")
    parser.add_argument("-d", "--duration", type=float, help="Recording duration in seconds")
    parser.add_argument("--stop", action="store_true", help="Wait for manual stop")

    args = parser.parse_args()

    # PyAudio configuration
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    p = pyaudio.PyAudio()

    stream = None
    try:
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        
        print(f"Recording to {args.output}...")
        
        frames = []
        start_time = time.time()
        
        if args.duration:
            duration = args.duration
        elif args.stop:
            duration = None
        else:
            print("Error: Please provide a duration (-d) or use --stop for manual control.")
            sys.exit(1)

        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
            
            if duration is not None and (time.time() - start_time) >= duration:
                break
            
            # Note: For a production CLI, we'd check for a specific stop signal 
            # from stdin here, but for now we rely on duration and Ctrl+C.

        save_recording(frames, args.output, CHANNELS, RATE, FORMAT, p)

    except (OSError, RuntimeError) as e:
        if "Device not found" in str(e) or "No default input device" in str(e):
            print(f"Error: Microphone not found or unavailable. ({e})", file=sys.stderr)
        else:
            print(f"Error: Could not open audio stream. ({e})", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when writing to {args.output}.", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nRecording stopped by user.")
        save_recording(frames, args.output, CHANNELS, RATE, FORMAT, p)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if stream:
            stream.stop_stream()
            stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
