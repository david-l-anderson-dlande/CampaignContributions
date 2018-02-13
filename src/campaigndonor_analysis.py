# campaigndonor_analysis.py
# I apologize for not building this as a class; future work.

import os
import bisect
import glob
from datetime import datetime


withinlinedict = {'CMTE_ID':0,
'NAME':7,
'ZIP_CODE':10,
'TRANSACTION_DT':13,
'TRANSACTION_AMT':14,
'OTHER_ID':15}




def cdanalysis(infolder = 'input', outfolder = 'output',\
               datainfile = 'itcont.txt', dataoutfile = 'repeat_donors.txt',\
               percentfile = 'percentile.txt'):

    percent_interest = percentileread(os.path.join(infolder, percentfile))
    donor_dict = {}
    contribution_dict = {}

    with open(os.path.join(outfolder, dataoutfile), 'w') as rd:
        with open(os.path.join(infolder, datainfile), 'r') as f:
            for line in f:
                if is_valid(line):

                    donor_string = line.split('|')[withinlinedict['ZIP_CODE']][:5]+'|'+line.split('|')[withinlinedict['NAME']]
                    current_date = datetime.strptime(line.split('|')[withinlinedict['TRANSACTION_DT']], '%m%d%Y')
                    if repeatdonor(donor_string, current_date, donor_dict):

                        ident_string = line.split('|')[withinlinedict['CMTE_ID']]+'|'+line.split('|')[withinlinedict['ZIP_CODE']][:5]+'|'+line.split('|')[withinlinedict['TRANSACTION_DT']][4:]
                        amount = float(line.split('|')[withinlinedict['TRANSACTION_AMT']])
                        newcontribution(ident_string, amount, contribution_dict)
                        
                        percen = str(percentile(percent_interest, contribution_dict[ident_string]))
                        amt = str(amountdonated(contribution_dict[ident_string]))
                        num = str(donationcount(contribution_dict[ident_string]))
                        rd.write(ident_string+'|'+percen+'|'+amt+'|'+num+'\n')

                    else:
                        adddonor(donor_string, current_date, donor_dict)






def percentileread(percentfilename):
    percent = list(open(percentfilename))[0]
    float(percent)
    if not (0 < float(percent) <= 100):
        raise ValueError("percentile out of range (must be 0 < percentile <= 100)")
    return float(percent)





def is_valid(inputstring):
    vcid = validcmteid(inputstring.split('|')[withinlinedict['CMTE_ID']])
    vname = nameexists(inputstring.split('|')[withinlinedict['NAME']])
    vzip = validzipcode(inputstring.split('|')[withinlinedict['ZIP_CODE']])
    vdate = validdate(inputstring.split('|')[withinlinedict['TRANSACTION_DT']])
    vtran = validtransaction(inputstring.split('|')[withinlinedict['TRANSACTION_AMT']])
    vother = emptyotherid(inputstring.split('|')[withinlinedict['OTHER_ID']])
    return vcid and vname and vzip and vdate and vtran and vother


def validcmteid(cmtestring):
    cmteisvalid=True
    if len(cmtestring) != 9:
        cmteisvalid = False
    return cmteisvalid

def nameexists(namestring):
    nameisempty=True
    if len(namestring) == 0:
        nameisempty = False
    return nameisempty

def validzipcode(zipstring):
    zipcodeisvalid=True
    if len(zipstring) < 5:
        zipcodeisvalid = False
    return zipcodeisvalid

def validdate(datestring):
    dateisvalid=True
    if len(datestring) != 8:
        dateisvalid = False
    try: datetime.strptime(datestring, '%m%d%Y')
    except ValueError:
        dateisvalid = False
    return dateisvalid

def validtransaction(amtstring):
    amtisvalid=True
    if len(amtstring) == 0:
        amtisvalid = False
    try: int(amtstring)
    except ValueError:
        amtisvalid = False
    return amtisvalid

def emptyotherid(otheridstring):
    otherisempty=True
    if len(otheridstring) > 0:
        otherisempty = False
    return otherisempty

# Yeah, there's a lot of these stupid things,
# but they're all just that teensy different. Future improvement.




def repeatdonor(identifierstring, date, donordictionary):
    donorisrepeat = False
    if identifierstring in donordictionary and donordictionary[identifierstring]<=date:
        donorisrepeat = True
    return donorisrepeat

def amountdonated(donationlist):
    return round(sum(donationlist))

def donationcount(donationlist):
    return len(donationlist)

def percentile(percentile_value, donationlist):
    if percentile_value == 100:
        returnpercentile = donationlist[-1]
    else:
        returnpercentile = donationlist[round(percentile_value*len(donationlist)//100)]
    return round(returnpercentile)



def adddonor(identifierstring, date, donor_dict):
    if (identifierstring not in donor_dict) \
        or (identifierstring in donor_dict and date < donor_dict[identifierstring]):
        donor_dict[identifierstring] = date
    return donor_dict


def newcontribution(identifierstring, value, contribution_dict):
    if identifierstring in contribution_dict:
        templist = contribution_dict[identifierstring]
        bisect.insort(templist, value)
        contribution_dict[identifierstring] = templist
    elif identifierstring not in contribution_dict:
        contribution_dict[identifierstring] = [value]
    return contribution_dict



if __name__ == '__main__':
    cdanalysis()
