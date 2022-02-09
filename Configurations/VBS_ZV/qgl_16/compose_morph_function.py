import ROOT as R
import os
import numpy as np
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--file1", type = str)
parser.add_argument('--file2', type=str)
parser.add_argument('--outputdir', type=str)
parser.add_argument('--outputfile', type=str)
parser.add_argument("--func1", nargs="+", type=str)
parser.add_argument("--func2", nargs="+", type=str)
parser.add_argument("--dostep2", type=str)
args=parser.parse_args()
os.makedirs(args.outputdir, exist_ok=True)

R.gStyle.SetOptStat(0)


morph1_file=R.TFile(args.file1, 'READ')
morph2_file=R.TFile(args.file2, 'READ')
out=R.TFile(args.outputdir + '/' + args.outputfile, "RECREATE")
morph_flags=[bool(int(c)) for c in args.dostep2]
for i,region in enumerate(args.func2):
    print(region)
    morph1=morph1_file.Get(args.func1[i])
    #morph1_file.Close()
    morph2=morph2_file.Get(args.func2[i])
    #morph2_file.Close()
    t = R.TGraph()
    t.SetName(region)
    for j,x in enumerate(np.linspace(0.,1.,200)):
        y1 = morph1.Eval(x)
        if y1>1: y1 = 1
        if morph_flags[i]==True:
            y = morph2.Eval(y1)
        else: y = y1
        if y>1: y=1
        t.SetPoint(j,x,y)
    t.Write()
out.Close()
    
