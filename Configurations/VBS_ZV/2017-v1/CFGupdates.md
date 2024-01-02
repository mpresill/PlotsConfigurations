# List of changes wrt older configs
## LIST OF UPDATES WRT TO CONFIG 2018_may23:

> This is the release started on 22 August 23 - when unblinding was proposed.
> Changes wrt may23 release:
    > removed PS nuisances modeling and tried to use the standard weights
    > eventually will extrapolate it from 2017 for buggy samples

## LIST OF UPDATES WRT TO CONFIG 2017-v0:
- minor backgrounds are gathered in the datacards
- PS weights for DY, Vg, VgS, top are computed with the old method 
- JES/JER are not log normal anymore (and they are included for all processes)
- b-tagging nuisances are shape


__________________________________________________
# list of commands to make it work:
1. run mkShape, get to end, and hadd
