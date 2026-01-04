import os

def fibonacci(n):
	sequence = []
	a, b = 0, 1
	for _ in range(n):
		sequence.append(a)
		a, b = b, a + b

	for i in sequence:
		print(i)

def main():
	n = int(input("Please enter the parameter of fibonacci:"))
	fibonacci(n)

if __name__ == "__main__":
	main() 
