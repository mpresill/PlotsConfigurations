/*
This macrol computes the AK4 jets categorization in the VBS event:   
    - the category of the event (1FJ, 0FJ or more than 1FJ)
    - mjj as the maximum of all the AK4 jets couples masses
    - their detajj
    - the indices of these VBS-jets
    - in the resolved case (4jets and no FJ), the inv mass of the other two jets (Vjets_mass)
Note that according to the definition in ll. 147, 149 we use the CleanJetNotFat indecing 
*/


#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "NNEvaluation/DNNTensorflow/interface/DNNEvaluator.hh"

#include "TMath.h"
#include "TGraph.h"
#include "TFile.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

#include <typeinfo>
#include <cmath>
#include <string>
#include <unordered_map>
#include <iostream>
#include <stdexcept>
#include <tuple>

using namespace std;
using namespace NNEvaluation;

namespace multidraw {
  extern thread_local TTree* currentTree;
}

// --- functions Helper

float deltaEtaqglFJ(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}

float deltaPhiqglFJ(float phi1, float phi2){
  float PHI = std::abs(phi1-phi2);
  if (PHI<=3.14159265)
    return PHI;
  else
    return 2*3.14159265-PHI;
}

int isRunningSample(TString targetSample){
  TString currentSampleName = TString(multidraw::currentTree->GetCurrentFile()->GetName());
  if ( currentSampleName.Contains(targetSample)) {
      return 1;
  }
  else return 0;
}


class jets_cat_qgl_FJ : public multidraw::TTreeFunction {
public:
  jets_cat_qgl_FJ( char const* _type, const char* year, const char* model_dir_pruned_bVeto, const char* model_dir_pruned_bReq,bool verbose, const char * morph_file,  const char * do_morph,
                    const char * morph_loweta_gluon_pt0, const char * morph_loweta_gluon_pt1,
                    const char * morph_higheta_gluon_pt0, const char * morph_higheta_gluon_pt1,
                    const char * morph_loweta_quark_pt0, const char * morph_loweta_quark_pt1, 
                    const char * morph_higheta_quark_pt0, const char * morph_higheta_quark_pt1);
  jets_cat_qgl_FJ( unsigned type, const char* year, const char* model_dir_pruned_bVeto, const char* model_dir_pruned_bReq,bool verbose, const char * file, const char * do_morph,
                    const char * morph_loweta_gluon_pt0, const char * morph_loweta_gluon_pt1,
                    const char * morph_higheta_gluon_pt0, const char * morph_higheta_gluon_pt1,
                    const char * morph_loweta_quark_pt0, const char * morph_loweta_quark_pt1, 
                    const char * morph_higheta_quark_pt0, const char * morph_higheta_quark_pt1);

  char const* getName() const override { return "jets_cat_qgl_FJ"; }
  TTreeFunction* clone() const override { return new jets_cat_qgl_FJ(returnVar_,year_.c_str(), model_dir_pruned_bVeto_.c_str(), model_dir_pruned_bReq_.c_str(),  verbose, morph_file_.c_str(), do_morph_.c_str(),
                                                morph_loweta_gluon_pt0_.c_str(), morph_loweta_gluon_pt1_.c_str(),
                                                morph_higheta_gluon_pt0_.c_str(),morph_higheta_gluon_pt1_.c_str(),
                                                morph_loweta_quark_pt0_.c_str(),morph_loweta_quark_pt1_.c_str(),
                                                morph_higheta_quark_pt0_.c_str(),morph_higheta_quark_pt1_.c_str()) ; }
  
  std::string model_dir_pruned_bVeto_;
  std::string model_dir_pruned_bReq_;
  

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  bool verbose;
  
  DNNEvaluator* dnn_tensorflow_boosted_pruned_bVeto;
  DNNEvaluator* dnn_tensorflow_resolved_pruned_bVeto;
  DNNEvaluator* dnn_tensorflow_boosted_pruned_bReq;
  DNNEvaluator* dnn_tensorflow_resolved_pruned_bReq;
  enum ReturnType {
    vbs_category, 
    vbs_jet_0,
    vbs_jet_1, 
    v_jet_0,
    v_jet_1,
    mjj_max, 
    detajj_mjjmax, 
    dphijj_mjjmax,
    Vjet_mass,
    njet30,
    nbtag,
    Zleppt,
    Vpt,
    dnn_output_pruned_bVeto,
    dnn_output_pruned_bReq,
    vbs_0_qgl_res,
    vbs_1_qgl_res,
    vjet_0_qgl_res,
    vjet_1_qgl_res, 
    vbs_0_qgl_boost,
     vbs_1_qgl_boost, 
    vbs_0_qglmorphed_res,
    vbs_1_qglmorphed_res, 
    vjet_0_qglmorphed_res, 
    vjet_1_qglmorphed_res, 
    vbs_0_qglmorphed_boost, 
    vbs_1_qglmorphed_boost, 
    vbs_0_partfl_res, 
    vbs_1_partfl_res, 
    vjet_0_partfl_res, 
    vjet_1_partfl_res, 
    vbs_0_partfl_boost, 
    vbs_1_partfl_boost,
    nVarTypes
  };
  
 
  void bindTree_(multidraw::FunctionLibrary&) override;

  unsigned returnVar_{nVarTypes};
  

  UIntValueReader* run{};
  UIntValueReader* luminosityBlock{};
  ULong64ValueReader* event{}; 

  static string year_;
  //static bool verbose;
  //static string model_dir_;
  static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;

  //qgl morphing variables
  string morph_file_;
  string do_morph_;
  static bool do_morph_gluon_loweta_pt0;
  static bool do_morph_gluon_loweta_pt1;
  static bool do_morph_gluon_higheta_pt0;
  static bool do_morph_gluon_higheta_pt1;
  static bool do_morph_quark_loweta_pt0;
  static bool do_morph_quark_loweta_pt1;
  static bool do_morph_quark_higheta_pt0;
  static bool do_morph_quark_higheta_pt1;
  string morph_higheta_gluon_pt0_;
  string morph_loweta_gluon_pt0_;
  string morph_higheta_quark_pt0_;
  string morph_loweta_quark_pt0_;
  string morph_higheta_gluon_pt1_;
  string morph_loweta_gluon_pt1_;
  string morph_higheta_quark_pt1_;
  string morph_loweta_quark_pt1_;
  static std::map<std::string, TGraph*> morphing_functions;
  
  static bool isRunningOnData;


  
  static UIntValueReader* nFatJet; 
  static FloatArrayReader* FatJet_pt;
  static FloatArrayReader* FatJet_eta;
  static FloatArrayReader* FatJet_phi;
  static FloatArrayReader* FatJet_mass;
  static FloatArrayReader* Jet_qgl;
  static IntArrayReader* Jet_partonFlavour;

