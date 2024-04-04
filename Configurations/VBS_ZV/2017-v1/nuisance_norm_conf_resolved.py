config = {
    "top" :
     { 
        "nuisances" : [ "QCDscale_top"],#"CMS_PS_FSR","CMS_PS_ISR",#"CMS_PU_2017"
        "phase_spaces" : {
            "Resolved" :  ["Resolved_topcr", "Resolved_SR_bVeto","Resolved_SR_bTag","Resolved_DYcr_bVeto","Resolved_DYcr_bTag"],
        } 
    },

}


###         uncomment for resolved DY 
DY_bins_res = []
for bin in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
    DY_bins_res.append("DY_Resolved_2d_"+bin)

for DYbin in DY_bins_res:
    config[DYbin] = { 
        "nuisances" : [ "QCDscale_DY"], #,"CMS_PS_ISR","QCDscale_Wjets","CMS_PU_2018"
        "phase_spaces" : {
            "Resolved_bVeto" :  ["Resolved_DYcr_bVeto", "Resolved_SR_bVeto"],
            "Resolved_bTag" :    ["Resolved_DYcr_bTag", "Resolved_SR_bTag"],
        }
    }

