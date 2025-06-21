from stats import get_word_count, get_each_char_count
import sys

def get_book_text(filepath: str):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	print("============ BOOKBOT ============")
	print("Analyzing book found at", sys.argv[1])
	book_text = get_book_text(sys.argv[1])
	print("----------- Word Count ----------")
	print("Found", get_word_count(book_text), "total words")
	print("--------- Character Count -------")
	for a in get_each_char_count(book_text):
		print(a["char"] + ":", a["count"])

main()