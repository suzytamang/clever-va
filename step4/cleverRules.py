import os, sys
from ruleFcns import *

ppath = sys.argv[1]
#clever = "/share/pi/stamang/nlp/clever-meddra/"
#Users/stamang/repos/CLEVER/proj/test/dm/ptseq
#ppath = clever + "proj/meddra/"
#ppath = "/share/pi/stamang/projects/covid/annotation/clever/meddra/test_shc/"
fins = ppath + "/linkedAnts.txt"
aclass = sys.argv[2]
print("Processing:", fins)
#print "PATIENTS with ANTS:", len(fins)

#Users/stamang/repos/CLEVER/proj/test/dm/ptseq
# output path for the final annotations
opath = ppath
ptPEvents = {}
ptNEvents = {}
ptEvents = {}
fout_pos = open(opath+"/allPos.txt","w")
fout_neg = open(opath+"/allNeg.txt","w")
#fout_misc = open(opath+"allMisc.txt","w")

with open(fins) as f:
    for line in f:
        tmp = line.strip()
        print("TEMP",tmp)
        if aclass not in tmp:
            continue
        label = assignLabel(tmp)
        tmpe = tmp.split("|")
        cid = tmpe[0]
        tseq = tmpe[1]
        longseq = tmpe[2]
        tterm = tmpe[3]
        pid = tmpe[4]
        nid = tmpe[5]
        ntype = tmpe[6]
        time = tmpe[7]
        year = tmpe[8]
        tclass = tmpe[9]
        tags = tmpe[14]
        snippet = tmpe[len(tmpe)-1]
        sum_out = label[0]+"|"+label[1]+"|"+pid+"|"+year+"|"+cid+"|"+time+"|"+ntype+"|"+nid+"|"+tterm+"|"+snippet
        long_out =  label[0]+"|"+label[1]+"|"+tmp
        tmpE = ""
        if label[0] == "POSITIVE":
                print(long_out, file=fout_pos)
        if label[0] == "NEGATIVE":
                print(long_out, file=fout_neg)
fout_pos.close()
fout_neg.close()
print("WROTE POS NEG FILES")

#print len(ptPEvents)
#print len(ptNEvents)
#print len(ptEvents)
#for pid in ptPEvents:
#        fpos = open(opath+"pt"+pid+"_pos.txt","w")
#        te = ptPEvents[pid]
#        for i in range(len(te)):
#                tevent = te[i]
#                print >> fpos,tevent
#                print pid,tevent
#        fpos.close()

#for pid in ptNEvents:
#        fneg = open(opath+"pt"+pid+"_neg.txt","w")
#        te = ptNEvents[pid]
#        for i in range(len(te)):
#                tevent = te[i] 
#                print >> fneg,tevent
#                print pid,tevent
#        fneg.close()

#for pid in ptEvents:
#        fcron = open(opath+"pt"+pid+"_cronology.txt","w")
#        te = ptEvents[pid]
#        for i in range(len(te)):
#                tevent = te[i] 
#                print >> fcron,tevent
#                print pid,tevent
#        fcron.close()

#s =assignMBCLabel(snippet)
#print s

#s = assignMBCLabel(s2)
