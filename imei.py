import hashlib


def check_imei_sum(imei: str) -> bool:
    digits = [int(e) for e in  imei[::-1]]
    impairs = [(e * 2) % 10 + (1 if 2*e > 9 else 0) for e in digits[1::2]]
    pairs = digits[0::2]
    return (sum(pairs + impairs) % 10) == 0


# Compute the unlock code
# Adapted from dogbert's original
def compute_imei_unlock_code(imei: str) -> str:
    salt = '5e8dd316726b0335'
    digest = hashlib.md5((imei + salt).lower().encode()).digest()
    code = 0
    for i in range(0, 4):
        code += ( ord(digest[i])
                ^ ord(digest[4 + i])
                ^ ord(digest[8 + i])
                ^ ord(digest[12 + i])
                ) << (3 - i) * 8
    code &= 0x1ffffff
    code |= 0x2000000
    return code
