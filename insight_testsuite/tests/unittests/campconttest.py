#campconttest.py

import unittest
import os
from campaigndonor_analysis import *





class Input(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f_read = open('input/test_itcont.txt')
        cls.percentinput = glob.glob('input/percentile*')
        cls.percentinput.sort()

    @classmethod
    def tearDownClass(cls):
        cls.f_read.close()




#    def test_readline(self):
#        """readline should read the given line in a file"""
#        self.assertEqual(readline(self.f_read), 'C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783') 



    def test_percentilereadlow(self):
        """percentileread should only accept values >0"""
        self.assertRaises(ValueError, percentileread, self.percentinput[5])
        
    def test_percentilereadhigh(self):
        """percentileread should only accept values<=100 """
        self.assertRaises(ValueError, percentileread, self.percentinput[4])

    def test_percentilereadnumber(self):
        """percentileread should only accept numerical values"""
        self.assertRaises(ValueError, percentileread, self.percentinput[3])

    def test_percentilereadgood(self):
        """percentileread should accept numerical values between 0 and 100"""
        self.assertEqual(float(100), percentileread(self.percentinput[0]))
        self.assertEqual(float(80), percentileread(self.percentinput[2]))
        self.assertEqual(float(30), percentileread(self.percentinput[1]))





#locations in line from test file
CMTE_ID = 0
NAME = 7
ZIP_CODE = 10
TRANSACTION_DT = 13
TRANSACTION_AMT =14
OTHER_ID =15


class ValidatingData(unittest.TestCase):
    @classmethod   
    def setUpClass(cls):
        cls.f_read = open('input/test_itcont.txt')
        cls.t_list = list(cls.f_read)

    @classmethod
    def tearDownClass(cls):
        cls.f_read.close()



    def test_emptyotheridnotempty(self):
        """emptyotherid should not accept OTHER_ID values which are not empty"""
        self.assertFalse(emptyotherid(self.t_list[0].split('|')[OTHER_ID]))

    def test_emptyotheridempty(self):
        """emptyotherid should only accept OTHER_ID values which are empty"""
        self.assertTrue(emptyotherid(self.t_list[1].split('|')[OTHER_ID]))



    def test_validzipcodeless(self):
        """validzipcode should not accept ZIP_CODE values which are < 5 digits"""
        self.assertFalse(validzipcode(self.t_list[2].split('|')[ZIP_CODE]))

    def test_validzipcodemore(self):
        """validzipcode should only accept ZIP_CODE values which are >= 5 digits"""
        self.assertTrue(validzipcode(self.t_list[3].split('|')[ZIP_CODE]))



    def test_nameexistsempty(self):
        """emptyname should not accept NAME values which are empty"""
        self.assertFalse(nameexists(self.t_list[4].split('|')[NAME]))

    def test_nameexistsfull(self):
        """emptyname should accept NAME values which are not empty"""
        self.assertTrue(nameexists(self.t_list[5].split('|')[NAME]))



    def test_validcmteid(self):
        """validcmteid should only accept CMTE_ID values which are 9 characters"""
        self.assertTrue(validcmteid(self.t_list[6].split('|')[CMTE_ID]))

    def test_validcmteidless(self):
        """validcmteid should not accept CMTE_ID values < 9 characters"""
        self.assertFalse(validcmteid(self.t_list[7].split('|')[CMTE_ID]))

    def test_validcmteidmore(self):
        """validcmteid should not accept CMTE_ID values > 9 characters"""
        self.assertFalse(validcmteid(self.t_list[8].split('|')[CMTE_ID]))



    def test_validtransactionamtempty(self):
        """validtransactionamt should not accept TRANSACTION_AMT values which are empty"""
        self.assertFalse(validtransaction(self.t_list[9].split('|')[TRANSACTION_AMT]))

    def test_validtransactionamtfull(self):
        """validtransactionamt should accept TRANSACTION_AMT values which are not empty and are numbers"""
        self.assertTrue(validtransaction(self.t_list[10].split('|')[TRANSACTION_AMT]))

    def test_validtransactionamtnum(self):
        """validtransactionamt should not accept TRANSACTION_AMT values which are not numbers"""
        self.assertFalse(validtransaction(self.t_list[11].split('|')[TRANSACTION_AMT]))



    def test_datelength(self):
        """validdate should only accept TRANSACTION_DT values which are 8 characters"""
        self.assertTrue(validdate(self.t_list[12].split('|')[TRANSACTION_DT]))

    def test_datelengthgreater(self):
        """validdate should not accept TRANSACTION_DT values > 8 characters"""
        self.assertFalse(validdate(self.t_list[13].split('|')[TRANSACTION_DT]))

    def test_datelengthless(self):
        """validdate should not accept TRANSACTION_DT values < 8 characters"""
        self.assertFalse(validdate(self.t_list[14].split('|')[TRANSACTION_DT]))

    def test_validdate(self):
        """validdate should only accept TRANSACTION_DT values which represent valid dates"""
        self.assertFalse(validdate(self.t_list[15].split('|')[TRANSACTION_DT]))







class ContributionCalculations(unittest.TestCase):

    def setUp(self):
        self.repeat_test_dict = {'first':2017, 'third':2016}
        self.contribution_test_dict = {'first':[2,3]}
        self.donation_test_list = [333, 384, 203, 50.30]
        self.percentile_test_list = [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20]
            #straight from Wikipedia

    def tearDown(self):
        pass  # this gets run after each test, whether or not the test passed/failed


    def test_identifyrepeatdonors(self):
        """repeatdonors should correctly identify previous donors"""
        self.assertTrue(repeatdonor('first', 2018, self.repeat_test_dict))

    def test_identifyfirstdonors(self):
        """repeatdonors should identify first-time donors"""
        self.assertFalse(repeatdonor('second', 2018, self.repeat_test_dict))

    def test_addfirstdonors(self):
        """adddonor should add first-time donors"""
        self.assertEqual({'first':2017, 'second':2018, 'third':2016}, adddonor('second', 2018, self.repeat_test_dict))

    def test_identifyoutoforder(self):
        """adddonor should correctly change dates for earlier donations"""
        self.assertEqual({'first':2017, 'third':2015}, adddonor('third', 2015, self.repeat_test_dict))



    def test_newcontribution(self):
        """newcontribution should correctly add the new amount to the dictionary"""
        self.assertEqual({'first':[2,3,4]}, newcontribution('first', 4, self.contribution_test_dict))

    def test_firstentry(self):
        """newcontribution should correctly add entries to the contribution dictionary"""
        self.assertEqual({'first':[2,3], 'second':[5]}, newcontribution('second', 5, self.contribution_test_dict))



    def test_amountdonated(self):
        """amountdonated should correctly calculate the total amount donated,
           including rounding"""
        self.assertEqual(970, amountdonated(self.donation_test_list))

    def test_donationcount(self):
        """donationcount should correctly calculate the number of donations"""
        self.assertEqual(4, donationcount(self.donation_test_list))




    def test_percentilemax(self):
        """percentile should correctly calculate 100 percentile"""
        self.assertEqual(20, percentile(100, self.percentile_test_list))

    def test_percentile25(self):
        """percentile should correctly calculate 100 percentile"""
        self.assertEqual(7, percentile(25, self.percentile_test_list))

    def test_percentile50(self):
        """percentile should correctly calculate 100 percentile"""
        self.assertEqual(9, percentile(50, self.percentile_test_list))

    def test_percentile75(self):
        """percentile should correctly calculate 100 percentile"""
        self.assertEqual(15, percentile(75, self.percentile_test_list))






    

class Output(unittest.TestCase):

    def test_writeline(self):
        """writeline should write the correct thing in a file"""
        self.assertEqual('CMTE_ID|ZIP_CODE(5digits)|YYYY', readline(writeline('CMTE_ID|ZIP_CODE(5digits)|YYYY')))





if __name__ == '__main__':
    unittest.main()
