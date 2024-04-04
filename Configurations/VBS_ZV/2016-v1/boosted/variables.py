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

#   DNN input variable in the resolved category:

#   - leading pt lepton
    #   - leading eta lepton
    #   - sub-leading eta lepton

#   - Zeppenfeld leading lep
#   - Zeppenfeld sub-leading lep

    #   - VBS jet eta leading
    #   - VBS jet eta sub-leading

#   - VBS jet pt sub-leading
#   - mjj
#   - Deta jj
#   - Dphi jj
#   - num AK4 jets

    #   - V-jet pt boosted
    #   - V-jet eta boostes
    #   - boosted jet Zeppenfeld
    #   - number of b-tagged jets

#   - DNN more bins b-veto
#   - DNN more bins b-req
#   - DNN 2016 bins b-veto
#   - DNN 2016 bins b-req
#   - DY binning variables
#   - events

variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (30,0.,400),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3,
                        
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

variables['VBS_jet_pt2']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_1],-9999.)',            #   variable name    
                        'range' : (40,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd VBS jet [GeV]',  #   x axis name
                        'fold' : 3,
                        }

variables['mjj']  = {   'name': 'mjj_max',            #   variable name    
                        'range' : (30,500,3500),    #   variable range
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

variables['nCleanJetNotFat']  = {
                        'name': 'nCleanJetNotFat',     
                        'range' : (10,0,10),   
                        'xaxis' : 'Number of jets (cleaned)',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }                           






variables['FatJet_pt']  = {
                        'name': 'Alt$(FatJet_pt_nom[0], -9999)',     
                        'range' : (30,150,800),   
                        'xaxis' : 'FatJet p_{T}',
                        'fold' : 3,
			               # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['FatJet_eta'] = {'name': 'Alt$(CleanFatJet_eta[0], -9999)',
                           'range' : (25,-2.7,2.7),
                           'xaxis' : '\eta FatJet',
                           'fold'  : 3,
                        
                           }

variables['Zlep_V_boosted'] = {   'name': '  ( CleanFatJet_eta[0] -0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) ) /detajj_mjjmax',      
                        'range' : (40,-1.5,1.5),  
                        'xaxis' : 'Z^{lep}_{V} (boosted)', 
                        'fold' : 3
                        }

variables['nbjets']  = {
                        'name': 'nbtag',     
                        'range' : (5,0,5),   
                        'xaxis' : 'Number of b-jets jets',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }   



    #**************** dy fitting variabl ***************#
variables['DYfit_Z_bin'] ={  'name' : 'fit_Z_bin',
                            'range' : (5,1,6), #(n.bins, 1, n.bins+1)
                            'xaxis' : 'fitting variable Z pt', 
                            'fold' : 3,
                            'divideByBinWidth': 1,

}

    #************* coarse binning (2016 only) ***************#
variables['DNNoutput_pruned_bVeto'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,                            
    'divideByBinWidth': 1,
}

variables['DNNoutput_pruned_bReq'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'divideByBinWidth': 1,
}

    #******************** DNN for 2017/2018

variables['DNNoutput_pruned_bVeto_morebins'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98,1.],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'divideByBinWidth': 1,
}

variables['DNNoutput_pruned_bReq_morebins'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98,1.],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'divideByBinWidth': 1,
}


    #************* extremly fine DNN for rebinning purposes ***************#
variables['DNNoutput_pruned_bReq_rebin'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range':  (1000,0,1),
    'xaxis': 'DNN output',
    'fold': 3 ,                            
    'divideByBinWidth': 1,
}

variables['DNNoutput_pruned_bVeto_rebin'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range':  (1000,0,1),
    'xaxis': 'DNN output',
    'fold': 3 ,                            
    'divideByBinWidth': 1,
}


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }


