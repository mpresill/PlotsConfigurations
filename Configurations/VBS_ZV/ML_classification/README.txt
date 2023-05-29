##Steps for trainig the DNN and export back in latino framework

Instructions taken from: https://unimib-analyses.docs.cern.ch/ml_tutorial/config_preparation/ & https://github.com/mpresill/PlotsConfigurations/tree/alexandre/Configurations/VBS_ZV/Alexandre 
1. Data_preparation.ipynb
2. Training_VBS.ipynb
3. See here: https://unimib-analyses.docs.cern.ch/ml_tutorial/apply_latino/


### replicating Alexandre's workflow (May23)
Conversion from Latinos format to Numpy is included in the folder: LatinosToNumpy
Here is the procedure:
- set up configurations similar to latinos', with some syntaxe differences detailed in the various folders included here (and from Alexandre's example: )
    - Unfold samples with unfold.sh:
    `source unfold.sh` (produces a json file encoding samples list in the desired folder)
    - Setup the environment in a clean session, NOT in a CMSSW environment (no cmsenv).
    - Extract tp numpy with tonumpy.sh (DY is computationally hevy, better to run it separately):
    `sh tonumpy.sh` adapting the name of samples, path and cuts according to your needings
- doing other studies, like DY binning: 
    - use SWAN.ch, and select the correct ipynb
