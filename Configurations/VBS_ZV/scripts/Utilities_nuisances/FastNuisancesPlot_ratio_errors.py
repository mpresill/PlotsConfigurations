import ROOT
import math
ROOT.gROOT.SetBatch(True)  # Enable batch mode
ROOT.objs = []

Hin = dict()
Hin_up = dict()
Hin_down = dict()
Rat_up = dict()
Rat_down = dict()
Rat_up_2 = dict()
Rat_down_2 = dict()

directory = '../../2016-v1/resolved/'
file = directory + 'plots_VBS_ZV_6Dec2023_2016_resolved_wPS_wQCD.root'

#file = '../../2017_may23/resolved/plots_VBS_ZV_6Dec2023_2017_resolved.root'

samples = ['Vg','VgS','tZq','sm_dipole','VBS_VV_QCD']
#samples = ['DY_bin1', 'DY_bin2', 'DY_bin3', 'DY_bin4', 'DY_bin5','top','tZq','VBS_VV_QCD','sm_dipole','VBS_VV_QCD','Vg','VgS']
##samples = ['DY_Boosted_Z_1', 'DY_Boosted_Z_2', 'DY_Boosted_Z_3', 'DY_Boosted_Z_4', 'DY_Boosted_Z_5']
#samples = ['DY_Resolved_2d_12', 'DY_Resolved_2d_11', 'DY_Resolved_2d_10', 'DY_Resolved_2d_09', 'DY_Resolved_2d_08', 'DY_Resolved_2d_07', 'DY_Resolved_2d_06', 'DY_Resolved_2d_05', 'DY_Resolved_2d_04', 'DY_Resolved_2d_03', 'DY_Resolved_2d_02', 'DY_Resolved_2d_01']
cuts = ['Resolved_SR_bVeto', 'Resolved_DYcr_bVeto', 'Resolved_SR_bTag', 'Resolved_DYcr_bTag']#,'Resolved_topcr']
variables = ['DNNoutput_pruned_bReq', 'DNNoutput_pruned_bVeto']
#variables = ['DYfit_2D_bin_Resolved', 'DNNoutput_pruned_bReq_morebins', 'DNNoutput_pruned_bVeto_morebins']
#variables = [ 'DYfit_Z_bin_Boosted','DNNoutput_pruned_bReq_morebins','DNNoutput_pruned_bVeto_morebins']#

QCDscale_uncertainties = ['PS_FSR']

