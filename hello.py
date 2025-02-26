#!/usr/bin/env python3

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


if __name__ == '__main__':
	main()


