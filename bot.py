#!/usr/bin/env python
###########################################################
# 
# Script for generating clickbait facebook images
# 
# Example code blatantly copied from:
# http://www.nltk.org/
# 

import nltk

sentence = """Trump has less of a mandate for his agenda than any 
President-elect in history."""

tokens = nltk.word_tokenize(sentence)

print(tokens)

