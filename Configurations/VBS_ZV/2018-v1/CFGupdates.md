# List of changes wrt older configs
# LIST OF UPDATES WRT TO CONFIG 2018_may23:

> This is the release started on 21 august 2023 - when unblinding procedure was starting.


## LIST OF UPDATES WRT TO CONFIG 2017-v0:
- minor backgrounds are gathered in the datacards
- PS weights for DY, Vg, VgS, top are computed with the old method 
    - we added PS_DY and PS_top nuisances computed with the latinos method to cross-check the validity of their extrapolation for these backgrounds
    [x] add link here to validation plots: https://mpresill.web.cern.ch/mpresill/VBS/nuisances/PS_ISR_comparison/6Dec2023_2018/?match=latinos 
    Not a good a approximation for DY. `PS_ISR_latinos` are commented for datacard making and thus for 2018 we will extrapolate `PS` for DY from 2018.
    [x] add here link to validate "other" PS unceratainties: https://mpresill.web.cern.ch/mpresill/VBS/nuisances/PS_ISR/6Dec2023_2018/ https://mpresill.web.cern.ch/mpresill/VBS/nuisances/PS_FSR/6Dec2023_2018/ : some fluctuations, but overall OK!
    [x] add here link to validate "other" QCDscale uncertainties: https://mpresill.web.cern.ch/mpresill/VBS/nuisances/QCDscale/6Dec2023_2018/ OK!
- JES/JER are not log normal anymore (and they are included for all processes)
- b-tagging nuisances are shape


__________________________________________________
# list of commands to make it work:
1. 
2. backup the file produced
```sh
cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted_copy.root

cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved_copy.root
```

3. a. (ONLY ONCE) 
    extract PS weights 
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved.root -o PS-plots_VBS_ZV_6Dec2023_2018_resolved.root -sf samples_PS_extraction.txt -cf cuts_PS_extraction.txt -v ALL -n PS_ISR PS_FSR
```
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted.root -o PS-plots_VBS_ZV_6Dec2023_2018_boosted.root -sf samples_PS_extraction.txt -cf cuts_PS_extraction.txt -v ALL -n PS_ISR PS_FSR
```
    extract QCDscale_VBS_VV_QCD
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved.root -o QCDscale-plots_VBS_ZV_6Dec2023_2018_resolved.root -s VBS_VV_QCD -cf cuts_PS_extraction.txt -v ALL -n QCDscale_VBS_VV_QCD
```
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted.root -o QCDscale-plots_VBS_ZV_6Dec2023_2018_boosted.root -s VBS_VV_QCD -cf cuts_PS_extraction.txt -v ALL -n QCDscale_VBS_VV_QCD
```

3. b. patch for QCD scale DY process:
```sh
sh QCDnorm_datacards.sh _6Dec2023_2018 resolved 2018-v1
sh QCDnorm_datacards.sh _6Dec2023_2018 boosted 2018-v1
```


4. make datacards:
```sh
mkDatacards.py --pycfg=configuration.py --inputFile=plots_VBS_ZV_6Dec2023_2018_resolved.root --skipMissingNuisance 
    
mkDatacards.py --pycfg=configuration.py --inputFile=plots_VBS_ZV_6Dec2023_2018_boosted.root --skipMissingNuisance
```

5. do the statistical analysis (check combine2018 or combineRun2 folder)