  static IntArrayReader* CleanJet_jetId;
  static IntArrayReader* CleanFatJet_jetId;
  static IntArrayReader* CleanJetNotFat_jetId;
  static FloatArrayReader* Jet_mass;
  static UIntValueReader* nCleanJetNotFat;
  static FloatArrayReader* CleanJet_pt;
  static FloatArrayReader* CleanJet_eta;
  static FloatArrayReader* CleanJet_phi;
  static FloatArrayReader* Lepton_pt;
  static FloatArrayReader* Lepton_eta;
  static FloatArrayReader* Lepton_phi;
  static UIntValueReader* nLepton;
  static FloatValueReader*  mll;
  static FloatArrayReader*  Jet_btagDeepB;
  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
  static float getMorphedGluon(float x, float eta, float pt);
  static float getMorphedQuark(float x, float eta, float pt);
};

std::tuple<UInt_t, UInt_t, ULong64_t> jets_cat_qgl_FJ::currentEvent{};

UIntValueReader* jets_cat_qgl_FJ::nFatJet{}; 
FloatArrayReader* jets_cat_qgl_FJ::FatJet_pt{};
FloatArrayReader* jets_cat_qgl_FJ::FatJet_eta{};
FloatArrayReader* jets_cat_qgl_FJ::FatJet_phi{};
FloatArrayReader* jets_cat_qgl_FJ::FatJet_mass{};
FloatArrayReader* jets_cat_qgl_FJ::Jet_qgl{};
IntArrayReader* jets_cat_qgl_FJ::Jet_partonFlavour{};
std::map<std::string, TGraph*> jets_cat_qgl_FJ::morphing_functions{};
bool jets_cat_qgl_FJ::isRunningOnData{false};
bool jets_cat_qgl_FJ::do_morph_gluon_loweta_pt0{false};
bool jets_cat_qgl_FJ::do_morph_gluon_higheta_pt0{false};
bool jets_cat_qgl_FJ::do_morph_quark_loweta_pt0{false};
bool jets_cat_qgl_FJ::do_morph_quark_higheta_pt0{false};
bool jets_cat_qgl_FJ::do_morph_gluon_loweta_pt1{false};
bool jets_cat_qgl_FJ::do_morph_gluon_higheta_pt1{false};
bool jets_cat_qgl_FJ::do_morph_quark_loweta_pt1{false};
bool jets_cat_qgl_FJ::do_morph_quark_higheta_pt1{false};


IntArrayReader*   jets_cat_qgl_FJ::CleanJet_jetId{};
IntArrayReader*   jets_cat_qgl_FJ::CleanFatJet_jetId{};
IntArrayReader*   jets_cat_qgl_FJ::CleanJetNotFat_jetId{};
FloatArrayReader* jets_cat_qgl_FJ::Jet_mass{};
UIntValueReader*  jets_cat_qgl_FJ::nCleanJetNotFat; 
FloatArrayReader* jets_cat_qgl_FJ::CleanJet_pt{};
FloatArrayReader* jets_cat_qgl_FJ::CleanJet_eta{};
FloatArrayReader* jets_cat_qgl_FJ::CleanJet_phi{};
FloatArrayReader* jets_cat_qgl_FJ::Lepton_pt{};
FloatArrayReader* jets_cat_qgl_FJ::Lepton_eta{};
FloatArrayReader* jets_cat_qgl_FJ::Lepton_phi{};
UIntValueReader* jets_cat_qgl_FJ::nLepton;
FloatValueReader*  jets_cat_qgl_FJ::mll{};
FloatArrayReader* jets_cat_qgl_FJ::Jet_btagDeepB{};

string jets_cat_qgl_FJ::year_{};
//string jets_cat_qgl_FJ::model_dir_{};
//bool jets_cat_qgl_FJ::verbose{};

std::array<double, jets_cat_qgl_FJ::nVarTypes> jets_cat_qgl_FJ::returnValues{};


// function Helper ---


