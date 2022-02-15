import ROOT as R
import os
import numpy as np
import argparse

R.gROOT.SetBatch(True)

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--outputdir", type=str)
parser.add_argument("--outputfile", type=str)
parser.add_argument("--jet-type", type=str)
args = parser.parse_args()

os.makedirs(args.outputdir, exist_ok=True)

R.gStyle.SetOptStat(0)



f= R.TFile(args.input, "READ")
def get_cdf_func(h_i, name):
    h = h_i.Clone(name)

    m = h.GetMinimum()
    if m<0:
        for ibin in range(1, h.GetNbinsX()+1):
            h.SetBinContent(ibin, h.GetBinContent(ibin) - m)

    h.Scale(1/h.Integral())

    h_cdf = h.GetCumulative()
    g_cdf = R.TGraph()
    g_inv = R.TGraph()
    g_cdf.SetName(name + '_cdf')
    g_inv.SetName(name + '_inv')
    g_cdf.SetBit(19)
    g_inv.SetBit(19)
    g_cdf.SetPoint(0, 0., 0.)
    g_inv.SetPoint(0, 0., 0.)
    for ibin in range(1, h_cdf.GetNbinsX()+1):
        #print(ibin,  h_cdf.GetBinCenter(ibin), h_cdf.GetBinContent(ibin))
        y = h_cdf.GetBinContent(ibin)
        if y>1: y=1
        g_cdf.SetPoint(ibin, h_cdf.GetBinCenter(ibin), y)
        g_inv.SetPoint(ibin, y ,h_cdf.GetBinCenter(ibin))

    g_cdf.SetPoint(ibin+1, 1., 1.)
    g_inv.SetPoint(ibin+1, 1., 1.)
    return g_cdf, g_inv,h

def get_morphing(gG, gT_inv, name):
    t = R.TGraph()
    t.SetName(name)
    for i,x in enumerate(np.linspace(0.,1.,200)):
        y1 = gG.Eval(x)
        if y1>1: y1 = 1
        y = gT_inv.Eval(y1)
        if y>1: y=1
        t.SetPoint(i,x,y)
    return t

out = R.TFile(args.outputdir + '/' + args.outputfile, "RECREATE")


jet_type="quark"
for e in ["_loweta", "_higheta"]:
    for ptbin in [ "_pt0","_pt1"] :
        morphs = {}
        region = e+ptbin
        #fuse jets and gluon/quarks
        hMC = f.Get( 'j0_gluon_qgl'+e +ptbin)
        hMC.Add(f.Get( 'j0_quark_qgl'+e +ptbin))
        hData = f.Get('DATA_j0_nogen_qgl' +e +ptbin )
        hOthers = f.Get('Fake_j0_nogen_qgl' +e +ptbin )
        for  i in range(1,4):
            hMC.Add(f.Get( 'j{}_gluon_qgl'.format(i)+e +ptbin))
            hMC.Add(f.Get( 'j{}_quark_qgl'.format(i)+e +ptbin))
            hData.Add(f.Get('DATA_j{}_nogen_qgl'.format(i) +e +ptbin ))
            hOthers = f.Get('Fake_j{}_nogen_qgl'.format(i) +e +ptbin )
        nTot = hMC.Integral() + hOthers.Integral()
        # Scale data to tot MC
        hData.Scale(nTot / hData.Integral())
        
        
        hMC_target = hData.Clone("hMC_target_")
        hMC_target.Add(hOthers, -1.)
        
        gMC, gMC_inv, hMCcorr= get_cdf_func(hMC, region) #jet?
        gT , gT_inv, hMCtarget_corr = get_cdf_func(hMC_target, region + "_target")

        morph = get_morphing(gMC, gT_inv, region + "_quark")
        morph.Write()
        morphs[region + "_quark"] = morph
        morph = get_morphing(gMC, gT_inv, region + "_gluon")
        morph.Write()
        morphs[region + "_gluon"] = morph

        c = R.TCanvas()
        leg = R.TLegend(0.6,0.1,0.9,0.3)
        hMCcorr.Draw("hist")
        hMCcorr.SetLineWidth(2)
        hMCcorr.SetLineColor(R.kBlue)
        hMCcorr.GetYaxis().SetRangeUser(0, 1.2*hMCcorr.GetMaximum())
        leg.AddEntry(hMCcorr, "qgl corrected")
        hMCtarget_corr.Draw("hist same")
        hMCtarget_corr.SetLineWidth(2)
        hMCtarget_corr.SetLineColor(R.kGreen)
        leg.AddEntry(hMCtarget_corr, "target")
        c.Draw()
        leg.Draw("same")
        c.SaveAs(args.outputdir + '/morphing_debug_{}_{}.png'.format( e,ptbin))


