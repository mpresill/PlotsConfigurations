#
#       Fast plots macro for nuisances debugging
#

import ROOT
import math
from ROOT import TFile, TTree, TLegend
ROOT.objs = []

Hin = dict()
Hin_up = dict()
Hin_down = dict()

directory = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_13Dec2022_2018/'

file = directory+'plots_VBS_ZV_13Dec2022_2018.root' 

samples = ['VBS_VV_QCD','sm_dipole','DY','top'] #CMS_scale_mVjmr_2016
colors = ['kBlue+1', 'kGreen+1', 'kRed+1']

variations = ['Up', 'Down']

#CleanFatJet_uncertainties = ['CMS_scale_cleanfatJER_2016', 'CMS_scale_cleanfatJES_2016']
#Prefiring_uncertainties = ['CMS_eff_prefiring_2016']
#
#subjets_uncertainties = ['CMS_scale_subjetjer_2016','CMS_scale_subjetjes_2016']
#
#mV_uncertainties = ['CMS_scale_mVjmr_2016', 'CMS_scale_mVjms_2016', 'CMS_scale_mVjesTotal_2016', 'CMS_scale_mVjer_2016']

QCDscale_uncertainties = ['QCDscale_v1_VBS_VV_QCD','QCDscale_v2_VBS_VV_QCD']

PS_uncertainties = ['PS_FSR_latinos','PS_ISR_latinos','PS_FSR','PS_ISR']

variables = [ 'DNNoutput_pruned_bReq_morebins', 'DNNoutput_pruned_bVeto_morebins', 'events','ZV_mass'] #

###
def Getting_histograms(sample, cut, variable):
        """Routine to get the histogram to plot from the .root files"""
	
#        for sample in samples:
        try:
		Fin = ROOT.TFile.Open(file)
        except:
                print('Could not open file')
                raise
        try:
                print('Taking histogram from sample ',sample)
			
		print('sample', sample)
		print(cut+'/'+variable+'/histo_'+sample)
                Hin[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample).Clone()
		print('TRY 1', Hin[sample])

        except:
                print('Could not get the histogram '+sample)
                raise

	#for uncertainty in mV_uncertainties+subjets_uncertainties+CleanFatJet_uncertainties:
	#for uncertainty in Prefiring_uncertainties:
	for uncertainty in PS_uncertainties:
		if Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Up'):
			Hin_up[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Up').Clone()
		if Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Down'):
			Hin_down[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Down').Clone()

        	#Fin.Close()

		print('TRY 2', Hin[sample])
		print('TRY 3', Hin_up[sample])
		print('TRY 4', Hin_down[sample])

		canvas = ROOT.TCanvas("plot_"+sample+"_"+variable, "Plot_"+sample+"_"+variable, 500, 500)
		#canvas.SetLogy()
	        canvas.Draw()
		canvas.cd()
       		print('plotting ', sample)
                Hin[sample].SetLineColor(ROOT.kBlue+1)
		Hin_up[sample].SetLineColor(ROOT.kGreen+1)
		Hin_down[sample].SetLineColor(ROOT.kRed+1)
		Hin[sample].SetLineWidth(2)
		Hin_up[sample].SetLineWidth(2)
		Hin_down[sample].SetLineWidth(2)
		Hin[sample].Draw("hist")
		Hin_up[sample].Draw("hist sames")
		Hin_down[sample].Draw("hist sames")
		legend = TLegend(0.55, 0.7, 0.88, .9)
		legend.SetTextSize(0.039)
		legend.SetFillStyle(0)
		legend.SetBorderSize(0)
		legend.AddEntry(Hin_up[sample], "Up", "l")
		legend.AddEntry(Hin[sample], "Nominal", "l")
		legend.AddEntry(Hin_down[sample], "Down", "l")
		legend.Draw("same")
     		canvas.Update()
		ROOT.objs.append([canvas,Hin_up[sample],Hin[sample], Hin_down[sample],legend])
		canvas.SaveAs('/eos/user/m/mpresill/www/VBS/nuisances/PSweights/'+uncertainty+'_'+cut+'_'+sample+'_'+variable+'.png')

###
if __name__ == '__main__':

        import sys

	cuts = ['Resolved_SR_bTag', 'Resolved_SR_bVeto','Boosted_SR_bVeto','Boosted_SR_bTag'] #, 'Resolved_DYcr_bVeto', 'Resolved_DYcr_bTag'
#	cut = 'Resolved_SR_bVeto'
	
	for sample in samples:
		for cut in cuts:
			for variable in variables:
				Getting_histograms(sample, cut, variable)
	
	raw_input("Press ENTER... ")
	#raw_input("prompt_ ")