
#!/bin/sh


BASEDIR=`pwd`/Remorphing
mkdir $BASEDIR
#No correction
./rdf_analyzer_morph_ptorder.o rootFile_12Jul2021_2018_qgltest/plots_VBS_ZV_12Jul2021_2018_qgltest.root Resolved_DYcr \
        ./output_histos_Resolved_DYcr_iter0.root  \
        0 A A A A A  A A A A 



mkdir $BASEDIR/output_Resolved_DYcr_iter0
#mkdir $BASEDIR/output_top_iter0

python extract_morphing.py --input output_histos_Resolved_DYcr_iter0.root \
                 --outputdir $BASEDIR/output_Resolved_DYcr_iter0 --outputfile morphing_gluon_iter0.root --jet-type gluon

python extract_morphing.py --input output_histos_Resolved_DYcr_iter0.root \
                 --outputdir $BASEDIR/output_Resolved_DYcr_iter0 --outputfile morphing_quark_iter0.root --jet-type quark
