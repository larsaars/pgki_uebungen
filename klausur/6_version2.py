from typing import Union


def caesar(msg: str, k: int = 3) -> Union[str, None]:
    out = ''

    if abs(k) >= 26:
        return None

    A, Z, a, z = ord('A'), ord('Z'), ord('a'), ord('z')

    for c in msg:
        oc = ord(c)

        if a <= oc <= z:
            shift = (oc - a + k) % 26
            out += chr(a + shift)
        elif A <= oc <= Z:
            shift = (oc - A + k) % 26
            out += chr(A + shift)
        else:
            out += c

    return None


if __name__ == '__main__':
    test_msg = 'this is a test xyz'
    encoded_msg = caesar(test_msg)

    # print encoded and again decoded msg
    print(encoded_msg)
    print(caesar(encoded_msg, -3))
