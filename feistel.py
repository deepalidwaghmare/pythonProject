import sys
import re

def encrypt(input, rounds, roundkeys):
	#TODO: Implement encryption of "input" in "rounds" rounds, using round keys "roundkeys"
	return "00000000"

def decrypt(input, rounds, roundkeys):
	#TODO: Implement decryption of "input" in "rounds" rounds, using round keys "roundkeys"
	return "11111111"

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

c = re.compile('^[01]{8}$')
try:
	input=args.pop(0)
except IndexError:
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
if not c.search(input):
	raise SystemExit("input is not a valid bit string")

try:
	rounds=int(args.pop(0))
except IndexError:
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
except ValueError:
	raise SystemExit("rounds is not a valid number")

if(len(args)<rounds):
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")

roundkeys=args
c = re.compile('^[01]{4}$')
if not all(c.search(elem) for elem in roundkeys):
	raise SystemExit("round key is not a valid bit string")

if "-d" in opts:
	result = decrypt(input,rounds,roundkeys)
else:
	result = encrypt(input,rounds,roundkeys)

print (result)