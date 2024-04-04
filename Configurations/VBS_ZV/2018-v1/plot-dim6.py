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




groupPlot['other']  = {  
                  'nameHR' : 'other',
                  'isSignal' : 0,
                  'color':   901, #kpink+1
                  'samples'  : ['other'],#,'WGJJ'
                  'fill': 1001

              }

groupPlot['tZq']  = {
                  'nameHR' : 'tZq',
                  'isSignal' : 0,
                  'color':   palette["Violet"],
                  'samples'  : ['tZq'],
                  'fill': 1001

              }

groupPlot['top']  = {
                 'nameHR' : 'top',
                 'isSignal' : 0,
                 'color':  colors["kOrange"]+1,
                 'samples'  : ['top'],
                 'fill': 1001
             }

groupPlot['Fake']  = {
                  'nameHR' : 'nonprompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake']
}

groupPlot['Vg+VgS']  = {
                  'nameHR' : "V#gamma+V#gamma*",
                  'isSignal' : 0,
                  'color'    : palette['LightBlue'],   # kOrange - 3
                  'samples'  : ['Vg','VgS'],
                  'fill': 1001
              }

groupPlot['vbfV+VV']  = {
                  'nameHR' : 'vbfV+VV',
                  'isSignal' : 0,
                  'color': palette["DarkBlue"],
                  'samples'  : ['VBS_VV_QCD','VBF-V'],
                  'fill': 1001
              }

 # if phase_spaces_boost is True:
 #     for i,DYbin in enumerate(DY_bins_boost):
 #             groupPlot[DYbin] = {
 #                             'nameHR': DYbin,
 #                             'isSignal' : 0,
 #                             'color' : DY_palette[i],
 #                             'samples' : DYbin,
 #                             'fill' : 1001,
 #                             'removeFromCuts': phase_spaces_res           
 #     }
 # else:
 #     for i,DYbin in enumerate(DY_bins_res):
 #             groupPlot[DYbin] = {
 #                             'nameHR': DYbin,
 #                             'isSignal' : 0,
 #                             'color' : DY_palette[i],
 #                             'samples' : DYbin,
 #                             'fill' : 1001,
 #                             'removeFromCuts': phase_spaces_boost               
 #     }


groupPlot['DY'] = {
        'nameHR': 'DY',
        'isSignal' : 0,
        'color' : palette["Green"],
        'samples' : DY_bins,
        'fill' : 1001,
    }
    
groupPlot['VBS']  = {
                 'nameHR' : 'VBS ewk',
                 'isSignal' : 1,
                 'color': colors["kRed"]+1,
                 'samples'  : ['sm'],
                 'fill': 1001
              }


groupPlot['sm_lin_quad_cW']  = {
                 'nameHR' : 'SM+Linear+Quadratic cW',
                 'isSignal' : 2,
                 'color': colors["kBlue"]+4,
                 'samples'  : ['sm_lin_quad_cW'],
                 'fill': 1001
              }
#
groupPlot['quad_cW']  = {
                 'nameHR' : 'Quadratic FT1',
                 'isSignal' : 2,
                 'color': colors["kBlue"]+1,
                 'samples'  : ['quad_cW'],
                 'fill': 1001
              }




# keys here must match keys in samples.py    
#
# 
# 
#  
plot['other']  = { 
                  'color': colors["kAzure"] -3,    
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


"""for DYbin in DY_bins:
	plot[DYbin] =  {   
                    'color': colors['kAzure']-1,
                    'isSignal' : 0,
                    'isData'   : 0, 
                    'scale'    : 1.0,
                    'removeFromCuts' : phase_spaces_res, 
                    }

for DYbin in DY_bins:
	plot[DYbin] =  {   
                    'color': colors['kAzure']-1,
                    'isSignal' : 0,
                    'isData'   : 0, 
                    'scale'    : 1.0,
                    'removeFromCuts' : phase_spaces_boost, 
                    }"""

for DYbin in DY_bins:
	plot[DYbin] =  {   
                    'color': colors['kAzure']-1,
                    'isSignal' : 0,
                    'isData'   : 0, 
                    'scale'    : 1.0,
                    }


plot['Vg']  = { 
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }
plot['VgS'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VBF-V']  = {
                  'color': colors['kYellow']+3,  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.
              }


plot['top'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 0,
                 'isData'   : 0, 
                 'scale'    : 1.
        }



plot['sm']  = {
                  'color': colors["kCyan"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }

plot['quad_cW']  = {
                  'color': colors["kCyan"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }

plot['sm_lin_quad_cW']  = {
                  'color': colors["kCyan"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   
              }


plot['VBS_VV_QCD']  = {
                  'color': colors["kCyan"]+1, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   
              }
              
plot['tZq']  = {
                  'color': colors["kCyan"]+2,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   
              }

#plot['WGJJ']= { 'color': colors["kCyan"]+4,
#                'isSignal' : 0,
#                'isData'   : 0,
#                'scale'    : 1.   
#            }

plot['Fake']  = {  
                'color': colors['kTeal'],
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0
            }

# data
plot['DATA']  = { 
                 'nameHR' : 'Data',
                 'color': 1 ,  
                 'isSignal' : 0,
                 'isData'   : 1 ,
#		         'scale' :1.,
#                 'cuts': {
#			        "Resolved_SR_bVeto" : 0,	
#			        "Resolved_SR_bTag" :0,
#			        "Boosted_SR_bVeto" : 0,
#			        "Boosted_SR_bTag" :0,
#		         }	
             }



# additional options

legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
