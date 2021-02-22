import sys, os, json

famr = open(sys.argv[1]+'.amr', 'w')
fsrc = open(sys.argv[1]+'.src', 'w')
ftgt = open(sys.argv[1]+'.snt', 'w')
amr = ''
src = ''
targ = ''
for i, line in enumerate(open(sys.argv[1]+'.txt', 'rU')):
    if line.strip() == '':
        amr = amr.strip()
        src = src.strip()
        targ = targ.strip()
        #if src == '' or sum(x=='(' for x in src) <= 2 or targ == '' or len(targ.split()) < 5:
        #    print i
        #    src = ''
        #    targ = ''
        #    continue
        if targ != '' and src != '':
            if sum(x=='(' for x in src) == sum(x==')' for x in src):
                print >>famr, amr
                print >>fsrc, src
                print >>ftgt, targ
            else:
                print i
                print amr
                print '------------'
        else:
            print '!!!'
        amr = ''
        src = ''
        targ = ''
    elif line.startswith('# ::snt'):
        src = ' '.join(line.strip().split()[2:])
    elif line.startswith('# ::de'):
        targ = ' '.join(line.strip().split()[2:])
    elif line[0] != '#':
        amr = amr + line.strip() + ' '

famr.close()
fsrc.close()
ftgt.close()

