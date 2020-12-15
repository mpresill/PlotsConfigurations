#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"

#include <cmath>
#include <string>
#include <iostream>

using namespace std;
using namespace NNEvaluation;

#ifndef MVAREADERResolved_v70_H
#define MVAREADERResolved_v70_H

typedef TTreeReaderValue<Double_t> DoubleValueReader;

class MVAReaderResolved_v70 : public multidraw::TTreeFunction {
public:
  
  MVAReaderResolved_v70(const char* model_path, bool verbose, int category);

  char const* getName() const override { return "MVAReaderResolved_v70"; }
  TTreeFunction* clone() const override { return new MVAReaderResolved_v70(model_path_.c_str(), verbose, category_); }

  std::string model_path_;
  int category_;
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:  
 
  bool verbose;
  void bindTree_(multidraw::FunctionLibrary&) override;
  
  DNNEvaluator* dnn_tensorflow;


  FloatValueReader* mll{};
  //DoubleValueReader* Zlep_1{};
  //DoubleValueReader* Zlep_2{};
  //DoubleValueReader* vbs_jet_pt1{};
  //DoubleValueReader* vbs_jet_pt2{};
  //DoubleValueReader* vbs_jet_eta1{};
  //DoubleValueReader* vbs_jet_eta2{};
  //DoubleValueReader* V_jet_pt1{};
  //DoubleValueReader* V_jet_pt2{};
  //DoubleValueReader* V_jet_eta1{};
  //DoubleValueReader* V_jet_eta2{};
  DoubleValueReader* mjj_max{};
  DoubleValueReader* detajj_mjjmax{};
  DoubleValueReader* V_jet_mass{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  DoubleValueReader* vbs_jet_0{};
  DoubleValueReader* vbs_jet_1{};
  FloatArrayReader* CleanJet_pt{};
  FloatArrayReader* CleanJet_eta{};
  DoubleValueReader* v_jet_0{};
  DoubleValueReader* v_jet_1{};
  DoubleValueReader* vbs_category{};
  //  IntValueReader* VBS_category{};
  //  FloatArrayReader* Lepton_pt{};
  //  FloatArrayReader* Lepton_eta{};
  //  FloatValueReader* vjet_0_pt{};
  //  FloatValueReader* vjet_1_pt{};
  //  FloatValueReader* vjet_0_eta{};
  //  FloatValueReader* vjet_1_eta{};
  //  FloatValueReader* deltaeta_vbs{};
  //  FloatValueReader* deltaphi_vbs{};
  //  FloatValueReader* vbs_0_pt{};
  //  FloatValueReader* vbs_1_pt{};
  //  FloatValueReader* vbs_0_eta{};
  //  FloatValueReader* vbs_1_eta{};
  //  FloatValueReader* mjj_vbs{};
  //  IntArrayReader* Lepton_flavour{};
};


MVAReaderResolved_v70::MVAReaderResolved_v70(const char* model_path, bool verbose, int category):
    model_path_(model_path), 
    verbose(verbose),
    category_(category)
{
    dnn_tensorflow = new DNNEvaluator(model_path_, verbose);
}


double
MVAReaderResolved_v70::evaluate(unsigned)
{
  // Run only if 
int category = (int)  *(vbs_category->Get());
if ( category != 1) {
    return -999.;
  }else{
  int vbs_jet1 = (int) *(vbs_jet_0->Get()) ;
  int vbs_jet2 = (int) *(vbs_jet_1->Get()) ;
  int v_jet1 = (int) *(v_jet_0->Get()) ;
  int v_jet2 = (int) *(v_jet_1->Get()) ;
  float Zlep_1 = (Lepton_eta->At(0))-0.5*((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2))) / *(detajj_mjjmax->Get());
  float Zlep_2 = (Lepton_eta->At(1))-0.5*((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2))) / *(detajj_mjjmax->Get());


 std::vector<float> input{};


  input.push_back( (Lepton_pt->At(0)) );
  input.push_back( (Lepton_pt->At(1)));
  input.push_back( (Lepton_eta->At(0)));
  input.push_back( (Lepton_eta->At(1)));
  input.push_back( *(mll->Get()) );
  input.push_back( Zlep_1 );
  input.push_back( Zlep_2 );
  //input.push_back( *(vbs_jet_pt1->Get()) );
  //input.push_back( *(vbs_jet_pt2->Get()) );
  //input.push_back( *(vbs_jet_eta1->Get()) );
  //input.push_back( *(vbs_jet_eta2->Get()) );
  //input.push_back( (CleanJet_pt->At(vbs_jet_0)) );
  //input.push_back( (CleanJet_pt->At(vbs_jet_1)) );
  //input.push_back( (CleanJet_eta->At(vbs_jet_0)) );
  //input.push_back( (CleanJet_eta->At(vbs_jet_1)) );
  input.push_back( (CleanJet_pt -> At(vbs_jet1)) );
  input.push_back( (CleanJet_pt -> At(vbs_jet2)) );
  input.push_back( (CleanJet_eta -> At(vbs_jet1)) );
  input.push_back( (CleanJet_eta -> At(vbs_jet2)) );
//input.push_back( *(V_jet_pt1->Get()) );
  //input.push_back( *(V_jet_pt2->Get()) );
  //input.push_back( *(V_jet_eta1->Get()) );
  //input.push_back( *(V_jet_eta2->Get()) );
  //input.push_back( (CleanJet_pt->At(v_jet_0)) );
  //input.push_back( (CleanJet_pt->At(v_jet_1)) );
  //input.push_back( (CleanJet_eta->At(v_jet_0)) );
  //input.push_back( (CleanJet_eta->At(v_jet_1)) );
  input.push_back( (CleanJet_pt -> At(v_jet1)) );
  input.push_back( (CleanJet_pt -> At(v_jet2)) );
  input.push_back( (CleanJet_eta -> At(v_jet1)) );
  input.push_back( (CleanJet_eta -> At(v_jet2)) );  
  input.push_back( *(mjj_max->Get()) );
  input.push_back( *(detajj_mjjmax->Get()) );
  input.push_back( *(V_jet_mass->Get()) );

