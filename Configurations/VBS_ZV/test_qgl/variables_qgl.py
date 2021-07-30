variables['VBS_jet_qgl1'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[vbs_jet_0]), -9999)',
                        'range' : (40,0,1),
                        'xaxis' : 'QGL 1st VBS jet',
                        'fold' : 3,
                        }
variables['VBS_jet_qgl2'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[vbs_jet_1]), -9999)',
                        'range' : (40,0,1),
                        'xaxis' : 'QGL 2nd VBS jet',
                        'fold' : 3,

}


variables['V_jet_qgl1'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[v_jet_0]), -9999)',
                        'range' : (40,0,1),
                        'xaxis' : 'QGL 1st V jet',
                        'fold' : 3,

}
variables['V_jet_qgl2'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[v_jet_1]), -9999)',
                        'range' : (40,0,1),
                        'xaxis' : 'QGL 2nd V jet',
                        'fold' : 3,


}

variables['VBS_jet_qgl1_morphed'] = {  'name': 'vbs_0_qglmorphed_res',
                        'range': (40,0.,1.),
                        'xaxis': 'Qgl VBS 0 jet',
                        'fold': 3,
                     
                }

variables['VBS_jet_qgl2_morphed'] = {  'name': 'vbs_1_qglmorphed_res',
                        'range': (40,0.,1.),
                        'xaxis': 'Qgl VBS 1 jet',
                        'fold': 3,
                              }

variables['V_jet_qgl1_morphed'] = {  'name': 'vjet_0_qglmorphed_res',
                        'range': (40,0.,1.),
                        'xaxis': 'Qgl Vjet 0 jet',
                        'fold': 3,
                                 }

variables['V_jet_qgl2_morphed'] = {  'name': 'vjet_1_qglmorphed_res',
                        'range': (40,0.,1.),
                        'xaxis': 'Qgl Vjet 1 jet',
                        'fold': 3,
                                 }

