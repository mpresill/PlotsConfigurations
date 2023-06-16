import ROOT
import math
ROOT.gROOT.SetBatch(True)  # Enable batch mode
ROOT.objs = []

Hin = dict()
Hin_up = dict()
Hin_down = dict()
Rat_up = dict()
Rat_down = dict()

directory = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_25May2023_2018/'
#directory = '/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2018_Dec22/resolved/'
#file = directory + 'plots_VBS_ZV_25May2023_2018_resolved.root'
file = '../../2018_may23/resolved/plots_VBS_ZV_25May2023_2018_resolved.root'
#file = directory + 'plots_VBS_ZV_25May2023_2018_resolved.root'

samples = ['DY_Resolved_2d_12', 'DY_Resolved_2d_11', 'DY_Resolved_2d_10', 'DY_Resolved_2d_09', 'DY_Resolved_2d_08', 'DY_Resolved_2d_07', 'DY_Resolved_2d_06', 'DY_Resolved_2d_05', 'DY_Resolved_2d_04', 'DY_Resolved_2d_03', 'DY_Resolved_2d_02', 'DY_Resolved_2d_01']
#samples = ['DY_Boosted_Z_1', 'DY_Boosted_Z_2', 'DY_Boosted_Z_3', 'DY_Boosted_Z_4', 'DY_Boosted_Z_5']
colors = ['kBlue+1', 'kGreen+1', 'kRed+1']

variations = ['Up', 'Down']

QCDscale_uncertainties = ['QCDscale_DY']#,'PS_FSR', 'PS_ISR']
#PS_uncertainties = ['PS_FSR', 'PS_ISR']

#variables = [ 'DYfit_Z_bin_Boosted','mjj','DNNoutput_pruned_bReq_morebins','DNNoutput_pruned_bVeto_morebins']#
variables = [ 'DYfit_2D_bin_Resolved','mjj','events','DNNoutput_pruned_bReq_morebins','DNNoutput_pruned_bVeto_morebins']#

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

    canvas = ROOT.TCanvas("plot_"+sample+"_"+variable, "Plot_"+sample+"_"+variable, 500, 600)
    canvas.Divide(1, 2)
    canvas.cd(1)
    canvas.cd(1).SetPad(0, 0.3, 1, 1)
    canvas.cd(1).SetBottomMargin(0.02)
    canvas.cd(1).SetTopMargin(0.1)
    canvas.cd(1).SetRightMargin(0.04)

    # Plot main histogram
    Hin[sample].SetLineColor(ROOT.kBlue+1)
    Hin_up[sample].SetLineColor(ROOT.kGreen+1)
    Hin_down[sample].SetLineColor(ROOT.kRed+1)
    Hin[sample].SetLineWidth(2)
    Hin_up[sample].SetLineWidth(2)
    Hin_down[sample].SetLineWidth(2)
    Hin[sample].Draw("hist")
    Hin_up[sample].Draw("hist sames")
    Hin_down[sample].Draw("hist sames")

    # Create and draw legend
    legend = ROOT.TLegend(0.55, 0.7, 0.88, .9)
    legend.SetTextSize(0.039)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.AddEntry(Hin_up[sample], "Up", "l")
    legend.AddEntry(Hin[sample], "Nominal", "l")
    legend.AddEntry(Hin_down[sample], "Down", "l")
    legend.Draw("same")
    canvas.Update()

    canvas.cd(2)
    canvas.cd(2).SetPad(0, 0, 1, 0.3)
    canvas.cd(2).SetTopMargin(0.02)
    canvas.cd(2).SetBottomMargin(0.3)
    canvas.cd(2).SetRightMargin(0.04)

    # Calculate and plot relative percentage ratios
    Rat_up[sample] = Hin_up[sample].Clone()
    Rat_down[sample] = Hin_down[sample].Clone()
    Rat_up[sample].Add(Hin[sample], -1.0)
    Rat_up[sample].Divide(Hin[sample])
    Rat_up[sample].Scale(100.0)
    Rat_down[sample].Add(Hin[sample], -1.0)
    Rat_down[sample].Divide(Hin[sample])
    Rat_down[sample].Scale(100.0)
    Rat_up[sample].SetLineColor(ROOT.kGreen+1)
    Rat_down[sample].SetLineColor(ROOT.kRed+1)
    Rat_up[sample].SetLineWidth(2)
    Rat_down[sample].SetLineWidth(2)
    Rat_up[sample].GetYaxis().SetTitle("(Up - Nom)/Nom [%]")
    Rat_up[sample].GetYaxis().SetTitleOffset(0.5)
    Rat_up[sample].GetYaxis().SetRangeUser(-50, 50)
    Rat_up[sample].Draw("hist")
    Rat_down[sample].Draw("hist sames")

    # Calculate and print the integral ratios in the legend
    histoIntegral = Hin[sample].Integral()
    histoUpIntegral = Hin_up[sample].Integral()
    histoDownIntegral = Hin_down[sample].Integral()

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
    legend_ratio.AddEntry(Rat_up[sample], "Diff Up: {:.4f}".format(diffUp), "l")
    legend_ratio.AddEntry(Rat_down[sample], "Diff Down: {:.4f}".format(diffDo), "l")
    legend_ratio.Draw("same")

    canvas.Update()

    ROOT.objs.append([canvas, Hin_up[sample], Hin[sample], Hin_down[sample], Rat_up[sample], Rat_down[sample], legend, legend_ratio])
    canvas.SaveAs('/eos/user/m/mpresill/www/VBS/nuisances/QCDscaleDY/25May2023_2018/'+uncertainty+'_'+cut+'_'+sample+'_'+variable+'-PATCHED.pdf')
    canvas.SaveAs('/eos/user/m/mpresill/www/VBS/nuisances/QCDscaleDY/25May2023_2018/'+uncertainty+'_'+cut+'_'+sample+'_'+variable+'-PATCHED.png')

if __name__ == '__main__':
    import sys
    cuts = [ 'Resolved_SR_bVeto', 'Resolved_DYcr_bVeto','Resolved_SR_bTag', 'Resolved_DYcr_bTag']
    for sample in samples:
        for cut in cuts:
            for variable in variables:
                Getting_histograms(sample, cut, variable)

#    input("Press ENTER to exit... ")    
    print("Plots saved in batch mode.")
