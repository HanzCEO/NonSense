import sys
from random import choice
from time import sleep

a = "aiueo"
b = "bcdfghjklmnpqrstvwxyz"
isBulk = False
bulkNum = 1
length = 5
auto = False

if len(sys.argv) > 1:
	isBulk = sys.argv[1] == "--bulk"

if isBulk and len(sys.argv) > 2:
	bulkNum = int(sys.argv[2])
elif len(sys.argv) == 2:
	print("USAGE: --bulk <num>")
	exit()
else:
	length = int(input("Length (5): ") or 5)
	auto = bool(input("Auto drive (false): "))

def suggest(l):
	f = "a"
	if choice([1,0]):
		f += choice(a)

	for i in range(l):
		if f[-1] in a:
			f += choice(b)
		else:
			f += choice(a)
	return f[1:l+1]

if not isBulk:
	print("Enter/Return - Get more suggestion")

if not auto and not isBulk:
	print("q/ctrl+c - Quit")
elif not isBulk:
	print("ctrl+c - Quit")

while bulkNum > 0:
	suggestion = suggest(length)

	try:
		if not auto and not isBulk:
			print(suggestion, end="")
			inp = input()
			if inp == "q":
				break
		elif auto:
			print(suggestion)
			sleep(1)
		elif isBulk:
			print(suggestion)
	except KeyboardInterrupt:
		break

	if isBulk:
		bulkNum -= 1
