import ROOT
import math
import os

ROOT.gROOT.SetBatch(True)  # Enable batch mode
ROOT.objs = []

Hin = dict()
Hin_up = dict()
Hin_down = dict()
Rat_up = dict()
Rat_down = dict()

file_Hin = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016-dim8/plots_VBS_ZV_6Dec2023_2016-dim8_boosted_wBkg_allOperators_v2.root'
file_Hin_up = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted.root'
file_Hin_down = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2016/corrections/plots_VBS_ZV_6Dec2023_2016_boosted.root'

outputPath='/eos/user/m/mpresill/www/VBS/EFTplots/validation/'

samples_Hin = ['sm' ] #, 'sm_lin_quad_cT0']
samples_Hin_up = ['sm_dipole'] #, 'sm_lin_quad_cT0']
samples_Hin_down = ['sm_dipole' ] #, 'sm_lin_quad_cT0']

colors = ['kBlue+1', 'kGreen+1', 'kRed+1']

variables = [ 'ZV_mass']

def Getting_histograms(sample_Hin, sample_Hin_up, sample_Hin_down, cut, variable):
    """Routine to get the histogram to plot from the .root files"""
    try:
        Fin_Hin = ROOT.TFile.Open(file_Hin)
        Fin_Hin_up = ROOT.TFile.Open(file_Hin_up)
        Fin_Hin_down = ROOT.TFile.Open(file_Hin_down)
    except:
        print('Could not open file')
        raise
    try:
        print('Taking histogram from sample', sample_Hin)
        print('sample:', sample_Hin)
        print(cut+'/'+variable+'/histo_'+sample_Hin)
        Hin[sample_Hin] = Fin_Hin.Get(cut+'/'+variable+'/histo_'+sample_Hin).Clone()
        Hin[sample_Hin].SetBinErrorOption(ROOT.TH1.kPoisson)
        Hin_up[sample_Hin_up] = Fin_Hin_up.Get(cut+'/'+variable+'/histo_'+sample_Hin_up).Clone()
        Hin_up[sample_Hin_up].SetBinErrorOption(ROOT.TH1.kPoisson)
        Hin_down[sample_Hin_down] = Fin_Hin_down.Get(cut+'/'+variable+'/histo_'+sample_Hin_down).Clone()
        Hin_down[sample_Hin_down].SetBinErrorOption(ROOT.TH1.kPoisson)
        print('TRY 1:', Hin[sample_Hin])
    except:
        print('Could not get the histogram', sample_Hin)
        raise

    print('TRY 2:', Hin[sample_Hin])
    print('TRY 3:', Hin_up[sample_Hin_up])
    print('TRY 4:', Hin_down[sample_Hin_down])

    canvas = ROOT.TCanvas("plot_"+sample_Hin+"_"+variable, "Plot_"+sample_Hin+"_"+variable, 500, 600)
    canvas.Divide(1, 2)
    canvas.cd(1)
    canvas.cd(1).SetPad(0, 0.3, 1, 1)
    canvas.cd(1).SetBottomMargin(0.02)
    canvas.cd(1).SetTopMargin(0.1)
    canvas.cd(1).SetRightMargin(0.04)
    canvas.cd(1).SetLogy() 


    # Plot main histogram
    Hin[sample_Hin].SetLineColor(ROOT.kBlue+1)
    Hin_up[sample_Hin_up].SetLineColor(ROOT.kGreen+1)
    Hin_down[sample_Hin_down].SetLineColor(ROOT.kRed+1)
    Hin[sample_Hin].SetLineWidth(2)
    Hin_up[sample_Hin_up].SetLineWidth(2)
    Hin_down[sample_Hin_down].SetLineWidth(2)
    Hin[sample_Hin].Draw("Ehist")
    Hin_up[sample_Hin_up].Draw("Ehist sames")
#    Hin_down[sample_Hin_down].Draw("Ehist sames")

    # Create and draw legend
    legend = ROOT.TLegend(0.55, 0.7, 0.88, .9)
    legend.SetTextSize(0.039)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    # Calculate the integral of the histograms
    integral_Hin_up = Hin_up[sample_Hin_up].Integral()
    integral_Hin = Hin[sample_Hin].Integral()
    integral_Hin_down = Hin_down[sample_Hin_down].Integral()

    # Add the integral to the labels
    legend.AddEntry(Hin_up[sample_Hin_up], "File 1, Integral: {:.2f}".format(integral_Hin_up), "l")
    legend.AddEntry(Hin[sample_Hin], "File 2, Integral: {:.2f}".format(integral_Hin), "l")
