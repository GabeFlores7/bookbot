def main(): # define script
	path = "books/frankenstein.txt"
	text = get_book_text(path)
	total_count = get_total_count(text)
#	print(f"{total_count} words found in the document")
	char_dict = get_char_stats(text)
#	print(f"frankenstein dictionary:  {char_dict}")
	get_agg_report(total_count,char_dict)

def get_book_text(path): # read contents of "frankenstein.txt" and return a string
	with open(path) as f:
		file_contents = f.read()
	return file_contents

def get_total_count(txt): #  Print and return a total count of words from the string returned above
	return len(txt.split())

def get_char_stats(txt): #create a dictionary for all characters that occur in text
	char_dict = {}
	txt= txt.lower()
	for char in txt:
		if char in char_dict: # if char exist in dict,
			char_dict[char] += 1 # update char value
		else: # if char doesn't exist, then initialize
			char_dict[char] = 1
	return char_dict

def convert_dictionary_to_list(dict): # return value of key for a dictionary
	list_of_dict = []
	for key in dict:
		value = dict[key]
		list_of_dict.append({"key":key, "val":value})
	return  list_of_dict
def sort_on(dict):
	return dict["val"]

def get_agg_report(count,char_dict): # create aggregate report including count and letter occurrence
	print("---Begin report of books/frankenstein.txt---")
	print(f"{count} words found in the document") # print total count of words
	char_list = convert_dictionary_to_list(char_dict) # convert dictionary into a list
	char_list.sort(reverse = True, key = sort_on) # sort the list
	for k in char_list: # for each key
		if k["key"].isalpha(): # is it from the alaphabet
			print(f"The '{k['key']}' character was found {k['val']} times")
	print("---End report---")
main()

