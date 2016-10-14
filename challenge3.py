def main():
	
	with open('challenge3data.txt') as f:
		data = f.read()

	data = data.replace("\n", "")
	list = []

	for i in range(3, len(data) - 4):
	
		B0 = ord("a") <= ord(data[i]) <= ord("z")
		B1 = ord("a") <= ord(data[i - 4])
		B2 = not ord("a") <= ord(data[i - 3])	
		B3 = not ord("a") <= ord(data[i - 2])
		B4 = not ord("a") <= ord(data[i - 1])
		B5 = not ord("a") <= ord(data[i + 1])
		B6 = not ord("a") <= ord(data[i + 2])
		B7 = not ord("a") <= ord(data[i + 3])
		B8 = ord("a") <= ord(data[i + 4])

		if B0 and B1 and B2 and B3 and B4 and B5 and B6 and B7 and B8:
			print(data[i - 4],data[i - 3],data[i - 2],data[i - 1],data[i],data[i + 1],data[i + 2],data[i + 3],data[i + 4])
			list.append(data[i] )
	print("\nhttp://www.pythonchallenge.com/pc/def/" + "".join(list) + ".php\n")	

if __name__ == '__main__':
	main()