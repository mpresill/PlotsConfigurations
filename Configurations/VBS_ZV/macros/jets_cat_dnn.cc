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
#include "TVector2.h"
#include "TSystem.h"
#include "TLorentzVector.h"

#include <cmath>
#include <string>
#include <unordered_map>
#include <iostream>
#include <stdexcept>
#include <tuple>

using namespace std;
using namespace NNEvaluation;

// --- functions Helper
float deltaEta(float eta1, float eta2) {
  return std::abs(eta1 - eta2);
}

float deltaPhi(float phi1, float phi2){
  float PHI = std::abs(phi1-phi2);
  if (PHI<=3.14159265)
    return PHI;
  else
    return 2*3.14159265-PHI;
}


class jets_cat_dnn : public multidraw::TTreeFunction {
public:
  jets_cat_dnn( char const* _type, const char* year, const char* model_dir, bool verbose);
  jets_cat_dnn( unsigned type, const char* year, const char* model_dir, bool verbose);

  char const* getName() const override { return "jets_cat_dnn"; }
  TTreeFunction* clone() const override { return new jets_cat_dnn(returnVar_,year_.c_str(),model_dir_.c_str(), verbose ); }
  std::string model_dir_;
  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  bool verbose;
  
  DNNEvaluator* dnn_tensorflow_boosted;
  DNNEvaluator* dnn_tensorflow_resolved;

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
    dnn_output, 
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
  
  static UIntValueReader* nFatJet; 
  static FloatArrayReader* FatJet_pt;
  static FloatArrayReader* FatJet_eta;
  static FloatArrayReader* FatJet_phi;
  static FloatArrayReader* FatJet_mass;

  static IntArrayReader* CleanJet_jetId;
  static IntArrayReader* CleanJetNotFat_jetId;
  static FloatArrayReader* Jet_mass;
  static UIntValueReader* nCleanJetNotFat;
  static FloatArrayReader* CleanJet_pt;
  static FloatArrayReader* CleanJet_eta;
  static FloatArrayReader* CleanJet_phi;
  static FloatArrayReader* Lepton_pt;
  static FloatArrayReader* Lepton_eta;
  static FloatValueReader*  mll;
  static std::array<double, nVarTypes> returnValues;

  static void setValues(UInt_t, UInt_t, ULong64_t);
};

std::tuple<UInt_t, UInt_t, ULong64_t> jets_cat_dnn::currentEvent{};

UIntValueReader* jets_cat_dnn::nFatJet{}; 
FloatArrayReader* jets_cat_dnn::FatJet_pt{};
FloatArrayReader* jets_cat_dnn::FatJet_eta{};
FloatArrayReader* jets_cat_dnn::FatJet_phi{};
FloatArrayReader* jets_cat_dnn::FatJet_mass{};


IntArrayReader*   jets_cat_dnn::CleanJet_jetId{};
IntArrayReader*   jets_cat_dnn::CleanJetNotFat_jetId{};
FloatArrayReader* jets_cat_dnn::Jet_mass{};
UIntValueReader*  jets_cat_dnn::nCleanJetNotFat; 
FloatArrayReader* jets_cat_dnn::CleanJet_pt{};
FloatArrayReader* jets_cat_dnn::CleanJet_eta{};
FloatArrayReader* jets_cat_dnn::CleanJet_phi{};
FloatArrayReader* jets_cat_dnn::Lepton_pt{};
FloatArrayReader* jets_cat_dnn::Lepton_eta{};
FloatValueReader*  jets_cat_dnn::mll{};

string jets_cat_dnn::year_{};
//string jets_cat_dnn::model_dir_{};
//bool jets_cat_dnn::verbose{};

std::array<double, jets_cat_dnn::nVarTypes> jets_cat_dnn::returnValues{};


// function Helper ---


jets_cat_dnn::jets_cat_dnn( char const* _type, const char* year, const char* model_dir, bool verbose):
   TTreeFunction(){
     
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
    else if (type == "dnn_output")
      returnVar_ = dnn_output;
    else
      throw std::runtime_error("unknown return type " + type);
    jets_cat_dnn::year_ = year;
    // jets_cat_dnn::model_dir_ = model_dir;
    // jets_cat_dnn::verbose = verbose;
}

jets_cat_dnn::jets_cat_dnn( unsigned type, const char* year, const char* model_dir, bool verbose):
TTreeFunction(), returnVar_(type), 
model_dir_(model_dir), verbose(verbose){
  jets_cat_dnn::year_ = year;
  //jets_cat_dnn::model_dir_ = model_dir;
  //jets_cat_dnn::verbose = verbose;
  std::string boosted_path_ = model_dir_ + year_ + "_SR/Boosted_SR/DNN/";
  dnn_tensorflow_boosted = new DNNEvaluator(boosted_path_, verbose);
  std::string resolved_path_ = model_dir_ + year_ + "_SR/Resolved_SR/DNN/";
  dnn_tensorflow_boosted = new DNNEvaluator(resolved_path_, verbose);
}