jets_cat_qgl_FJ::jets_cat_qgl_FJ( char const* _type, const char* year, const char* model_dir_pruned_bVeto, const char* model_dir_pruned_bReq,  bool verbose,   const char * morph_file, const char * do_morph,
                    const char * morph_loweta_gluon_pt0, const char * morph_loweta_gluon_pt1,
                    const char * morph_higheta_gluon_pt0, const char * morph_higheta_gluon_pt1,
                    const char * morph_loweta_quark_pt0, const char * morph_loweta_quark_pt1, 
                    const char * morph_higheta_quark_pt0, const char * morph_higheta_quark_pt1):
   TTreeFunction(), model_dir_pruned_bVeto_(model_dir_pruned_bVeto), model_dir_pruned_bReq_(model_dir_pruned_bReq),  verbose(verbose), morph_file_(morph_file),  do_morph_(do_morph),
  morph_loweta_gluon_pt0_(morph_loweta_gluon_pt0),morph_loweta_gluon_pt1_(morph_loweta_gluon_pt1),
  morph_higheta_gluon_pt0_(morph_higheta_gluon_pt0),morph_higheta_gluon_pt1_(morph_higheta_gluon_pt1),
  morph_loweta_quark_pt0_(morph_loweta_quark_pt0),morph_loweta_quark_pt1_(morph_loweta_quark_pt1),
  morph_higheta_quark_pt0_(morph_higheta_quark_pt0),morph_higheta_quark_pt1_(morph_higheta_quark_pt1){
   // cout << "1" << endl;  
    std::string type(_type);
    if (type ==  "vbs_category")
      returnVar_ = vbs_category;
    else if (type ==  "vbs_jet_0")
      returnVar_ = vbs_jet_0;
    else if (type == "vbs_jet_1")
      returnVar_ = vbs_jet_1;
    else if (type ==  "v_jet_0")
      returnVar_ = v_jet_0;
    else if (type == "v_jet_1")
      returnVar_ = v_jet_1;
    else if (type == "Vjet_mass")
      returnVar_ = Vjet_mass;
    else if (type == "mjj_max")
      returnVar_ = mjj_max;
    else if (type == "detajj_mjjmax")
      returnVar_ = detajj_mjjmax;
    else if (type == "dphijj_mjjmax")
      returnVar_ = dphijj_mjjmax;
    else if (type == "njet30")
      returnVar_ = njet30;
    else if (type == "nbtag")
      returnVar_ = nbtag;
    else if (type== "Zleppt")
      returnVar_ = Zleppt;
    else if (type== "Vpt")
      returnVar_ = Vpt;
    else if (type == "dnn_output_pruned_bVeto")
      returnVar_ = dnn_output_pruned_bVeto;
    else if (type == "dnn_output_pruned_bReq")
      returnVar_ = dnn_output_pruned_bReq;
    else  if (type ==  "vbs_0_qgl_res")
    returnVar_ = vbs_0_qgl_res;
    else if (type == "vbs_1_qgl_res")
        returnVar_ = vbs_1_qgl_res;
    else if (type == "vjet_0_qgl_res")
        returnVar_ = vjet_0_qgl_res;
    else if (type == "vjet_1_qgl_res")
        returnVar_ = vjet_1_qgl_res;
    else if (type == "vbs_0_qgl_boost")
        returnVar_ = vbs_0_qgl_boost;
    else if (type == "vbs_1_qgl_boost")
        returnVar_ = vbs_1_qgl_boost;
    
    else if (type ==  "vbs_0_qglmorphed_res")
        returnVar_ = vbs_0_qglmorphed_res;
    else if (type == "vbs_1_qglmorphed_res")
        returnVar_ = vbs_1_qglmorphed_res;
    else if (type == "vjet_0_qglmorphed_res")
        returnVar_ = vjet_0_qglmorphed_res;
    else if (type == "vjet_1_qglmorphed_res")
        returnVar_ = vjet_1_qglmorphed_res;
    else if (type == "vbs_0_qglmorphed_boost")
        returnVar_ = vbs_0_qglmorphed_boost;
    else if (type == "vbs_1_qglmorphed_boost")
        returnVar_ = vbs_1_qglmorphed_boost;
    
    else if (type ==  "vbs_0_partfl_res")
        returnVar_ = vbs_0_partfl_res;
    else if (type == "vbs_1_partfl_res")
        returnVar_ = vbs_1_partfl_res;
    else if (type == "vjet_0_partfl_res")
        returnVar_ = vjet_0_partfl_res;
    else if (type == "vjet_1_partfl_res")
        returnVar_ = vjet_1_partfl_res;
    else if (type == "vbs_0_partfl_boost")
        returnVar_ = vbs_0_partfl_boost;
    else if (type == "vbs_1_partfl_boost")
        returnVar_ = vbs_1_partfl_boost;
    else
      throw std::runtime_error("unknown return type " + type);
    jets_cat_qgl_FJ::year_ = year;
    // jets_cat_qgl_FJ::model_dir_ = model_dir;
    // jets_cat_qgl_FJ::verbose = verbose;
    int do_morph_flags = std::stoi(do_morph_,0,2);
    jets_cat_qgl_FJ::do_morph_gluon_loweta_pt0 = do_morph_flags & 1;
    jets_cat_qgl_FJ::do_morph_gluon_loweta_pt1 = do_morph_flags >>1 & 1;
    jets_cat_qgl_FJ::do_morph_gluon_higheta_pt0 = do_morph_flags >> 2 & 1;
    jets_cat_qgl_FJ::do_morph_gluon_higheta_pt1 = do_morph_flags >> 3 & 1;
    jets_cat_qgl_FJ::do_morph_quark_loweta_pt0 = do_morph_flags >> 4 & 1;
    jets_cat_qgl_FJ::do_morph_quark_loweta_pt1 = do_morph_flags >> 5 & 1;
    jets_cat_qgl_FJ::do_morph_quark_higheta_pt0 = do_morph_flags >> 6 & 1;
    jets_cat_qgl_FJ::do_morph_quark_higheta_pt1 = do_morph_flags >> 7 & 1;
    
    TFile rfile {morph_file, "READ"};
    jets_cat_qgl_FJ::morphing_functions["gluon_loweta_pt0"] = (TGraph*) rfile.Get(morph_loweta_gluon_pt0);
    jets_cat_qgl_FJ::morphing_functions["gluon_loweta_pt1"] = (TGraph*) rfile.Get(morph_loweta_gluon_pt1);
    jets_cat_qgl_FJ::morphing_functions["gluon_higheta_pt0"] = (TGraph*) rfile.Get(morph_higheta_gluon_pt0);
    jets_cat_qgl_FJ::morphing_functions["gluon_higheta_pt1"] = (TGraph*) rfile.Get(morph_higheta_gluon_pt1);
    jets_cat_qgl_FJ::morphing_functions["quark_loweta_pt0"] = (TGraph*) rfile.Get(morph_loweta_quark_pt0);
    jets_cat_qgl_FJ::morphing_functions["quark_loweta_pt1"] = (TGraph*) rfile.Get(morph_loweta_quark_pt1);
    jets_cat_qgl_FJ::morphing_functions["quark_higheta_pt0"] = (TGraph*) rfile.Get(morph_higheta_quark_pt0);
    jets_cat_qgl_FJ::morphing_functions["quark_higheta_pt1"] = (TGraph*) rfile.Get(morph_higheta_quark_pt1);
    rfile.Close();
}

jets_cat_qgl_FJ::jets_cat_qgl_FJ( unsigned type, const char* year, const char* model_dir_pruned_bVeto, const char* model_dir_pruned_bReq,  bool verbose,const char * morph_file, const char * do_morph,
                    const char * morph_loweta_gluon_pt0, const char * morph_loweta_gluon_pt1,
                    const char * morph_higheta_gluon_pt0, const char * morph_higheta_gluon_pt1,
                    const char * morph_loweta_quark_pt0, const char * morph_loweta_quark_pt1, 
                    const char * morph_higheta_quark_pt0, const char * morph_higheta_quark_pt1 ):
TTreeFunction(), returnVar_(type), 
model_dir_pruned_bVeto_(model_dir_pruned_bVeto), model_dir_pruned_bReq_(model_dir_pruned_bReq), verbose(verbose),morph_file_(morph_file),  do_morph_(do_morph),
  morph_loweta_gluon_pt0_(morph_loweta_gluon_pt0),morph_loweta_gluon_pt1_(morph_loweta_gluon_pt1),
  morph_higheta_gluon_pt0_(morph_higheta_gluon_pt0),morph_higheta_gluon_pt1_(morph_higheta_gluon_pt1),
  morph_loweta_quark_pt0_(morph_loweta_quark_pt0),morph_loweta_quark_pt1_(morph_loweta_quark_pt1),
  morph_higheta_quark_pt0_(morph_higheta_quark_pt0),morph_higheta_quark_pt1_(morph_higheta_quark_pt1){
  //cout << "2" <<endl;
  jets_cat_qgl_FJ::year_ = year;
  //jets_cat_qgl_FJ::model_dir_ = model_dir;
  //jets_cat_qgl_FJ::verbose = verbose  std::string boosted_path_pruned_bVeto_ = model_dir_pruned_bVeto_ + "/Boosted/";
  dnn_tensorflow_boosted_pruned_bVeto = new DNNEvaluator(boosted_path_pruned_bVeto_, verbose);
  std::string resolved_path_pruned_bVeto_ = model_dir_pruned_bVeto_ + "/Resolved/";
  dnn_tensorflow_resolved_pruned_bVeto = new DNNEvaluator(resolved_path_pruned_bVeto_, verbose);

  std::string boosted_path_pruned_bReq_ = model_dir_pruned_bReq_ + "/Boosted/";
  dnn_tensorflow_boosted_pruned_bReq = new DNNEvaluator(boosted_path_pruned_bReq_, verbose);
  std::string resolved_path_pruned_bReq_ = model_dir_pruned_bReq_ + "/Resolved/";
  dnn_tensorflow_resolved_pruned_bReq = new DNNEvaluator(resolved_path_pruned_bReq_, verbose);


int do_morph_flags = std::stoi(do_morph_,0,2);
jets_cat_qgl_FJ::do_morph_gluon_loweta_pt0 = do_morph_flags & 1;
jets_cat_qgl_FJ::do_morph_gluon_loweta_pt1 = do_morph_flags >>1 & 1;
jets_cat_qgl_FJ::do_morph_gluon_higheta_pt0 = do_morph_flags >> 2 & 1;
jets_cat_qgl_FJ::do_morph_gluon_higheta_pt1 = do_morph_flags >> 3 & 1;
jets_cat_qgl_FJ::do_morph_quark_loweta_pt0 = do_morph_flags >> 4 & 1;
jets_cat_qgl_FJ::do_morph_quark_loweta_pt1 = do_morph_flags >> 5 & 1;
jets_cat_qgl_FJ::do_morph_quark_higheta_pt0 = do_morph_flags >> 6 & 1;
jets_cat_qgl_FJ::do_morph_quark_higheta_pt1 = do_morph_flags >> 7 & 1;

TFile rfile {morph_file, "READ"};
jets_cat_qgl_FJ::morphing_functions["gluon_loweta_pt0"] = (TGraph*) rfile.Get(morph_loweta_gluon_pt0);
jets_cat_qgl_FJ::morphing_functions["gluon_loweta_pt1"] = (TGraph*) rfile.Get(morph_loweta_gluon_pt1);
jets_cat_qgl_FJ::morphing_functions["gluon_higheta_pt0"] = (TGraph*) rfile.Get(morph_higheta_gluon_pt0);
jets_cat_qgl_FJ::morphing_functions["gluon_higheta_pt1"] = (TGraph*) rfile.Get(morph_higheta_gluon_pt1);
jets_cat_qgl_FJ::morphing_functions["quark_loweta_pt0"] = (TGraph*) rfile.Get(morph_loweta_quark_pt0);
jets_cat_qgl_FJ::morphing_functions["quark_loweta_pt1"] = (TGraph*) rfile.Get(morph_loweta_quark_pt1);
jets_cat_qgl_FJ::morphing_functions["quark_higheta_pt0"] = (TGraph*) rfile.Get(morph_higheta_quark_pt0);
jets_cat_qgl_FJ::morphing_functions["quark_higheta_pt1"] = (TGraph*) rfile.Get(morph_higheta_quark_pt1);
rfile.Close();
}


