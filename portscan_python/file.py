import os.path

filepath = "/home/sami/portscan_python/testfile.txt"

if os.path.isfile(filepath):
	print("File already exist")
	file = open("/home/sami/portscan_python/testfile.txt","a")
	file.write("tralalalalalalal")
	file = open("/home/sami/portscan_python/testfile.txt","r")
	for line in file:
		line = line.strip()
		print("das wars")
	file.close()
else:
	print("File not exist")


