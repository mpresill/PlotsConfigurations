
#!/bin/sh


BASEDIR=`pwd`/Remorphing
mkdir $BASEDIR
#No correction
./rdf_analyzer_morph_ptorder.o rootFile_19Dec2021_2017_qgl/plots_VBS_ZV_19Dec2021_2017_qgl.root Resolved_DYcr \
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
hadd -f morphing_functions_step1.root output_Resolved_DYcr_iter0/morphing_gluon_iter0.root output_Resolved_DYcr_iter0/morphing_quark_iter0.root

cd ..
#first iteration: use purest regions corrections
./rdf_analyzer_morph_ptorder.o  rootFile_19Dec2021_2017_qgl/plots_VBS_ZV_19Dec2021_2017_qgl.root Resolved_DYcr \
         output_histos_Resolved_DYcr_iter1.root  \
         11111111 $BASEDIR/morphing_functions_step1.root \
         j3_loweta_pt0_gluon j3_loweta_pt0_gluon j3_loweta_pt0_gluon j3_loweta_pt0_gluon \
         j0_higheta_pt1_quark j0_higheta_pt1_quark  j0_higheta_pt1_quark j0_higheta_pt1_quark

mkdir $BASEDIR/output_Resolved_DYcr_iter1

python extract_morphing2.py --input output_histos_Resolved_DYcr_iter1.root \
                 --outputdir $BASEDIR/ --outputfile morphing_functions_step2.root --jet-type gluon

python compose_morph_function.py --file1 Remorphing/morphing_functions_step1.root --file2 Remorphing/morphing_functions_step2.root --outputdir Remorphing --outputfile morphing_functions_comb.root --func1 j3_loweta_pt0_gluon j3_loweta_pt0_gluon j3_loweta_pt0_gluon j3_loweta_pt0_gluon j0_higheta_pt1_quark j0_higheta_pt1_quark  j0_higheta_pt1_quark j0_higheta_pt1_quark --func2 _loweta_pt0_gluon _loweta_pt1_gluon _higheta_pt0_gluon _higheta_pt1_gluon _loweta_pt0_quark _loweta_pt1_quark _higheta_pt0_quark _higheta_pt1_quark --dostep2 11111111
