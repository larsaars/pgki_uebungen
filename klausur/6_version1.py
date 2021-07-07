from typing import Union


def caesar(msg: str, k: int = 3) -> Union[str, None]:
    out = ''

    if abs(k) >= 26:
        return None

    A, Z, a, z = ord('A'), ord('Z'), ord('a'), ord('z')

    def shift_index(i: int, lower: int, upper: int) -> int:
        i += k

        if i > upper:
            i = lower + abs(i - upper) - 1
        elif i < lower:
            i = upper - abs(i - lower) + 1

        return i

    for c in msg:
        oc = ord(c)

        if A <= oc <= Z:
            out += chr(shift_index(oc, A, Z))
        elif a <= oc <= z:
            out += chr(shift_index(oc, a, z))
        else:
            out += c

    return out


if __name__ == '__main__':
    test_msg = 'this is a test xyz'
    encoded_msg = caesar(test_msg)

    # print encoded and again decoded msg
    print(encoded_msg)
    print(caesar(encoded_msg, -3))
