config = {
    "top" :
     { 
        "nuisances" : [ "QCDscale_top"],#"CMS_PS_FSR","CMS_PS_ISR",#"CMS_PU_2017"
        "phase_spaces" : {
            "Boosted" :  ["Boosted_topcr", "Boosted_SR_bVeto","Boosted_SR_bTag","Boosted_DYcr_bVeto","Boosted_DYcr_bTag"],
        } 
    },
}


DY_bins_boost = []
for bin in range(1,6):
     DY_bins_boost.append("DY_Boosted_Z_"+str(bin))

for DYbin in DY_bins_boost:
    config[DYbin] = { 
        "nuisances" : [ "QCDscale_DY"], #,"CMS_PS_ISR","QCDscale_Wjets","CMS_PU_2018"
        "phase_spaces" : {
            "Boosted_bVeto" :  ["Boosted_DYcr_bVeto", "Boosted_SR_bVeto"],
            "Boosted_bTag" :    ["Boosted_DYcr_bTag", "Boosted_SR_bTag"],
        }
    }
