operators = {
    'cS0': {
        'quadReweight': '( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[80] + LHEReweightingWeight[0] - 2 * LHEReweightingWeight[40]))',
        'LinReweight': '( 0.5* (1/(30)) * ( LHEReweightingWeight[80] - LHEReweightingWeight[0] ))',
        'sm': '( LHEReweightingWeight[40] )'
    },
    'cS1': {
        'quadReweight': '( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[161] + LHEReweightingWeight[81] - 2 * LHEReweightingWeight[121]))',
        'LinReweight': '( 0.5* (1/(30)) * ( LHEReweightingWeight[161] - LHEReweightingWeight[81] ))',
        'sm': '( LHEReweightingWeight[121] )'
    },
    'cS2': {
        'quadReweight': '( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[242] + LHEReweightingWeight[162] - 2 * LHEReweightingWeight[202]))',
        'LinReweight': '( 0.5* (1/(30)) * ( LHEReweightingWeight[242] - LHEReweightingWeight[162] ))',
        'sm': '( LHEReweightingWeight[202] )'
    },
    'cT0': {
        'quadReweight': '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[870] + LHEReweightingWeight[830] - 2 * LHEReweightingWeight[850]))',
        'LinReweight': '( 0.5* (1/(1)) * ( LHEReweightingWeight[870] - LHEReweightingWeight[830] ))',
        'sm': '( LHEReweightingWeight[850] )',
    },
    'cT1': {
        'quadReweight': '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[951] + LHEReweightingWeight[911] - 2 * LHEReweightingWeight[931]))',
        'LinReweight': '( 0.5* (1/(1)) * ( LHEReweightingWeight[951] - LHEReweightingWeight[911] ))',
        'sm': '( LHEReweightingWeight[931] )',
    },
    'cT2': {
        'quadReweight': '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[1022] + LHEReweightingWeight[1002] - 2 * LHEReweightingWeight[1012]))',
        'LinReweight': '( 0.5* (1/(1)) * ( LHEReweightingWeight[1022] - LHEReweightingWeight[1002] ))',
        'sm': '( LHEReweightingWeight[1012] )',
    },
    'cT3': {
        'quadReweight': '( 0.5* (1/(4)) * (1/(4)) * ( LHEReweightingWeight[1133] + LHEReweightingWeight[1053] - 2 * LHEReweightingWeight[1093]))',
        'LinReweight': '( 0.5* (1/(4)) * ( LHEReweightingWeight[1133] - LHEReweightingWeight[1053] ))',
        'sm': '( LHEReweightingWeight[1093] )'
    },
    'cT4': {
        'quadReweight': '( 0.5* (1/(4)) * (1/(4)) * ( LHEReweightingWeight[1214] + LHEReweightingWeight[1134] - 2 * LHEReweightingWeight[1174]))',
        'LinReweight': '( 0.5* (1/(4)) * ( LHEReweightingWeight[1214] - LHEReweightingWeight[1134] ))',
        'sm': '( LHEReweightingWeight[1174] )'
    },
    'cT5': {
        'quadReweight': '( 0.5* (1/(8)) * (1/(8)) * ( LHEReweightingWeight[1295] + LHEReweightingWeight[1215] - 2 * LHEReweightingWeight[1255]))',
        'LinReweight': '( 0.5* (1/(8)) * ( LHEReweightingWeight[1295] - LHEReweightingWeight[1215] ))',
        'sm': '( LHEReweightingWeight[1255] )'
    },
    'cT6': {
        'quadReweight': '( 0.5* (1/(8)) * (1/(8)) * ( LHEReweightingWeight[1376] + LHEReweightingWeight[1296] - 2 * LHEReweightingWeight[1336]))',
        'LinReweight': '( 0.5* (1/(8)) * ( LHEReweightingWeight[1376] - LHEReweightingWeight[1296] ))',
        'sm': '( LHEReweightingWeight[1336] )'
    },
    'cT7': {
        'quadReweight': '( 0.5* (1/(16)) * (1/(16)) * ( LHEReweightingWeight[1457] + LHEReweightingWeight[1377] - 2 * LHEReweightingWeight[1417]))',
        'LinReweight': '( 0.5* (1/(16)) * ( LHEReweightingWeight[1457] - LHEReweightingWeight[1377] ))',
        'sm': '( LHEReweightingWeight[1417] )'
    },
    'cT8': {
        'quadReweight': '( 0.5* (1/(20)) * (1/(20)) * ( LHEReweightingWeight[1538] + LHEReweightingWeight[1458] - 2 * LHEReweightingWeight[1498]))',
        'LinReweight': '( 0.5* (1/(20)) * ( LHEReweightingWeight[1538] - LHEReweightingWeight[1458] ))',
        'sm': '( LHEReweightingWeight[1498] )'
    },
    'cT9': {
        'quadReweight': '( 0.5* (1/(20)) * (1/(20)) * ( LHEReweightingWeight[1619] + LHEReweightingWeight[1539] - 2 * LHEReweightingWeight[1579]))',
        'LinReweight': '( 0.5* (1/(20)) * ( LHEReweightingWeight[1619] - LHEReweightingWeight[1539] ))',
        'sm': '( LHEReweightingWeight[1579] )'
    },
    'cM0': {
        'quadReweight': '( 0.5* (1/(5.4)) * (1/(5.4)) * ( LHEReweightingWeight[289] + LHEReweightingWeight[277] - 2 * LHEReweightingWeight[283]))',
        'LinReweight': '( 0.5* (1/(5.4)) * ( LHEReweightingWeight[289] - LHEReweightingWeight[277] ))',
        'sm': '( LHEReweightingWeight[283] )'
    },
    'cM1': {
        'quadReweight': '( 0.5* (1/(14)) * (1/(14)) * ( LHEReweightingWeight[384] + LHEReweightingWeight[344] - 2 * LHEReweightingWeight[364]))',
        'LinReweight': '( 0.5* (1/(14)) * ( LHEReweightingWeight[384] - LHEReweightingWeight[344] ))',
        'sm': '( LHEReweightingWeight[364] )'
    },
    'cM2': {
        'quadReweight': '( 0.5* (1/(60)) * (1/(60)) * ( LHEReweightingWeight[485] + LHEReweightingWeight[405] - 2 * LHEReweightingWeight[445]))',
        'LinReweight': '( 0.5* (1/(60)) * ( LHEReweightingWeight[485] - LHEReweightingWeight[405] ))',
        'sm': '( LHEReweightingWeight[445] )'
    },
    'cM3': {
        'quadReweight': '( 0.5* (1/(80)) * (1/(80)) * ( LHEReweightingWeight[566] + LHEReweightingWeight[486] - 2 * LHEReweightingWeight[526]))',
        'LinReweight': '( 0.5* (1/(80)) * ( LHEReweightingWeight[566] - LHEReweightingWeight[486] ))',
        'sm': '( LHEReweightingWeight[526] )'
    },
    'cM4': {
        'quadReweight': '( 0.5* (1/(80)) * (1/(80)) * ( LHEReweightingWeight[647] + LHEReweightingWeight[567] - 2 * LHEReweightingWeight[607]))',
        'LinReweight': '( 0.5* (1/(80)) * ( LHEReweightingWeight[647] - LHEReweightingWeight[567] ))',
        'sm': '( LHEReweightingWeight[607] )'
    },
    'cM5': {
        'quadReweight': '( 0.5* (1/(160)) * (1/(160)) * ( LHEReweightingWeight[728] + LHEReweightingWeight[648] - 2 * LHEReweightingWeight[688]))',
        'LinReweight': '( 0.5* (1/(160)) * ( LHEReweightingWeight[728] - LHEReweightingWeight[648] ))',
        'sm': '( LHEReweightingWeight[688] )'
    },
    'cM7': {
        'quadReweight': '( 0.5* (1/(24)) * (1/(24)) * ( LHEReweightingWeight[781] + LHEReweightingWeight[757] - 2 * LHEReweightingWeight[769]))',
        'LinReweight': '( 0.5* (1/(24)) * ( LHEReweightingWeight[781] - LHEReweightingWeight[757] ))',
        'sm': '( LHEReweightingWeight[769] )'
    }
}



