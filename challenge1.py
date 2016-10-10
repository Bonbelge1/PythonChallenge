def mapping(string):
	return "".join(chr(((ord(i) + 2) % ord("a")) % 26 + ord("a")) if ord("a") <= ord(i) <= ord("z") else i for i in string)

def main():
	string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	print(mapping(string))
	print("\nhttp://www.pythonchallenge.com/pc/def/" + str(mapping("map")) + ".html\n")

if __name__ == '__main__':
	main()