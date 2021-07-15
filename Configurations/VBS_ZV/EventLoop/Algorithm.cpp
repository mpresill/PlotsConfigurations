#include "Algorithm.h"

Algorithm::Algorithm() {
}


void Algorithm::initialize(Data* data) {
    m_data = data;
}



void Algorithm::execute() {

    // apply selection. Exit if didn't pass
    if(!passedSelection()) return;

    // fill the plots
    fillPlots();
}



bool Algorithm::passedSelection()
{
    // select specific flavor combinations
    if (cut_SR && m_data->patElectron_pt->at(0)<150)
        return false;
    if (cut_dyCR && m_data->patElectron_pt->at(0)<100)
        return false;

    // passed all the cuts
    return true;
}


void Algorithm::fillPlots(){
    // here we fill the histograms. We protect the code against the empty pointers.
    if(h_pt_e1) h_pt_e1->Fill( m_data->patElectron_pt->at(0) );
}
