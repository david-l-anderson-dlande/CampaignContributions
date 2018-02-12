#campconttest.py

import unittest
import CampaignDonor-analysis

class Input(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_readline(self):
        """readline should read the given line in a file"""
        #stuff goes here

    def test_percentileread(self):
        """percentileread should only accept correct values"""
        #stuff goes here

class ValidatingData(unittest.TestCase):
    def setupClass(self):
        pass

    def teardownClass(self):
        pass

    def test_emptyotherid(self):
        """emptyotherid should only accept OTHER_ID values which are empty"""
        #stuff goes here

    def test_validzipcode(self):
        """validzipcode should only accept ZIP_CODE values which are >= 5 digits"""
        #stuff goes here

    def test_emptyname(self):
        """emptyname should not accept NAME values which are empty"""
        #stuff goes here

    def test_validcmteid(self):
        """validcmteid should only accept CMTE_ID values which are 9 characters"""
        #stuff goes here

    def test_emptytransactionamt(self):
        """emptytransactionamt should not accept TRANSACTION_AMT values which are empty"""
        #stuff goes here

    def test_datelength(self):
        """validdate should only accept TRANSACTION_DT values which are 8 characters"""
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
        """identifyrepeatdonors should correctly identify previous donors"""
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
