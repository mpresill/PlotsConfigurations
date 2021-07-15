#include "EventLoop.h"
#include <iostream>
#include <stdexcept>

#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <math.h>
#include <fstream>
#include <string>
#include <sstream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
using namespace std;




EventLoop::EventLoop()
{
  // nothing to do here
}

void EventLoop::initialize()
{
  // create an instance of the TChain class
  m_chain = new TChain(treeName);

  // loop through the input files and add them to the chain
  for (auto inputFile : inputFiles)
  {
    m_chain->Add(inputFile);
    std::cout << "Added file: " << inputFile << std::endl;
  }

  // create an instance of the Data class. Here the variables
  // are linked with the tree using the SetBranchAddress method
  m_data = new Data(m_chain);

}

void EventLoop::execute()
{
  // sanity check. m_chain must not be zero
  if (!m_chain)
  {
    throw std::runtime_error("Calling execute while the event loop was not initialized.");
  }
  // here we do the actual event loop
  ofstream out("outputFile.dat");
  for (int i = 0; i < m_chain->GetEntries(); ++i)
  {
    // event number printout
    if (i % 1000 == 0){
      std::cout << "Event " << i << std::endl;
    }
    // read the data for i-th event
    m_chain->GetEntry(i);






    // what do we want to print?????
    //test: printin "event" variable
    //every 1000 entries of the input dataset
 
    if (i % 1000 == 0){
      std::cout << "event = " << m_data->event << std::endl;
      out << m_chain->GetEntry(i) << "\t" << m_data->event  << "\n";
    }
  }

  out.close();

}