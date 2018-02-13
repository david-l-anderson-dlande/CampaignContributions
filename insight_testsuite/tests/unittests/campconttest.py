#campconttest.py

import unittest
import CampaignDonor_analysis




class Input(unittest.TestCase):
    def setupClass(self):
        pass

    def teardownClass(self):
        pass

    def test_readline(self):
        """readline should read the given line in a file"""
        #stuff goes here

    def test_percentilereadlow(self):
        """percentileread should only accept values >0"""
        #stuff goes here
    def test_percentilereadhigh(self):
        """percentileread should only accept values<=100 """
        #stuff goes here
    def test_percentilereadnumber(self):
        """percentileread should only accept numerical values"""
        #stuff goes here
    def test_percentilereadgood(self):
        """percentileread should accept numerical values between 0 and 100"""
        #stuff goes here







class ValidatingData(unittest.TestCase):
    def setupClass(self):
        pass

    def teardownClass(self):
        pass

    def test_emptyotheridempty(self):
        """emptyotherid should only accept OTHER_ID values which are empty"""
        #stuff goes here
    def test_emptyotheridnotempty(self):
        """emptyotherid should not accept OTHER_ID values which are not empty"""
        #stuff goes here


    def test_validzipcodeless(self):
        """validzipcode should not accept ZIP_CODE values which are < 5 digits"""
        #stuff goes here
    def test_validzipcodemore(self):
        """validzipcode should only accept ZIP_CODE values which are >= 5 digits"""
        #stuff goes here

    def test_emptynameempty(self):
        """emptyname should not accept NAME values which are empty"""
        #stuff goes here
    def test_emptynamefull(self):
        """emptyname should accept NAME values which are not empty"""
        #stuff goes here

    def test_validcmteid(self):
        """validcmteid should only accept CMTE_ID values which are 9 characters"""
        #stuff goes here
    def test_validcmteidless(self):
        """validcmteid should not accept CMTE_ID values < 9 characters"""
        #stuff goes here
    def test_validcmteidmore(self):
        """validcmteid should not accept CMTE_ID values > 9 characters"""
        #stuff goes here

    def test_emptytransactionamtempty(self):
        """emptytransactionamt should not accept TRANSACTION_AMT values which are empty"""
        #stuff goes here
    def test_emptytransactionamtfull(self):
        """emptytransactionamt should accept TRANSACTION_AMT values which are not empty"""
        #stuff goes here
    def test_emptytransactionamtnum(self):
        """emptytransactionamt should not accept TRANSACTION_AMT values which are not numbers"""
        #stuff goes here

    def test_datelength(self):
        """validdate should only accept TRANSACTION_DT values which are 8 characters"""
        #stuff goes here
    def test_datelengthgreater(self):
        """validdate should not accept TRANSACTION_DT values > 8 characters"""
        #stuff goes here
    def test_datelengthless(self):
        """validdate should not accept TRANSACTION_DT values < 8 characters"""
        #stuff goes here
    def test_validdate(self):
        """validdate should only accept TRANSACTION_DT values which represent valid dates"""
        #stuff goes here








class ContributionCalculations(unittest.TestCase):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_identifyrepeatdonors(self):
        """repeatdonors should correctly identify previous donors"""
        #stuff goes here
    def test_identifyfirstdonors(self):
        """repeatdonors should add first-time donors"""
        #stuff goes here
    def test_identifyoutoforder(self):
        """repeatdonors should correctly change dates for earliest donation"""
        #stuff goes here

    def test_newcontribution(self):
        """newcontribution should correctly add the new amount to the list"""
        #stuff goes here

    def test_firstcontribution(self):
        """first contribution should correctly add to the calculated donor dictionary"""
        #stuff goes here


    def test_amountdonated(self):
        """amountdonated should correctly calculate the total amount donated"""
        #stuff goes here

    def test_donationcount(self):
        """donationcount should correctly calculate the number of donations"""
        #stuff goes here

    def test_donationround(self):
        """donationcount should correctly return a whole dollar amount"""
        #stuff goes here
    





    

class Output(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_writeline(self):
        """writeline should write the correct thing in a file"""
        #stuff goes here





if __name__ == "__main__":
    unittest.main()
