import argparse
import json
'''
This script saves in a TFile the effect of the selected nuisance for the 
given samples and variables. 

The effect is saved as the ratio of variationn/nominal.


example 1:
python nuisance_to_json.py \
    -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_13Sep2022_2018/plots_VBS_ZV_13Sep2022_2018.root \
        -o testNorm.json -s VBS_VV_QCD -c Boosted_SR_bVeto -n QCDscale_VBS_VV_QCD

example 2 (via cut-file.txt):
python nuisance_to_json.py \
    -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_13Sep2022_2018/plots_VBS_ZV_13Sep2022_2018.root \
        -o ../2016_Jul22/VBS_VV_QCD_QCDscale.json -s VBS_VV_QCD -cf cut-file.txt -n QCDscale_VBS_VV_QCD


python nuisance_to_json.py \
    -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_12Sep2022_2016/plots_VBS_ZV_12Sep2022_2016.root \
        -o ../2016_Jul22/VBS_VV_QCD_QCDscale_2016.json -s VBS_VV_QCD -cf cut-file.txt -n QCDscale_VBS_VV_QCD
'''
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-o","--output", help="Output file", type=str)
parser.add_argument("-s","--samples", help="Samples", type=str, nargs="+")
parser.add_argument("-c","--cuts", help="Cut", type=str)
parser.add_argument("-cf","--cuts-file", help="Cut", type=str)
parser.add_argument("-n","--nuisances", help="Nuisances", type=str, nargs="+")
args = parser.parse_args()

import ROOT as R 
R.gROOT.SetBatch(True)
R.TH1.SetDefaultSumw2()


iF = R.TFile.Open(args.input, "READ")
output = {}

##new
if args.cuts and len(args.cuts) > 0:
    cuts = args.cuts 
elif args.cuts_file:
    cuts = [c.strip() for c in open(args.cuts_file).readlines()]
else:
    print("Please provide cuts of file with a list of cuts")
    exit(1)


for cut in cuts:

    output[cut] = {}
    print "Cut: ", cut
    for s in args.samples:
#        output[s] = {}
        print ">> Sample: ", s 
        h_nom = iF.Get("{}/events/histo_{}".format(cut, s ))

        for n in args.nuisances:
            try:
                h_up = iF.Get("{}/events/histo_{}_{}Up".format(cut, s, n))
                h_do = iF.Get("{}/events/histo_{}_{}Down".format(cut, s, n))
                corr_up = h_nom.Integral()/h_up.Integral()
                corr_do = h_nom.Integral()/h_do.Integral()
                print s, " | ", n, " | nom: ",h_nom.Integral(), " | up: ", h_up.Integral(), " (", corr_up , \
                                            ") | do: ", h_do.Integral(), " (" , corr_do, ") |"
                output[cut][n] = (corr_up, corr_do)
                #print(output[cut])
#                output[s][n] = (corr_up, corr_do)

            except:
                continue
         
print "------------------------------"

with open(args.output,'w') as out:
    out.write(json.dumps(output, indent=2))