import sys, os, json

fsrc = open(sys.argv[1]+'.amr', 'w')
ftgt = open(sys.argv[1]+'.snt', 'w')
src = ''
targ = ''
for i, line in enumerate(open(sys.argv[1]+'.txt', 'rU')):
    if line.strip() == '':
        src = src.strip()
        targ = targ.strip()
        #if src == '' or sum(x=='(' for x in src) <= 2 or targ == '' or len(targ.split()) < 5:
        #    print i
        #    src = ''
        #    targ = ''
        #    continue
        if sum(x=='(' for x in src) == sum(x==')' for x in src):
            print >>fsrc, src
            print >>ftgt, targ
        else:
            print i
            print src
            print '------------'
        src = ''
        targ = ''
    elif line.startswith('# ::tok'):
        targ = ' '.join(line.strip().lower().split()[2:])
    elif line[0] != '#':
        src = src + line.strip() + ' '

fsrc.close()
ftgt.close()

