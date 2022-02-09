# variables

#variables = {}
'''
variables['VARIABLE']  = {  
          'name': 'expression',        # variable expression as one would use in TTree::Draw. Also 2D expression works e.g. var1:var2    
          'range' : range:             # anything that a TH1 can digest van be put here: 
                                       # a 3-valued tuple is interpreted as (nbins, xmin, xmax).
                                       # a 6-valued tuple is interpreted as (nbinsx, xmin, xmax, nbinsy, ymin, ymax)
                                       # a ([list]) is interpreted as a vector of bin edges
                                       # a ([list],[list],) is interpreted as a 2D vector of bin edges (mind the comma before the closing ")")
          'xaxis' : 'DR_{ll}',         # x axis name, human readable name, what goes into h->GetXaxis()->SetTitle()
          'fold' : NUMBER,             # 0 -> no underflow/overflow folding. 1 -> fold underflow in the first bin. 2-> fold overflow in the last bin. 3 -> fold both underflow and overflow.
          'divideByBinWidth': VALUE,   #OPTIONAL, whether to divide (1) or not (0) the bin content by the bin width (for variable bin size histograms). Default is 0
} 
'''
"""
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }
"""

resolved_cuts = [ c for c in cuts if 'Resolved' in c]
boosted_cuts = [ c for c in cuts if 'Boosted' in c]
#
# leptons
#

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,400),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3,
                        
                        }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,0.,400),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3,
                        
                        }

variables['Zleppt'] = { 'name' : 'Alt$(Zleppt, -999)',
			'range' : (20,0.,800),
			'xaxis' : 'p_{T} leptonic Z [GeV]',
			'fold' : 3,

}

variables['Vpt'] = { 'name' : 'Alt$(Vpt, -999)',
                        'range' : (20,0.,800),
                        'xaxis' : 'p_{T} hadronic V [GeV]',
                        'fold' : 3,

}


#fitting with Z+vbs jet2 pt binning
#variables['fit_Z_vbs1_bin_Resolved'] ={  'name' : 'fit_Z_vbs1_bin_Resolved',
#                            'range' : (6,1,7), #(n.bins, 1, n.bins+1)
#                            'xaxis' : 'fitting variable Resolved Z pt, VBS jet pt2', 
#                            'fold' : 3,
#}  


#fitting with Z pt binning
"""
variables['DYfit_Z_bin_Resolved'] ={  'name' : 'fit_Z_bin_Resolved',
                            'range' : (6,1,7), #(n.bins, 1, n.bins+1)
                            'xaxis' : 'fitting variable Resolved Z pt', 
                            'fold' : 3,
}
"""  
variables['DYfit_Z_bin_Boosted'] ={  'name' : 'fit_Z_bin_Boosted',
                            'range' : (5,1,6), #(n.bins, 1, n.bins+1)
                            'xaxis' : 'fitting variable Boosted Z pt', 
                            'fold' : 3,

}


variables['DYfit_2D_bin_Resolved'] = { 'name' : 'fit_2D_bin_Resolved',
                                        'range' : (12,1,13),
                                        'xaxis' : 'fitting variable Resolved Z + vbs2 pt',
                                        'fold' : 3,


}

variables['eta1']  = {   'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold' :3,
                        
                        }

variables['eta2']  = {   'name': 'Alt$(Lepton_eta[1],-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold' : 3,
                        
                        }

variables['mll-peak']  = {   'name': 'mll',            #   variable name    
                        'range' : (30,60,120),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3,
                        
                        }

"""
#
# VBS jet AK4
#

"""
variables['nCleanJetNotFat']  = {
                        'name': 'nCleanJetNotFat',     
                        'range' : (15,0,15),   
                        'xaxis' : 'Number of jets (cleaned)',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
"""
"""
variables['VBS_jet_eta1'] = {  'name': 'Alt$(CleanJet_eta[vbs_jet_0],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 1st VBS jet',
                        'fold' : 3,
                        
                        }
variables['VBS_jet_eta2'] = {  'name': 'Alt$(CleanJet_eta[vbs_jet_1],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 2nd VBS jet',
                        'fold' : 3,
                        
                        }

variables['VBS_jet_pt1']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_0],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 1st VBS jet [GeV]',  #   x axis name
                        'fold' : 3,
                        
                        }
