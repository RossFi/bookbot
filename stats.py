def get_num_words(file_path):
        with open("./" + file_path) as f:
                file_contents = f.read().split()
                num_words = len(file_contents)

        print(f"Found {num_words} total words")

def get_char_count(file_path):
	with open("./" + file_path) as f:
		file_contents = f.read().split()
		lower_case_contents = [item.lower() for item in file_contents]
		word_dict = {}
		for word in lower_case_contents:
			for char in word:
				if char not in word_dict:
					word_dict[char] = 1
				else:
					word_dict[char] += 1
		return word_dict

def get_sorted_count(messy_dict):
	initial_list = []
	for entry in messy_dict:
		if entry.isalpha():
			initial_list.append({"char": entry, "num": messy_dict[entry]})
	initial_list.sort(key=lambda item: item["num"], reverse = True)
	return initial_list
