
def main():
	with open('challenge2data.txt') as f:
		data = f.read()
		
	print("http://www.pythonchallenge.com/pc/def/" + "".join([i for i in data if i not in data[data.index(i) + 1:]]) + ".html")

if __name__ == '__main__':
	main()