def Getting_histograms(sample, cut, variable):
    """Routine to get the histogram to plot from the .root files"""
    try:
        Fin = ROOT.TFile.Open(file)
    except:
        print('Could not open file')
        raise
    try:
        print('Taking histogram from sample', sample)
        print('sample:', sample)
        print(cut+'/'+variable+'/histo_'+sample)
        Hin[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample).Clone()
        print('TRY 1:', Hin[sample])
    except:
        print('Could not get the histogram', sample)
        raise

    for uncertainty in QCDscale_uncertainties:
        if Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Up'):
            Hin_up[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Up').Clone()
        if Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Down'):
            Hin_down[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Down').Clone()

    print('TRY 2:', Hin[sample])
    print('TRY 3:', Hin_up[sample])
    print('TRY 4:', Hin_down[sample])

    canvas = ROOT.TCanvas("plot_"+sample+"_"+variable, "Plot_"+sample+"_"+variable, 500, 800)  # Updated canvas size
    canvas.Divide(1, 3)  # Divide canvas into 3 rows

    canvas.cd(1)
    canvas.cd(1).SetPad(0, 0.4, 1, 1)  # Updated top panel coordinates
    canvas.cd(1).SetBottomMargin(0.0)
    canvas.cd(1).SetTopMargin(0.1)
    canvas.cd(1).SetRightMargin(0.04)

    # Plot main histogram
    Hin[sample].SetLineColor(ROOT.kBlue+1)
    Hin_up[sample].SetLineColor(ROOT.kGreen+1)
    Hin_down[sample].SetLineColor(ROOT.kRed+1)
    Hin[sample].SetLineWidth(2)
    Hin_up[sample].SetLineWidth(2)
    Hin_down[sample].SetLineWidth(2)
    Hin[sample].Sumw2()
    Hin_up[sample].Sumw2()
    Hin_down[sample].Sumw2()
    Hin[sample].Draw("Ehist")
    Hin_up[sample].Draw("Ehist sames")
    Hin_down[sample].Draw("Ehist sames")

    legend = ROOT.TLegend(0.55, 0.75, 0.88, 0.9)  # Updated legend position
    legend.SetTextSize(0.039)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.AddEntry(Hin_up[sample], "Up", "l")
    legend.AddEntry(Hin[sample], "Nominal", "l")
    legend.AddEntry(Hin_down[sample], "Down", "l")
    legend.Draw("same")
    canvas.Update()

    canvas.cd(2)
    canvas.cd(2).SetPad(0, 0.2, 1, 0.4)  # Updated middle panel coordinates
    canvas.cd(2).SetBottomMargin(0.0)
    canvas.cd(2).SetTopMargin(0.0)
    canvas.cd(2).SetRightMargin(0.04)

    # Calculate and plot relative differences btw up-nominal and down-nominal
    Rat_up[sample] = Hin_up[sample].Clone()
    Rat_down[sample] = Hin_down[sample].Clone()
    Rat_up[sample].Add(Hin[sample], -1.0)
#    Rat_up[sample].Divide(Hin[sample])
#    Rat_up[sample].Scale(100.0)
    Rat_down[sample].Add(Hin[sample], -1.0)
#    Rat_down[sample].Divide(Hin[sample])
#    Rat_down[sample].Scale(100.0)
    Rat_up[sample].SetLineColor(ROOT.kGreen+1)
    Rat_down[sample].SetLineColor(ROOT.kRed+1)
    Rat_up[sample].SetLineWidth(2)
    Rat_down[sample].SetLineWidth(2)
    Rat_up[sample].GetYaxis().SetTitle("(Variation - Nom)")
    Rat_up[sample].GetYaxis().SetTitleOffset(0.5)
    Rat_up[sample].SetTitle("Variation - Nom")
    #Rat_up[sample].GetYaxis().SetRangeUser(-30, 30)
    Rat_up[sample].Draw("Ehist")
    Rat_down[sample].Draw("Ehist sames")

############################################################################################################################################
    canvas.cd(3)
    canvas.cd(3).SetPad(0, 0, 1, 0.2)
    canvas.cd(3).SetTopMargin(0.0)
    canvas.cd(3).SetBottomMargin(0.3)
    canvas.cd(3).SetRightMargin(0.04)

    # Calculate and plot relative percentage ratios
    Rat_up_2[sample] = Hin_up[sample].Clone()
    Rat_down_2[sample] = Hin_down[sample].Clone()
    Rat_up_2[sample].Add(Hin[sample], -1.0)
    Rat_up_2[sample].Divide(Hin[sample])
    Rat_up_2[sample].Scale(100.0)
    Rat_down_2[sample].Add(Hin[sample], -1.0)
    Rat_down_2[sample].Divide(Hin[sample])
    Rat_down_2[sample].Scale(100.0)
    Rat_up_2[sample].SetLineColor(ROOT.kGreen+1)
    Rat_down_2[sample].SetLineColor(ROOT.kRed+1)
    Rat_up_2[sample].SetLineWidth(2)
    Rat_down_2[sample].SetLineWidth(2)
    Rat_up_2[sample].GetYaxis().SetTitle("(Variation - Nom)/Nom [%]")
    Rat_up_2[sample].GetYaxis().SetTitleOffset(0.5)
    Rat_up_2[sample].SetTitle("(Variation - Nom)/Nom [%]")
#    Rat_up_2[sample].GetYaxis().SetRangeUser(-30, 30)
    Rat_up_2[sample].Draw("Ehist")
    Rat_down_2[sample].Draw("Ehist sames")

    legend_ratio = ROOT.TLegend(0.55, 0.75, 0.88, 0.9)  # Updated legend position
    legend_ratio.SetTextSize(0.039)
    legend_ratio.SetFillStyle(0)
    legend_ratio.SetBorderSize(0)

    # Calculate and print the integral ratios in the legend
    histoIntegral = Hin[sample].Integral()
    histoUpIntegral = Hin_up[sample].Integral()
    histoDownIntegral = Hin_down[sample].Integral()

    diffUp = 0.
    if histoIntegral > 0. and histoUpIntegral > 0.:
        diffUp = (histoUpIntegral - histoIntegral) / histoIntegral * 100

    diffDo = 0.
    if histoIntegral > 0. and histoDownIntegral > 0.:
        diffDo = (histoDownIntegral - histoIntegral) / histoIntegral * 100

    legend_ratio.AddEntry(Rat_up_2[sample], "Averga Diff Up: {:.2f}%".format(diffUp), "l")
    legend_ratio.AddEntry(Rat_down_2[sample], "Averga Diff Down: {:.2f}%".format(diffDo), "l")
############################
    Rat_up_2[sample].Draw("Ehist")
    Rat_down_2[sample].Draw("Ehist sames")
    legend_ratio.Draw("same")

    canvas.Update()

    ROOT.objs.append([canvas, Hin_up[sample], Hin[sample], Hin_down[sample], Rat_up[sample], Rat_up_2[sample], Rat_down[sample], Rat_down_2[sample],legend, legend_ratio])
    canvas.SaveAs('/eos/user/m/mpresill/www/VBS/nuisances/PS_FSR/6Dec2023_2016/'+uncertainty+'_'+cut+'_'+sample+'_'+variable+'.pdf')
    canvas.SaveAs('/eos/user/m/mpresill/www/VBS/nuisances/PS_FSR/6Dec2023_2016/'+uncertainty+'_'+cut+'_'+sample+'_'+variable+'.png')

if __name__ == '__main__':
    for sample in samples:
        for cut in cuts:
            for variable in variables:
                Getting_histograms(sample, cut, variable)

    print("Plots saved in batch mode.")
