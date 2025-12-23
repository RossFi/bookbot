import sys
from stats import get_num_words, get_char_count, get_sorted_count

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

char_dict = get_char_count(sys.argv[1])
sorted_dict = get_sorted_count(char_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
get_num_words(sys.argv[1])
print("--------- Character Count -------")
for each in sorted_dict:
	print(f"{each["char"]}: {each["num"]}")
print("============= END ===============")
