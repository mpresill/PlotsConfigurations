# LIST OF UPDATES WRT TO CONFIG 2016_Jul22:


>updated pdf for 2016 bkg to rms for bkgs and correlated to 17 and 18 for signals.
>updated PS parametrization, extrapolated from fiducial region 2018
>updated QCD scale for VBS QCD VV, extrapolated from fiducial region 2018 as Log-Normal
>dy rate parameters initialized to post-fit values

# LIST OF UPDATES WRT TO CONFIG 2018_Dec22:

> This is the release started on 22 may 2023 - latest to date.
> Modification to samples.py (both topologies):
    > removed `(Sum$(abs(GenPart_pdgId)==6)==0)` from ZZ_ewk signal (not needed here)
    > included both the tZq_ll bkg and the tZq obtained from `(Sum$(abs(GenPart_pdgId)==6)!=0)`(i.e. by reverting this cut)
    >changes on DY samples:
        > removed `DY_LO_pTllrw` and `DY_NLO_pTllrw`
        > removed  `DYJetsToLL_M-50_HT-70to100` and put the cut btw inclusive and HT-binned to `LHE_HT == 100`
        >removed all `DYJetsToLL_M-5to50_HT*`
        > split 'VZ' samples in 'VZ' and 'ZZlep', but we'll only use the ZZlep ones in the structure file - following ARC comments
        > removed 'WWG' from VVV samples as supposed to overlap with 'ggWW'