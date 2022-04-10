from random import choice
from time import sleep

a = "aiueo"
b = "bcdfghjklmnpqrstvwxyz"
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

print("Enter/Return - Get more suggestion")

if not auto:
	print("q/ctrl+c - Quit")
else:
	print("ctrl+c - Quit")

while True:
	suggestion = suggest(length)

	try:
		if not auto:
			print(suggestion, end="")
			inp = input()
			if inp == "q":
				break
		else:
			print(suggestion)
			sleep(1)
	except KeyboardInterrupt:
		break
