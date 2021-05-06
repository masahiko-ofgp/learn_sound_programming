from wavew import MonoPcm, StereoPcm
import math

def sine_mono(pcm, a, f0):
    for n in range(0, pcm.length):
        pcm.s[n] = a * math.sin(2.0 * math.pi * f0 * n / pcm.fs)

def sine_stereo(pcm, a, f0):
    for n in range(0, pcm.length):
        pcm.sL[n] = a * math.sin(2.0 * math.pi * f0 * n / pcm.fs)
        pcm.sR[n] = a * math.sin(2.0 * math.pi * f0 * n / pcm.fs)


if __name__ == '__main__':

    # 8bit sine wave (Mono)
    mono8 = MonoPcm(44100, 8)
    sine_mono(mono8, 0.1, 500.0)
    mono8.wave_write_8bit("./wavefiles/mono8_sine.wave")

    # 16bit sine wave (Mono)
    mono16 = MonoPcm(44100, 16)
    sine_mono(mono16, 0.1, 500.0)
    mono16.wave_write_16bit("./wavefiles/mono16_sine.wave")

    # 8bit sine wave (Stereo)
    stereo8 = StereoPcm(44100, 8)
    sine_stereo(stereo8, 0.1, 500.0)
    stereo8.wave_write_8bit("./wavefiles/stereo8_sine.wave")

    # 16bit sine wave (Stereo)
    stereo16 = StereoPcm(44100, 16)
    sine_stereo(stereo16, 0.1, 500.0)
    stereo16.wave_write_16bit("./wavefiles/stereo16_sine.wave")


