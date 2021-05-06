from wavew import MonoPcm, StereoPcm
import math

def triangle_mono(pcm, f0):
    for i in range(1, 45, 2):
        for n in range(0, pcm.length):
            pcm.s[n] += 1.0 / i / i * math.sin(
                    math.pi * i / 2.0) * math.sin(
                            2.0 * math.pi * i * f0 * n / pcm.fs
                            )
    gain = 0.1
    for n in range(0, pcm.length):
        pcm.s[n] *= gain

def triangle_stereo(pcm, f0):
    for i in range(1, 45):
        for n in range(0, pcm.length):
            pcm.sL[n] += 1.0 / i / i * math.sin(
                    math.pi * i / 2.0) * math.sin(
                            2.0 * math.pi * i * f0 * n / pcm.fs
                            )
            pcm.sR[n] += 1.0 / i * math.sin(
                    math.pi * i / 2.0) * math.sin(
                            2.0 * math.pi * i * f0 * n / pcm.fs
                            )
    gain = 0.1
    for n in range(0, pcm.length):
        pcm.sL[n] *= gain
        pcm.sR[n] *= gain


if __name__ == '__main__':

    # 8bit triangle wave (Mono)
    mono8 = MonoPcm(44100, 8)
    triangle_mono(mono8, 500.0)
    mono8.wave_write_8bit("./wavefiles/mono8_triangle.wave")

    # 16bit triangle wave (Mono)
    mono16 = MonoPcm(44100, 16)
    triangle_mono(mono16, 500.0)
    mono16.wave_write_16bit("./wavefiles/mono16_triangle.wave")

    # 8bit triangle wave (Stereo)
    stereo8 = StereoPcm(44100, 8)
    triangle_stereo(stereo8, 500.0)
    stereo8.wave_write_8bit("./wavefiles/stereo8_triangle.wave")

    # 16bit triangle wave (Stereo)
    stereo16 = StereoPcm(44100, 16)
    triangle_stereo(stereo16, 500.0)
    stereo16.wave_write_16bit("./wavefiles/stereo16_triangle.wave")


