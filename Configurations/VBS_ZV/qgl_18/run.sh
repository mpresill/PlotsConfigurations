
#!/bin/sh


BASEDIR=`pwd`/Remorphing
mkdir $BASEDIR
#No correction
./rdf_analyzer_morph_ptorder.o rootFile_12Jul2021_2018_qgltest/plots_VBS_ZV_12Jul2021_2018_qgltest.root Resolved_DYcr \
        ./output_histos_Resolved_DYcr_iter0.root  \
        0 A A A A A  A A A A 


#./scripts/QGL_morphing/rdf_analyzer_morph_ptorder.o ../rootFile_test_qgl_tree/plots_test_qgl_tree.root res_topcr  \
#        $BASEDIR/output_histos_topcr_iter0.root \
#        0 A A A A A A A A A 

mkdir $BASEDIR/output_Resolved_DYcr_iter0
#mkdir $BASEDIR/output_top_iter0

python extract_morphing.py --input output_histos_Resolved_DYcr_iter0.root \
                 --outputdir $BASEDIR/output_Resolved_DYcr_iter0 --outputfile morphing_gluon_iter0.root --jet-type gluon

python extract_morphing.py --input output_histos_Resolved_DYcr_iter0.root \
                 --outputdir $BASEDIR/output_Resolved_DYcr_iter0 --outputfile morphing_quark_iter0.root --jet-type quark

cd $BASEDIR
hadd -f morphing_functions_iter0.root output_Resolved_DYcr_iter0/morphing_gluon_iter0.root output_Resolved_DYcr_iter0/morphing_quark_iter0.root

cd ..
#first iteration: use purest regions corrections
./rdf_analyzer_morph_ptorder.o rootFile_12Jul2021_2018_qgltest/plots_VBS_ZV_12Jul2021_2018_qgltest.root Resolved_DYcr \
         output_histos_Resolved_DYcr_iter1.root  \
         11111111 $BASEDIR/morphing_functions_iter0.root \
         j3_loweta_pt0_gluon j3_loweta_pt0_gluon j3_loweta_pt0_gluon j3_loweta_pt0_gluon \
         j0_higheta_pt1_quark j0_higheta_pt1_quark  j0_higheta_pt1_quark j0_higheta_pt1_quark
"""
mkdir $BASEDIR/output_Resolved_DYcr_iter1

python extract_morphing.py --input output_histos_Resolved_DYcr_iter1.root \
                 --outputdir $BASEDIR/output_Resolved_DYcr_iter1 --outputfile morphing_gluon_iter1.root --jet-type gluon

python extract_morphing.py --input output_histos_Resolved_DYcr_iter1.root \
                 --outputdir $BASEDIR/output_Resolved_DYcr_iter1 --outputfile morphing_quark_iter1.root --jet-type quark

cd $BASEDIR
hadd -f morphing_functions_iter1_tmp.root output_Resolved_DYcr_iter1/morphing_gluon_iter1.root output_Resolved_DYcr_iter1/morphing_quark_iter1.root


python ../prepare_morphing_functions_file.py \
                 --inputs morphing_functions_iter0.root morphing_functions_iter1_tmp.root \
                 --outputfile morphing_functions_iter1.root \
                 --func1 j3_loweta_pt0_gluon  j3_loweta_pt1_gluon   j0_higheta_pt0_quark j0_higheta_pt1_quark \
                 --func2 j1_higheta_pt0_gluon j1_higheta_pt1_gluon  j1_loweta_pt0_quark j1_loweta_pt1_quark  
 cd ..
"""
