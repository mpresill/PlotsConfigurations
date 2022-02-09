#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include "TFile.h"
#include "TGraph.h"
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

#include <cmath>
#include <string>
#include <unordered_map>
#include <iostream>
#include <stdexcept>
#include <tuple>

namespace multidraw {
  extern thread_local TTree* currentTree;
}


int isRunningSample(TString targetSample){
  TString currentSampleName = TString(multidraw::currentTree->GetCurrentFile()->GetName());
  if ( currentSampleName.Contains(targetSample)) {
      return 1;
  }
  else return 0;
}

class QglVarsMorphing : public multidraw::TTreeFunction {
public:
  QglVarsMorphing(const char * type,  const char * file1, const char * file2,  const char * do_morph1, const char * do_morph2,
                    const char * morph1_loweta_gluon_pt0, const char * morph1_loweta_gluon_pt1,
                    const char * morph1_higheta_gluon_pt0, const char * morph1_higheta_gluon_pt1,
                    const char * morph1_loweta_quark_pt0, const char * morph1_loweta_quark_pt1, 
                    const char * morph1_higheta_quark_pt0, const char * morph1_higheta_quark_pt1,
                    const char * morph2_loweta_gluon_pt0, const char * morph2_loweta_gluon_pt1,
                    const char * morph2_higheta_gluon_pt0, const char * morph2_higheta_gluon_pt1,
                    const char * morph2_loweta_quark_pt0, const char * morph2_loweta_quark_pt1, 
                    const char * morph_2higheta_quark_pt0, const char * morph2_higheta_quark_pt1);
  QglVarsMorphing(unsigned type,  const char * file1, const char * file2,  const char * do_morph1, const char * do_morph2,
                    const char * morph1_loweta_gluon_pt0, const char * morph1_loweta_gluon_pt1,
                    const char * morph1_higheta_gluon_pt0, const char * morph1_higheta_gluon_pt1,
                    const char * morph1_loweta_quark_pt0, const char * morph1_loweta_quark_pt1, 
                    const char * morph1_higheta_quark_pt0, const char * morph1_higheta_quark_pt1,
                    const char * morph2_loweta_gluon_pt0, const char * morph2_loweta_gluon_pt1,
                    const char * morph2_higheta_gluon_pt0, const char * morph2_higheta_gluon_pt1,
                    const char * morph2_loweta_quark_pt0, const char * morph2_loweta_quark_pt1, 
                    const char * morph2_higheta_quark_pt0, const char * morph2_higheta_quark_pt1);
  char const* getName() const override { return "QglVarsMorphing"; }
  TTreeFunction* clone() const override { return new QglVarsMorphing(returnVar_, file1_.c_str(), file2_.c_str(), do_morph1_.c_str(), do_morph2_.c_str(),
                                                morph1_loweta_gluon_pt0_.c_str(), morph1_loweta_gluon_pt1_.c_str(),
                                                morph1_higheta_gluon_pt0_.c_str(),morph1_higheta_gluon_pt1_.c_str(),
                                                morph1_loweta_quark_pt0_.c_str(),morph1_loweta_quark_pt1_.c_str(),
                                                morph1_higheta_quark_pt0_.c_str(),morph1_higheta_quark_pt1_.c_str(),
                                                morph2_loweta_gluon_pt0_.c_str(), morph2_loweta_gluon_pt1_.c_str(),
                                                morph2_higheta_gluon_pt0_.c_str(),morph2_higheta_gluon_pt1_.c_str(),
                                                morph2_loweta_quark_pt0_.c_str(),morph2_loweta_quark_pt1_.c_str(),
                                                morph2_higheta_quark_pt0_.c_str(),morph2_higheta_quark_pt1_.c_str()); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
      vbs_0_qgl_res, vbs_1_qgl_res, vjet_0_qgl_res, vjet_1_qgl_res, 
      vbs_0_qgl_boost, vbs_1_qgl_boost, 
      vbs_0_qglmorphed_res, vbs_1_qglmorphed_res, vjet_0_qglmorphed_res, vjet_1_qglmorphed_res, 
      vbs_0_qglmorphed_boost, vbs_1_qglmorphed_boost, 
      vbs_0_partfl_res, vbs_1_partfl_res, vjet_0_partfl_res, vjet_1_partfl_res, 
      vbs_0_partfl_boost, vbs_1_partfl_boost,
      nVarTypes
  };


  void bindTree_(multidraw::FunctionLibrary&) override;

  unsigned returnVar_{nVarTypes};
  //bool dostep2;
  string file1_;
  string file2_;
  string do_morph1_;
  string do_morph2_;
  static bool do_morph1_gluon_loweta_pt0;
  static bool do_morph1_gluon_loweta_pt1;
  static bool do_morph1_gluon_higheta_pt0;
  static bool do_morph1_gluon_higheta_pt1;
  static bool do_morph1_quark_loweta_pt0;
  static bool do_morph1_quark_loweta_pt1;
  static bool do_morph1_quark_higheta_pt0;
  static bool do_morph1_quark_higheta_pt1;
  static bool do_morph2_gluon_loweta_pt0;
  static bool do_morph2_gluon_loweta_pt1;
  static bool do_morph2_gluon_higheta_pt0;
  static bool do_morph2_gluon_higheta_pt1;
  static bool do_morph2_quark_loweta_pt0;
  static bool do_morph2_quark_loweta_pt1;
  static bool do_morph2_quark_higheta_pt0;
  static bool do_morph2_quark_higheta_pt1;
  string morph1_higheta_gluon_pt0_;
  string morph1_loweta_gluon_pt0_;
  string morph1_higheta_quark_pt0_;
  string morph1_loweta_quark_pt0_;
  string morph1_higheta_gluon_pt1_;
  string morph1_loweta_gluon_pt1_;
  string morph1_higheta_quark_pt1_;
  string morph1_loweta_quark_pt1_;
  string morph2_higheta_gluon_pt0_;
  string morph2_loweta_gluon_pt0_;
  string morph2_higheta_quark_pt0_;
  string morph2_loweta_quark_pt0_;
  string morph2_higheta_gluon_pt1_;
  string morph2_loweta_gluon_pt1_;
  string morph2_higheta_quark_pt1_;
  string morph2_loweta_quark_pt1_;
  static std::map<std::string, TGraph*> morphing_functions1;
  static std::map<std::string, TGraph*> morphing_functions2;
  static bool isRunningOnData;
 
