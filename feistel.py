import sys
import re


# to run encryption in terminal:
# python3 feistel.py 10101010 5 0101 1111 1010 0101 0101
# to run decryption in terminal:
# python3 feistel.py -d 10100000 5 0101 1111 1010 0101 0101
def get_rnd_func_key(K, R):
    key = ''
    if len(K) == len(R):
        for i in range(0, len(K)):
            key += str(int(bool(int(K[i])) and bool(int(R[i]))))
    else:
        return None

    return key


def xor(L, FKR):
    new_R = ''
    if len(L) == len(FKR):
        for i in range(0, len(L)):
            new_R += str(int(bool(int(L[i])) ^ bool(int(FKR[i]))))
        return new_R
    else:
        return None


def encrypt(input, rounds, roundkeys):
    # TODO: Implement encryption of "input" in "rounds" rounds, using round keys "roundkeys"
    L = input[0:len(input) // 2]
    R = input[len(input) // 2:]
    for round in range(0, rounds):
        key = roundkeys[round]
        f_rk = get_rnd_func_key(key, R)
        new_R = xor(L, f_rk)
        L = R
        R = new_R

    cyphertext = R + L

    return cyphertext


def decrypt(input, rounds, roundkeys):
    # TODO: Implement decryption of "input" in "rounds" rounds, using round keys "roundkeys"
    roundkeys_reversed = []
    for elem in reversed(roundkeys):
        roundkeys_reversed.append(elem)

    L = input[0:len(input) // 2]
    R = input[len(input) // 2:]
    for round in range(0, rounds):
        key = roundkeys_reversed[round]
        f_rk = get_rnd_func_key(key, R)
        new_R = xor(L, f_rk)
        L = R
        R = new_R

    plaintext = R + L

    return plaintext


opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

c = re.compile('^[01]{8}$')
try:
    input = args.pop(0)
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
if not c.search(input):
    raise SystemExit("input is not a valid bit string")

try:
    rounds = int(args.pop(0))
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
except ValueError:
    raise SystemExit("rounds is not a valid number")

if (len(args) < rounds):
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")

roundkeys = args
c = re.compile('^[01]{4}$')
if not all(c.search(elem) for elem in roundkeys):
    raise SystemExit("round key is not a valid bit string")

if "-d" in opts:
    result = decrypt(input, rounds, roundkeys)
else:
    result = encrypt(input, rounds, roundkeys)

print(result)