double
jets_cat_dnn::evaluate(unsigned)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());

  //if returnVar_ = dnnoutput, run dnn

  if (returnVar_ == dnn_output){
  int category = (int) returnValues[vbs_category];
  int vbs_jet1 = (int) returnValues[vbs_jet_0];
  int vbs_jet2 = (int) returnValues[vbs_jet_1];
  int v_jet1 = (int) returnValues[v_jet_0];
  int v_jet2 = (int) returnValues[v_jet_1];
  float Vjetmass = (float) returnValues[Vjet_mass];
  float mjj = (float) returnValues[mjj_max];
  float detajj = (float)returnValues[detajj_mjjmax];

  //Boosted
  if (category ==0){
          cout << "Boosted DNN " << endl;

      float Zlep_1 = ((Lepton_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zlep_2 = ((Lepton_eta->At(1)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;

      std::vector<float> input{};

      input.push_back((Lepton_pt->At(0)));
      input.push_back((Lepton_pt->At(1)));
      input.push_back((Lepton_eta->At(0)));
      input.push_back((Lepton_eta->At(1)));
      input.push_back(*(mll->Get()));
      input.push_back((FatJet_pt->At(0)));
      input.push_back((FatJet_eta->At(0)));
      input.push_back(Zlep_1);
      input.push_back(Zlep_2);
      input.push_back((CleanJet_pt->At(vbs_jet1)));
      input.push_back((CleanJet_pt->At(vbs_jet2)));
      input.push_back((CleanJet_eta->At(vbs_jet1)));
      input.push_back((CleanJet_eta->At(vbs_jet2)));
      input.push_back(mjj);
      input.push_back(detajj);

      returnValues[dnn_output]= dnn_tensorflow_boosted->analyze(input);

//Resolved
  }else if (category == 1){


      float Zlep_1 = ((Lepton_eta->At(0)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;
      float Zlep_2 = ((Lepton_eta->At(1)) - 0.5 * ((CleanJet_eta->At(vbs_jet1)) + (CleanJet_eta->At(vbs_jet2)))) / detajj;


        std::vector<float> input{};


        input.push_back( (Lepton_pt->At(0)) );
        input.push_back( (Lepton_pt->At(1)));
        input.push_back( (Lepton_eta->At(0)));
        input.push_back( (Lepton_eta->At(1)));
        input.push_back( *(mll->Get()) );
        input.push_back( Zlep_1 );
        input.push_back( Zlep_2 );
        input.push_back( (CleanJet_pt -> At(vbs_jet1)) );
        input.push_back( (CleanJet_pt -> At(vbs_jet2)) );
        input.push_back( (CleanJet_eta -> At(vbs_jet1)) );
        input.push_back( (CleanJet_eta -> At(vbs_jet2)) );
        input.push_back( (CleanJet_pt -> At(v_jet1)) );
        input.push_back( (CleanJet_pt -> At(v_jet2)) );
        input.push_back( (CleanJet_eta -> At(v_jet1)) );
        input.push_back( (CleanJet_eta -> At(v_jet2)) );  
        input.push_back( mjj);
        input.push_back( detajj);
        input.push_back( Vjetmass);

        returnValues[dnn_output]= dnn_tensorflow_resolved->analyze(input);

    }
  }
  return returnValues[returnVar_];
}

void
jets_cat_dnn::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nFatJet, "nCleanFatJet");
    _library.bindBranch(FatJet_pt, "CleanFatJet_pt");
    _library.bindBranch(FatJet_eta, "CleanFatJet_eta");
    _library.bindBranch(FatJet_phi, "CleanFatJet_phi");
    _library.bindBranch(FatJet_mass, "CleanFatJet_mass");

    _library.bindBranch(CleanJetNotFat_jetId, "CleanJetNotFat_jetIdx");
    _library.bindBranch(CleanJet_jetId, "CleanJet_jetIdx");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(nCleanJetNotFat, "nCleanJetNotFat");
    _library.bindBranch(CleanJet_pt, "CleanJet_pt");
    _library.bindBranch(CleanJet_eta, "CleanJet_eta");
    _library.bindBranch(CleanJet_phi, "CleanJet_phi");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(mll, "mll");
    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {

                                     nFatJet = nullptr;
                                     FatJet_pt = nullptr;
                                     FatJet_eta = nullptr;
                                     FatJet_phi = nullptr;
                                     FatJet_mass = nullptr;
                                     nCleanJetNotFat = nullptr;
                                     CleanJet_pt = nullptr;
                                     CleanJet_eta = nullptr;
                                     CleanJet_phi = nullptr;
                                     Jet_mass = nullptr;
                                     CleanJet_jetId = nullptr;
                                     CleanJetNotFat_jetId = nullptr;
                                     Lepton_pt = nullptr;
                                     Lepton_eta = nullptr;
                                     mll = nullptr;
                                   });
}

/*static*/
void
jets_cat_dnn::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

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
  // Index in the collection of CleanJetNotFat
  int VBS_jets[2] = {999,999};
  int V_jets[2]   = {999,999};
  int category = 999;  // 0 fatjet, 1 resolved, -1 none
  float pt_cut = 30;


  // Load all the quadrivectors for performance reason
  std::vector<TLorentzVector> vectors; 
  for (unsigned int ijet=0 ; ijet<njet ; ijet++){
    TLorentzVector jet0; 
    jet0.SetPtEtaPhiM(CleanJet_pt->At(CleanJetNotFat_jetId->At(ijet)), CleanJet_eta->At(CleanJetNotFat_jetId->At(ijet)),
                      CleanJet_phi->At(CleanJetNotFat_jetId->At(ijet)),Jet_mass->At(CleanJet_jetId->At(CleanJetNotFat_jetId->At(ijet)))); 
    if(jet0.Pt()>pt_cut){vectors.push_back(jet0);} //this is for the minimal threhsold in the jet ak4 pt => vetoing ak4 with pt>30 GeV
    //vectors.push_back(jet0);
   }
  njet=vectors.size();
  if (njet>=2){
    // Calculate max mjj invariant pair on CleanJetNotFat to exclude the correct jets
    for (unsigned int ijet=0 ; ijet<njet ; ijet++){
      for (unsigned int jjet= ijet+1 ; jjet<njet ; jjet++){
        if (ijet==jjet) continue;
        TLorentzVector jet0 = vectors.at(ijet);
        TLorentzVector jet1 = vectors.at(jjet); 

        Mjj_tmp = (jet0 + jet1).M();
        
        if( Mjj_tmp >= Mjj_max ){
          Mjj_max=Mjj_tmp;
          detajj_mjj_max=deltaEta(CleanJet_eta->At(CleanJetNotFat_jetId->At(ijet)),CleanJet_eta->At(CleanJetNotFat_jetId->At(jjet)));
          dphijj_mjj_max=deltaPhi(CleanJet_phi->At(CleanJetNotFat_jetId->At(ijet)),CleanJet_phi->At(CleanJetNotFat_jetId->At(jjet)));
          // Index in the collection of CleanJetNotFat
          VBS_jets[0]= ijet;
          VBS_jets[1]= jjet;
        }
      }
    }

    // Now we have the njets
    // Check if boosted
    if (nFJ >= 1){
        cout << "Boosted" << endl;
        category = 0;
        Vjet_mass_max = FatJet_mass->At(0);

    }else if (njet>=4)
    { 
      category = 1;
      for (unsigned int ijet=0 ; ijet<njet ; ijet++){
      for (unsigned int jjet= ijet+1 ; jjet<njet ; jjet++){
          if (VBS_jets[0] == ijet || VBS_jets[1] == ijet || VBS_jets[0] == jjet || VBS_jets[1] == jjet) continue;
          else{
            TLorentzVector jet0 = vectors.at(ijet);
            TLorentzVector jet1 = vectors.at(jjet); 
            float mvjet = (jet0+jet1).M();
            float dmass = abs( mvjet - 85.7863 );
            if (dmass < deltamass_Vjet){
              // Index in the collection of CleanJetNotFat
              V_jets[0] = ijet;
              V_jets[1] = jjet;
              deltamass_Vjet = dmass;
              Vjet_mass_max = mvjet;
            }
          }
        }
      }
    }else{
      category = -1;
    }
  
  }else{
    category = -1;
  }

  // Now go back to CleanJet indexes for easy use of the collection
  if (VBS_jets[0] != 999) returnValues[vbs_jet_0] = CleanJetNotFat_jetId->At(VBS_jets[0]);
  else                     returnValues[vbs_jet_0] = 999;

  if (VBS_jets[1] != 999) returnValues[vbs_jet_1] = CleanJetNotFat_jetId->At(VBS_jets[1]);
  else                     returnValues[vbs_jet_1] = 999;
 
  if (V_jets[0] != 999) returnValues[v_jet_0] = CleanJetNotFat_jetId->At(V_jets[0]);
  else                     returnValues[v_jet_0] = 999;

  if (V_jets[1] != 999) returnValues[v_jet_1] = CleanJetNotFat_jetId->At(V_jets[1]);
  else                     returnValues[v_jet_1] = 999;


  returnValues[mjj_max]= Mjj_max;
  returnValues[detajj_mjjmax] = detajj_mjj_max;
  returnValues[dphijj_mjjmax] = dphijj_mjj_max;
  returnValues[Vjet_mass] = Vjet_mass_max;
  returnValues[vbs_category] = category;
  returnValues[dnn_output] = -0.2;

  //run DNN 
  
  }