  UIntValueReader* run{};
  UIntValueReader* luminosityBlock{};
  ULong64ValueReader* event{}; 

  static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;
  //must define Double reader
  typedef TTreeReaderValue<Double_t> DoubleValueReader;
  typedef std::unique_ptr<DoubleValueReader> DoubleValueReaderPtr;
  static IntArrayReader*  CleanJet_jetIdx;
  static FloatArrayReader*  CleanJet_eta;
  static FloatArrayReader*  CleanJet_pt;
  static FloatArrayReader* Jet_qgl;
  static IntArrayReader* Jet_partonFlavour;
  static UIntValueReader* nFatJet; 
  static FloatArrayReader* FatJet_pt;
  static FloatArrayReader* FatJet_eta;
  static FloatArrayReader* FatJet_phi;
  static FloatArrayReader* FatJet_mass;
  static IntArrayReader* CleanFatJet_jetIdx;
  static IntArrayReader* CleanJetNotFat_jetIdx;
  static FloatArrayReader* Jet_mass;
  static UIntValueReader* nCleanJetNotFat;
  static FloatArrayReader* CleanJet_phi;
  static FloatArrayReader* Lepton_pt;
  static FloatArrayReader* Lepton_eta;
  static FloatArrayReader* Lepton_phi;
  static UIntValueReader* nLepton;
  static FloatValueReader*  mll;

  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
  static float getMorphedGluon1(float x, float eta, float pt);
  static float getMorphedQuark1(float x, float eta, float pt);
  static float getMorphedGluon2(float x, float eta, float pt);
  static float getMorphedQuark2(float x, float eta, float pt);
};

std::tuple<UInt_t, UInt_t, ULong64_t> QglVarsMorphing::currentEvent{};

IntArrayReader* QglVarsMorphing::CleanJet_jetIdx{};
FloatArrayReader* QglVarsMorphing::CleanJet_eta{};
FloatArrayReader* QglVarsMorphing::CleanJet_pt{};
IntArrayReader* QglVarsMorphing::Jet_partonFlavour{};
FloatArrayReader* QglVarsMorphing::Jet_qgl{};
UIntValueReader* QglVarsMorphing::nFatJet{}; 
FloatArrayReader* QglVarsMorphing::FatJet_pt{};
FloatArrayReader* QglVarsMorphing::FatJet_eta{};
FloatArrayReader* QglVarsMorphing::FatJet_phi{};
FloatArrayReader* QglVarsMorphing::FatJet_mass{};
IntArrayReader*   QglVarsMorphing::CleanFatJet_jetIdx{};
IntArrayReader*   QglVarsMorphing::CleanJetNotFat_jetIdx{};
FloatArrayReader* QglVarsMorphing::Jet_mass{};
UIntValueReader*  QglVarsMorphing::nCleanJetNotFat; 
FloatArrayReader* QglVarsMorphing::CleanJet_phi{};
FloatArrayReader* QglVarsMorphing::Lepton_pt{};
FloatArrayReader* QglVarsMorphing::Lepton_eta{};
FloatArrayReader* QglVarsMorphing::Lepton_phi{};
UIntValueReader* QglVarsMorphing::nLepton;
FloatValueReader*  QglVarsMorphing::mll{};

std::map<std::string, TGraph*> QglVarsMorphing::morphing_functions1{};
std::map<std::string, TGraph*> QglVarsMorphing::morphing_functions2{};
bool QglVarsMorphing::isRunningOnData{false};
bool QglVarsMorphing::do_morph1_gluon_loweta_pt0{false};
bool QglVarsMorphing::do_morph1_gluon_higheta_pt0{false};
bool QglVarsMorphing::do_morph1_quark_loweta_pt0{false};
bool QglVarsMorphing::do_morph1_quark_higheta_pt0{false};
bool QglVarsMorphing::do_morph1_gluon_loweta_pt1{false};
bool QglVarsMorphing::do_morph1_gluon_higheta_pt1{false};
bool QglVarsMorphing::do_morph1_quark_loweta_pt1{false};
bool QglVarsMorphing::do_morph1_quark_higheta_pt1{false};
bool QglVarsMorphing::do_morph2_gluon_loweta_pt0{false};
bool QglVarsMorphing::do_morph2_gluon_higheta_pt0{false};
bool QglVarsMorphing::do_morph2_quark_loweta_pt0{false};
bool QglVarsMorphing::do_morph2_quark_higheta_pt0{false};
bool QglVarsMorphing::do_morph2_gluon_loweta_pt1{false};
bool QglVarsMorphing::do_morph2_gluon_higheta_pt1{false};
bool QglVarsMorphing::do_morph2_quark_loweta_pt1{false};
bool QglVarsMorphing::do_morph2_quark_higheta_pt1{false};

std::array<double, QglVarsMorphing::nVarTypes> QglVarsMorphing::returnValues{};

QglVarsMorphing::QglVarsMorphing(char const* _type, const char * file1, const char * file2,  const char * do_morph1, const char * do_morph2,
                    const char * morph1_loweta_gluon_pt0, const char * morph1_loweta_gluon_pt1,
                    const char * morph1_higheta_gluon_pt0, const char * morph1_higheta_gluon_pt1,
                    const char * morph1_loweta_quark_pt0, const char * morph1_loweta_quark_pt1, 
                    const char * morph1_higheta_quark_pt0, const char * morph1_higheta_quark_pt1,
                    const char * morph2_loweta_gluon_pt0, const char * morph2_loweta_gluon_pt1,
                    const char * morph2_higheta_gluon_pt0, const char * morph2_higheta_gluon_pt1,
                    const char * morph2_loweta_quark_pt0, const char * morph2_loweta_quark_pt1, 
                    const char * morph2_higheta_quark_pt0, const char * morph2_higheta_quark_pt1)
                    :
  TTreeFunction(),  file1_(file1),  file2_(file2) ,do_morph1_(do_morph1),do_morph2_(do_morph2),
  morph1_loweta_gluon_pt0_(morph1_loweta_gluon_pt0),morph1_loweta_gluon_pt1_(morph1_loweta_gluon_pt1),
  morph1_higheta_gluon_pt0_(morph1_higheta_gluon_pt0),morph1_higheta_gluon_pt1_(morph1_higheta_gluon_pt1),
  morph1_loweta_quark_pt0_(morph1_loweta_quark_pt0),morph1_loweta_quark_pt1_(morph1_loweta_quark_pt1),
  morph1_higheta_quark_pt0_(morph1_higheta_quark_pt0),morph1_higheta_quark_pt1_(morph1_higheta_quark_pt1),
  morph2_loweta_gluon_pt0_(morph2_loweta_gluon_pt0),morph2_loweta_gluon_pt1_(morph2_loweta_gluon_pt1),
  morph2_higheta_gluon_pt0_(morph2_higheta_gluon_pt0),morph2_higheta_gluon_pt1_(morph2_higheta_gluon_pt1),
  morph2_loweta_quark_pt0_(morph2_loweta_quark_pt0),morph2_loweta_quark_pt1_(morph2_loweta_quark_pt1),
  morph2_higheta_quark_pt0_(morph2_higheta_quark_pt0),morph2_higheta_quark_pt1_(morph2_higheta_quark_pt1)
{
  std::string type(_type);
  if (type ==  "vbs_0_qgl_res")
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
  
  int do_morph1_flags = std::stoi(do_morph1_,0,2);
  QglVarsMorphing::do_morph1_gluon_loweta_pt0 = do_morph1_flags & 1;
  QglVarsMorphing::do_morph1_gluon_loweta_pt1 = do_morph1_flags >>1 & 1;
  QglVarsMorphing::do_morph1_gluon_higheta_pt0 = do_morph1_flags >> 2 & 1;
  QglVarsMorphing::do_morph1_gluon_higheta_pt1 = do_morph1_flags >> 3 & 1;
  QglVarsMorphing::do_morph1_quark_loweta_pt0 = do_morph1_flags >> 4 & 1;
  QglVarsMorphing::do_morph1_quark_loweta_pt1 = do_morph1_flags >> 5 & 1;
  QglVarsMorphing::do_morph1_quark_higheta_pt0 = do_morph1_flags >> 6 & 1;
  QglVarsMorphing::do_morph1_quark_higheta_pt1 = do_morph1_flags >> 7 & 1;

  int do_morph2_flags = std::stoi(do_morph2_,0,2);
  QglVarsMorphing::do_morph2_gluon_loweta_pt0 = do_morph2_flags & 1;
  QglVarsMorphing::do_morph2_gluon_loweta_pt1 = do_morph2_flags >>1 & 1;
  QglVarsMorphing::do_morph2_gluon_higheta_pt0 = do_morph2_flags >> 2 & 1;
  QglVarsMorphing::do_morph2_gluon_higheta_pt1 = do_morph2_flags >> 3 & 1;
  QglVarsMorphing::do_morph2_quark_loweta_pt0 = do_morph2_flags >> 4 & 1;
  QglVarsMorphing::do_morph2_quark_loweta_pt1 = do_morph2_flags >> 5 & 1;
  QglVarsMorphing::do_morph2_quark_higheta_pt0 = do_morph2_flags >> 6 & 1;
  QglVarsMorphing::do_morph2_quark_higheta_pt1 = do_morph2_flags >> 7 & 1;
  
  TFile rfile1 {file1, "READ"};
  QglVarsMorphing::morphing_functions1["gluon_loweta_pt0"] = (TGraph*) rfile1.Get(morph1_loweta_gluon_pt0);
  QglVarsMorphing::morphing_functions1["gluon_loweta_pt1"] = (TGraph*) rfile1.Get(morph1_loweta_gluon_pt1);
  QglVarsMorphing::morphing_functions1["gluon_higheta_pt0"] = (TGraph*) rfile1.Get(morph1_higheta_gluon_pt0);
  QglVarsMorphing::morphing_functions1["gluon_higheta_pt1"] = (TGraph*) rfile1.Get(morph1_higheta_gluon_pt1);
  QglVarsMorphing::morphing_functions1["quark_loweta_pt0"] = (TGraph*) rfile1.Get(morph1_loweta_quark_pt0);
  QglVarsMorphing::morphing_functions1["quark_loweta_pt1"] = (TGraph*) rfile1.Get(morph1_loweta_quark_pt1);
  QglVarsMorphing::morphing_functions1["quark_higheta_pt0"] = (TGraph*) rfile1.Get(morph1_higheta_quark_pt0);
  QglVarsMorphing::morphing_functions1["quark_higheta_pt1"] = (TGraph*) rfile1.Get(morph1_higheta_quark_pt1);
  rfile1.Close();
  TFile rfile2 {file2, "READ"};
  QglVarsMorphing::morphing_functions2["gluon_loweta_pt0"] = (TGraph*) rfile2.Get(morph2_loweta_gluon_pt0);
  QglVarsMorphing::morphing_functions2["gluon_loweta_pt1"] = (TGraph*) rfile2.Get(morph2_loweta_gluon_pt1);
  QglVarsMorphing::morphing_functions2["gluon_higheta_pt0"] = (TGraph*) rfile2.Get(morph2_higheta_gluon_pt0);
  QglVarsMorphing::morphing_functions2["gluon_higheta_pt1"] = (TGraph*) rfile2.Get(morph2_higheta_gluon_pt1);
  QglVarsMorphing::morphing_functions2["quark_loweta_pt0"] = (TGraph*) rfile2.Get(morph2_loweta_quark_pt0);
  QglVarsMorphing::morphing_functions2["quark_loweta_pt1"] = (TGraph*) rfile2.Get(morph2_loweta_quark_pt1);
  QglVarsMorphing::morphing_functions2["quark_higheta_pt0"] = (TGraph*) rfile2.Get(morph2_higheta_quark_pt0);
  QglVarsMorphing::morphing_functions2["quark_higheta_pt1"] = (TGraph*) rfile2.Get(morph2_higheta_quark_pt1);
  rfile2.Close();
}


QglVarsMorphing::QglVarsMorphing(unsigned type,  const char * file1, const char * file2,  const char * do_morph1, const char * do_morph2,
                    const char * morph1_loweta_gluon_pt0, const char * morph1_loweta_gluon_pt1,
                    const char * morph1_higheta_gluon_pt0, const char * morph1_higheta_gluon_pt1,
                    const char * morph1_loweta_quark_pt0, const char * morph1_loweta_quark_pt1, 
                    const char * morph1_higheta_quark_pt0, const char * morph1_higheta_quark_pt1,
                    const char * morph2_loweta_gluon_pt0, const char * morph2_loweta_gluon_pt1,
                    const char * morph2_higheta_gluon_pt0, const char * morph2_higheta_gluon_pt1,
                    const char * morph2_loweta_quark_pt0, const char * morph2_loweta_quark_pt1, 
                    const char * morph2_higheta_quark_pt0, const char * morph2_higheta_quark_pt1) :
  TTreeFunction(),
  returnVar_(type),  file1_(file1),  file2_(file2) ,do_morph1_(do_morph1),do_morph2_(do_morph2),
  morph1_loweta_gluon_pt0_(morph1_loweta_gluon_pt0),morph1_loweta_gluon_pt1_(morph1_loweta_gluon_pt1),
  morph1_higheta_gluon_pt0_(morph1_higheta_gluon_pt0),morph1_higheta_gluon_pt1_(morph1_higheta_gluon_pt1),
  morph1_loweta_quark_pt0_(morph1_loweta_quark_pt0),morph1_loweta_quark_pt1_(morph1_loweta_quark_pt1),
  morph1_higheta_quark_pt0_(morph1_higheta_quark_pt0),morph1_higheta_quark_pt1_(morph1_higheta_quark_pt1),
  morph2_loweta_gluon_pt0_(morph2_loweta_gluon_pt0),morph2_loweta_gluon_pt1_(morph2_loweta_gluon_pt1),
  morph2_higheta_gluon_pt0_(morph2_higheta_gluon_pt0),morph2_higheta_gluon_pt1_(morph2_higheta_gluon_pt1),
  morph2_loweta_quark_pt0_(morph2_loweta_quark_pt0),morph2_loweta_quark_pt1_(morph2_loweta_quark_pt1),
  morph2_higheta_quark_pt0_(morph2_higheta_quark_pt0),morph2_higheta_quark_pt1_(morph2_higheta_quark_pt1)
  {
    //cout <<"file" << file <<endl;
    // Read the binary flag
    int do_morph1_flags = std::stoi(do_morph1_,0,2);
  QglVarsMorphing::do_morph1_gluon_loweta_pt0 = do_morph1_flags & 1;
  QglVarsMorphing::do_morph1_gluon_loweta_pt1 = do_morph1_flags >>1 & 1;
  QglVarsMorphing::do_morph1_gluon_higheta_pt0 = do_morph1_flags >> 2 & 1;
  QglVarsMorphing::do_morph1_gluon_higheta_pt1 = do_morph1_flags >> 3 & 1;
  QglVarsMorphing::do_morph1_quark_loweta_pt0 = do_morph1_flags >> 4 & 1;
  QglVarsMorphing::do_morph1_quark_loweta_pt1 = do_morph1_flags >> 5 & 1;
  QglVarsMorphing::do_morph1_quark_higheta_pt0 = do_morph1_flags >> 6 & 1;
  QglVarsMorphing::do_morph1_quark_higheta_pt1 = do_morph1_flags >> 7 & 1;

  int do_morph2_flags = std::stoi(do_morph2_,0,2);
  QglVarsMorphing::do_morph2_gluon_loweta_pt0 = do_morph2_flags & 1;
  QglVarsMorphing::do_morph2_gluon_loweta_pt1 = do_morph2_flags >>1 & 1;
  QglVarsMorphing::do_morph2_gluon_higheta_pt0 = do_morph2_flags >> 2 & 1;
  QglVarsMorphing::do_morph2_gluon_higheta_pt1 = do_morph2_flags >> 3 & 1;
  QglVarsMorphing::do_morph2_quark_loweta_pt0 = do_morph2_flags >> 4 & 1;
  QglVarsMorphing::do_morph2_quark_loweta_pt1 = do_morph2_flags >> 5 & 1;
  QglVarsMorphing::do_morph2_quark_higheta_pt0 = do_morph2_flags >> 6 & 1;
  QglVarsMorphing::do_morph2_quark_higheta_pt1 = do_morph2_flags >> 7 & 1;
  
  TFile rfile1 {file1, "READ"};
  QglVarsMorphing::morphing_functions1["gluon_loweta_pt0"] = (TGraph*) rfile1.Get(morph1_loweta_gluon_pt0);
  QglVarsMorphing::morphing_functions1["gluon_loweta_pt1"] = (TGraph*) rfile1.Get(morph1_loweta_gluon_pt1);
  QglVarsMorphing::morphing_functions1["gluon_higheta_pt0"] = (TGraph*) rfile1.Get(morph1_higheta_gluon_pt0);
  QglVarsMorphing::morphing_functions1["gluon_higheta_pt1"] = (TGraph*) rfile1.Get(morph1_higheta_gluon_pt1);
  QglVarsMorphing::morphing_functions1["quark_loweta_pt0"] = (TGraph*) rfile1.Get(morph1_loweta_quark_pt0);
  QglVarsMorphing::morphing_functions1["quark_loweta_pt1"] = (TGraph*) rfile1.Get(morph1_loweta_quark_pt1);
  QglVarsMorphing::morphing_functions1["quark_higheta_pt0"] = (TGraph*) rfile1.Get(morph1_higheta_quark_pt0);
  QglVarsMorphing::morphing_functions1["quark_higheta_pt1"] = (TGraph*) rfile1.Get(morph1_higheta_quark_pt1);
  rfile1.Close();
  TFile rfile2 {file2, "READ"};
  QglVarsMorphing::morphing_functions2["gluon_loweta_pt0"] = (TGraph*) rfile2.Get(morph2_loweta_gluon_pt0);
  QglVarsMorphing::morphing_functions2["gluon_loweta_pt1"] = (TGraph*) rfile2.Get(morph2_loweta_gluon_pt1);
  QglVarsMorphing::morphing_functions2["gluon_higheta_pt0"] = (TGraph*) rfile2.Get(morph2_higheta_gluon_pt0);
  QglVarsMorphing::morphing_functions2["gluon_higheta_pt1"] = (TGraph*) rfile2.Get(morph2_higheta_gluon_pt1);
  QglVarsMorphing::morphing_functions2["quark_loweta_pt0"] = (TGraph*) rfile2.Get(morph2_loweta_quark_pt0);
  QglVarsMorphing::morphing_functions2["quark_loweta_pt1"] = (TGraph*) rfile2.Get(morph2_loweta_quark_pt1);
  QglVarsMorphing::morphing_functions2["quark_higheta_pt0"] = (TGraph*) rfile2.Get(morph2_higheta_quark_pt0);
  QglVarsMorphing::morphing_functions2["quark_higheta_pt1"] = (TGraph*) rfile2.Get(morph2_higheta_quark_pt1);
  rfile2.Close();
}


