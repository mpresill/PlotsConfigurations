# LatinosToNumpy
Conversion from latinos to numpy for ML training

User guide: 
https://unimib-analyses.docs.cern.ch/ml_tutorial/numpy_extraction/

1. set up configurations similar to latinos', with some syntaxe differences detailed in the aforementionned link
2. Unfold samples with unfold.sh
3. Extract tp numpy with tonumpy.sh (DY is computationally hevy, better to run it separately


# DNN training
1. DNN_optimization.ipynb is used to optimize the hyperparameters of DNNs. Require Numpy files.
2. DNN_train.ipynb is used to train a model with given paameters (from previous step for example) and plot some training metrics
3. Dump_DNN.ipynb required for latinos integration. Be careful, while previous can use Tensorflow2, this step requires Tensorflow 1.x
4. Added trained models in case my eos gets reomved after the end of my contract

# Utilities
1. DY_2Dbinning.ipynb was used to optimize DY sample 2D binning
2. QGL.ipynb was used to devise purest qaurk/gluon regions for morphing
(qgl morphing is extracted via the run.sh macro in the VBS_ZV/qgl_X folders, where X corresponds to the year)
3. rateparams.py is used to extract optimal rateparams values from fit so they can be used as initialization 
