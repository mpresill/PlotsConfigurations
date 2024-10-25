from itertools import product, chain
# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    
"""
structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0
              }
"""

phase_spaces_boost = [c for c in cuts if "Boosted" in c]
phase_spaces_res = [c for c in cuts if "Resolved" in c]

DY_bins = []
for bin in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        DY_bins.append("DY_Resolved_2d_" + bin)
for bin in range(1,6):
     DY_bins.append("DY_Boosted_Z_"+str(bin))
for DYbin in DY_bins:
	if 'Boosted' in DYbin:
		structure[DYbin] = {
			'isSignal':0,
			'isData' : 0,
			'removeFromCuts': phase_spaces_res
		}
    	elif 'Resolved' in DYbin:
         	structure[DYbin] = {
                        'isSignal':0,
                        'isData' : 0,
                        'removeFromCuts': phase_spaces_boost
                }
"""
structure['DY'] = {
		'isSignal':0,
		'isData':0
}	
"""

structure['other']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }


#structure['WJets']  = {  
#                  'isSignal' : 0,
#                  'isData'   : 0 
#              }

structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }


structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


#structure['WW']  = {
#                  'isSignal' : 0,
#                  'isData'   : 0    
#                  }
"""
structure['WWewk']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
"""

##NELLA CATEGORIA BOOSTED NON HA EVENTI IN NESSUNA REGIONE!!! PROVOCA SOLO WARNING E CASINI CON COMBINE
#structure['ggWW']  = {                         
#                  'isSignal' : 0,
#                  'isData'   : 0 ,
#                  'removeFromCuts': phase_spaces_boost   
#                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS'] = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

#structure['ZZlep']  = { 
#                  'isSignal' : 0,
#                  'isData'   : 0 
#                  }
#
#structure['VVV']  = { 
#                  'isSignal' : 0,
#                  'isData'   : 0 
#                  }
#
structure['VBF-V']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VBS_VV_QCD'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['tZq'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }



############################signals                  
structure['sm'] = {
                  'isSignal' : 1,
                  'isData'   : 0    
                  }
                  
ops = ['cT0','cT1','cT2','cT3','cT4','cT5','cT6','cT7', 'cT8','cT9','cS0','cS1','cS2','cM0','cM1','cM2','cM3','cM4','cM5','cM7'] 
for op in ops:
    structure['quad_'+op] = {
                      'isSignal' : 1,
                      'isData'   : 0    
                      }
    structure['sm_lin_quad_'+op] = {
                      'isSignal' : 1,
                      'isData'   : 0    
                      }

######## signal for VBS combination effort 

#structure['ewk_ZZ'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['ewk_WmZ'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                 }
#structure['ewk_WpZ'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
                  
#### EFT ###
#structure['quad_cS0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cS0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
##
#structure['quad_cS1'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cS1'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
##
#structure['quad_cM0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cM0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
##
#structure['quad_cM1'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cM1'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
##
#structure['quad_cM6'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cM6'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
##
#structure['quad_cM7'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cM7'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }

##
#structure['quad_cT9'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cT9'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
###
#structure['quad_cT0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cT0'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
##
#structure['quad_cT2'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#structure['sm_lin_quad_cT2'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }

#structure['quad_cT6'] = {
#'isSignal' : 1,
#'isData'   : 0    
#}
#structure['sm_lin_quad_cT6'] = {
#                  'isSignal' : 1,
#                  'isData'   : 0    
#                  }
#############################
# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }

"""
print "INSTRUCTURE"
print cuts
print nuisances['']
print "OK"

for nuis in nuisances.itervalues():
  if 'cutspost' in nuis:
    nuis['cuts'] = nuis['cutspost'](nuis, cuts)

    print nuis

"""


