import zlib

def crc32_hash(string, max_unique=1000):
    checksum = zlib.crc32(string.encode('utf-8'))
    return checksum % max_unique