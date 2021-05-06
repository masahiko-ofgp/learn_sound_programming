from wavew import MonoPcm, StereoPcm
import math

def saw_mono(pcm, f0):
    for i in range(1, 45):
        for n in range(0, pcm.length):
            pcm.s[n] += 1.0 / i * math.sin(
                    2.0 * math.pi * i * f0 * n / pcm.fs
                    )
    gain = 0.1
    for n in range(0, pcm.length):
        pcm.s[n] *= gain

def saw_stereo(pcm, f0):
    for i in range(1, 45):
        for n in range(0, pcm.length):
            pcm.sL[n] += 1.0 / i * math.sin(
                    2.0 * math.pi * i * f0 * n / pcm.fs
                    )
            pcm.sR[n] += 1.0 / i * math.sin(
                    2.0 * math.pi * i * f0 * n / pcm.fs
                    )
    gain = 0.1
    for n in range(0, pcm.length):
        pcm.sL[n] *= gain
        pcm.sR[n] *= gain


if __name__ == '__main__':

    # 8bit saw wave (Mono)
    mono8 = MonoPcm(44100, 8)
    saw_mono(mono8, 500.0)
    mono8.wave_write_8bit("./wavefiles/mono8_saw.wave")

    # 16bit saw wave (Mono)
    mono16 = MonoPcm(44100, 16)
    saw_mono(mono16, 500.0)
    mono16.wave_write_16bit("./wavefiles/mono16_saw.wave")

    # 8bit saw wave (Stereo)
    stereo8 = StereoPcm(44100, 8)
    saw_stereo(stereo8, 500.0)
    stereo8.wave_write_8bit("./wavefiles/stereo8_saw.wave")

    # 16bit saw wave (Stereo)
    stereo16 = StereoPcm(44100, 16)
    saw_stereo(stereo16, 500.0)
    stereo16.wave_write_16bit("./wavefiles/stereo16_saw.wave")