void
QglVarsMorphing::bindTree_(multidraw::FunctionLibrary& _library)
{   cout << "bindtree" <<endl;   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");
    _library.bindBranch(nFatJet, "nCleanFatJet");
    _library.bindBranch(FatJet_pt, "CleanFatJet_pt");
    _library.bindBranch(FatJet_eta, "CleanFatJet_eta");
    _library.bindBranch(FatJet_phi, "CleanFatJet_phi");
    _library.bindBranch(FatJet_mass, "CleanFatJet_mass");
    _library.bindBranch(Jet_qgl, "Jet_qgl");
    _library.bindBranch(CleanJetNotFat_jetIdx, "CleanJetNotFat_jetIdx");
    _library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");
    _library.bindBranch(CleanFatJet_jetIdx, "CleanFatJet_jetIdx");
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

    QglVarsMorphing::isRunningOnData = isRunningSample("Run");
    if (!QglVarsMorphing::isRunningOnData){
      //exclude Data and fakes
       _library.bindBranch(Jet_partonFlavour, "Jet_partonFlavour");
    }
  
    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {
                
                                    CleanJet_jetIdx=nullptr;
                                    CleanJet_eta =nullptr;
                                    CleanJet_pt= nullptr;
                                    Jet_partonFlavour =nullptr;
                                    morphing_functions1.clear();
                                    morphing_functions2.clear();
                                   });
}

double
QglVarsMorphing::evaluate(unsigned)
{ //cout << "evaluate" <<endl;
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[returnVar_];
}
 
