
import sys

ids = []
proc = {}
for line in open(sys.argv[1]+'-dfs-linear.txt','rU'):
    a, b, c = line.strip().split('\t')
    proc[a] = [b.strip(), c.strip(), ]
    ids.append(a)

orig = {}
for line in open(sys.argv[1]+'-nl.txt','rU'):
    a, b = line.strip().split('\t')
    orig[a] = b.strip().lower()

fsrc = open(sys.argv[1]+'-dfs-linear_src.txt','w')
ftarg = open(sys.argv[1]+'-dfs-linear_targ.txt','w')
for id in ids:
    print >>fsrc, proc[id][0]
    print >>ftarg, orig[id]

