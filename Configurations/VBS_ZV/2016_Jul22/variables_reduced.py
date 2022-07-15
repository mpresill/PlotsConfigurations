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

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }


resolved_cuts = [ c for c in cuts if 'Resolved' in c]
boosted_cuts = [ c for c in cuts if 'Boosted' in c]



#fitting with Z pt binning

variables['DYfit_Z_bin'] ={  'name' : 'fit_Z_bin',
                            'range' : (5,1,6), #(n.bins, 1, n.bins+1)
                            'xaxis' : 'fitting variable Z pt', 
                            'fold' : 3,

}


## mZV invariant mass
variables['ZV_mass'] = { 'name': 'mZV',            #   variable name    
                        'range' : ([200.,300.,400.,500.,600., 700.,800.,900., 1000., 1250., 1500., 2000., 2500.],),   #   variable range
                        'xaxis' : 'm_{ZV} [GeV]',  #   x axis name
                        'fold' :3,                   
}



### DNN variables
"""variables['DNNoutput_pruned_bVeto'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bTag": [0.8,1],
        "Boosted_SR_bTag": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}

variables['DNNoutput_pruned_bReq'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'blind': {
        "Resolved_SR_bVeto": [0.8,1],
        "Boosted_SR_bVeto": [0.8,1],
        "Resolved_SR_bTag": [0.8,1],
        "Boosted_SR_bTag": [0.8,1],
        "Boosted_SR": [0.8,1],
        "Resolved_SR": [0.8,1],

    }
}"""

variables['DNNoutput_pruned_bVeto_morebins'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98,1.],),
    'xaxis': 'DNN output',
    'fold': 3 ,
}

variables['DNNoutput_pruned_bReq_morebins'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98,1.],),
    'xaxis': 'DNN output',
    'fold': 3 ,
}
