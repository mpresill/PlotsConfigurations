variables['VBS_jet_qgl1_idx'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[vbs_jet_0]), -9999)',
                        'range' : (55,-0.1,1),
                        'xaxis' : 'QGL 1st VBS jet',
                        'fold' : 3,
                        }
variables['VBS_jet_qgl2_idx'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[vbs_jet_1]), -9999)',
                        'range' : (55,-0.1,1),
                        'xaxis' : 'QGL 2nd VBS jet',
                        'fold' : 3,

}


variables['V_jet_qgl1_idx'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[v_jet_0]), -9999)',
                        'range' : (55,-0.1,1),
                        'xaxis' : 'QGL 1st V jet',
                        'fold' : 3,

}
variables['V_jet_qgl2_idx'] = { 'name' : 'Alt$(Jet_qgl->At(CleanJet_jetIdx[v_jet_1]), -9999)',
                        'range' : (55,-0.1,1),
                        'xaxis' : 'QGL 2nd V jet',
                        'fold' : 3,


}

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
                        'xaxis': 'Qgl Vjet 1st jet unmorphed',
                        'fold': 3,
                                 }

variables['V_jet_qgl2_unmorphed'] = {  'name': 'vjet_1_qgl_res',
                        'range': (55,-0.1,1.),
                        'xaxis': 'Qgl Vjet 2nd jet unmorphed',
                        'fold': 3,
                                 }
