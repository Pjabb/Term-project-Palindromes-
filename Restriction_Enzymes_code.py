import itertools, sys, re, os
file = "/rhome/yoza001/Project_practice/Scchr1.fasta"
inputfile="Scchr1.fasta"
if not os.path.exists(inputfile):
    os.system("curl -O {}".format(file))

# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence

with open(file,"rt") as fh:
    seqs = aspairs(fh)
    for seqinfo in seqs:
        seqstr = seqinfo[1].lower()

reffile = "resenzsmall.txt"
with open(reffile,"r") as f:
     for line in f.readlines():
        words = line.split()
         #seqs[words[0]] = (words[1], words[2])
        pattern = re.compile(words[1])
        match = pattern.search(seqstr)
        count = pattern.findall(seqstr)
        print(words[0],"matches", len(count), "sites")
        #newseq=re.sub(PREsite,REPLACE,seqstr,flags=re.IGNORECASE)
        #print(seqstr)

