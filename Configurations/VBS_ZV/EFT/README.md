# Useful in EFT Latinos


## how to use Combine model for likelihood scans

Link to some useful slides with a discussion with Massiro: 
https://docs.google.com/presentation/d/1JaxtY-08P8fxv1QUr7J5rP73NWfhLUFYSFdrhRW-XBY/edit?usp=sharing 

Link to all instructions for inputs here: https://github.com/mpresill/AnalyticAnomalousCoupling/blob/master/README.md 

LHEReweighting weights maps:
 - reweighting weights 16 https://github.com/singh-ramanpreet/VBS-customNanoAODProduction/blob/main/NanoAODProduction/data/initrwgt_aQGC16.header#L154   
 - reweighting weights 16/17 https://github.com/singh-ramanpreet/VBS-customNanoAODProduction/blob/main/NanoAODProduction/data/initrwgt_aQGC17.header#L152 
 
 
Here is an example of samples.py:
 - define weights: https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/2016_Jul22/samples.py#L122-L125 
 - define samples (quad, and sm+lin+quad): https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/2016_Jul22/samples.py#L189-L218 

A new script is available to extract per-event weights for quadratic and linear and sm components from EFT samples directly from reweighting Madgraph card:
https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/EFT/ReweightFactory/readWCs.py 

____________________________________________________
## EFT2Obs, NanoAOD reweighting Tool

Links:
 - EFT2Obs tool: 
 - NanoAOD reweighting tool setup and example: https://github.com/Charlotte-Knight/nanoAOD-tools/blob/eventIDSkimming/READMEs/walkthrough.md 


Approximations tested so far:
- `MG2.6.7` version here vs. `MG2.6.5` used in UL SM samples generation
    - this should not be a problem since 2.6.7 is essentially identical, physics-wise
    - please note that for ReReco campaign the version should be MG2.4.X, so please check the `env.sh` and the other steps in EFT2Obs where it downloads madgraph (more instructions will follow at some point on this)
- on-shell decay of vector bosons (it's ok for semi-leptonic VBS analysis)
- modeL with no restrict cards (SMEFT), but for Eboli basis et Al. there should be no issue in just leading the correct model


## series of commands that I tested:

### EFT2Obs part:

0. set-up EFT2Obs tool (in a lxplus7 environment, no cmsenv - although it seems to work also in ETP machines):
    ```sh
    git clone https://github.com/ajgilbert/EFT2Obs.git
    cd EFT2Obs
    source env.sh

    ./scripts/setup_mg5.sh
    ./scripts/setup_rivet.sh
    ```

2. setup the model used for MC generation (default options are HEL and SMEFT)
    For Eboli basis need to re-adapt this step: https://github.com/ajgilbert/EFT2Obs#setup-models
    Hint: it should be pretty simple to clone the script for Eboli basis model and replace the path for the SMEFT example https://github.com/ajgilbert/EFT2Obs/blob/master/scripts/setup_model_SMEFTsim.sh#L10 with the most recent Eboli model https://feynrules.irmp.ucl.ac.be/attachment/wiki/AnomalousGaugeCoupling/quarticCKM21v2.tgz 
    Then launch the setup of this model:
    ```sh
    ./scripts/setup_model_YOUR_MODEL_SCRIPT.sh
    ```

1. create a folder containing the cards used for the process, using a Madgraph-standalone-like syntax.
   Here some care is needed to adapt the cards from CMS genproduction, e.g.:
    - replace ...

2. Setup the chosen 



```sh
./scripts/setup_process.sh WWjjTolnulnu_SS_ewk_dim6
```

### Prepare MG cards
Prepare MG cards: at the setup step it clones the existing cards in the `cads/process` folder, but we can modify reweighting card acconrdin to following config file. 
Prepare congif `.json` file coding the reweighting options used
```sh
python scripts/make_config.py -p WWjjTolnulnu_SS_ewk_dim6 -o config_WWjjTolnulnu_SS_ewk_dim6.json   \
--pars SMEFT:2,7,9,5,4,21,22,24,25,29,30,31,32,33,34 --def-val 0.01 --def-sm 0.0 --def-gen 0.0
```
Note the following SMEFT operators numbering scheme in the ouput:
    - [2] cw
    - [7] chw
    - [9] chwb
    - [5] chdd
    - [4] chbox
    - [21] chl1
    - [22] chl3
    - [24] chq1
    - [25] chq3
    - [29] cll
    - [30] cll1
    - [31] cqq1
    - [32] cqq11
    - [33] cqq3
    - [34] cqq31
Since the param card command in the following line does no work
```sh
python scripts/make_param_card.py -p zh-WWjjTolnulnu_SS_ewk_dim6 -c config_WWjjTolnulnu_SS_ewk_dim6.json \
-o cards/WWjjTolnulnu_SS_ewk_dim6/
```
we simply copy the existing default param_card.dat from `MG5_aMC_v2_6_7/WWjjTolnulnu_SS_ewk_dim6/Cards/` to `cards/WWjjTolnulnu_SS_ewk_dim6/`
Then we set up the reweighting card with the following command:
```sh
python scripts/make_reweight_card.py config_WWjjTolnulnu_SS_ewk_dim6.json cards/WWjjTolnulnu_SS_ewk_dim6/reweight_card.dat
```

### Make the gridpack (along with the reweighting module)
```sh 
./scripts/make_gridpack.sh WWjjTolnulnu_SS_ewk_dim6 1
```




### Reweighting Tool part: