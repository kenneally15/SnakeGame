#!/usr/bin/env python3

from human import Human


def add(x,y):
	return x+y

def mult(x,y):
	return x*y

def main():
	print("Hello world!")
	print("Test script")

	x = 2
	y = 3

	print(f"{x} + {y} =",add(x,y))
	print(f"{x}*{y}=",mult(x,y))

	l = Human()
	k = Human("Kevin")
	m = Human("Marianne",2)

	k.say("hello")

if __name__ == '__main__':
	main()


