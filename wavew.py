from struct import pack
import math

RIFF_CHUNK_ID = 0x52494646     # 'RIFF'
FILE_FORMAT_TYPE = 0x57415645  # 'WAVE'
FMT_CHUNK_ID = 0x666D7420      # 'fmt '
DATA_CHUNK_ID = 0x64617461     # 'data'


class MonoPcm:
    def __init__(self, fs, bits, length=None):
        self.fs = fs
        self.bits = bits
        if length is None:
            self.length = fs * 1
        else:
            self.length = length
        self.s = [0] * self.length

    def wave_write_8bit(self, filename):
        riff_chunk_id = pack(">I", RIFF_CHUNK_ID)
        riff_chunk_size = pack("<I", 36 + self.length)
        file_format_type = pack(">I", FILE_FORMAT_TYPE)
        fmt_chunk_id = pack(">I", FMT_CHUNK_ID)
        fmt_chunk_size = pack("<I", 16)
        wave_format_type = pack("<H", 1)
        channel = pack("<H", 1)
        samples_per_sec = pack("<I", self.fs)
        bytes_per_sec = pack("<I", self.fs * self.bits // 8)
        block_size = pack("<H", self.bits // 8)
        bits_per_sample = pack("<H", self.bits)
        data_chunk_id = pack(">I", DATA_CHUNK_ID)
        data_chunk_size = pack("<I", self.length)
        
        with open(filename, "wb") as f:
            f.write(riff_chunk_id)
            f.write(riff_chunk_size)
            f.write(file_format_type)
            f.write(fmt_chunk_id)
            f.write(fmt_chunk_size)
            f.write(wave_format_type)
            f.write(channel)
            f.write(samples_per_sec)
            f.write(bytes_per_sec)
            f.write(block_size)
            f.write(bits_per_sample)
            f.write(data_chunk_id)
            f.write(data_chunk_size)

            for n in range(0, self.length):
                tmp = (self.s[n] + 1.0) / 2.0 * 256.0

                if tmp > 255.0:
                    tmp = 255.0
                elif tmp < 0.0:
                    tmp = 0.0

                data = pack("<B", round(tmp + 0.5))
                f.write(data)

            if (self.length % 2) == 1:
                data = pack("<B", 0)
                f.write(data)

    def wave_write_16bit(self, filename):
        riff_chunk_id = pack(">I", RIFF_CHUNK_ID)
        riff_chunk_size = pack("<I", 36 + self.length * 2)
        file_format_type = pack(">I", FILE_FORMAT_TYPE)
        fmt_chunk_id = pack(">I", FMT_CHUNK_ID)
        fmt_chunk_size = pack("<I", 16)
        wave_format_type = pack("<H", 1)
        channel = pack("<H", 1)
        samples_per_sec = pack("<I", self.fs)
        bytes_per_sec = pack("<I", self.fs * self.bits // 8)
        block_size = pack("<H", self.bits // 8)
        bits_per_sample = pack("<H", self.bits)
        data_chunk_id = pack(">I", DATA_CHUNK_ID)
        data_chunk_size = pack("<I", self.length * 2)
        
        with open(filename, "wb") as f:
            f.write(riff_chunk_id)
            f.write(riff_chunk_size)
            f.write(file_format_type)
            f.write(fmt_chunk_id)
            f.write(fmt_chunk_size)
            f.write(wave_format_type)
            f.write(channel)
            f.write(samples_per_sec)
            f.write(bytes_per_sec)
            f.write(block_size)
            f.write(bits_per_sample)
            f.write(data_chunk_id)
            f.write(data_chunk_size)

            for n in range(0, self.length):
                tmp = (self.s[n] + 1.0) / 2.0 * 65536.0

                if tmp > 65535.0:
                    tmp = 65535.0
                elif tmp < 0.0:
                    tmp = 0.0

                data = pack("<h", round(tmp + 0.5) - 32768)
                f.write(data)


class StereoPcm:
    def __init__(self, fs, bits, length=None):
        self.fs = fs
        self.bits = bits
        
        if length is None:
            self.length = fs * 1
        else:
            self.length = length

        self.sL = [0] * self.length
        self.sR = [0] * self.length

    def wave_write_8bit(self, filename):
        riff_chunk_id = pack(">I", RIFF_CHUNK_ID)
        riff_chunk_size = pack("<I", 36 + self.length * 2)
        file_format_type = pack(">I", FILE_FORMAT_TYPE)
        fmt_chunk_id = pack(">I", FMT_CHUNK_ID)
        fmt_chunk_size = pack("<I", 16)
        wave_format_type = pack("<H", 1)
        channel = pack("<H", 2)
        samples_per_sec = pack("<I", self.fs)
        bytes_per_sec = pack("<I", self.fs * self.bits // 8 * 2)
        block_size = pack("<H", self.bits // 8 * 2)
        bits_per_sample = pack("<H", self.bits)
        data_chunk_id = pack(">I", DATA_CHUNK_ID)
        data_chunk_size = pack("<I", self.length * 2)
        
        with open(filename, "wb") as f:
            f.write(riff_chunk_id)
            f.write(riff_chunk_size)
            f.write(file_format_type)
            f.write(fmt_chunk_id)
            f.write(fmt_chunk_size)
            f.write(wave_format_type)
            f.write(channel)
            f.write(samples_per_sec)
            f.write(bytes_per_sec)
            f.write(block_size)
            f.write(bits_per_sample)
            f.write(data_chunk_id)
            f.write(data_chunk_size)

            for n in range(0, self.length):
                tmp1 = (self.sL[n] + 1.0) / 2.0 * 256.0

                if tmp1 > 255.0:
                    tmp1 = 255.0
                elif tmp1 < 0.0:
                    tmp1 = 0.0

                data1 = pack("<B", round(tmp1 + 0.5))
                f.write(data1)

                tmp2 = (self.sR[n] + 1.0) / 2.0 * 256.0

                if tmp2 > 255.0:
                    tmp2 = 255.0
                elif tmp2 < 0.0:
                    tmp2 = 0.0

                data2 = pack("<B", round(tmp2 + 0.5))
                f.write(data2)

    def wave_write_16bit(self, filename):
        riff_chunk_id = pack(">I", RIFF_CHUNK_ID)
        riff_chunk_size = pack("<I", 36 + self.length * 4)
        file_format_type = pack(">I", FILE_FORMAT_TYPE)
        fmt_chunk_id = pack(">I", FMT_CHUNK_ID)
        fmt_chunk_size = pack("<I", 16)
        wave_format_type = pack("<H", 1)
        channel = pack("<H", 2)
        samples_per_sec = pack("<I", self.fs)
        bytes_per_sec = pack("<I", self.fs * self.bits // 8 * 2)
        block_size = pack("<H", self.bits // 8 * 2)
        bits_per_sample = pack("<H", self.bits)
        data_chunk_id = pack(">I", DATA_CHUNK_ID)
        data_chunk_size = pack("<I", self.length * 4)
        
        with open(filename, "wb") as f:
            f.write(riff_chunk_id)
            f.write(riff_chunk_size)
            f.write(file_format_type)
            f.write(fmt_chunk_id)
            f.write(fmt_chunk_size)
            f.write(wave_format_type)
            f.write(channel)
            f.write(samples_per_sec)
            f.write(bytes_per_sec)
            f.write(block_size)
            f.write(bits_per_sample)
            f.write(data_chunk_id)
            f.write(data_chunk_size)

            for n in range(0, self.length):
                tmp1 = (self.sL[n] + 1.0) / 2.0 * 65536.0

                if tmp1 > 65535.0:
                    tmp1 = 65535.0
                elif tmp1 < 0.0:
                    tmp1 = 0.0

                data1 = pack("<h", round(tmp1 + 0.5) - 32768)
                f.write(data1)

                tmp2 = (self.sR[n] + 1.0) / 2.0 * 65536.0

                if tmp2 > 65535.0:
                    tmp2 = 65535.0
                elif tmp2 < 0.0:
                    tmp2 = 0.0

                data2 = pack("<h", round(tmp2 + 0.5) - 32768)
                f.write(data2)
