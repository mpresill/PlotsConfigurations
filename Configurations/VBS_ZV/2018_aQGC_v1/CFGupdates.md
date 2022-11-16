# First attempt of sync for EFT combination
## Date 15November 2022.
This folder contains the first version of the sync for samples name and nuisances name with WV analysis for aQGC measurement.


# LIST OF UPDATES WRT TO CONFIG [2018_Jul22](https://github.com/mpresill/PlotsConfigurations/tree/matteo/Configurations/VBS_ZV/2018_Jul22):
Changes implemented: 
- [ ] updated samples name in boosted category according to [Irene's configs](https://github.com/IreneZoi/PlotsConfigurations/tree/VBSjjlnu_v7_aQGC/Configurations/VBSjjlnu/Full2018v7/conf_fit_v4.5_aQGC)
- [ ] QCDscale is fully correlated amongst linear, quadratic and SM "signals". Name convention ```Nuisance_signal```

# To-do-list:
- [ ] extend to resolved
- [ ] split PS_ISR and PS_FSR per samples, as is done by Davide 
- [ ] add more complex variables (like mjj+mZV) 
- [ ] test an additional signal region obtained cutting high in DNN variable


# Open questions:
- [ ] Does it make sense to truncate series to linear term? It would be an "inverse proxy" for dim-6 sensitivty