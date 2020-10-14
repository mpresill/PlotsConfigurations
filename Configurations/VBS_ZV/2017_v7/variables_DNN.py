##leptons
"""
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep [GeV]',
                        'fold' :3
                        }
variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 2nd lep [GeV]',
                        'fold' :3
                        }


variables['eta1']  = {   'name': 'Alt$(Lepton_eta[0],-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold' :3
                        }

variables['eta2']  = {   'name': 'Alt$(Lepton_eta[1],-9999.)',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold' : 3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (30,60,120),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        'fold' :3
                        }


#
# jets AK8
#

#variables['nFatJet']  = {
#                        'name': 'Sum(FatJet_pt>200.)',     
#                        'range' : (6,0,6),   
#                        'xaxis' : 'Number of FatJets w/ p_{T}>200 GeV',
#                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                        }
#variables['FatJet_pt']  = {
#                        'name': 'Alt$(FatJet_pt,0,-999)',     
#                        'range' : (30,150,800),   
#                        'xaxis' : 'FatJet p_{T}',
#                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                        }
#variables['FatJeteta'] = {'name': 'Alt$(FatJet_eta,0,-999)',
#                           'range' : (25,-2.7,2.7),
#                           'xaxis' : '\eta FatJet',
#                           'fold'  : 3
#                           }
#variables['FatJet_softdropmass'] = {   'name': 'Alt$(FatJet_mass,0,0.)',
#                               'range': (50,0.,200),
#                               'xaxis': 'AK8 jet softdrop mass',
#                               'fold': 3
#                               }
##this is the softdrop mass
                                                                                                                     
#variables['FatJet_tau21'] = {   'name': 'Alt$(CleanFatJet_tau21,0,-999)',
#                        'range' : (50,0,1),
#                        'xaxis' : '#tau_{21}',
#                        'fold' : 3
#                        }



#Zeppenfeld variables

variables['Zlep_1'] = {   'name': '( Lepton_eta[0]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax',      
                        'range' : (40,-2.5,2.5),  
                        'xaxis' : 'Z^{lep}_{l1}', 
                        'fold' : 3
                        }

variables['Zlep_2'] = {   'name': '( Lepton_eta[1]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax',      
                        'range' : (40,-2.5,2.5),  
                        'xaxis' : 'Z^{lep}_{l2}', 
                        'fold' : 3
                        }



#jet cat
#variables['category'] = {'name' : 'category',
#                         'range' : (3,-1,1),
#                         'xaxis' : 'category',
#                         'fold' : 3
#                        }

variables['vbs_jet_eta1'] = {  'name': 'Alt$(CleanJet_eta[vbs_jet_0],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 1st vbs jet',
                        'fold' : 3
                        }
variables['vbs_jet_eta2'] = {  'name': 'Alt$(CleanJet_eta[vbs_jet_1],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 2nd vbs jet',
                        'fold' : 3
                        }

variables['vbs_jet_pt1']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_0],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 1st vbs jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['vbs_jet_pt2']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_1],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd vbs jet [GeV]',  #   x axis name
                        'fold' : 3
                        }

#
# V- jet(s) #

variables['V_jet_eta1'] = {  'name': 'Alt$(CleanJet_eta[v_jet_0],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 1st vbs jet',
                        'fold' : 3
                        }
variables['V_jet_eta2'] = {  'name': 'Alt$(CleanJet_eta[v_jet_1],-9999.)',
                        'range': (30,-5,5),
                        'xaxis': '#eta 2nd vbs jet',
                        'fold' : 3
                        }

variables['V_jet_pt1']  = {   'name': 'Alt$(CleanJet_pt[v_jet_0],-9999.)',            #   variable name    
                        'range' : (60,0,800),    #   variable range
                        'xaxis' : 'p_{T} 1st vbs jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['V_jet_pt2']  = {   'name': 'Alt$(CleanJet_pt[v_jet_1],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd vbs jet [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['mjj_max']  = {   'name': 'mjj_max',            #   variable name    
                        'range' : (20,200,4000),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3
                        }

variables['detajj_mjjmax']  = {   'name': 'detajj_mjjmax',            #   variable name    
                           'range' : (12,2.0,8.0),    #   variable range
                           'xaxis' : '#Delta #eta jj',  #   x axis name
                           'fold' :3
                           }

variables['V_jet_mass']  = {   'name': 'V_jet_mass',            #   variable name    
                           'range' : (35,0,220),    #   variable range
                           'xaxis' : 'V_jet_mass',  #   x axis name
                           'fold' :3
                           }
                           """
####################
#### mva variables: remember to blind at high-DNN/BDT bings in the signal region
####################
### DNN variables

variables['DNNoutput_resolved'] = {
    'name': 'DNNoutput_resolved',
    'range': ([0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {   
        "Resolved_SR": [0.8,1],
        #"boost_sig_mjjincl_ele": [0.8,1],
    }
}
### BDT output

#variables['BDToutput'] = {
#    'name': 'BDToutput',
#    'range': ([0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
#    'xaxis': 'BDT output',
#    'fold': 3 ,
#    'blind': {
#        "res_sig_mjjincl_ele": [0.8,1],
#        "res_sig_mjjincl_mu": [0.8,1], 
#        "res_sig_mjjincl_dnnhigh_mu": [0.8,1], 
#        "res_sig_mjjincl_dnnhigh_ele": [0.8,1],
#        "boost_sig_mjjincl_ele": [0.8,1],
#        "boost_sig_mjjincl_mu": [0.8,1],
#        "boost_sig_mjjincl_dnnhigh_ele": [0.8,1],
#        "boost_sig_mjjincl_dnnhigh_mu": [0.8,1],
#    }
#}

###########################