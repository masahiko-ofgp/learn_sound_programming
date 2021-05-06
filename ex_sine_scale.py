from wavew import MonoPcm, StereoPcm
import math

def sine_scale_mono(pcm, f0, a, offset, duration):
    dur = int(duration)
    tmp = [0]*dur

    for n in range(0, dur):
        tmp[n] = a * math.sin(2.0 * math.pi * f0 * n / pcm.fs)

    for n in range(0, int(pcm.fs * 0.01)):
        tmp[n] *= n / int(pcm.fs * 0.01)
        tmp[dur - n - 1] *= n / int(pcm.fs * 0.01)

    for n in range(0, dur):
        pcm.s[int(offset + n)] += tmp[n]

def sine_scale_stereo(pcm, f0, a, offset, duration):
    dur = int(duration)
    tmp = [0]*dur

    for n in range(0, dur):
        tmp[n] = a * math.sin(2.0 * math.pi * f0 * n / pcm.fs)

    for n in range(0, int(pcm.fs * 0.01)):
        tmp[n] *= n / int(pcm.fs * 0.01)
        tmp[dur - n - 1] *= n / int(pcm.fs * 0.01)

    for n in range(0, dur):
        pcm.sL[int(offset + n)] += tmp[n]
        pcm.sR[int(offset + n)] += tmp[n]
        

if __name__ == '__main__':

    C4 = 261.63
    D4 = 293.66
    E4 = 329.63
    F4 = 349.23
    G4 = 392.00
    A4 = 440.00
    B4 = 493.88
    C5 = 523.25
    
    # 16bit sine scale (Mono)
    pcm = MonoPcm(44100, 16, 44100 * 2)
    sine_scale_mono(pcm, C4, 0.1, pcm.fs * 0.00, pcm.fs * 0.25)
    sine_scale_mono(pcm, D4, 0.1, pcm.fs * 0.25, pcm.fs * 0.25)
    sine_scale_mono(pcm, E4, 0.1, pcm.fs * 0.50, pcm.fs * 0.25)
    sine_scale_mono(pcm, F4, 0.1, pcm.fs * 0.75, pcm.fs * 0.25)
    sine_scale_mono(pcm, G4, 0.1, pcm.fs * 1.00, pcm.fs * 0.25)
    sine_scale_mono(pcm, A4, 0.1, pcm.fs * 1.25, pcm.fs * 0.25)
    sine_scale_mono(pcm, B4, 0.1, pcm.fs * 1.50, pcm.fs * 0.25)
    sine_scale_mono(pcm, C5, 0.1, pcm.fs * 1.75, pcm.fs * 0.25)
    pcm.wave_write_16bit("./wavefiles/mono16_sine_scale.wave")

    # 16bit sine scale (Stereo)
    pcm2 = MonoPcm(44100, 16, 44100 * 2)
    sine_scale_mono(pcm2, C4, 0.1, pcm2.fs * 0.00, pcm2.fs * 0.25)
    sine_scale_mono(pcm2, D4, 0.1, pcm2.fs * 0.25, pcm2.fs * 0.25)
    sine_scale_mono(pcm2, E4, 0.1, pcm2.fs * 0.50, pcm2.fs * 0.25)
    sine_scale_mono(pcm2, F4, 0.1, pcm2.fs * 0.75, pcm2.fs * 0.25)
    sine_scale_mono(pcm2, G4, 0.1, pcm2.fs * 1.00, pcm2.fs * 0.25)
    sine_scale_mono(pcm2, A4, 0.1, pcm2.fs * 1.25, pcm2.fs * 0.25)
    sine_scale_mono(pcm2, B4, 0.1, pcm2.fs * 1.50, pcm2.fs * 0.25)
    sine_scale_mono(pcm2, C5, 0.1, pcm2.fs * 1.75, pcm2.fs * 0.25)
    pcm2.wave_write_16bit("./wavefiles/stereo16_sine_scale.wave")
