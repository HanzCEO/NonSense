from random import choice

a = "aiueo"
b = "bcdfghjklmnpqrstvwxyz"

def suggest(l):
	f = "a"
	if choice([1,0]):
		f += choice(a)

	for i in range(l-1):
		if f[-1] in a:
			f += choice(b)
		else:
			f += choice(a)
	return f[1:]

print("Enter/Return - Get more suggestion")
print("q/ctrl+c - Quit")
while True:
	print(suggest(6), end="")

	try:
		inp = input()
		if inp == "q": break
	except KeyboardInterrupt:
		break
