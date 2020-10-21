#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

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

class lept_eta : public multidraw::TTreeFunction {
public:
  lept_eta( char const* _type, const char* year);
  lept_eta( unsigned type, const char* year);

  char const* getName() const override { return "lept_eta"; }
  TTreeFunction* clone() const override { return new lept_eta(returnVar_,year_.c_str() ); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  enum ReturnType {
    eta1,
    eta2, 
    nVarTypes
  };

    void bindTree_(multidraw::FunctionLibrary&) override;
     unsigned returnVar_{nVarTypes};
  

   UIntValueReader* run{};
   UIntValueReader* luminosityBlock{};
   ULong64ValueReader* event{}; 
    static string year_;
    static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;
    static FloatArrayReader* Lepton_eta{};
    static std::array<double, nVarTypes> returnValues;

   static void setValues(UInt_t, UInt_t, ULong64_t);
};

std::tuple<UInt_t, UInt_t, ULong64_t> lept_eta::currentEvent{};
FloatArrayReader* lept_eta::Lepton_eta{};
std::array<double, lept_eta::nVarTypes> lept_eta::returnValues{};

lept_eta::lept_eta( char const* _type, const char* year):
   TTreeFunction(){
     
    std::string type(_type);
    if (type ==  "eta1")
      returnVar_ = eta1;
    if (type ==  "eta2")
      returnVar_ = eta2;
   }

double
lept_eta::evaluate(unsigned)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[returnVar_];
}

void
lept_eta::bindTree_(multidraw::FunctionLibrary& _library)
{   
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");
    _library.bindBranch(Lepton_eta, "Lepton_eta");

    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {

                                     Lepton_eta = nullptr;
    });
}
void
lept_eta::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{

  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

  currentEvent = std::make_tuple(_run, _luminosityBlock, _event);
  float eta1 = Lepton_eta->At(0);
  float eta2 = Lepton_eta->At(1);

  returnValues[eta1]=eta1;
  returnValues[eta2]=eta2;

}

