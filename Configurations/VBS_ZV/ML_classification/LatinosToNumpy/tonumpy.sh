#! /bin/bash

#source /cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/setup.sh
#try LCG97?

source /cvmfs/sft.cern.ch/lcg/views/LCG_97python3//x86_64-centos7-gcc8-opt/setup.sh



python latinoRDF_numpy_exporter.py\
  --config-dir ./2016_qgl\
  --cut preselection\
  --o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Numpy\
  --vers v1\
  --s  VBS_ZV VBS_VV_QCD top WJets WW Vg VgS ggWW VZ VVV tZq VBF-V\
  --debug --functions functions_qgl.hh 
#DY jobs can take too long, better to separate from the rest
python latinoRDF_numpy_exporter.py\
  --config-dir ./2016_qgl\
  --cut preselection\
  --o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Numpy\
  --vers v1\
  --s  DY\
  --debug --functions functions_qgl.hh