########################################
#######       EFT weights       ########
########################################
#### S0 - wc=30
#quadReweight_cS0 = '( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[80] + LHEReweightingWeight[0] - 2 * LHEReweightingWeight[40]))'
#LinReweight_cS0 = '( 0.5* (1/(30)) * ( LHEReweightingWeight[80] - LHEReweightingWeight[0] ))'
#sm_cS0 = '( LHEReweightingWeight[40] )'
#### S1 - wc=30
#quadReweight_cS1 ='( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[161] + LHEReweightingWeight[81] - 2 * LHEReweightingWeight[121]))'
#LinReweight_cS1 = '( 0.5* (1/(30)) * ( LHEReweightingWeight[161] - LHEReweightingWeight[81] ))'
#sm_cS1 = '( LHEReweightingWeight[121] )'
#### S2 - wc=30
#quadReweight_cS2 = '( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[242] + LHEReweightingWeight[162] - 2 * LHEReweightingWeight[202]))'
#LinReweight_cS2 = '( 0.5* (1/(30)) * ( LHEReweightingWeight[242] - LHEReweightingWeight[162] ))'
#sm_cS2 = '( LHEReweightingWeight[202] )'
#### T0 - wc =1
#quadReweight_cT0 = '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[870] + LHEReweightingWeight[830] - 2 * LHEReweightingWeight[850]))'
#LinReweight_cT0 = '( 0.5* (1/(1)) * ( LHEReweightingWeight[870] - LHEReweightingWeight[830] ))'
#sm_cT0 = '( LHEReweightingWeight[850] )'
#LinQuadReweight_cT0 = '(' + quadReweight_cT0 + '+' + LinReweight_cT0 + ')'
#smLinQuadReweight_cT0 = '(' + sm_cT0 + '+' + quadReweight_cT0 + '+' + LinReweight_cT0 + ')'
#### T1 - wc =1
#quadReweight_cT1 = '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[951] + LHEReweightingWeight[911] - 2 * LHEReweightingWeight[931]))'
#LinReweight_cT1 = '( 0.5* (1/(1)) * ( LHEReweightingWeight[951] - LHEReweightingWeight[911] ))'
#sm_cT1 = '( LHEReweightingWeight[931] )'
#LinQuadReweight_cT1 = '(' +  quadReweight_cT1 + '+' + LinReweight_cT1 + ')'
#smLinQuadReweight_cT1 = '(' + sm_cT0 + '+' +  quadReweight_cT1 + '+' + LinReweight_cT1 + ')'
#### T2 - wc =1
#quadReweight_cT2 = '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[1022] + LHEReweightingWeight[1002] - 2 * LHEReweightingWeight[1012]))'
#LinReweight_cT2 = '( 0.5* (1/(1)) * ( LHEReweightingWeight[1022] - LHEReweightingWeight[1002] ))'
#sm_cT2 = '( LHEReweightingWeight[1012] )'
#LinQuadReweight_cT2 = '(' + quadReweight_cT2 + '+' + LinReweight_cT2 + ')'
#smLinQuadReweight_cT2 = '(' + sm_cT0 + '+' +  quadReweight_cT2 + '+' + LinReweight_cT2 + ')'
#### T3 -  wc=4
#quadReweight_cT3 ='( 0.5* (1/(4)) * (1/(4)) * ( LHEReweightingWeight[1133] + LHEReweightingWeight[1053] - 2 * LHEReweightingWeight[1093]))'
#LinReweight_cT3 = '( 0.5* (1/(4)) * ( LHEReweightingWeight[1133] - LHEReweightingWeight[1053] ))'
#sm_cT3 = '( LHEReweightingWeight[1093] )'
#### T4 - wc =4
#quadReweight_cT4 = '( 0.5* (1/(4)) * (1/(4)) * ( LHEReweightingWeight[1214] + LHEReweightingWeight[1134] - 2 * LHEReweightingWeight[1174]))'
#LinReweight_cT4 = '( 0.5* (1/(4)) * ( LHEReweightingWeight[1214] - LHEReweightingWeight[1134] ))'
#sm_cT4 = '( LHEReweightingWeight[1174] )'
##### T5 - wc=8
#quadReweight_cT5 = '( 0.5* (1/(8)) * (1/(8)) * ( LHEReweightingWeight[1295] + LHEReweightingWeight[1215] - 2 * LHEReweightingWeight[1255]))'
#LinReweight_cT5 = '( 0.5* (1/(8)) * ( LHEReweightingWeight[1295] - LHEReweightingWeight[1215] ))'
#sm_cT5 = '( LHEReweightingWeight[1255] )'
##### T6 - wc=8
#quadReweight_cT6 = '( 0.5* (1/(8)) * (1/(8)) * ( LHEReweightingWeight[1376] + LHEReweightingWeight[1296] - 2 * LHEReweightingWeight[1336]))'
#LinReweight_cT6 = '( 0.5* (1/(8)) * ( LHEReweightingWeight[1376] - LHEReweightingWeight[1296] ))'
#sm_cT6 = '( LHEReweightingWeight[1336] )'
#### T7 - wc=16
#quadReweight_cT7 = '( 0.5* (1/(16)) * (1/(16)) * ( LHEReweightingWeight[1457] + LHEReweightingWeight[1377] - 2 * LHEReweightingWeight[1417]))'
#LinReweight_cT7 = '( 0.5* (1/(16)) * ( LHEReweightingWeight[1457] - LHEReweightingWeight[1377] ))'
#sm_cT7 = '( LHEReweightingWeight[1417] )'
#### T8 - wc=20
#quadReweight_cT8 = '( 0.5* (1/(20)) * (1/(20)) * ( LHEReweightingWeight[1538] + LHEReweightingWeight[1458] - 2 * LHEReweightingWeight[1498]))'
#LinReweight_cT8 = '( 0.5* (1/(20)) * ( LHEReweightingWeight[1538] - LHEReweightingWeight[1458] ))'
#sm_cT8 = '( LHEReweightingWeight[1498] )'
#### T9 - wc=20
#quadReweight_cT9 = '( 0.5* (1/(20)) * (1/(20)) * ( LHEReweightingWeight[1619] + LHEReweightingWeight[1539] - 2 * LHEReweightingWeight[1579]))'
#LinReweight_cT9 = '( 0.5* (1/(20)) * ( LHEReweightingWeight[1619] - LHEReweightingWeight[1539] ))'
#sm_cT9 = '( LHEReweightingWeight[1579] )'
### cM0 - wc=5-4
#quadReweight_cM0 = '( 0.5* (1/(5.4)) * (1/(5.4)) * ( LHEReweightingWeight[289] + LHEReweightingWeight[277] - 2 * LHEReweightingWeight[283]))'
#LinReweight_cM0 = '( 0.5* (1/(5.4)) * ( LHEReweightingWeight[289] - LHEReweightingWeight[277] ))'
#sm_cM0 = '( LHEReweightingWeight[283] )'
#### cM1 - wc=14
#quadReweight_cM1 = '( 0.5* (1/(14)) * (1/(14)) * ( LHEReweightingWeight[384] + LHEReweightingWeight[344] - 2 * LHEReweightingWeight[364]))'
#LinReweight_cM1 = '( 0.5* (1/(14)) * ( LHEReweightingWeight[384] - LHEReweightingWeight[344] ))'
#sm_cM1 = '( LHEReweightingWeight[364] )'
#### cM2 - wc=60
#quadReweight_cM2 = '( 0.5* (1/(60)) * (1/(60)) * ( LHEReweightingWeight[485] + LHEReweightingWeight[405] - 2 * LHEReweightingWeight[445]))'
#LinReweight_cM2 = '( 0.5* (1/(60)) * ( LHEReweightingWeight[485] - LHEReweightingWeight[405] ))'
#sm_cM2 = '( LHEReweightingWeight[445] )'
#### cM3 - wc=80
#quadReweight_cM3 = '( 0.5* (1/(80)) * (1/(80)) * ( LHEReweightingWeight[566] + LHEReweightingWeight[486] - 2 * LHEReweightingWeight[526]))'
#LinReweight_cM3 = '( 0.5* (1/(80)) * ( LHEReweightingWeight[566] - LHEReweightingWeight[486] ))'
#sm_cM3 ='( LHEReweightingWeight[526] )'
#### cM4 - wc=80
#quadReweight_cM4 = '( 0.5* (1/(80)) * (1/(80)) * ( LHEReweightingWeight[647] + LHEReweightingWeight[567] - 2 * LHEReweightingWeight[607]))'
#LinReweight_cM4 = '( 0.5* (1/(80)) * ( LHEReweightingWeight[647] - LHEReweightingWeight[567] ))'
#sm_cM4 = '( LHEReweightingWeight[607] )'
#### cM5 - wc=160
#quadReweight_cM5 = '( 0.5* (1/(160)) * (1/(160)) * ( LHEReweightingWeight[728] + LHEReweightingWeight[648] - 2 * LHEReweightingWeight[688]))'
#LinReweight_cM5 = '( 0.5* (1/(160)) * ( LHEReweightingWeight[728] - LHEReweightingWeight[648] ))'
#sm_cM5 = '( LHEReweightingWeight[688] )'
#### cM7 - wc=24
#quadReweight_cM7 = '( 0.5* (1/(24)) * (1/(24)) * ( LHEReweightingWeight[781] + LHEReweightingWeight[757] - 2 * LHEReweightingWeight[769]))'
#LinReweight_cM7 = '( 0.5* (1/(24)) * ( LHEReweightingWeight[781] - LHEReweightingWeight[757] ))'
#sm_cM7 = '( LHEReweightingWeight[769] )'
