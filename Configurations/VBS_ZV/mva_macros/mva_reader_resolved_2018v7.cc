#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"
#include "TGraph.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

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

  DoubleValueReader* category{};
  FloatArrayReader* Lepton_eta{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* CleanJet_pt{};
  FloatArrayReader* CleanJet_eta{};
  FloatValueReader* mll{};
  FloatArrayReader* CleanJet_phi{};
  DoubleValueReader* vbs_jet_0{};
  DoubleValueReader* vbs_jet_1{};
  DoubleValueReader* v_jet_0{};
  DoubleValueReader* v_jet_1{};
  FloatArrayReader* Jet_mass{};
  IntArrayReader* CleanJet_jetId{};

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
//  if ( *(VBS_category->Get()) != category_) {
 //   return -999.;
  //}
  int vbs_jet0_idx = *(vbs_jet_0->Get());
  int vbs_jet1_idx = *(vbs_jet_1->Get());
  int v_jet0_idx = *(v_jet_0->Get());
  int v_jet1_idx = *(v_jet_1->Get());
  TLorentzVector vbs_jet0;
  TLorentzVector vbs_jet1;
  TLorentzVector v_jet0;
  TLorentzVector v_jet1;

  vbs_jet0.SetPtEtaPhiM(CleanJet_pt->At(vbs_jet0_idx), CleanJet_eta->At(vbs_jet0_idx), CleanJet_phi->At(vbs_jet0_idx), Jet_mass->At(CleanJet_jetId->At(vbs_jet0_idx)));
  vbs_jet1.SetPtEtaPhiM(CleanJet_pt->At(vbs_jet1_idx), CleanJet_eta->At(vbs_jet1_idx), CleanJet_phi->At(vbs_jet1_idx), Jet_mass->At(CleanJet_jetId->At(vbs_jet1_idx)));
  vbs_jet0.SetPtEtaPhiM(CleanJet_pt->At(v_jet0_idx), CleanJet_eta->At(v_jet0_idx), CleanJet_phi->At(v_jet0_idx), Jet_mass->At(CleanJet_jetId->At(v_jet0_idx)));
  vbs_jet0.SetPtEtaPhiM(CleanJet_pt->At(v_jet1_idx), CleanJet_eta->At(v_jet1_idx), CleanJet_phi->At(v_jet1_idx), Jet_mass->At(CleanJet_jetId->At(v_jet1_idx)));

  float mean_eta_vbs = TMath::Abs(CleanJet_eta->At(vbs_jet0_idx) + CleanJet_eta->At(vbs_jet1_idx))*0.5;
  float detajj =TMath::Abs(CleanJet_eta->At(vbs_jet0_idx) - CleanJet_eta->At(vbs_jet1_idx)) ;
  float mjj =(vbs_jet0 + vbs_jet1).M() ;
  float V_mass =(v_jet0 + v_jet1).M() ;
  float Zlep_1 = (Lepton_eta->At(0) - mean_eta_vbs) / detajj;
  float Zlep_2 = (Lepton_eta->At(1) - mean_eta_vbs) / detajj;
  std::vector<float> input{};


  input.push_back( (Lepton_pt->At(0) ));//pt1
  input.push_back( (Lepton_pt->At(1) ));//pt2
  input.push_back( (Lepton_eta->At(0) ));//#eta1
  input.push_back( (Lepton_eta->At(1) ));//#eta2
  input.push_back( *(mll->Get()) );
  input.push_back(Zlep_1);
  input.push_back(Zlep_2);
  input.push_back(vbs_jet0.Pt());
  input.push_back(vbs_jet1.Pt());
  input.push_back(vbs_jet0.Eta());
  input.push_back(vbs_jet1.Eta());
  input.push_back(v_jet0.Pt());
  input.push_back(v_jet1.Pt());
  input.push_back(v_jet0.Eta());
  input.push_back(v_jet1.Eta());
  input.push_back(mjj);
  input.push_back(detajj);
  input.push_back(V_mass);
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

  _library.bindBranch(category, "vbs_category");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(mll, "mll");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(vbs_jet_0, "vbs_jet_0");
  _library.bindBranch(vbs_jet_1, "vbs_jet_1");
  _library.bindBranch(v_jet_0, "v_jet_0");
  _library.bindBranch(v_jet_1, "v_jet_1");
  _library.bindBranch(Jet_mass, "Jet_mass");
  _library.bindBranch(CleanJet_jetId, "CleanJet_jetIdx");


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
