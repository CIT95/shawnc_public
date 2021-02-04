def do_thing(): 
	try: 
		word = "Bird!Bird!Bird!"
		return word
	except NameError: 
		return "Bird is not the word."

print(do_thing())