variables['VBS_jet_pt2']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_1],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd VBS jet [GeV]',  #   x axis name
                        'fold' : 3,
                        
                        }
"""
variables['VBS_jet_qgl1'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetId[vbs_jet_0]), -9999)',
			'range' : (20,0,1),
			'xaxis' : 'QGL 1st VBS jet',
			'fold' : 3,
                        }
variables['VBS_jet_qgl2'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetId[vbs_jet_1]), -9999)',
                        'range' : (20,0,1),
                        'xaxis' : 'QGL 2nd VBS jet',
                        'fold' : 3,
                   
}
"""

#
# V- jet(s) #

variables['V_jet_eta1'] = {  'name': 'Alt$(CleanJet_eta[v_jet_0],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 1st V jet',
                        'fold' : 3,
                        
                        }
variables['V_jet_eta2'] = {  'name': 'Alt$(CleanJet_eta[v_jet_1],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 2nd V jet',
                        'fold' : 3,
                        
                        }

variables['V_jet_pt1']  = {   'name': 'Alt$(CleanJet_pt[v_jet_0],-9999.)',            #   variable name    
                        'range' : (60,0,800),    #   variable range
                        'xaxis' : 'p_{T} 1st V jet [GeV]',  #   x axis name
                        'fold' : 3,
                        'cuts' : resolved_cuts
                        }
variables['V_jet_pt2']  = {   'name': 'Alt$(CleanJet_pt[v_jet_1],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd V jet [GeV]',  #   x axis name
                        'fold' : 3,
                        'cuts' : resolved_cuts
                        }
"""
variables['V_jet_qgl1'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetId[v_jet_0]), -9999)',
                        'range' : (20,0,1),
                        'xaxis' : 'QGL 1st V jet',
                        'fold' : 3,
                        
}
variables['V_jet_qgl2'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetId[v_jet_1]), -9999)',
                        'range' : (20,0,1),
                        'xaxis' : 'QGL 2nd V jet',
                        'fold' : 3,
                        

}
"""
#qgl
variables['VBS_jet_qgl1_morphed'] = {  'name': 'vbs_0_qglmorphed_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl VBS 1st jet morphed',
                        'fold': 3,

                }

variables['VBS_jet_qgl2_morphed'] = {  'name': 'vbs_1_qglmorphed_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl VBS 2nd jet morphed',
                        'fold': 3,
                              }

variables['V_jet_qgl1_morphed'] = {  'name': 'vjet_0_qglmorphed_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl Vjet 1st jet morphed',
                        'fold': 3,
                                 }

variables['V_jet_qgl2_morphed'] = {  'name': 'vjet_1_qglmorphed_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl Vjet 2nd jet morphed',
                        'fold': 3,
                                 }
variables['VBS_jet_qgl1_unmorphed'] = {  'name': 'vbs_0_qgl_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl VBS 1st jet unmorphed',
                        'fold': 3,

                }

variables['VBS_jet_qgl2_unmorphed'] = {  'name': 'vbs_1_qgl_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl VBS 2nd jet unmorphed',
                        'fold': 3,
                              }

variables['V_jet_qgl1_unmorphed'] = {  'name': 'vjet_0_qgl_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl VBS 1st jet unmorphed',
                        'fold': 3,

                }

variables['V_jet_qgl2_unmorphed'] = {  'name': 'vjet_1_qgl_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl VBS 2nd jet unmorphed',
                        'fold': 3,
                              }

variables['Vjet_mass'] = { 'name': 'Alt$(Vjet_mass,-9999.)',            #   variable name    
                        'range' : (50,40,160),    #   variable range
                        'xaxis' : 'V-jet mass [GeV]',  #   x axis name
                        'fold' : 3,
                        
                        }
