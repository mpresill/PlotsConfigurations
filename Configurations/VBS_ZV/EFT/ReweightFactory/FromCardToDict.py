import os
from collections import OrderedDict

def CardToDict(dim, op = ""):
    coeffdict = OrderedDict()
    
    if not "rwgcard" in os.getcwd():
        cardpath = "./" + dim
        #rwgcard = open("rwgcards/" + dim + "_" + op + ".txt", "r")
    else:
        cardpath = dim + ""
    if op != "":
        cardpath += "_" + op
    cardpath += ".txt"
    print("Opening card", cardpath)
    rwgcard = open(cardpath, "r")
    
    if dim == "dim8":
        interlines = [line.replace("\n","").replace("\t", "") for line in rwgcard.readlines() if line.startswith("launch") or line.startswith("\t")]
    elif dim == "dim6":
        interlines = [line.replace("\n","").replace("   set", "set") for line in rwgcard.readlines() if line.startswith("# c")]
    
    coeff = ""
    valstr = ""
    sign = ""
    idl = 0
    idc = 0
    for idl, line in enumerate(interlines):
        line = interlines[idl]

        if dim == "dim8" and line.startswith("launch"):
            flag = line.split("=")[-1]
            if flag.endswith("_0p0"):
                flag = flag.replace("_0p0", "_0")
            coeff, val = flag.split("_")
            val = val.replace("m", "")
            try:
                coeffdict[coeff] is None
            except KeyError:
                coeffdict[coeff] = OrderedDict()
            else:
                pass

        elif dim == "dim8" and line.startswith("set ano"):
            value = float(line.split("anoinputs")[-1].split(" ")[-1].split("e")[0])

            if (value != 0 and val != "0"):
                if val not in coeffdict[coeff].keys():
                    coeffdict[coeff][val] = [None, None]
                if flag == op:
                    if "_m" in flag:
                        idx = 0
                    else:
                        idx = 1
                    coeffdict[coeff][val][idx] = -1
                    continue
                if value < 0.:
                    coeffdict[coeff][val][0] = idc
                elif value > 0.:
                    coeffdict[coeff][val][1] = idc
                idc += 1

            elif (value == 0 and val == "0"):
                if val not in coeffdict[coeff].keys():
                    coeffdict[coeff][val] = [None, None]
                    coeffdict[coeff][val][0] = idc
                    coeffdict[coeff][val][1] = idc
                    idc += 1
                else:
                    pass
        
        elif dim == "dim6":
            coeff = ""
            val = ""

            rline = line.replace("#", "")
            coeffs = [rl.replace(",", "") for rl in rline.split(" ") if rl.startswith("c")]
            IsSingle = False
            if len(coeffs) == 1:
                IsSingle = True
            
            for ecoeff in coeffs:
                if IsSingle:
                    coeff, val = ecoeff.split("=")
                    value = float(val)
                    val = val.replace("-", "").replace(".", "p")
                    
                else:
                    if coeff == "":
                        coeff += ecoeff.split("=")[0]
                        val += ecoeff.split("=")[1]
                    else:
                        coeff += "_" + ecoeff.split("=")[0]
                        val += "_" + ecoeff.split("=")[1]
                    
                try:
                    coeffdict[coeff] is None
                except KeyError:
                    coeffdict[coeff] = OrderedDict()
                    if "_" in coeff:
                        coeffdict[coeff]['0_0'] = [0, 0]
                    else:
                        coeffdict[coeff]['0'] = [0, 0]
                    if idc == 0:
                        idc += 1
                else:
                    pass

            if val not in coeffdict[coeff].keys():
                coeffdict[coeff][val] = [None, None]
            if value < 0.:
                coeffdict[coeff][val][0] = idc
            elif value > 0.:
                coeffdict[coeff][val][1] = idc
            idc += 1
    
    print('ehi', coeffdict)
    return coeffdict
    

#for k, v in CardToDict("dim8", "FT1_2p0").items():
#top = ""
#for k, v in CardToDict("dim6").items():
    #print("\ncoeff\t", k)
    #print(k)
    #for kv, vv in v.items():
        #print("\n", kv)
        #print(vv)
    #print(v)
    #cfs = k.split("_")
    #vs = list(v.keys())[1].split("_")
    
    #top = ""
    #if top != "":
        #top += ","
    #for idc, cf in enumerate(cfs):
        #if top != "":
            #top += "_"
        #else:
            #top += '\"'
        #if not top.endswith(",") and top != "":
            #top += ":"
        #top += cf + "_" + str(vs[idc])
    #top += '\",'
#print(top)
CardToDict("dim8", "FT1_2p0")
#CardToDict("dim6")
