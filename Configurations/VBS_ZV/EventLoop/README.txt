with this sets of macros you can:
	- access TTrees in several samples
	- do whatever you want with their branches



how to run?
	make clean
	make -j 8
	python runMe.py


what you can edit quickly?
	input branch to be printed: initialize it in Data.h, declare it in Data.cpp, do whatever you want with this variable (or more than one variable) in EventLoop.cpp
	it allows defining more input samples with same TTree/variable names, to be specified in runMe.py
	

