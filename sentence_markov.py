import random

'''
doc_dict = {}
doc_dict_keys = []

def subset_from_word(w):
	if len(doc_dict_keys) == 0:
		doc_dict_keys = doc_dict.keys()

	if w in doc_dict.keys():
		return " ".join(doc_dict[w])
	else:
		return ""
		'''

def find_largest_sub(source, s):
	s_split = s.split()
	for r in range(min(10, len(s_split)+1), 0, -1):

		s2 = ""
		for i in range(1, r):
			s2 = s_split[-i] + " " + s2

		
		s2 = s2.strip()

		if s2 in source:
			return r-1, s2


	return 0, ""

def get_new(source, s):
	a, b = get_new_helper(source, s)
	if a == "" or a == " ":
		a = random.choice(source.split())
		b = 0
	return a, b

def get_new_helper(source, s):
	if s == "":
		return random.choice(source.split()), 0

	d, subs = find_largest_sub(source, s)

	if d == 0:
		return random.choice(source.split()), 0

	N = source.count(" " + subs.strip() + " ")
	p = min(0.95,(N) / (2 + N))

	A = random.random() < p
	if A:
		split_source = source.split(" " + subs.strip() + " ")[1:]
		b = random.choice(split_source).strip()
		#print(b, len(b) > 0)
		if len(b) > 0:
			return b.split()[0].strip(), d
		else:
			return random.choice(source.split()), 0

	elif len(s.split()) == 0:
		return random.choice(source.split()), 0
	elif random.random() < 0.7:
		without_last = " ".join(s.split()[1:])
		return get_new_helper(source, without_last)
	elif random.random() < 0.9:
		return get_new_helper(source, s.split()[-1])
	else:
		return random.choice(source.split()), 0

source_str = open("data/" + "output.txt", "r").read()

source_str_l = source_str.lower().replace(".", "").replace(",", "").split()
l_all, l_unique = len(source_str_l), len(set(source_str_l))
print(l_unique, l_all, l_all / l_unique, l_unique / l_all)

#math.log(0)
#source_str = source_str.replace("\n", " NEWLINE ").replace(",", " COMMA ")
source_str = source_str.lower().replace("\n\n", " NEWLINENEWLINE ").replace("\n", " ").replace(",", " COMMA ")

def main():
	full = "tärkeää muistaa"
	current = full.lower()
	for i in range(100):
		#subset_str = subset_from_word(current)
		new_word, d = get_new(source_str, current)
		if i % 2 == 0:
			print("new word", new_word, d)
		current += " " + new_word
		full += " " + new_word
		full = full.strip()
		current = current.strip()
		if len(current.split()) > 10:
			current = " ".join(current.split()[1:])

		current = current.strip()
		'''
		if current in source_str:
			print("OVERFIT")
			new_word, d = get_new(source_str, new_word)
			print("new word", new_word, d)
			current += " " + new_word
			full += " " + new_word
			full = full.strip()
			current = current.strip()
			if len(current.split()) > 10:
				current = " ".join(current.split()[1:])
		'''

	full = full.replace("NEWLINE", "\n").replace("COMMA", ", ").replace(" , ", ", ").replace(",  ", ", ")
	print(full)


main()