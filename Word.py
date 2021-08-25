badletters = ["g", "p", "m", "d"]

with open("english.txt", "r") as f:
	text = f.read().split()
	cleanlist = []

	for word in text:
		is_clean = not any(letter in word for letter in badletters)
		if is_clean:
			cleanlist.append(word)

with open("english2.txt", "w") as f:


	cleanstring = "\n".join(cleanlist)
	f.write(cleanstring)