#    legend.AddEntry(Hin_down[sample_Hin_down], "File 3, Integral: {:.2f}".format(integral_Hin_down), "l")

    legend.Draw("same")
    canvas.Update()

    canvas.cd(2)
    canvas.cd(2).SetPad(0, 0, 1, 0.3)
    canvas.cd(2).SetTopMargin(0.02)
    canvas.cd(2).SetBottomMargin(0.3)
    canvas.cd(2).SetRightMargin(0.04)

    # Calculate and plot relative percentage ratios
    Rat_up[sample_Hin] = Hin_up[sample_Hin_up].Clone()
    Rat_down[sample_Hin] = Hin_down[sample_Hin_down].Clone()
    Rat_up[sample_Hin].Add(Hin[sample_Hin], -1.0)
    Rat_up[sample_Hin].Divide(Hin[sample_Hin])
    Rat_up[sample_Hin].Scale(100.0)
    Rat_down[sample_Hin].Add(Hin[sample_Hin], -1.0)
    Rat_down[sample_Hin].Divide(Hin[sample_Hin])
    Rat_down[sample_Hin].Scale(100.0)
    Rat_up[sample_Hin].SetLineColor(ROOT.kGreen+1)
    Rat_down[sample_Hin].SetLineColor(ROOT.kRed+1)
    Rat_up[sample_Hin].SetLineWidth(2)
    Rat_down[sample_Hin].SetLineWidth(2)
    Rat_up[sample_Hin].GetYaxis().SetTitle("(Up - Nom)/Nom [%]")
    Rat_up[sample_Hin].GetYaxis().SetTitleOffset(0.5)
    Rat_up[sample_Hin].GetYaxis().SetRangeUser(-50, 50)
    Rat_up[sample_Hin].Draw("hist")
    Rat_down[sample_Hin].Draw("hist sames")

    # Calculate and print the integral ratios in the legend
    histoIntegral = Hin[sample_Hin].Integral()
    histoUpIntegral = Hin_up[sample_Hin_up].Integral()
    histoDownIntegral = Hin_down[sample_Hin_down].Integral()

    diffUp = 0.
    if histoIntegral > 0. and histoUpIntegral > 0.:
        diffUp = (histoUpIntegral - histoIntegral) / histoIntegral

    diffDo = 0.
    if histoIntegral > 0. and histoDownIntegral > 0.:
        diffDo = (histoDownIntegral - histoIntegral) / histoIntegral

    legend_ratio = ROOT.TLegend(0.55, 0.1, 0.88, 0.3)
    legend_ratio.SetTextSize(0.039)
    legend_ratio.SetFillStyle(0)
    legend_ratio.SetBorderSize(0)
    legend_ratio.AddEntry(Rat_up[sample_Hin], "Diff Up: {:.4f}".format(diffUp), "l")
    legend_ratio.AddEntry(Rat_down[sample_Hin], "Diff Down: {:.4f}".format(diffDo), "l")
    legend_ratio.Draw("same")

    canvas.Update()

    ROOT.objs.append([canvas, Hin_up[sample_Hin_up], Hin[sample_Hin], Hin_down[sample_Hin_down], Rat_up[sample_Hin], Rat_down[sample_Hin], legend, legend_ratio])
    canvas.SaveAs(outputPath+'_'+cut+'_'+sample_Hin+'_'+variable+'.pdf')
    canvas.SaveAs(outputPath+'_'+cut+'_'+sample_Hin+'_'+variable+'.png')

if __name__ == '__main__':
    import sys
    cuts = [ 'Boosted_SR_bVeto','Boosted_SR_bTag'] 

    for sample_Hin, sample_Hin_up, sample_Hin_down in zip(samples_Hin, samples_Hin_up, samples_Hin_down):
        for cut in cuts:
            for variable in variables:
                Getting_histograms(sample_Hin, sample_Hin_up, sample_Hin_down, cut, variable)

    print("Plots saved in batch mode.")