float QglVarsMorphing::getMorphedGluon1(float x, float eta, float pt){
  //cout << "gluon x,eta, pt = " << x << eta << pt <<endl; 
  if (x<= 0.) return x;
  if (x>= 1.) return x;
  float y = x;
  if (abs(eta)<3 && pt < 75  && QglVarsMorphing::do_morph1_gluon_loweta_pt0) {
	//cout <<"gluon low eta lowpt "<<endl;
          y =  QglVarsMorphing::morphing_functions1["gluon_loweta_pt0"]->Eval(x);}
  if (abs(eta)<3 && pt >= 75  && QglVarsMorphing::do_morph1_gluon_loweta_pt1) 
          y =  QglVarsMorphing::morphing_functions1["gluon_loweta_pt1"]->Eval(x);
  if (abs(eta)>=3 && pt < 75  && QglVarsMorphing::do_morph1_gluon_higheta_pt0) 
          y =  QglVarsMorphing::morphing_functions1["gluon_higheta_pt0"]->Eval(x);
  if (abs(eta)>=3 && pt >= 75  && QglVarsMorphing::do_morph1_gluon_higheta_pt1) 
          y =  QglVarsMorphing::morphing_functions1["gluon_higheta_pt1"]->Eval(x);
  if (y<0) return 0.;
  if (y>1.) return 1.;
  return y;
}

float QglVarsMorphing::getMorphedGluon2(float x, float eta, float pt){
  //cout << "gluon x,eta, pt = " << x << eta << pt <<endl; 
  if (x<= 0.) return x;
  if (x>= 1.) return x;
  float y = x;
  if (abs(eta)<3 && pt < 75  && QglVarsMorphing::do_morph2_gluon_loweta_pt0) {
	//cout <<"gluon low eta lowpt "<<endl;
          y =  QglVarsMorphing::morphing_functions2["gluon_loweta_pt0"]->Eval(x);}
  if (abs(eta)<3 && pt >= 75  && QglVarsMorphing::do_morph2_gluon_loweta_pt1) 
          y =  QglVarsMorphing::morphing_functions2["gluon_loweta_pt1"]->Eval(x);
  if (abs(eta)>=3 && pt < 75  && QglVarsMorphing::do_morph2_gluon_higheta_pt0) 
          y =  QglVarsMorphing::morphing_functions2["gluon_higheta_pt0"]->Eval(x);
  if (abs(eta)>=3 && pt >= 75  && QglVarsMorphing::do_morph2_gluon_higheta_pt1) 
          y =  QglVarsMorphing::morphing_functions2["gluon_higheta_pt1"]->Eval(x);
  if (y<0) return 0.;
  if (y>1.) return 1.;
  return y;
}

float QglVarsMorphing::getMorphedQuark1(float x, float eta, float pt){
  //cout << "quark x,eta, pt = " << x << eta << pt <<endl; 
  if (x<= 0.) return x;
  if (x>= 1.) return x;
  float y = x ;
  if (abs(eta)<3 && pt < 75  && QglVarsMorphing::do_morph1_quark_loweta_pt0) 
          y =  QglVarsMorphing::morphing_functions1["quark_loweta_pt0"]->Eval(x);
  if (abs(eta)<3 && pt >= 75  && QglVarsMorphing::do_morph1_quark_loweta_pt1){ 
	//cout << "quark low eta high pt" <<endl;
          y =  QglVarsMorphing::morphing_functions1["quark_loweta_pt1"]->Eval(x);
	//cout << "y =" << y <<endl;
}
  if (abs(eta)>=3 && pt < 75  && QglVarsMorphing::do_morph1_quark_higheta_pt0){ 
//	cout << "quark high eta low pt" <<endl;
          y =  QglVarsMorphing::morphing_functions1["quark_higheta_pt0"]->Eval(x);
//	cout << "y="<< y<<endl;
}
  if (abs(eta)>=3 && pt >= 75  && QglVarsMorphing::do_morph1_quark_higheta_pt1) 
          y =  QglVarsMorphing::morphing_functions1["quark_higheta_pt1"]->Eval(x);
  if (y<0) return 0.;
  if (y>1.) return 1.;
  return y;
}


float QglVarsMorphing::getMorphedQuark2(float x, float eta, float pt){
  //cout << "quark x,eta, pt = " << x << eta << pt <<endl; 
  if (x<= 0.) return x;
  if (x>= 1.) return x;
  float y = x ;
  if (abs(eta)<3 && pt < 75  && QglVarsMorphing::do_morph2_quark_loweta_pt0) 
          y =  QglVarsMorphing::morphing_functions2["quark_loweta_pt0"]->Eval(x);
  if (abs(eta)<3 && pt >= 75  && QglVarsMorphing::do_morph2_quark_loweta_pt1){ 
	//cout << "quark low eta high pt" <<endl;
          y =  QglVarsMorphing::morphing_functions2["quark_loweta_pt1"]->Eval(x);
	//cout << "y =" << y <<endl;
}
  if (abs(eta)>=3 && pt < 75  && QglVarsMorphing::do_morph2_quark_higheta_pt0){ 
//	cout << "quark high eta low pt" <<endl;
          y =  QglVarsMorphing::morphing_functions2["quark_higheta_pt0"]->Eval(x);
//	cout << "y="<< y<<endl;
}
  if (abs(eta)>=3 && pt >= 75  && QglVarsMorphing::do_morph2_quark_higheta_pt1) 
          y =  QglVarsMorphing::morphing_functions2["quark_higheta_pt1"]->Eval(x);
  if (y<0) return 0.;
  if (y>1.) return 1.;
  return y;
}


