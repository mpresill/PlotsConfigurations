
#!/bin/bash

set -e 
DATE=10Nov2021_2016
DIR=$PWD
JOB="/afs/cern.ch/work/m/mpresill/Latino/jobs"
#QUEUE="espresso" #
#QUEUE="workday" 
QUEUE="longlunch"
newQUEUE="workday"


#for year in Full2017nano_STXS_1p1 Full2018nano_STXS_1p1 #Full2016nano_STXS_1p1 Full2017nano_STXS_1p1 Full2018nano_STXS_1p1
#do
#    YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "nano" '{print $1}'`
#    echo " --> $year"
#    cd $DIR; cd $year
    #cd $JOB/mkShapes__VBS_ZV${DATE} 
    #cd $JOB/NanoGardening__Summer16_102X_nAODv7_Full2016v7
    for i in /afs/cern.ch/work/m/mpresill/Latino/jobs/mkShapes__VBS_ZV_${DATE}/*jid
    #for i in *jid
    do 
	CHECK=`echo "$i" | awk -F "/" '{print $NF}'`
        if [ ${CHECK} == "*jid" ]
        then
            echo "CONGRATULATION ALL JOB FINISHED"
        else    
	    echo "sed -i \"s/${QUEUE}/${newQUEUE}/g\" ${i/jid/jds}"
	    sed -i "s/${QUEUE}/${newQUEUE}/g" ${i/jid/jds}
	    condor_submit ${i/jid/jds}
	fi
    done
#done

        cd $DIR
        
condor_q


#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done
