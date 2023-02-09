import os
from multiprocessing import Pool
import pwd
import sys 

tag = sys.argv[1]

#-E 
def hadd(sample):
    os.system("haddfast -C -j 10 /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_{0}_v2/plots_VBS_ZV_{0}_boosted_{1}.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_{0}/plots_VBS_ZV_{0}_boosted_ALL_{1}.*".format(tag, sample))    #step 1
#    os.system("haddfast -C -j 10 ../tmp/plots_VBS_ZV_{0}_{1}.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_{0}/plots_VBS_ZV_{0}_EFT_ALL_{1}.*".format(tag, sample))    #step 1
    #os.system("haddfast -C -j 12 plots_VBS_ZV_{0}.root plots_VBS_ZV_{0}_{1}.root".format(tag, sample))             #step 2
    #os.system("hadd -j 12 ../tmp/plots_VBS_ZV_{0}_{1}.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_{0}/plots_VBS_ZV_{0}_ALL_{1}*".format(tag, sample))

#def haddTOT(sample):
    


samples = ['VBS_VV_QCD','tZq','top','DATA','Fake','VVV','VZ','VgS','Vg','DY','VBF-V','ggWW','WW','WJets','quad_cT0','sm_lin_quad_cT0','quad_cT1','sm_lin_quad_cT1','quad_cT2','sm_lin_quad_cT2']
#samples = ['quad_cT0','sm_lin_quad_cT0','quad_cT1','sm_lin_quad_cT1','quad_cT2','sm_lin_quad_cT2']
#samples = ['quad_cM7','sm_lin_quad_cM7','quad_cM5','sm_lin_quad_cM5','quad_cM4','sm_lin_quad_cM4','quad_cM3','sm_lin_quad_cM3','quad_cM2','sm_lin_quad_cM2','quad_cM1','sm_lin_quad_cM1','quad_cM0','sm_lin_quad_cM0','quad_cS0','sm_lin_quad_cS0','quad_cS1','sm_lin_quad_cS1']
#samples = ['quad_cT2','sm_lin_quad_cT2','quad_cT5','sm_lin_quad_cT5','quad_cT6','sm_lin_quad_cT6','quad_cT7','sm_lin_quad_cT7','quad_cT8','sm_lin_quad_cT8','quad_cT9','sm_lin_quad_cT9']

p= Pool()

#for s in samples:
#    hadd(s)
p.map(hadd,samples)


    #   run it like:
    #   python hadd_manual_fast.py 9May2022_2016 
    #   python hadd_manual_fast.py 23May2022_2016 