double
jets_cat_qgl_FJ::evaluate(unsigned)
{ 
  //cout << "evaluate event " << *event->Get()<< endl;
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());

  //if returnVar_ = dnnoutput, run dnn
  //cout << "evaluate event " << *event->Get()<< endl;
  int category = (int) returnValues[vbs_category];
  int vbs_jet1 = (int) returnValues[vbs_jet_0];
  int vbs_jet2 = (int) returnValues[vbs_jet_1];
  int v_jet1 = (int) returnValues[v_jet_0];
  int v_jet2 = (int) returnValues[v_jet_1];
  float Vjetmass = (float) returnValues[Vjet_mass];
  float mjj = (float) returnValues[mjj_max];
  float detajj = (float)returnValues[detajj_mjjmax];
  int njet30 = (int)returnValues[njet30];
  float dphijj = (float)returnValues[dphijj_mjjmax];
  int btag = (int)returnValues[nbtag];
  //if (nbtag >0) {//cout << "nbtag DNN = " << nbtag << endl;}
  
////////////DNNoutput_pruned bVeto///////////////////////////////////////////
  if (returnVar_ == dnn_output_pruned_bVeto){
  //Boosted

  //carefull, inputs must be in same order than in scaler.txt
  if (category ==0 ){
          //cout <<"event "<<*event->Get()<<  " : Boosted  "<<returnValues[vbs_category]<<" vbs1 : " << vbs_jet1 << " vbs2: "<< vbs_jet2 <<  endl;
  //    cout << "boosted pruned morphed" << endl;
      float Zlep_1 = ((Lepton_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zlep_2 = ((Lepton_eta->At(1)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zvjet = ((FatJet_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      std::vector<float> input{};
     
      input.push_back((Lepton_pt->At(0)));
      //input.push_back((Lepton_pt->At(1)));
      input.push_back((Lepton_eta->At(0)));
      input.push_back((Lepton_eta->At(1)));
      //input.push_back(*(mll->Get()));
      input.push_back((FatJet_pt->At(CleanFatJet_jetId->At(0))));
      input.push_back((FatJet_eta->At(0)));
      input.push_back(Zlep_1);
      input.push_back(Zlep_2);
      //input.push_back((CleanJet_pt->At(vbs_jet1)));
      input.push_back((CleanJet_pt->At(vbs_jet2)));
      //input.push_back((CleanJet_eta->At(vbs_jet1)));
      input.push_back((CleanJet_eta->At(vbs_jet2)));
      input.push_back(mjj);
      input.push_back(detajj);
      input.push_back(dphijj);
      input.push_back(njet30);
      input.push_back(Zvjet);
      //input.push_back(vbs_0_qgl_morphed);
      //input.push_back((vbs_1_qgl_morphed);

      returnValues[dnn_output_pruned_bVeto]= dnn_tensorflow_boosted_pruned_bVeto->analyze(input);
	
//Resolved
   }else if (category == 1){ 
    //cout <<"event "<<*event->Get()<<  " : Resolved  "<<" vbs1 : " << vbs_jet1 << " vbs2: "<< vbs_jet2 <<" v1 : " << v_jet1 << " v2: "<< v_jet2 <<  endl;
//	cout << "resolved pruned morphed" <<endl;
      float Zlep_1 = ((Lepton_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zlep_2 = ((Lepton_eta->At(1)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float vbs_0_qgl_morphed = (float)returnValues[vbs_0_qglmorphed_res];
      float vbs_1_qgl_morphed =(float)returnValues[vbs_1_qglmorphed_res];
      float v_0_qgl_morphed =(float)returnValues[vjet_0_qglmorphed_res];
      float v_1_qgl_morphed =(float)returnValues[vjet_1_qglmorphed_res];


        std::vector<float> input{};

        input.push_back(Zlep_1);
        input.push_back(Zlep_2);
        input.push_back((CleanJet_pt -> At(vbs_jet2)));
        input.push_back( (CleanJet_pt -> At(v_jet1)) );
	input.push_back( (CleanJet_pt -> At(v_jet2)) );
        input.push_back( (CleanJet_eta -> At(v_jet1)) );
        input.push_back( (CleanJet_eta -> At(v_jet2)) );
	input.push_back(mjj);
	input.push_back(detajj);
	input.push_back(njet30);
	input.push_back(dphijj);
	input.push_back( Vjetmass);
        input.push_back(v_0_qgl_morphed);
        input.push_back(v_1_qgl_morphed);

       returnValues[dnn_output_pruned_bVeto]= dnn_tensorflow_resolved_pruned_bVeto->analyze(input);

     }
  }else if (returnVar_ == dnn_output_pruned_bReq){
//Boosted

  if (category ==0 ){
          //cout <<"event "<<*event->Get()<<  " : Boosted  "<<returnValues[vbs_category]<<" vbs1 : " << vbs_jet1 << " vbs2: "<< vbs_jet2 <<  endl;
  //    cout << "boosted full morphed" <<endl;
      float Zlep_1 = ((Lepton_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zlep_2 = ((Lepton_eta->At(1)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zvjet = ((FatJet_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      std::vector<float> input{};

      input.push_back((Lepton_pt->At(0)));
     // input.push_back((Lepton_pt->At(1)));
      //input.push_back((Lepton_eta->At(0)));
      //input.push_back((Lepton_eta->At(1)));
      //input.push_back(*(mll->Get()));
      input.push_back((FatJet_pt->At(CleanFatJet_jetId->At(0))));
      input.push_back((FatJet_eta->At(0)));
      input.push_back(Zlep_1);
      input.push_back(Zlep_2);
      //input.push_back((CleanJet_pt->At(vbs_jet1)));
      input.push_back((CleanJet_pt->At(vbs_jet2)));
      input.push_back((CleanJet_eta->At(vbs_jet1)));
      input.push_back((CleanJet_eta->At(vbs_jet2)));
      input.push_back(mjj);
      input.push_back(detajj);
      //input.push_back(dphijj);
      input.push_back(njet30);
      input.push_back(Zvjet);
      //input.push_back((Jet_qgl->At(CleanJet_jetId->At(vbs_jet1))));
      //input.push_back((Jet_qgl->At(CleanJet_jetId->At(vbs_jet2))));
      input.push_back(btag);

      returnValues[dnn_output_pruned_bReq]= dnn_tensorflow_boosted_pruned_bReq->analyze(input);

//Resolved
  }else if (category == 1){
    //cout <<"event "<<*event->Get()<<  " : Resolved  "<<" vbs1 : " << vbs_jet1 << " vbs2: "<< vbs_jet2 <<" v1 : " << v_jet1 << " v2: "<< v_jet2 <<  endl;
//      cout << "resolved full morphed" <<endl;
      float Zlep_1 = ((Lepton_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zlep_2 = ((Lepton_eta->At(1)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float vbs_0_qgl_morphed = returnValues[vbs_0_qglmorphed_res];
      float vbs_1_qgl_morphed =returnValues[vbs_1_qglmorphed_res];
      float v_0_qgl_morphed =returnValues[vjet_0_qglmorphed_res];
      float v_1_qgl_morphed =returnValues[vjet_1_qglmorphed_res];

        std::vector<float> input{};


        input.push_back( (Lepton_pt->At(0)) );
        //input.push_back( (Lepton_pt->At(1)));
        //input.push_back( (Lepton_eta->At(0)));
        //input.push_back( (Lepton_eta->At(1)));
        input.push_back( *(mll->Get()) );
        input.push_back( Zlep_1 );
        input.push_back( Zlep_2 );
        //input.push_back( (CleanJet_pt -> At(vbs_jet1)) );
        input.push_back( (CleanJet_pt -> At(vbs_jet2)) );
        //input.push_back( (CleanJet_eta -> At(vbs_jet1)) );
        //input.push_back( (CleanJet_eta -> At(vbs_jet2)) );
        input.push_back( (CleanJet_pt -> At(v_jet1)) );
        input.push_back( (CleanJet_pt -> At(v_jet2)) );
        input.push_back( (CleanJet_eta -> At(v_jet1)) );
        input.push_back( (CleanJet_eta -> At(v_jet2)) );
        input.push_back( mjj);
        input.push_back( detajj);
        input.push_back(dphijj);
        input.push_back( Vjetmass);
        input.push_back(njet30);
        //input.push_back(vbs_0_qgl_morphed);
        //input.push_back(vbs_1_qgl_morphed);
        input.push_back(v_0_qgl_morphed);
        //input.push_back(v_1_qgl_morphed);
        //input.push_back(btag);
        returnValues[dnn_output_pruned_bReq]= dnn_tensorflow_resolved_pruned_bReq->analyze(input);

    
      }
  }   
  return returnValues[returnVar_];
}

void
jets_cat_qgl_FJ::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nFatJet, "nCleanFatJet");
    _library.bindBranch(FatJet_pt, "FatJet_pt_nom"); //CleanFatJet_pt updated to FatJet_pt_nom, reference passed to cleanfat jet collection
    _library.bindBranch(FatJet_eta, "CleanFatJet_eta");
    _library.bindBranch(FatJet_phi, "CleanFatJet_phi");
    _library.bindBranch(FatJet_mass, "FatJet_msoftdrop_nom"); //CleanFatJet_mass updated to FatJet_msoftdrop_nom, reference passed to cleanfat jet collectio
    _library.bindBranch(Jet_qgl, "Jet_qgl");


    _library.bindBranch(CleanJetNotFat_jetId, "CleanJetNotFat_jetIdx");
    _library.bindBranch(CleanJet_jetId, "CleanJet_jetIdx");
    _library.bindBranch(CleanFatJet_jetId, "CleanFatJet_jetIdx");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(nCleanJetNotFat, "nCleanJetNotFat");
    _library.bindBranch(CleanJet_pt, "CleanJet_pt");
    _library.bindBranch(CleanJet_eta, "CleanJet_eta");
    _library.bindBranch(CleanJet_phi, "CleanJet_phi");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(mll, "mll");
    _library.bindBranch(Jet_btagDeepB, "Jet_btagDeepB");
    jets_cat_qgl_FJ::isRunningOnData = isRunningSample("Run");
    if (!jets_cat_qgl_FJ::isRunningOnData){
      //exclude Data and fakes
       _library.bindBranch(Jet_partonFlavour, "Jet_partonFlavour");
    }
    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {

                                     nFatJet = nullptr;
                                     FatJet_pt = nullptr;
                                     FatJet_eta = nullptr;
                                     FatJet_phi = nullptr;
                                     FatJet_mass = nullptr;
                                     Jet_qgl = nullptr;
                                     nCleanJetNotFat = nullptr;
                                     CleanJet_pt = nullptr;
                                     CleanJet_eta = nullptr;
                                     CleanJet_phi = nullptr;
                                     Jet_mass = nullptr;
                                     CleanJet_jetId = nullptr;
                                     CleanFatJet_jetId = nullptr;
                                     CleanJetNotFat_jetId = nullptr;
                                     Lepton_pt = nullptr;
                                     Lepton_eta = nullptr;
				     Lepton_phi = nullptr;
                                     nLepton = nullptr;
				     mll = nullptr;
                                     Jet_btagDeepB = nullptr;
                                     Jet_partonFlavour =nullptr;
                                    morphing_functions.clear();
                                   });
}

/*static*/
void
jets_cat_qgl_FJ::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{ //cout << "Set values event :" << _event <<endl;

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;
  //cout << "event :" << _event <<endl;
  currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

  //first part: compute the mjj_max of all the AK4 (CleanedNotFat)
  float Mjj_tmp=0;
  float Mjj_max=0;
  float deltamass_Vjet=1e5;
  float detajj_mjj_max=0;
  float dphijj_mjj_max=0;
  float Vjet_mass_max = 0.;
  unsigned int njet{*nCleanJetNotFat->Get()};
  unsigned int nFJ{*nFatJet->Get()};
  unsigned int nLep{*nLepton->Get()};
  // Index in the collection of CleanJetNotFat
  int VBS_jets[2] = {999,999};
  int V_jets[2]   = {999,999};
  int category = 999;  // 0 fatjet, 1 resolved, -1 none
  float pt_cut = 30;
  int _nbtag = 0;
  float btag_cut = 0.;
  std::vector<int> vectors_id;
  float _Zleppt =0.;
  float _Vpt = 0.;
  returnValues[Vpt]=-999;
  returnValues[Zleppt] = -999;

  //default qgl morph returns
returnValues[vbs_0_qgl_boost] = -1;
returnValues[vbs_1_qgl_boost] = -1;
returnValues[vbs_0_qgl_res] = -1;
returnValues[vbs_1_qgl_res] = -1;
returnValues[vjet_0_qgl_res] = -1;
returnValues[vjet_1_qgl_res] = -1;

returnValues[vbs_0_qglmorphed_boost] = -1;
returnValues[vbs_1_qglmorphed_boost] = -1;
returnValues[vbs_0_qglmorphed_res] = -1;
returnValues[vbs_1_qglmorphed_res] = -1;
returnValues[vjet_0_qglmorphed_res] = -1;
returnValues[vjet_1_qglmorphed_res] = -1;

returnValues[vbs_0_partfl_boost] = 0;
returnValues[vbs_1_partfl_boost] = 0;
returnValues[vbs_0_partfl_res] = 0;
returnValues[vbs_1_partfl_res] = 0;
returnValues[vjet_0_partfl_res] = 0;
returnValues[vjet_1_partfl_res] = 0;
  //cout <<  returnValues[Zleppt] << endl;
  //calculate leptonic Z pt
  if (nLep == 2) {
	//cout << " 2 Leptons " << endl;
  	TLorentzVector lep0;
  	TLorentzVector lep1;
  	lep0.SetPtEtaPhiM(Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0);
  	lep1.SetPtEtaPhiM(Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0);
  	_Zleppt = (lep0+lep1).Pt();
  	//cout << _Zleppt <<endl;
  }

  //btag cut values
  //cout << jets_cat_qgl_FJ::year_ <<endl;
  if (jets_cat_qgl_FJ::year_ == "2018") btag_cut=0.1241;
  else if (jets_cat_qgl_FJ::year_ == "2017") btag_cut = 0.1522;
  else if (jets_cat_qgl_FJ::year_ == "2016") btag_cut = 0.2217;
  //cout << btag_cut <<endl;
  // Load all the quadrivectors for performance reason
  std::vector<TLorentzVector> vectors; 
  for (unsigned int ijet=0 ; ijet<njet ; ijet++){
    TLorentzVector jet0; 
    jet0.SetPtEtaPhiM(CleanJet_pt->At(CleanJetNotFat_jetId->At(ijet)), CleanJet_eta->At(CleanJetNotFat_jetId->At(ijet)),
                      CleanJet_phi->At(CleanJetNotFat_jetId->At(ijet)),Jet_mass->At(CleanJet_jetId->At(CleanJetNotFat_jetId->At(ijet)))); 
    if(jet0.Pt()>pt_cut){
        vectors.push_back(jet0);
        vectors_id.push_back(ijet);
        if(Jet_btagDeepB->At(CleanJet_jetId->At(CleanJetNotFat_jetId->At(ijet)))>=btag_cut && std::abs(jet0.Eta())<2.5){
            _nbtag ++;
            }
        } 
    }

  njet=vectors.size();

  if (njet>=2){
        // Calculate max mjj invariant pair on CleanJetNotFat to exclude the correct jets
        for (unsigned int ijet=0 ; ijet<(njet-1) ; ijet++){
            for (unsigned int jjet= ijet+1 ; jjet<njet ; jjet++){
                if (ijet==jjet) continue; //useless?
         

                TLorentzVector jet0 = vectors.at(ijet);
                TLorentzVector jet1 = vectors.at(jjet); 

                Mjj_tmp = (jet0 + jet1).M();
                
                if( Mjj_tmp >= Mjj_max ){
                    Mjj_max=Mjj_tmp;
                    detajj_mjj_max=deltaEtaqgl((vectors.at(ijet)).Eta(),(vectors.at(jjet)).Eta());
                    dphijj_mjj_max=deltaPhiqgl((vectors.at(ijet)).Phi(),(vectors.at(jjet)).Phi());
                    // Index in vectors
                    VBS_jets[0]= ijet;
                    VBS_jets[1]= jjet;
                    int vbs_jet_0 =CleanJetNotFat_jetId->At(vectors_id.at(VBS_jets[0]));
                    int vbs_jet_1 =CleanJetNotFat_jetId->At(vectors_id.at(VBS_jets[1]));
                }
            }
        }

        // Now we have the njets
        // Check if boosted
        if (nFJ >= 1){
            //cout << "Boosted" << endl;
            category = 0;
            Vjet_mass_max = FatJet_mass->At(0);
	        _Vpt = FatJet_pt->At(0);  //does it need to be the first FatJet?

            //qgl morph
            
            returnValues[vbs_0_qgl_boost] = Jet_qgl->At(CleanJet_jetId->At(vbs_jet_0));
            returnValues[vbs_1_qgl_boost] = Jet_qgl->At(CleanJet_jetId->At(vbs_jet_1));
            returnValues[vbs_0_qgl_res] = -1;
            returnValues[vbs_1_qgl_res] = -1;
            returnValues[vjet_0_qgl_res] = -1;
            returnValues[vjet_1_qgl_res] = -1;

            if (!jets_cat_qgl_FJ::isRunningOnData){
                returnValues[vbs_0_partfl_boost] = Jet_partonFlavour->At(CleanJet_jetId->At(vbs_jet_0));
                returnValues[vbs_1_partfl_boost] = Jet_partonFlavour->At(CleanJet_jetId->At(vbs_jet_1));
                returnValues[vbs_0_partfl_res] = 0;
                returnValues[vbs_1_partfl_res] = 0;
                returnValues[vjet_0_partfl_res] = 0;
                returnValues[vjet_1_partfl_res] = 0;
                returnValues[vbs_0_qglmorphed_boost] = returnValues[vbs_0_partfl_boost]==21 ?  
                                                          getMorphedGluon(returnValues[vbs_0_qgl_boost], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)) : 
                                                          getMorphedQuark(returnValues[vbs_0_qgl_boost], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0));
                returnValues[vbs_1_qglmorphed_boost] = returnValues[vbs_1_partfl_boost]==21 ?  
                                                          getMorphedGluon(returnValues[vbs_1_qgl_boost], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)):  
                                                          getMorphedQuark(returnValues[vbs_1_qgl_boost], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1));
                returnValues[vbs_0_qglmorphed_res] = -1;
                returnValues[vbs_1_qglmorphed_res] = -1;
                returnValues[vjet_0_qglmorphed_res] = -1;
                returnValues[vjet_1_qglmorphed_res] = -1;


            }else{

                returnValues[vbs_0_partfl_boost] = 0;
                returnValues[vbs_1_partfl_boost] = 0;
                returnValues[vbs_0_partfl_res] = 0;
                returnValues[vbs_1_partfl_res] = 0;
                returnValues[vjet_0_partfl_res] = 0;
                returnValues[vjet_1_partfl_res] = 0;

                returnValues[vbs_0_qglmorphed_boost] = returnValues[vbs_0_qgl_boost];
                returnValues[vbs_1_qglmorphed_boost] = returnValues[vbs_1_qgl_boost];
                returnValues[vbs_0_qglmorphed_res] = -1;
                returnValues[vbs_1_qglmorphed_res] = -1;
                returnValues[vjet_0_qglmorphed_res] = -1;
                returnValues[vjet_1_qglmorphed_res] = -1;
            }
                

        }else if (njet>=4) { 
            category = 1;
	    int v_jet_0 =999;
            int v_jet_1 =999;
            //cout << "resolved " << endl;
           // cout << "vbs1 "<< VBS_jets[0] <<" vbs2 "<< VBS_jets[1]<< endl;
            for (unsigned int ijet=0 ; ijet<(njet-1) ; ijet++){
                if (ijet == VBS_jets[0] || ijet == VBS_jets[1]) continue;
                else for (unsigned int jjet= ijet+1 ; jjet<njet ; jjet++){
                    if ( VBS_jets[0] == jjet || VBS_jets[1] == jjet) continue;
                    else{
                       // cout <<"potential Vjets: "<<ijet<<jjet<<endl;
                        TLorentzVector jet0 = vectors.at(ijet);
                        TLorentzVector jet1 = vectors.at(jjet); 
                        float mvjet = (jet0+jet1).M();
                        float dmass = abs( mvjet - 85.7863 );
                        if (dmass < deltamass_Vjet){
                            // Index in the collection of vectors
                            V_jets[0] = ijet;
                            V_jets[1] = jjet;
                            v_jet_0 =CleanJetNotFat_jetId->At(vectors_id.at(V_jets[0]));
                            v_jet_1 =CleanJetNotFat_jetId->At(vectors_id.at(V_jets[1]));
			    //cout << "v_jet_1"<< v_jet_1 <<endl;
                            deltamass_Vjet = dmass;
                            Vjet_mass_max = mvjet;
			    _Vpt=(jet0+jet1).Pt();
                        }
                    }
                }
            }
	    //cout << "isrunningondata" << jets_cat_qgl_FJ::isRunningOnData <<endl;
	    //cout << "vectors size " << vectors.size() <<endl;
            //cout << "vectors_id.size " << vectors_id.size() <<endl;
	    //cout << "ncleanjet" << endl;
	    //cout << "V_jets[1] " << V_jets[1] <<endl;
	    //cout << "vectors_id.at(V_jets[1]) " << vectors_id.at(V_jets[1]) << endl;
	    //cout << "v_jet_1"<< v_jet_1 <<endl;
	    //cout << "v_jet_1 =CleanJetNotFat_jetId->At(vectors_id.at(V_jets[1])) " << CleanJetNotFat_jetId->At(vectors_id.at(V_jets[1])) << endl;
	    //cout << "v_jet_1"<< v_jet_1 <<endl;
	    //cout << "Vjet 2 cleanJet jet Idx" << CleanJet_jetId->At(v_jet_1 ) << endl;

            //Resolved morph qgl
            returnValues[vbs_0_qgl_boost] = -1;
            returnValues[vbs_1_qgl_boost] = -1;
            returnValues[vbs_0_qgl_res] = Jet_qgl->At(CleanJet_jetId->At(vbs_jet_0));
            //cout << "vbs 1 " << returnValues[vbs_0_qgl_res]<< endl;
	     //   cout << "Vbs 1 index" << vbs_jet_0<< endl;
            //cout << "Vbs 1 cleanJet jet Idx" << CleanJet_jetId->At(vbs_jet_0) << endl;
            //cout << "Vbs1 qgl" << Jet_qgl->At(CleanJet_jetId->At(vbs_jet_0)) << endl;
	    //cout << "vectors size " << vectors.size() <<endl;
	    //cout << "vectors_id.size " << vectors_id.size() <<endl;
            returnValues[vbs_1_qgl_res] = Jet_qgl->At(CleanJet_jetId->At(vbs_jet_1));
            //cout << "vbs 1 qgl " << returnValues[vbs_1_qgl_res]<< endl;
            //cout << "Vjet 2 index" << v_jet_1<< endl;
	    //cout << "v_jet_1"<< v_jet_1 <<endl;
            //cout << "Vjet 2 cleanJet jet Idx" << CleanJet_jetId->At(v_jet_1 ) << endl;
            //cout << "vjet2 pf"<< Jet_partonFlavour->At(CleanJet_jetId->At(v_jet_1 ))<<endl;
	    //cout << "Vjet2 qgl" << Jet_qgl->At(CleanJet_jetId->At(v_jet_1)) << endl;
            returnValues[vjet_0_qgl_res] = Jet_qgl->At(CleanJet_jetId->At(v_jet_0));
            //cout << "V 1 " << returnValues[vjet_0_qgl_res]<< endl;
            returnValues[vjet_1_qgl_res] = Jet_qgl->At(CleanJet_jetId->At(v_jet_1));
            //cout << "V 2 " << returnValues[vjet_1_qgl_res]<< endl;

            if (!jets_cat_qgl_FJ::isRunningOnData){
		//cout << "running on MC" <<endl;
                returnValues[vbs_0_partfl_boost] = 0;
                returnValues[vbs_1_partfl_boost] = 0;
		//cout << "looking at pf" <<endl;
                returnValues[vbs_0_partfl_res] = Jet_partonFlavour->At(CleanJet_jetId->At(vbs_jet_0));
                returnValues[vbs_1_partfl_res] = Jet_partonFlavour->At(CleanJet_jetId->At(vbs_jet_1));
                returnValues[vjet_0_partfl_res] = Jet_partonFlavour->At(CleanJet_jetId->At(v_jet_0));
                returnValues[vjet_1_partfl_res] = Jet_partonFlavour->At(CleanJet_jetId->At(v_jet_1));
		//cout << "vbs 1 pf"<< Jet_partonFlavour->At(CleanJet_jetId->At(vbs_jet_0))<<endl;
                returnValues[vbs_0_qglmorphed_boost] = -1;
                returnValues[vbs_1_qglmorphed_boost] = -1;
                returnValues[vbs_0_qglmorphed_res] = returnValues[vbs_0_partfl_res]==21 ?  
                                                    getMorphedGluon(returnValues[vbs_0_qgl_res], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)) : 
                                                    getMorphedQuark(returnValues[vbs_0_qgl_res], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0));
                returnValues[vbs_1_qglmorphed_res] = returnValues[vbs_1_partfl_res]==21 ?  
                                                    getMorphedGluon(returnValues[vbs_1_qgl_res], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)) : 
                                                    getMorphedQuark(returnValues[vbs_1_qgl_res], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1));
                returnValues[vjet_0_qglmorphed_res] = returnValues[vjet_0_partfl_res]==21 ?  
                                                    getMorphedGluon(returnValues[vjet_0_qgl_res], CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0)) :
                                                    getMorphedQuark(returnValues[vjet_0_qgl_res], CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0));
                returnValues[vjet_1_qglmorphed_res] = returnValues[vjet_1_partfl_res]==21 ?  
                                                    getMorphedGluon(returnValues[vjet_1_qgl_res], CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1)) : 
                                                    getMorphedQuark(returnValues[vjet_1_qgl_res], CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1));
            }else{
                returnValues[vbs_0_partfl_boost] = 0;
                returnValues[vbs_1_partfl_boost] = 0;
                returnValues[vbs_0_partfl_res] = 0;
                returnValues[vbs_1_partfl_res] = 0;
                returnValues[vjet_0_partfl_res] = 0;
                returnValues[vjet_1_partfl_res] = 0;

                returnValues[vbs_0_qglmorphed_boost] = -1;
                returnValues[vbs_1_qglmorphed_boost] = -1;
                returnValues[vbs_0_qglmorphed_res] =  returnValues[vbs_0_qgl_res];
                returnValues[vbs_1_qglmorphed_res] =  returnValues[vbs_1_qgl_res];
                returnValues[vjet_0_qglmorphed_res] = returnValues[vjet_0_qgl_res]; 
                returnValues[vjet_1_qglmorphed_res] = returnValues[vjet_1_qgl_res];
            }

        }else{
            category = 3;

        }
    
    }else{
    category = 3;
    }

        
    //set default values
    returnValues[Vpt]=_Vpt;
    returnValues[vbs_jet_0] = 999;
    returnValues[vbs_jet_1] = 999;
    returnValues[v_jet_0] = 999;
    returnValues[v_jet_1] = 999;
    returnValues[dnn_output_full_bVeto] = -0.2;


  // Now go back to CleanJet indexes for easy use of the collection
    if (category != 3) {
         //cout << "event " << _event << endl;
        if (VBS_jets[0] != 999) returnValues[vbs_jet_0] = CleanJetNotFat_jetId->At(vectors_id.at(VBS_jets[0]));
        else   cout << "error : Boosted or resolved category but VBS_jets[0] = 999"       << endl;     

        if (VBS_jets[1] != 999) returnValues[vbs_jet_1] = CleanJetNotFat_jetId->At(vectors_id.at(VBS_jets[1]));
        else   cout << "error : Boosted or resolved category but VBS_jets[1] = 999" << endl;                  
        
        if (category ==1){
            if (V_jets[0] != 999) returnValues[v_jet_0] = CleanJetNotFat_jetId->At(vectors_id.at(V_jets[0]));
            else       cout << "error :resolved category but V_jets[0] = 999" << endl;               

            if ( V_jets[1] != 999) returnValues[v_jet_1] = CleanJetNotFat_jetId->At(vectors_id.at(V_jets[1]));
            else       cout << "error :resolved category but V_jets[1] = 999" << endl;               
        }
    }

  returnValues[mjj_max]= Mjj_max;
  returnValues[detajj_mjjmax] = detajj_mjj_max;
  returnValues[dphijj_mjjmax] = dphijj_mjj_max;
  returnValues[Vjet_mass] = Vjet_mass_max;
  returnValues[njet30] = njet;
  //cout << "test" <<endl;
  returnValues[Zleppt] = _Zleppt;
  //cout << returnValues[Zleppt]<<endl;
  //cout << "nbtag = " << nbtag << endl;
  returnValues[nbtag] = _nbtag;
  //cout << _event << " cat : " << category << endl;
  returnValues[vbs_category] = category;
  //cout << _event << " vbs cat : " << returnValues[vbs_category]  << endl;
   /* if (category != 3){
        cout << " values set, category = " << category <<" returnValues[category] = " << returnValues[vbs_category] << " vbs1, vbs2, v1, v2 = " <<VBS_jets[0] << VBS_jets[1]<< V_jets[0]<< V_jets[1] <<endl;
        //if (VBS_jets[0]==999 | VBS_jets[1]== 999) cout << "error : category "<<category << " but VBS jets not found" <<endl;
        cout << "category : " << category << " type " << typeid(category).name()<< endl;
        cout << "returnValues[category] : " << returnValues[vbs_category] << " type " << typeid(returnValues[vbs_category]).name()<<endl;
    }
*/
//cout << "njet "<< njet <<" retval "  << returnValues[njet30] << endl;
//cout << "nbtag" << nbtag << " retval " << returnValues[nbtag] << endl;

  if (category != returnValues[vbs_category]){

    cout << _event<< " category : " << category << endl;

    cout <<_event<< " returnValues[category] : " << returnValues[vbs_category] <<endl;



  }

     
}

 
float jets_cat_qgl_FJ::getMorphedGluon(float x, float eta, float pt){
  //cout << "gluon x,eta, pt = " << x << eta << pt <<endl; 
  if (x<= 0.) return x;
  if (x>= 1.) return x;
  float y = x;
  if (abs(eta)<3 && pt < 75  && jets_cat_qgl_FJ::do_morph_gluon_loweta_pt0) {
//	cout <<"gluon low eta lowpt "<<endl;
          y =  jets_cat_qgl_FJ::morphing_functions["gluon_loweta_pt0"]->Eval(x);}
  if (abs(eta)<3 && pt >= 75  && jets_cat_qgl_FJ::do_morph_gluon_loweta_pt1) 
          y =  jets_cat_qgl_FJ::morphing_functions["gluon_loweta_pt1"]->Eval(x);
  if (abs(eta)>=3 && pt < 75  && jets_cat_qgl_FJ::do_morph_gluon_higheta_pt0) 
          y =  jets_cat_qgl_FJ::morphing_functions["gluon_higheta_pt0"]->Eval(x);
  if (abs(eta)>=3 && pt >= 75  && jets_cat_qgl_FJ::do_morph_gluon_higheta_pt1) 
          y =  jets_cat_qgl_FJ::morphing_functions["gluon_higheta_pt1"]->Eval(x);
  if (y<0) return 0.;
  if (y>1.) return 1.;
  return y;
}

float jets_cat_qgl_FJ::getMorphedQuark(float x, float eta, float pt){
  //cout << "quark x,eta, pt = " << x << eta << pt <<endl; 
  if (x<= 0.) return x;
  if (x>= 1.) return x;
  float y = x ;
  if (abs(eta)<3 && pt < 75  && jets_cat_qgl_FJ::do_morph_quark_loweta_pt0) 
          y =  jets_cat_qgl_FJ::morphing_functions["quark_loweta_pt0"]->Eval(x);
  if (abs(eta)<3 && pt >= 75  && jets_cat_qgl_FJ::do_morph_quark_loweta_pt1){ 
//	cout << "quark low eta high pt" <<endl;
          y =  jets_cat_qgl_FJ::morphing_functions["quark_loweta_pt1"]->Eval(x);
//	cout << "y =" << y <<endl;
	}
  if (abs(eta)>=3 && pt < 75  && jets_cat_qgl_FJ::do_morph_quark_higheta_pt0){ 
//	cout << "quark high eta low pt" <<endl;
          y =  jets_cat_qgl_FJ::morphing_functions["quark_higheta_pt0"]->Eval(x);
	//cout << "y="<< y<<endl;
	}
  if (abs(eta)>=3 && pt >= 75  && jets_cat_qgl_FJ::do_morph_quark_higheta_pt1) 
          y =  jets_cat_qgl_FJ::morphing_functions["quark_higheta_pt1"]->Eval(x);
  if (y<0) return 0.;
  if (y>1.) return 1.;
  return y;
}


