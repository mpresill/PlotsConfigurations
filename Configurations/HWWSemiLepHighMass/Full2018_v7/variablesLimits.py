# # variables
#
# #variables = {}
#


controlRegions = {x for x in cuts if 'SB' in x or 'TopCR' in x}
hmSR  = {x for x in cuts if 'HMSR' in x}
boostedSR   = {x for x in cuts if 'BoostedSR' in x}
resolvedSR  = {x for x in cuts if 'ResolvedSR' in x}


variables['events']  = {
    'name' : '1',
    'range': (1,0,2),
    'xaxis': 'events',
    'cuts' : controlRegions
    'fold' : 3
}


variables['resolvHiggsMass'] = {
    'name' : 'HM_Hlnjj_mass',
    # 'range': ([0, 200, 250, 300, 350, 400, 450, 500, 550, 600,
    #           650, 700, 750, 800, 900, 1100, 1500, 2500],),
    'range': ([0, 200, 250, 290, 330, 370, 420, 470, 520,
               570, 620, 670, 720, 775, 870, 1000, 2000],),
    'xaxis': 'reconstr. H mass [GeV]',
    'cuts' : resolvedSR,
    'fold' : 3
}
variables['boostHiggsMass_ggf'] = {
    'name' : 'HM_CleanFatJetPassMBoosted_HlnFat_mass[0]',
    # 'range': ([0, 200, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800,
    #           900, 1000, 1100, 1200, 1350, 1500, 1700, 2000, 3000, 5000],),
    'range': ([0, 220, 300, 350, 400, 450, 490, 530, 580, 630, 680,
               730, 780, 840, 950, 1075, 1175, 1370, 1900, 5000],),
    'xaxis': 'reconstr. H mass [GeV]',
    'cuts' : boostedSR,
    'fold' : 3
}
variables['boostHiggsMass_vbf'] = {
    'name' : 'HM_CleanFatJetPassMBoosted_HlnFat_mass[0]',
    # 'range': ([0, 200, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800,
    #           900, 1000, 1100, 1200, 1350, 1500, 1700, 2000, 3000, 5000],),
    'range': ([0, 220, 300, 350, 400, 450, 490, 530, 580, 630, 680,
               730, 780, 840, 950, 1100, 1300, 1800, 5000],),
    'xaxis': 'reconstr. H mass [GeV]',
    'cuts' : boostedSR,
    'fold' : 3
}
variables['hmHiggsMass'] = {
    'name' : 'HM_CleanFatJetPassMBoosted_HlnFat_mass[0]',
    # 'range': ([0, 900, 1000, 1100, 1200, 1350, 1500, 1700, 2000, 3000, 5000],),
    # 'range': ([0, 900, 1000, 1100, 1200, 1325, 1580, 2050, 5000],),
    'range': ([0, 900, 990, 1085, 1185, 1300, 1550, 2000, 5000],),
    'xaxis': 'reconstr. H mass [GeV]',
    'cuts' : hmSR,
    'fold' : 3
}
