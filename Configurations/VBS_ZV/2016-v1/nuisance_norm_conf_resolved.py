config = {
    "top" :
     { 
        "nuisances" : [ "QCDscale_top"],#"CMS_PS_FSR","CMS_PS_ISR",#"CMS_PU_2017"
        "phase_spaces" : {
            "Resolved" :  ["Resolved_topcr", "Resolved_SR_bVeto","Resolved_SR_bTag","Resolved_DYcr_bVeto","Resolved_DYcr_bTag"],
        } 
    },
}


DY_bins_ = []
for bin in range(1,6):
     DY_bins_.append("DY_bin"+str(bin))

for DYbin in DY_bins_:
    config[DYbin] = { 
        "nuisances" : [ "QCDscale_DY"], #"QCDscale_DY","CMS_PS_ISR","QCDscale_Wjets","CMS_PU_2018"
        "phase_spaces" : {
            "Resolved_bVeto" :  ["Resolved_DYcr_bVeto", "Resolved_SR_bVeto"],
            "Resolved_bTag" :    ["Resolved_DYcr_bTag", "Resolved_SR_bTag"],
        }
    }

