#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:52:57 2023

@author: sam
"""

import spacy 
nlp = spacy.load('en_core_web_sm')
gardenpathSentences = ["When Fred Douglas eats food gets thrown.",
                       "Mary gave the child the dog bit a Band-Aid.",
                       "The cotton clothing is made of grows in Mississippi.",
                       "Until the L.A police arrest the drug dealers control the street.",
                       "The Inuit can fish in their new factory in town.",
                       "British left waffles on Falklands."]

print("These are garden path sentences")
print(gardenpathSentences)

print("\n")


for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Tokenisation")
    print([(token, token.orth_, token.orth) for token in doc])
    print("\n")
    
    print("This is entity recognition")
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print("\n")
 
print(f" NORP: {spacy.explain('NORP')}")
print(f" GPE: {spacy.explain('GPE')}")

#I looked up the entity NORP, it is for Nationalities or religious or
# political groups. And it is used correctly in all the sentences. 

#I also looked up GPE and it is for countries, cities, or states. It 
#is mainly used correctly, however it did not recognise L.A police as an 
# entity. 

  
    
