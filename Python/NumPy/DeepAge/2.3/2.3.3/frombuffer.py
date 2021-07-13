import numpy as np
import time
import wave

wf = wave.open('sample_sound.wav')
channels = wf.getnchannels()

print(wf.getparams())
print("-" * 30)

chunk_size = wf.getnframes()
print(chunk_size)
print("-" * 30)

data = wf.readframes(chunk_size)


def print_time(fn):
    start_time = time.time()
    fn
    print(time.time() - start_time)
    print("-" * 30)


print_time(np.frombuffer(data, dtype='int16'))
print_time(np.fromiter(data, dtype='int16'))
