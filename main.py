# import sounddevice as sd
# from scipy.io.wavfile import write

# fs = 44100  # Sample rate
# seconds = 3  # Duration of recording

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# print(sd)
# write('output.wav', fs, myrecording)  # Save as WAV file


import sounddevice as sd
duration = 5.5  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))