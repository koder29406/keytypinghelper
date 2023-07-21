
import hashlib
from dataclasses import dataclass

@dataclass
class KeyInfo:
	"""Class to collect info about a key file"""
	lines: int
	line_hashes: list[str]
	key_hash: str
        
def shasum(text: str):
    return hashlib.sha1(text.encode('UTF-8')).hexdigest()

def hashbyline(lines):
    line_hashes = []
    for line in lines:
        line_hashes.append(hashlib.sha1(line.encode('UTF-8')).hexdigest())
    return line_hashes

def print_key_info(key_info: KeyInfo):
     print("  Key lines: " + str(key_info.lines))
     print("   Key hash: " + key_info.key_hash)
     for n in range(len(key_lines)):
          print(f"Line {n + 1} hash: {key_info.line_hashes[n]}")

prev_key_hash = None
filename = "newkey"
while True:
	try:
		with open(filename, "r") as file:
			key = file.read()
	except FileNotFoundError:
		continue
	key_lines = key.splitlines(True)

	key_info = KeyInfo(lines=len(key_lines), line_hashes=hashbyline(key_lines), key_hash=shasum(key))

	try:
		if key_info.key_hash != prev_key_hash:
			#formatted = ':'.join(a+b for a,b in zip(shad.hexdigest()[::2], shad.hexdigest()[1::2]))
			print_key_info(key_info)
	except AttributeError:
		print_key_info(key_info)
	prev_key_hash = key_info.key_hash
