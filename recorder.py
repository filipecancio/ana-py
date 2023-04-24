# codigo adaptado a partir de outro encontrado em https://gist.github.com/mabdrabo/8678538
import pyaudio
import wave
import os

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 6

def record(temp_dir=".", segundos=RECORD_SECONDS):
    audio = pyaudio.PyAudio()

    # start recording
    print("fale alguma coisa...")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    for _ in range(0, int(RATE / CHUNK * segundos)):
        data = stream.read(CHUNK,exception_on_overflow = False)
        if data:
            frames.append(data)

    # stop secording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save temporary audio file
    temp_file = temp_dir + "/speech.wav"
    if os.path.isfile(temp_file):
        os.remove(temp_file)

    print(f"arquivo de audio sendo gerado: {temp_file}")
    with wave.open(temp_file, "wb") as wave_file: 
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

    return os.path.isfile(temp_file), temp_file

if __name__ == "__main__":
    record("audio")