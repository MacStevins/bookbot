def _sort_on_key(item, key: str):
	return item[key]

def get_word_count(text: str):
	return len(text.split())

def get_each_char_count(text: str):
	text = text.lower()
	chars = []
	chars_count = []
	
	for c in text:
		if c not in chars:
			chars.append(c)
			
			if c == "\n":
				chars_count.append({"char": "\\n", "count": text.count(c)})
			else:
				chars_count.append({"char": c, "count": text.count(c)})
	
	chars_count.sort(reverse=True, key=lambda item: _sort_on_key(item, "count"))
	
	return chars_count