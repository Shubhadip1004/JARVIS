# live_vosk.py
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer, SetLogLevel
import json
import sys
import os

username = os.getlogin()

SetLogLevel(-1)

MODEL_PATH = "vosk-model-small-en-us-0.15" 


SAMPLE_RATE = 16000
CHUNK = 4000  # in frames (~0.25s at 16k)

q = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print("Status:", status, file=sys.stderr)
    q.put(bytes(indata))

def transcriber():
    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, SAMPLE_RATE)
    rec.SetWords(True)  # include word timings if model supports it

    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=CHUNK, dtype='int16', 
                           channels=1, callback=audio_callback):
        print("Listening... ")
        # try:
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                    res = json.loads(rec.Result())
                    text = res.get("text", "")
                    print(f"[{username}]", text)
                    if text:  # only execute if something was recognized
                        return text
                    return
            else:
                    res = json.loads(rec.PartialResult())
                    return res.get("partial", "")+'\r'
        # except:
        #     pass
        # except KeyboardInterrupt:
        #     print("\nStopping...")
        #     print(json.loads(rec.FinalResult()))
        #     sys.exit(0)
