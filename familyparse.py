import sys
from Bio import SeqIO
input_file = sys.argv[1]


WXG100=[]
FTSK=[]

for seq_record in SeqIO.parse(input_file, "fasta"):
	identity= seq_record.description

       	if 'WXG' in identity or 'secreted' in identity or 'target' in identity:
               	print(seq_record.name)
  	     	print(seq_record.seq.tostring())
                WXG100.append(seq_record)
        else:
               	print(seq_record.name)
		print(seq_record.seq.tostring())
		FTSK.append(seq_record)


SeqIO.write(WXG100, "WXG", "fasta")
SeqIO.write(FTSK, "FTSK", "fasta")
