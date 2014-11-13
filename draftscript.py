#!/usr/bin/env python


import sys
import os 
import glob
input_file = sys.argv[1]  
from Bio import SeqIO

gene=[]

for fasta in glob.glob(input_file + '*.faa'):
	for seq_record in SeqIO.parse(fasta, "fasta"):
       		identity= seq_record.description

        	if 'WXG' in identity or 'type VII' in identity or 'Type VII' in identity:
                	print(seq_record.name)
               		print(seq_record.seq.tostring())
                	gene.append(seq_record)
        	else:
                	continue

print(gene) 
SeqIO.write(gene, "ftskWXG.faa" , "fasta")

