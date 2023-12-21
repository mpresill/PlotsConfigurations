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

#   DNN input variable in the resolved category:



    #**************** dy fitting variabl ***************#
variables['DYfit_Z_bin'] ={  'name' : 'fit_Z_bin',
                            'range' : (5,1,6), #(n.bins, 1, n.bins+1)
                            'xaxis' : 'fitting variable Z pt', 
                            'fold' : 3,
                            'divideByBinWidth': 1,

}

    #************* coarse binning (2016 only) ***************#
variables['DNNoutput_pruned_bVeto'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,                            
    'divideByBinWidth': 1,
}

variables['DNNoutput_pruned_bReq'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'divideByBinWidth': 1,
}

    #******************** DNN for 2017/2018

variables['DNNoutput_pruned_bVeto_morebins'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98,1.],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'divideByBinWidth': 1,
}

variables['DNNoutput_pruned_bReq_morebins'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range': ([0,0.1,0.2,0.3,0.4,0.5,0.55, 0.6,0.65,0.7,0.75,0.8,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98,1.],),
    'xaxis': 'DNN output',
    'fold': 3 ,
    'divideByBinWidth': 1,
}


    #************* extremly fine DNN for rebinning purposes ***************#
variables['DNNoutput_pruned_bReq_rebin'] = {
    'name': 'DNNoutput_pruned_bReq',
    'range':  (1000,0,1),
    'xaxis': 'DNN output',
    'fold': 3 ,                            
    'divideByBinWidth': 1,
}

variables['DNNoutput_pruned_bVeto_rebin'] = {
    'name': 'DNNoutput_pruned_bVeto',
    'range':  (1000,0,1),
    'xaxis': 'DNN output',
    'fold': 3 ,                            
    'divideByBinWidth': 1,
}


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

## mZV invariant mass (Giacomo's binning)
variables['Mzv'] = {   'name': 'mZV',
                        'range' : ([ 200., 400., 600., 800., 1000., 1200., 1500., 2000., 3000.],), #variable range  
                        'xaxis' : 'M_{ZV} [GeV]',
                        'fold' : 3,
                        }
## mZV invariant mass (smp-28-006 binning)
variables['ZV_mass'] = { 'name': 'mZV',            #   variable name    
                        'range' : ([200.,300.,400.,500.,600., 700.,800.,900., 1000., 1250., 1500., 2000., 2500.],),   #   variable range
                        'xaxis' : 'm_{ZV} [GeV]',  #   x axis name
                        'fold' :3,        
}
