# Run grep with multiple inputs
# patterns_to_use.txt should be the grep input
# file_to_search.txt should be the file to be searched
# Output is written to results.txt

import re
def grep(pattern,file_to_search):
	with open(file_to_search, "r") as f:
		results = {}
		linecount = 0
		search_file = f.readlines()
		for word in pattern:
			for line in search_file:
				try:
					if re.search(word, line):
						results[word] = line
				except:
					results[word] = "ERROR searching: \"{line} \"".format(line=line)
					print("found an error processing pattern {pattern}!".format(pattern=word))
			linecount += 1
			if linecount % 1000 == 0:
				print("Parsed line {}, still working...".format(linecount))
		return results

def pattern_variable(pattern_file):
	with open(pattern_file) as pf:
		lines = pf.readlines()
		pattern = []
		for line in lines:
			word = line.strip()
			pattern.append(word)
	return pattern

def main():
	pattern = (pattern_variable("patterns_to_use.txt"))
	results = grep(pattern,"file_to_search.txt")
	with open("results.txt", "w") as results_file:
		for key, value in results.items():
			results_file.write("pattern: {key}, match: {value}".format(key=key, value=value))
		results_file.close()


if __name__ == "__main__":
	main()