/*static*/
void
QglVarsMorphing::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

   currentEvent = std::make_tuple(_run, _luminosityBlock, _event);
   //cout << "setValues()" <<endl;
   //cout << "event :" << _event <<endl;  


    //calculate category and jet indices
    float Mjj_tmp=0;
    float Mjj_max=0;
    float deltamass_Vjet=1e5;
    float Vjet_mass_max = 0.;
    bool dostep2 =true;
    unsigned int njet{*nCleanJetNotFat->Get()};
    unsigned int nFJ{*nFatJet->Get()};
    unsigned int nLep{*nLepton->Get()};
    // Index in the collection of CleanJetNotFat
    int VBS_jets[2] = {999,999};
    int V_jets[2]   = {999,999};
    int category = 999;  // 0 fatjet, 1 resolved, -1 none
    float pt_cut = 30;
    int vbs_jet_0 = 999;
    int vbs_jet_1 = 999;
    int v_jet_0 = 999;
    int v_jet_1 = 999;
    std::vector<int> vectors_id;
    std::vector<TLorentzVector> vectors; 

    if (nLep == 2) {
        //cout << " 2 Leptons " << endl;
        TLorentzVector lep0;
        TLorentzVector lep1;
        lep0.SetPtEtaPhiM(Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0);
        lep1.SetPtEtaPhiM(Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0);
        //cout << _Zleppt <<endl;
    }
   
    for (unsigned int ijet=0 ; ijet<njet ; ijet++){
        TLorentzVector jet0; 
        jet0.SetPtEtaPhiM(CleanJet_pt->At(CleanJetNotFat_jetIdx->At(ijet)), CleanJet_eta->At(CleanJetNotFat_jetIdx->At(ijet)),
                        CleanJet_phi->At(CleanJetNotFat_jetIdx->At(ijet)),Jet_mass->At(CleanJet_jetIdx->At(CleanJetNotFat_jetIdx->At(ijet)))); 
        if(jet0.Pt()>pt_cut){
            vectors.push_back(jet0);
            vectors_id.push_back(ijet);
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
                    // Index in vectors
                    VBS_jets[0]= ijet;
                    VBS_jets[1]= jjet;
                }
            }
        }
        
        vbs_jet_0 =CleanJetNotFat_jetIdx->At(vectors_id.at(VBS_jets[0]));
        vbs_jet_1 =CleanJetNotFat_jetIdx->At(vectors_id.at(VBS_jets[1]));
        // Now we have the njets

        // Check if boosted
        if (nFJ >= 1){
     //       cout << "Boosted" << endl;
            category = 0;

        }else if (njet>=4) { 
            category = 1;
       //    cout << "resolved "  << endl;
  
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
                            deltamass_Vjet = dmass;
                            Vjet_mass_max = mvjet;
                        }
                    }
                }
            }
        v_jet_0 =CleanJetNotFat_jetIdx->At(vectors_id.at(V_jets[0]));
        v_jet_1 =CleanJetNotFat_jetIdx->At(vectors_id.at(V_jets[1]));
        }else{
            category = 3;
        }
    
    }else{
    category = 3;
    }

   //cout << "cat :" << category << endl;
	if (category ==0){
//	cout << "cat :" << category << endl;
   //cout << "running on Data:" << QglVarsMorphing::isRunningOnData<<endl;      
      //boosted
      returnValues[vbs_0_qgl_boost] = Jet_qgl->At(CleanJet_jetIdx->At(vbs_jet_0));
      returnValues[vbs_1_qgl_boost] = Jet_qgl->At(CleanJet_jetIdx->At(vbs_jet_1));
      returnValues[vbs_0_qgl_res] = -1;
      returnValues[vbs_1_qgl_res] = -1;
      returnValues[vjet_0_qgl_res] = -1;
      returnValues[vjet_1_qgl_res] = -1;

      if (!QglVarsMorphing::isRunningOnData){
        returnValues[vbs_0_partfl_boost] = Jet_partonFlavour->At(CleanJet_jetIdx->At(vbs_jet_0));
        returnValues[vbs_1_partfl_boost] = Jet_partonFlavour->At(CleanJet_jetIdx->At(vbs_jet_1));
        returnValues[vbs_0_partfl_res] = 0;
        returnValues[vbs_1_partfl_res] = 0;
        returnValues[vjet_0_partfl_res] = 0;
        returnValues[vjet_1_partfl_res] = 0;

        if (dostep2){ 
            returnValues[vbs_0_qglmorphed_boost] = returnValues[vbs_0_partfl_boost]==21 ?  
                                                            getMorphedGluon2(getMorphedGluon1(returnValues[vbs_0_qgl_boost], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)),CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0))  : 
                                                            getMorphedQuark2(getMorphedQuark1(returnValues[vbs_0_qgl_boost], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)),CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)) ;
            returnValues[vbs_1_qglmorphed_boost] = returnValues[vbs_1_partfl_boost]==21 ?  
                                                            getMorphedGluon2(getMorphedGluon1(returnValues[vbs_1_qgl_boost], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)),CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1))  : 
                                                            getMorphedQuark2(getMorphedQuark1(returnValues[vbs_1_qgl_boost], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)),CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)) ;
        }else {


            returnValues[vbs_0_qglmorphed_boost] = returnValues[vbs_0_partfl_boost]==21 ?  
                                                            getMorphedGluon1(returnValues[vbs_0_qgl_boost], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)) : 
                                                            getMorphedQuark1(returnValues[vbs_0_qgl_boost], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0));
            returnValues[vbs_1_qglmorphed_boost] = returnValues[vbs_1_partfl_boost]==21 ?  
                                                            getMorphedGluon1(returnValues[vbs_1_qgl_boost], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)):  
                                                            getMorphedQuark1(returnValues[vbs_1_qgl_boost], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1));
            }
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


    }else if(category == 1){

      returnValues[vbs_0_qgl_boost] = -1;
      returnValues[vbs_1_qgl_boost] = -1;
      returnValues[vbs_0_qgl_res] = Jet_qgl->At(CleanJet_jetIdx->At(vbs_jet_0));
      returnValues[vbs_1_qgl_res] = Jet_qgl->At(CleanJet_jetIdx->At(vbs_jet_1));
      returnValues[vjet_0_qgl_res] = Jet_qgl->At(CleanJet_jetIdx->At(v_jet_0));
      returnValues[vjet_1_qgl_res] = Jet_qgl->At(CleanJet_jetIdx->At(v_jet_1));


      if (!QglVarsMorphing::isRunningOnData){

        returnValues[vbs_0_partfl_boost] = 0;
        returnValues[vbs_1_partfl_boost] = 0;
        returnValues[vbs_0_partfl_res] = Jet_partonFlavour->At(CleanJet_jetIdx->At(vbs_jet_0));
        returnValues[vbs_1_partfl_res] = Jet_partonFlavour->At(CleanJet_jetIdx->At(vbs_jet_1));
        returnValues[vjet_0_partfl_res] = Jet_partonFlavour->At(CleanJet_jetIdx->At(v_jet_0));
        returnValues[vjet_1_partfl_res] = Jet_partonFlavour->At(CleanJet_jetIdx->At(v_jet_1));

        returnValues[vbs_0_qglmorphed_boost] = -1;
        returnValues[vbs_1_qglmorphed_boost] = -1;

        if (dostep2){
            returnValues[vbs_0_qglmorphed_res] = returnValues[vbs_0_partfl_res]==21 ?  
                                                            getMorphedGluon2(getMorphedGluon1(returnValues[vbs_0_qgl_res], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)),CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0))  : 
                                                            getMorphedQuark2(getMorphedQuark1(returnValues[vbs_0_qgl_res], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)),CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)) ;
            returnValues[vbs_1_qglmorphed_res] = returnValues[vbs_1_partfl_res]==21 ?  
                                                            getMorphedGluon2(getMorphedGluon1(returnValues[vbs_1_qgl_res], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)),CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1))  : 
                                                            getMorphedQuark2(getMorphedQuark1(returnValues[vbs_1_qgl_res], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)),CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)) ;
            returnValues[vjet_0_qglmorphed_res] = returnValues[vjet_0_partfl_res]==21 ?  
                                                            getMorphedGluon2(getMorphedGluon1(returnValues[vjet_0_qgl_res], CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0)),CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0))  : 
                                                            getMorphedQuark2(getMorphedQuark1(returnValues[vjet_0_qgl_res], CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0)),CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0)) ;
            returnValues[vjet_1_qglmorphed_res] = returnValues[vjet_1_partfl_res]==21 ?  
                                                            getMorphedGluon2(getMorphedGluon1(returnValues[vjet_1_qgl_res], CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1)),CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1))  : 
                                                            getMorphedQuark2(getMorphedQuark1(returnValues[vjet_1_qgl_res], CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1)),CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1)) ;
        }else{
            returnValues[vbs_0_qglmorphed_res] = returnValues[vbs_0_partfl_res]==21 ?  
                                                getMorphedGluon1(returnValues[vbs_0_qgl_res], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0)) : 
                                                getMorphedQuark1(returnValues[vbs_0_qgl_res], CleanJet_eta->At(vbs_jet_0),CleanJet_pt->At(vbs_jet_0));
            returnValues[vbs_1_qglmorphed_res] = returnValues[vbs_1_partfl_res]==21 ?  
                                                getMorphedGluon1(returnValues[vbs_1_qgl_res], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1)) : 
                                                getMorphedQuark1(returnValues[vbs_1_qgl_res], CleanJet_eta->At(vbs_jet_1),CleanJet_pt->At(vbs_jet_1));
            returnValues[vjet_0_qglmorphed_res] = returnValues[vjet_0_partfl_res]==21 ?  
                                                getMorphedGluon1(returnValues[vjet_0_qgl_res], CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0)) :
                                                getMorphedQuark1(returnValues[vjet_0_qgl_res], CleanJet_eta->At(v_jet_0),CleanJet_pt->At(v_jet_0));
            returnValues[vjet_1_qglmorphed_res] = returnValues[vjet_1_partfl_res]==21 ?  
                                                getMorphedGluon1(returnValues[vjet_1_qgl_res], CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1)) : 
                                                getMorphedQuark1(returnValues[vjet_1_qgl_res], CleanJet_eta->At(v_jet_1),CleanJet_pt->At(v_jet_1));
        }

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

      //cout << returnValues[vbs_0_partfl_res] << "  > " <<  returnValues[vbs_0_qgl_res] << " morphed -> " <<  returnValues[vbs_0_qglmorphed_res]  <<endl;
    }
    
    else{
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
    }


}



