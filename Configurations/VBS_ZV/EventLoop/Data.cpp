#include "Data.h"

 Data::Data(TTree* tree) : m_tree(tree) {
     /**
      * @brief tree variable that needs to be declared: run, event, ...?
      * 
      */
     m_tree->SetBranchAddress("event", &event);
}

