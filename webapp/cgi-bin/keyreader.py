def getkey(loc):
	try:
		with open(loc) as key:
			key_list = key.read()
			key_list = key_list.split('\n')
			for each_item in key_list:
				print("<br><a>" + each_item + "</a>")

	except IOError as err:
		print('File Error: ' + str(err))