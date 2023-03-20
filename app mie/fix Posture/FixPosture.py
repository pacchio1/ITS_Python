
import time
import wave
import pyaudio

# Carica il file audio da riprodurre
wave_file = wave.open("C:/Users/parco/Music/siediti_bene.wav", 'rb')

# Inizializza l'oggetto PyAudio
p = pyaudio.PyAudio()

# Definisci la funzione per riprodurre l'audio


def play_audio():
    # Apri lo stream audio
    stream = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                    channels=wave_file.getnchannels(),
                    rate=wave_file.getframerate(),
                    output=True)
    # Riproduci l'audio
    data = wave_file.readframes(1024)
    while data:
        stream.write(data)
        data = wave_file.readframes(1024)
    # Chiudi lo stream audio
    stream.stop_stream()
    stream.close()


# Riproduci l'audio ogni 20 minuti
while True:
    play_audio()
    time.sleep(20 * 60)  # 20 minuti