  //input.push_back( *(mjj_vbs->Get()) );
  //input.push_back( *(vbs_0_pt->Get()) );
  //input.push_back( *(vbs_1_pt->Get()) );
  //input.push_back( *(deltaeta_vbs->Get()) );
  //input.push_back( *(deltaphi_vbs->Get()) );
  //input.push_back( *(vjet_0_pt->Get()) );
  //input.push_back( *(vjet_1_pt->Get()) );
  //input.push_back( *(vjet_0_eta->Get()) );
  //input.push_back( *(vjet_1_eta->Get()) );
  //input.push_back( Lepton_pt->At(0) );
  //input.push_back( TMath::Abs(Lepton_eta->At(0)) );
  //input.push_back( TMath::Abs((float)Lepton_flavour->At(0) ));

  return dnn_tensorflow->analyze(input);
 }  
}

void
MVAReaderResolved_v70::bindTree_(multidraw::FunctionLibrary& _library)
{  
 // _library.bindBranch(VBS_category, "VBS_category");
 // _library.bindBranch(mjj_vbs, "mjj_vbs");
 // _library.bindBranch(vbs_0_pt, "vbs_0_pt");
 // _library.bindBranch(vbs_1_pt, "vbs_1_pt");
 // _library.bindBranch(deltaeta_vbs, "deltaeta_vbs");
 // _library.bindBranch(deltaphi_vbs, "deltaphi_vbs");
 // _library.bindBranch(vjet_0_pt, "vjet_0_pt");
 // _library.bindBranch(vjet_1_pt, "vjet_1_pt");
 // _library.bindBranch(vjet_0_eta, "vjet_0_eta");
 // _library.bindBranch(vjet_1_eta, "vjet_1_eta");
 // _library.bindBranch(Lepton_pt, "Lepton_pt");
 // _library.bindBranch(Lepton_eta, "Lepton_eta");
 // _library.bindBranch(Lepton_flavour, "Lepton_pdgId");

  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(mll, "mll");
  //_library.bindBranch(Zlep_1, "Zlep_1");
  //_library.bindBranch(Zlep_2, "Zlep_2");
  //_library.bindBranch(vbs_jet_pt1, "vbs_jet_pt1");
  //_library.bindBranch(vbs_jet_pt2, "vbs_jet_pt2");
  //_library.bindBranch(vbs_jet_eta1, "vbs_jet_eta1");
  //_library.bindBranch(vbs_jet_eta2, "vbs_jet_eta2");
  //_library.bindBranch(V_jet_pt1, "V_jet_pt1");
  //_library.bindBranch(V_jet_pt2, "V_jet_pt2");
  //_library.bindBranch(V_jet_eta1, "V_jet_eta1");
  //_library.bindBranch(V_jet_eta2, "V_jet_eta2");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(vbs_jet_0, "vbs_jet_0");
  _library.bindBranch(vbs_jet_1, "vbs_jet_1");
  _library.bindBranch(v_jet_0, "v_jet_0");
  _library.bindBranch(v_jet_1, "v_jet_1");
  _library.bindBranch(mjj_max, "mjj_max");
  _library.bindBranch(detajj_mjjmax, "detajj_mjjmax");
  _library.bindBranch(V_jet_mass, "V_jet_mass");
  _library.bindBranch(vbs_category, "vbs_category");

  // _library.addDestructorCallback([&]() {
  //       VBS_category = nullptr;
  //       mjj_vbs = nullptr;
  //       vbs_0_pt = nullptr;
  //       vbs_1_pt = nullptr;
  //       deltaeta_vbs = nullptr;
  //       deltaphi_vbs = nullptr;
  //       vjet_0_eta= nullptr;
  //       vjet_1_eta = nullptr;
  //       vjet_0_pt = nullptr;
  //       vjet_1_pt = nullptr;
  //       Lepton_pt = nullptr;
  //       Lepton_eta = nullptr;
  //       Lepton_flavour = nullptr;
  //       delete dnn_tensorflow;
  //     });
}


#endif 
