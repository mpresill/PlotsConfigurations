# LIST OF UPDATES WRT TO CONFIG 2017_Apr22_v2-FJ-EFT:

> fixed xsections for signal samples (sm, EFT)
> kept only Transverse EFT operators
> added two sets of VBS EWK processes: "sm" (global recoil, for EFT limits), "sm_dipole" (dipole recoil, for EWK measurement)
> added LogNormal for Fakes shape uncertainties
> removed non-essential variables in "variables_reduced.py"

 (date: 12th Sept '22)

> updated training models (before we missed Prefiring weights in those trainings)

> Updated JET PU ID SF in nominal histograms: before we were erroneausly using 'PUJetIdSF' in nominal histos, but ‘Jet_PUIDSF_down’ (other implementation) for nuisances. NOW WE USE ONLY ONE! (FIXED changing nominal to ‘Jet_PUIDSF’ as it is very similar but should be computational less expensive and identical from physics p.o.v.) - same fixing happened for 2016. Checked that also other HWW-analyses use this easier implementation-