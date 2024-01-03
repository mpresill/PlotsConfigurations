# List of changes wrt older configs
# LIST OF UPDATES WRT TO CONFIG 2018_may23:

> This is the release started on 21 august 2023 - when unblinding procedure was starting.


## LIST OF UPDATES WRT TO CONFIG 2017-v0:
- minor backgrounds are gathered in the datacards
- PS weights for DY, Vg, VgS, top are computed with the old method 
    - we added PS_DY and PS_top nuisances computed with the latinos method to cross-check the validity of their extrapolation for these backgrounds
    [ ] add link here to validation plots: 
    [ ] add here link to validate "other" PS unceratainties:
    [ ] add here link to validate "other" QCDscale uncertainties: 
- JES/JER are not log normal anymore (and they are included for all processes)
- b-tagging nuisances are shape


__________________________________________________
# list of commands to make it work:
1. run mkShape, get to end, and hadd