# Fat Jet
variables['nFatJet']  = {
                        'name': 'nCleanFatJet',     
                        'range' : (6,0,6),   
                        'xaxis' : 'Number of FatJets w/ p_{T}>200 GeV',
                        'fold' : 2,
                           # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

"""
"""
variables['FatJet_pt']  = {
                        'name': 'Alt$(CleanFatJet_pt, -9999)',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 0,
			'cuts' : boosted_cuts
                          # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJet_eta'] = {'name': 'Alt$(CleanFatJet_eta, -9999)',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 0,
                        
                           }


variables['FatJet_tau21'] = {   'name': 'CleanFatJet_tau21',
                        'range' : (50,0,1),
                        'xaxis' : '#tau_{21}',
                        'fold' : 0,
                       }

# new variables

variables['mjj_max']  = {   'name': 'mjj_max',            #   variable name    
                        'range' : (20,200,4000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3,
                        
                        }

variables['detajj_mjjmax']  = {   'name': 'detajj_mjjmax',            #   variable name    
                           'range' : (12,2.0,8.0),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :3,
                        
                           }

variables['dphijj_mjjmax']  = {   'name': 'dphijj_mjjmax',            #   variable name    
                           'range' : (8,0,3.14),    #   variable range
                           'xaxis' : '#Delta #phi jj',  #   x axis name
                           'fold' :3,
                        
                           }


#Zeppenfeld variables
variables['Zlep_1'] = {   'name': '( Lepton_eta[0]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{l1}', 
                        'fold' : 3,
			       }

variables['Zlep_2'] = {   'name': '( Lepton_eta[1]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{l2}', 
                        'fold' : 3,
   			
                 }


"""

variables['Zlep_ll'] = {   'name': '  ( Lepton_eta[0]+Lepton_eta[1]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) ) /detajj_mjjmax',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{ll}', 
                        'fold' : 3
                        }


variables['Zlep_V_res'] = {   'name': '  ( CleanJet_eta[v_jet_0]+CleanJet_eta[v_jet_1]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) ) /detajj_mjjmax',      
                        'range' : (40,-1.5,-1.5),  
                        'xaxis' : 'Z^{lep}_{V} (resolved)', 
                        'fold' : 3
                        }

variables['Zlep_V_boosted'] = {   'name': '  ( CleanFatJet_eta[0] -0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) ) /detajj_mjjmax',      
                        'range' : (40,-1.5,-1.5),  
                        'xaxis' : 'Z^{lep}_{V} (boosted)', 
                        'fold' : 3
                        }

"""


### DNN variables

variables['DNNoutput_full_bVeto'] = {
    'name': 'DNNoutput_full_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bTag": [0.8,1],
        "Boosted_SR_bTag": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}
variables['DNNoutput_pruned_bVeto'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bTag": [0.8,1],
        "Boosted_SR_bTag": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}

variables['DNNoutput_full_bReq'] = {
    'name': 'DNNoutput_full_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bTag": [0.8,1],
        "Boosted_SR_bTag": [0.8,1],
	"Boosted_SR": [0.8,1],
	"Resolved_SR": [0.8,1],

    }
}
variables['DNNoutput_pruned_bReq'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bTag": [0.8,1],
        "Boosted_SR_bTag": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}
"""
variables['DNNoutput_full_bVeto_morphed'] = {
    'name': 'DNNoutput_full_bVeto_morphed',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bReq": [0.8,1],
        "Boosted_SR_bReq": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}
variables['DNNoutput_pruned_bVeto_morphed'] = {
    'name': 'DNNoutput_pruned_bVeto_morphed',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_nobVeto": [0.8,1],
        "Boosted_SR_nobVeto": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}

variables['DNNoutput_full_bReq_morphed'] = {
    'name': 'DNNoutput_full_bReq_morphed',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bReq": [0.8,1],
        "Boosted_SR_bReq": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}
variables['DNNoutput_pruned_bReq_morphed'] = {
    'name': 'DNNoutput_pruned_bReq_morphed',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_nobVeto": [0.8,1],
        "Boosted_SR_nobVeto": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}
"""
