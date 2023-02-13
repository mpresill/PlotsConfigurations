## to do post-fit plots:


### *_Dec22 vesion:
Since we have two types of binning: one for 2016, and one for 2017 and 2018, we have two different macros:
> `postfit_loop_2016.sh` takes as inputs `sh postfit_loop_2016.sh date folder CATEGORY CUT VARIABLEtoPLOT`
> `postfit_loop_2017+2018.sh` (similar inputs) 
to launch these two scripts, use `launch_plotting.sh`, where you have to specify the various arguments corresponding to datacards epoch and category to plot.
Macros have been modified to allow normalization to bin width.

Note that the first plot you produce with these macros need to produce the `FitDiagnostic` output, meaning that specific lines in `postfit_loop_2016.sh` & `postfit_loop_2017+2018.sh` need t be uncommented.

Necessary plots for the analysis note:
> boosted b-veto
> boosted b-tag
> resolved b-veto
> resolved b-tag
in SR blind, DY cr, TOP cr.


