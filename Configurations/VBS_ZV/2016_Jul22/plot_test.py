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


DY_palette = ['#093316','#006400', '#008000',  '#32CD32','#00FF00', '#ADFF2F', '#FFFF00', '#FFC800', '#FF9D00', '#FF7700', '#FF3300','#FF003C', '#006400', '#008000',  '#32CD32','#00FF00', '#ADFF2F'  ]


phase_spaces_boost = [c for c in cuts if "Boosted" in c]
phase_spaces_res = [c for c in cuts if "Resolved" in c]


plot['sm_global']  = {
                  'color': colors["kRed"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }
"""
plot['sm_dipole']  = {
                  'color': colors["kOrange"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }

plot['sm_cT0']  = {
                  'color': colors["kGreen"], 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }

plot['sm_cT1']  = {
                  'color': colors["kYellow"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }

plot['ZZ_EFT']  = {
                    'color': colors["kBlue"]-3, 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }


plot['WP_EFT']  = {
                    'color': colors["kBlue"], 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }

plot['WM_EFT']  = {
                    'color': colors["kCyan"]+3, 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }

plot['ZZ']  = {
                  'color': colors["kCyan"]+1,
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }



plot['WM']  = {
                  'color': colors["kGreen"]+2, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }

plot['WP']  = {
                  'color': colors["kYellow"]+2, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }



plot['ZZ_EFT_v2']  = {
                    'color': colors["kYellow"]-3, 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }


plot['WP_EFT_v2']  = {
                    'color': colors["kYellow"], 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }

plot['WM_EFT_v2']  = {
                    'color': colors["kYellow"]+3, 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }



plot['sm_cT0']  = {
                  'color': colors["kGreen"], 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }
"""

plot['sm_cT0']  = {
                    'color': colors["kYellow"], 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }

plot['quad_cT0']  = {
                    'color': colors["kYellow"]+3, 
                    'isSignal' : 1,
                    'isData'   : 0,
                    'scale'    : 1.   
                }



plot['lin_cT0']  = {
                  'color': colors["kGreen"], 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }



# additional options

legend['lumi'] = 'L = 35.87/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
