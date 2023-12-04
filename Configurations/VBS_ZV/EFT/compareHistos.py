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

directory_nominal = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_21Aug2023_2018/'
directory_up = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_1Dec2023_2018-dim8/'
directory_down = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_1Dec2023_2018-dim6/'

samples = ['sm']
cuts = ['Boosted_SR_bVeto', 'Boosted_DYcr_bVeto', 'Boosted_SR_bTag', 'Boosted_DYcr_bTag', 'Boosted_topcr']
variables = ['events', 'DNNoutput_pruned_bReq_morebins', 'DNNoutput_pruned_bVeto_morebins']
QCDscale_uncertainties = ['']

def Getting_histograms(sample, cut, variable):
    """Routine to get the histogram to plot from the .root files"""
    try:
        Fin_nominal = ROOT.TFile.Open(directory_nominal + 'plots_VBS_ZV_21Aug2023_2018_boosted.root')
        Fin_up = ROOT.TFile.Open(directory_up + 'plots_VBS_ZV_1Dec2023_2018-dim8_boosted.root')
        Fin_down = ROOT.TFile.Open(directory_down + 'plots_VBS_ZV_1Dec2023_2018-dim6_boosted.root')
    except:
        print('Could not open file')
        raise
    try:
        print('Taking histogram from sample', sample)
        print('sample:', sample)
        print(cut+'/'+variable+'/histo_'+sample)
        if sample in ['sm']:
            Hin[sample] = Fin_nominal.Get(cut+'/'+variable+'/histo_'+sample+'_dipole').Clone()
        else:
            Hin[sample] = Fin_nominal.Get(cut+'/'+variable+'/histo_'+sample).Clone()
        Hin_up[sample] = Fin_up.Get(cut+'/'+variable+'/histo_'+sample).Clone()
        Hin_down[sample] = Fin_down.Get(cut+'/'+variable+'/histo_'+sample).Clone()
        print('TRY 1:', Hin[sample])
    except:
        print('Could not get the histogram', sample)
        raise

#    for uncertainty in QCDscale_uncertainties:
#        if Fin.Get(cut+'/'+variable+'/histo_'+sample):
#            Hin_up[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample).Clone()
#        if Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Down'):
#            Hin_down[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample).Clone()

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

    # Calcola l'integrale
    integral_nominal = Hin[sample].Integral()
    integral_up = Hin_up[sample].Integral()
    integral_down = Hin_down[sample].Integral()

    # Trova il massimo tra i massimi degli istogrammi Up, Down e Nominal
    max_value = max(Hin[sample].GetMaximum(), Hin_up[sample].GetMaximum(), Hin_down[sample].GetMaximum())

    # Imposta il range dell'asse y in modo che nessun istogramma venga tagliato fuori
    canvas.cd(1)
    canvas.cd(1).SetPad(0, 0.4, 1, 1)
    canvas.cd(1).SetBottomMargin(0.0)
    canvas.cd(1).SetTopMargin(0.1)
    canvas.cd(1).SetRightMargin(0.04)
    Hin[sample].Draw("Ehist")
    Hin[sample].GetYaxis().SetRangeUser(0, 1.2 * max_value)  # Imposta il range dell'asse y

    Hin_up[sample].Draw("Ehist sames")
    Hin_down[sample].Draw("Ehist sames")

    # Aggiungi l'integrale e l'errore statistico totale alla legenda
    legend = ROOT.TLegend(0.15, 0.75, 0.88, 0.9)
    legend.SetTextSize(0.039)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)

    integral_up = Hin_up[sample].Integral()
    error_up = math.sqrt(sum([Hin_up[sample].GetBinError(bin)**2 for bin in range(1, Hin_up[sample].GetNbinsX() + 1)]))

    integral_nominal = Hin[sample].Integral()
    error_nominal = math.sqrt(sum([Hin[sample].GetBinError(bin)**2 for bin in range(1, Hin[sample].GetNbinsX() + 1)]))

    integral_down = Hin_down[sample].Integral()
    error_down = math.sqrt(sum([Hin_down[sample].GetBinError(bin)**2 for bin in range(1, Hin_down[sample].GetNbinsX() + 1)]))

    legend.AddEntry(Hin_up[sample], "Dim-8 (Integral: {:.2f} +/- {:.2f})".format(integral_up, error_up), "l")
    legend.AddEntry(Hin[sample], "SM (Integral: {:.2f} +/- {:.2f})".format(integral_nominal, error_nominal), "l")
    legend.AddEntry(Hin_down[sample], "Dim-6 (Integral: {:.2f} +/- {:.2f})".format(integral_down, error_down), "l")
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
    canvas.SaveAs('/eos/user/m/mpresill/www/VBS/nuisances/test/'+cut+'_'+sample+'_'+variable+'.pdf')
    canvas.SaveAs('/eos/user/m/mpresill/www/VBS/nuisances/test/'+cut+'_'+sample+'_'+variable+'.png')

if __name__ == '__main__':
    for sample in samples:
        for cut in cuts:
            for variable in variables:
                Getting_histograms(sample, cut, variable)

    print("Plots saved in batch mode.")
