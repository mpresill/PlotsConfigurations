variables['VBS_jet_pt1_idx']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_0],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 1st VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['VBS_jet_pt2_idx']  = {   'name': 'Alt$(CleanJet_pt[vbs_jet_1],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['V_jet_pt1_idx']  = {   'name': 'Alt$(CleanJet_pt[v_jet_0],-9999.)',            #   variable name    
                        'range' : (60,0,800),    #   variable range
                        'xaxis' : 'p_{T} 1st V jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['V_jet_pt2_idx']  = {   'name': 'Alt$(CleanJet_pt[v_jet_1],-9999.)',            #   variable name    
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd V jet [GeV]',  #   x axis name
                        'fold' : 3
                        }


variables['VBS_jet_pt1']  = {   'name': 'Alt$(vbs_jet_pt1,-9999.)',            #   variable name
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 1st VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['VBS_jet_pt2']  = {   'name': 'Alt$(vbs_jet_pt2,-9999.)',            #   variable name
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd VBS jet [GeV]',  #   x axis name
                        'fold' : 3
                        }

variables['V_jet_pt1']  = {   'name': 'Alt$(v_jet_pt1,-9999.)',            #   variable name
                        'range' : (60,0,800),    #   variable range
                        'xaxis' : 'p_{T} 1st V jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
variables['V_jet_pt2']  = {   'name': 'Alt$(vbs_jet_pt2,-9999.)',            #   variable name
                        'range' : (30,0,400),    #   variable range
                        'xaxis' : 'p_{T} 2nd V jet [GeV]',  #   x axis name
                        'fold' : 3
                        }
