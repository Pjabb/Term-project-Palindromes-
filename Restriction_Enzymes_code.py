import itertools, sys, re, os
file = "/rhome/yoza001/Project_practice/pRS426_seq.fasta" #change the path here if using another file
inputfile="pRS426_seq.fasta" #use same filename as used above in 'file'
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

reffile = "resenz.txt" #change the restriction enzyme database file here
with open(reffile,"r") as f:
     for line in f.readlines():
        words = line.split()
         #seqs[words[0]] = (words[1], words[2])
        pattern = re.compile(words[1])
        match = pattern.search(seqstr)
        count = pattern.findall(seqstr)
        print(words[0],"matches", len(count), "sites and produces ",words[2],"ends.") #0, 1, 2 refer to column 1, 2, 3 from left in database file
        

