#!/usr/bin/env python

##gigaword_for_SLM_preprocess.py; previously saved elsewhere as "buffer.py" or "SLM_preprocess.py".

##2013/09/28. LK: This script was created to do some preprocessing on training (& testing) texts for the CMU SLM Toolkit, specifically for the purpose of building ngram language models with the toolkit (but it should be appropriate for other uses of the toolkit). The main purpose of this script is to split the punctuation off from words in the training text, because the SLM Toolkit does not do this. For example, in training a toy model on Moby Dick, I found that "Egyptians", "Egyptians.", and "Egyptians;" are all treated as different word types, which is not how we'd like to handle this-- it leads to data sparsity problems, etc. The toolkit also allows the user to specify a start symbol that will occur before each sentence; we're writing the outfile with 1 sentence per line, so the "start symbol" is really just "\n".

##usage:
##the training text needs to be compiled into a single file (unless you want to modify this script or run it within a shell that iterates through a directory). (Note that a script is included in this github repository that unzips all the gigaword .gz files and compiles them into a single text file; this script is called "gigaword_compile.sh".) The file names below for infile and outfile should be changed as necessary/desired.

import re
from nltk.tokenize import word_tokenize, sent_tokenize

##infile = open("trainingtoy.txt", "r")
##outfile = open("trainingtoyout.txt", "a")
infile = open("gigaword.txt", "r")
outfile = open("gigaword_for_SLM.txt", "a")

inline = infile.readline().lower()
while inline != '': ##blank lines == "\n", the end of the file == '' (which is NOT an exception)
	counter = 0
	bufferstring = ''
	while counter < 500 and inline != '':
		while inline.strip() != '<text>' and inline.strip() != '':
			inline = infile.readline().lower()
		inline = infile.readline().lower()
		while inline.strip() != '</text>' and inline.strip() != '':
			if inline.strip() != '<p>' and inline.strip() != '</p>':
				bufferstring = ''.join([bufferstring, inline])
				inline = infile.readline().lower()
				counter += 1
			else:
				inline = infile.readline().lower()
	bufferstring = bufferstring.replace("\n\n", "\n")
	bufferstring = bufferstring.replace("\n", " ")
	#print bufferstring
	try:
		buffersents = sent_tokenize(bufferstring)
		for sent in buffersents:
			buffsentwords = word_tokenize(sent)
			cleanwords = []
			for word in buffsentwords:
				##for whatever reason, word_tokenize(string) converts quotation marks into a different form, which I reverse below
				word = word.replace("``", '"')
				word = word.replace("''", '"')
				cleanwords.append(word)
			cleanwords.insert(0, '<s>')
			cleanstring = ' '.join(cleanwords)
			#print cleanstring
			outfile.write(cleanstring)
			outfile.write('\n')
	except:
		pass
	inline = infile.readline().lower()
