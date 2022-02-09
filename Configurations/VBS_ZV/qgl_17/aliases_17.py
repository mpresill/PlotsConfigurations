import os
pmpormorphed_res'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_qgl.cc+' % configurations
    ],
    'class': 'jets_cat_qgl',
    'args': ('vbs_0_qglmorphed_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}


aliases['vbs_1_qglmorphed_res'] =  {
'class': 'jets_cat_qgl',
    'args': ('vbs_1_qglmorphed_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}

aliases['vjet_0_qglmorphed_res'] = {
'class': 'jets_cat_qgl',
    'args': ('vjet_0_qglmorphed_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}
aliases['vjet_1_qglmorphed_res'] = {
'class': 'jets_cat_qgl',
    'args': ('vjet_1_qglmorphed_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}
aliases['vbs_0_qgl_res'] =  {
'class': 'jets_cat_qgl',
    'args': ('vbs_0_qgl_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}

aliases['vbs_1_qgl_res'] =  {
'class': 'jets_cat_qgl',
    'args': ('vbs_1_qgl_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}

aliases['vjet_0_qgl_res'] = {
'class': 'jets_cat_qgl',
    'args': ('vjet_0_qgl_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}
aliases['vjet_1_qgl_res'] = {
'class': 'jets_cat_qgl',
    'args': ('vjet_1_qgl_res','2017', models_path, models_path_pruned,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
}

"""


