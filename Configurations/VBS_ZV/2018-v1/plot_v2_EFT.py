# plot configuration

from ROOT import TColor

# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used

colors = {
    # https://root.cern.ch/doc/master/classTColor.html#C02
    'kWhite'   : 0,
    'kBlack'   : 1,
    'kGray'    : 920,
    'kRed'     : 632,
    'kGreen'   : 416,
    'kBlue'    : 600,
    'kYellow'  : 400,
    'kMagenta' : 616,
    'kCyan'    : 432,
    'kOrange'  : 800,
    'kSpring'  : 820,
    'kTeal'    : 840,
    'kAzure'   : 860,
    'kViolet'  : 880,
    'kPink'    : 900, 
}

palette = {
    "Orange": (242, 108, 13), #f26c0d  
    "Yellow": (247, 195, 7), #f7c307
    "LightBlue": (153, 204, 255), #99ccff
    "MediumBlue": (72, 145, 234),  #4891ea
    "MediumBlue2": (56, 145, 224),    #3891e0
    "DarkBlue": (8, 103, 136), #086788
    "Green": (47, 181, 85), #2fb555
    "Green2": (55, 183, 76),  #37b74c
    "LightGreen" : (82, 221, 135), #52dd87
    "Violet": (242, 67, 114), #f24372   
}

'''
Colors
"Wjets6": ( 246, 137, 61 ), #f6893d 
"Wjets2": (240, 115, 66), #f07342
"Wjets3": (233, 119, 73), #e97749
"Wjets4": (229, 94, 41), #e55e29
"Wjets5": (211, 87, 38), #d34912 
'''
#
 

DY_palette = ['#093316','#006400', '#008000',  '#32CD32','#00FF00', '#ADFF2F', '#FFFF00', '#FFC800', '#FF9D00', '#FF7700', '#FF3300','#FF003C', '#006400', '#008000',  '#32CD32','#00FF00', '#ADFF2F'  ]


phase_spaces_boost = [c for c in cuts if "Boosted" in c]
phase_spaces_res = [c for c in cuts if "Resolved" in c]
"""
DY_bins = []
for bin in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
    DY_bins.append("DY_Resolved_2d_"+bin)
for bin in range(1,6):
     DY_bins.append("DY_Boosted_Z_"+str(bin))"""

DY_bins = ["DY_Resolved_2d_"+str(ir) for ir in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']] + ["DY_Boosted_Z_"+str(ir) for ir in range(1,6)]  




groupPlot['lin_FT0']  = {
                  'nameHR' : 'linear (from FT0)',
                  'isSignal' : 1,
                  'color': palette["LightGreen"],    # kGray + 1
                  'samples'  : ['lin_FT0']
}

groupPlot['quad_FT0']  = {
                  'nameHR' : 'quadratic (from FT0)',
                  'isSignal' : 1,
                  'color': palette["Green2"],    # kGray + 1
                  'samples'  : ['quad_FT0']
}

groupPlot['lin_FT1']  = {
                  'nameHR' : 'linear (from FT1)',
                  'isSignal' : 1,
                  'color': palette["LightBlue"],    # kGray + 1
                  'samples'  : ['lin_FT1']
}

groupPlot['quad_FT1']  = {
                  'nameHR' : 'quadratic (from FT1)',
                  'isSignal' : 1,
                  'color': palette["MediumBlue2"],    # kGray + 1
                  'samples'  : ['quad_FT1']
}

groupPlot['lin_FT2']  = {
                  'nameHR' : 'linear (from FT2)',
                  'isSignal' : 1,
                  'color': palette["Yellow"],    # kGray + 1
                  'samples'  : ['lin_FT2']
}

#groupPlot['quad_FT2']  = {
#                  'nameHR' : 'quadratic (from FT2)',
#                  'isSignal' : 1,
#                  'color': palette["Orange"],    # kGray + 1
#                  'samples'  : ['quad_FT2']
#}

groupPlot['sm_dipole']  = {
                 'nameHR' : 'VBS ewk dipole',
                 'isSignal' : 1,
                 'color': palette["DarkBlue"],
                 'samples'  : ['sm_dipole'],
                 'fill': 1001
              }
            

#groupPlot['sm_global']  = {
#                 'nameHR' : 'VBS ewk global',
#                 'isSignal' : 1,
#                 'color': colors["kRed"],
#                 'samples'  : ['sm_global'],
#                 'fill': 1001
#              }


#plot['sm_global']  = { 
#                  'color': colors["kAzure"] -3,    
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }


plot['lin_FT0'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }

plot['quad_FT0'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }

plot['lin_FT1'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }

plot['quad_FT1'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }


plot['lin_FT2'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 1,
                 'isData'   : 0, 
                 'scale'    : 1.
        }

#plot['quad_FT2'] = {   
#                 'color': colors['kAzure']-1,
#                 'isSignal' : 1,
#                 'isData'   : 0, 
#                 'scale'    : 1.
#        }
#plot['WmTo2J_ZTo2L_aQGC']  = {
#                  'color':  colors['kRed']-3,
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#              }

plot['sm_dipole']  = {
                  'color': colors["kCyan"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }


#plot['WmTo2J_ZTo2L_aQGC_eboliv2']  = {
#                  'color': colors["kCyan"]+2,
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1.   
#              }
#
#plot['WGJJ']= { 'color': colors["kCyan"]+4,
#                'isSignal' : 0,
#                'isData'   : 0,
#                'scale'    : 1.   
#            }
#
#plot['sm_FT1']  = {  
#                'color': colors['kTeal'],
#                'isSignal' : 1,
#                'isData'   : 0, 
#                'scale'    : 1.0
#            }
#
#plot['sm_FT2']  = {  
#                'color': colors['kTeal'],
#                'isSignal' : 1,
#                'isData'   : 0, 
#                'scale'    : 1.0
#            }


# additional options

legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
