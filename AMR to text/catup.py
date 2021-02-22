
import sys, os, codecs, json



for i in range(19,20):
    #cmd = 'cat /home/lsong10/ws/exp.nmt/data.de-en/parallel/all.tok_le50.en_shares/parsed/10K_%03d*amr > 100K_%02d.txt' %(i,i)
    #print cmd
    #os.system(cmd)
    #cmd = "sed -i -e 's/\"(\"/\"-\"/g' 100K_%02d.txt" %i
    #print cmd
    #os.system(cmd)
    #cmd = "sed -i -e 's/\")\"/\"-\"/g' 100K_%02d.txt" %i
    #print cmd
    #os.system(cmd)
    cmd = "./anonDeAnon_java.sh anonymizeAmrFull true 100K_%02d.amr" %i
    print cmd
    os.system(cmd)

