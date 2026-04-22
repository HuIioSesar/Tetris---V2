import wave
import struct
import os
import math

SAMPLE_RATE = 44100
VOLUME = 0.5

OUTPUT_DIR = "assets/sounds"
OUTPUT_FILE = "line_clear.wav"


# def generate_square_note(frequency, duration, volume=VOLUME, duty=0.5):
#     """
#     Generate a single square-wave note with simple decay envelope.
#     duty = fraction of the cycle that is "high".
#     """
#     num_samples = int(SAMPLE_RATE * duration)
#     samples = []

#     for i in range(num_samples):
#         t = i / SAMPLE_RATE
#         phase = (frequency * t) % 1.0
#         sample = volume if phase < duty else -volume

#         # Slightly slower decay than before (less steep)
#         decay = 1.0 - (i / num_samples)
#         sample *= decay

#         samples.append(sample)

#     return samples


# def generate_silence(duration):
#     num_samples = int(SAMPLE_RATE * duration)
#     return [0.0] * num_samples


# def generate_pitch_sweep(start_freq, end_freq, duration, volume=VOLUME, duty=0.5):
#     """
#     Square wave with linear pitch sweep: for the 'wiun'.
#     """
#     num_samples = int(SAMPLE_RATE * duration)
#     samples = []

#     for i in range(num_samples):
#         t = i / SAMPLE_RATE
#         # Linear sweep: start_freq -> end_freq
#         f = start_freq + (end_freq - start_freq) * (i / num_samples)

#         phase = (f * t) % 1.0
#         sample = volume if phase < duty else -volume

#         # Decay envelope
#         decay = 1.0 - (i / num_samples)
#         sample *= decay

#         samples.append(sample)

#     return samples


# def create_line_clear_sound():
#     """
#     Build: piru piru - wiun

#     - piru: two notes, but now high -> low, slightly slower
#     - repeated twice
#     - wiun: downward sweep, also slightly slower
#     """
#     all_samples = []

#     # --- PIRU configuration ---
#     # Now HIGH -> LOW (reversed pitch)
#     piru_notes = [1200.0, 800.0]   # high → lower
#     note_duration = 0.09           # a bit slower than before
#     gap_between_notes = 0.02      # small gap

#     def add_piru():
#         for freq in piru_notes:
#             all_samples.extend(generate_square_note(freq, note_duration))
#             all_samples.extend(generate_silence(gap_between_notes))

#     # piru
#     add_piru()

#     # small gap between the two "piru"
#     all_samples.extend(generate_silence(0.04))

#     # piru again
#     add_piru()

#     # --- Gap before WIUN ---
#     all_samples.extend(generate_silence(0.06))

#     # --- WIUN configuration ---
#     # Slightly slower, deeper sweep
#     start_freq = 1300.0    # high start
#     end_freq = 350.0       # lower end
#     wiun_duration = 0.25   # slower "wiun"

#     all_samples.extend(generate_pitch_sweep(start_freq, end_freq, wiun_duration))

#     # Convert to 16-bit PCM
#     pcm_data = b""
#     for sample in all_samples:
#         s = max(-1.0, min(1.0, sample))  # clamp
#         pcm_value = int(s * 32767)
#         pcm_data += struct.pack("<h", pcm_value)

#     os.makedirs(OUTPUT_DIR, exist_ok=True)
#     filepath = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

#     with wave.open(filepath, "wb") as wf:
#         wf.setnchannels(1)       # mono
#         wf.setsampwidth(2)       # 16-bit
#         wf.setframerate(SAMPLE_RATE)
#         wf.writeframes(pcm_data)

#     print("Saved:", filepath)


# if __name__ == "__main__":
#     create_line_clear_sound()





# PIECE DROP - SOUND

import wave
import struct
import math

# configuración de audio
sample_rate = 44100
duration = 0.072  # duración real aproximada (~72 ms)
num_samples = int(sample_rate * duration)

# características del canal de pulso del Game Boy
duty_cycle = 0.125  # 12.5%

# pitch aproximado del efecto original
start_freq = 1046.5   # cercano a C6
end_freq = 784.0      # cercano a G5

# envelope estilo hardware
initial_volume = 0.9
envelope_steps = 6
envelope_rate = 64  # Hz (Game Boy envelope clock)

phase = 0.0
samples = []

for i in range(num_samples):

    t = i / sample_rate

    # pitch sweep descendente
    sweep_progress = i / num_samples
    freq = start_freq + (end_freq - start_freq) * sweep_progress

    # avanzar fase
    phase += freq / sample_rate
    phase %= 1.0

    # onda cuadrada con duty cycle real
    if phase < duty_cycle:
        wave_value = 1
    else:
        wave_value = -1

    # envelope por pasos (imitando hardware)
    envelope_time = int(t * envelope_rate)
    envelope_factor = max(0, initial_volume - (envelope_time / envelope_steps))

    sample = wave_value * envelope_factor

    # convertir a 16-bit PCM
    samples.append(int(sample * 32767))

# guardar WAV
with wave.open("tetro_lock.wav", "w") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for s in samples:
        wav.writeframes(struct.pack("<h", s))

print("Archivo generado: tetro_lock.wav")