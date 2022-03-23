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
     DY_bins.append("DY_Boosted_Z_bin"+str(bin))
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
	



structure['WJets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }


structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }
"""
structure['WWewk']  = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
"""

structure['ggWW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS'] = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VBF-V']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VBS_VV_QCD'] = {
                  'isSignal' : 0,
                  'isData'   : 0,
                  }

structure['VBS_ZV'] = {
                  'isSignal' : 1,
                  'isData'   : 0    
                  }
structure['tZq'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }
structure['WGJJ'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

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


