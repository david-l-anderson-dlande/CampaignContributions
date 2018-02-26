#campconttest.py

import unittest
import os
from campaigndonor_analysis import *





class Input(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f_read = open('input/test_itcont.txt')
        cls.percentinput = glob.glob('input/percentile_*')
        cls.percentinput.sort()

    @classmethod
    def tearDownClass(cls):
        cls.f_read.close()
        #cls.percentinput.close()


    def test_percentile_readlow(self):
        """percentile_read should only accept values >0"""
        self.assertRaises(ValueError, percentile_read, self.percentinput[5])
        
    def test_percentile_readhigh(self):
        """percentile_read should only accept values<=100 """
        self.assertRaises(ValueError, percentile_read, self.percentinput[4])

    def test_percentile_readnumber(self):
        """percentile_read should only accept numerical values"""
        self.assertRaises(ValueError, percentile_read, self.percentinput[3])

    def test_percentile_readgood(self):
        """percentile_read should accept numerical values between 0 and 100"""
        self.assertEqual(float(100), percentile_read(self.percentinput[0]))
        self.assertEqual(float(80), percentile_read(self.percentinput[2]))
        self.assertEqual(float(30), percentile_read(self.percentinput[1]))






class ValidatingData(unittest.TestCase):
    @classmethod   
    def setUpClass(cls):
        cls.f_read = open('input/test_itcont.txt')
        cls.t_list = list(cls.f_read)

    @classmethod
    def tearDownClass(cls):
        cls.f_read.close()



    def test_is_valid_otheridnotempty(self):
        """is_valid_otherid should not accept OTHER_ID values which are not empty"""
        self.assertFalse(is_valid_otherid(self.t_list[0].split('|')[withinlinedict['OTHER_ID']]))

    def test_is_valid_otheridempty(self):
        """is_valid_otherid should only accept OTHER_ID values which are empty"""
        self.assertTrue(is_valid_otherid(self.t_list[1].split('|')[withinlinedict['OTHER_ID']]))

    def test_is_valid_lineotheridnotempty(self):
        """is_valid_line should not accept OTHER_ID values which are not empty"""
        self.assertFalse(is_valid_line(self.t_list[0].split('|')))

    def test_is_valid_lineotheridempty(self):
        """is_valid_line should only accept OTHER_ID values which are empty"""
        self.assertTrue(is_valid_line(self.t_list[1].split('|')))



    def test_is_valid_zipcodeless(self):
        """is_valid_zipcode should not accept ZIP_CODE values which are < 5 digits"""
        self.assertFalse(is_valid_zipcode(self.t_list[2].split('|')[withinlinedict['ZIP_CODE']]))

    def test_is_valid_zipcodemore(self):
        """is_valid_zipcode should only accept ZIP_CODE values which are >= 5 digits"""
        self.assertTrue(is_valid_zipcode(self.t_list[3].split('|')[withinlinedict['ZIP_CODE']]))

    def test_is_valid_linezipcodeless(self):
        """is_valid_line should not accept ZIP_CODE values which are < 5 digits"""
        self.assertFalse(is_valid_line(self.t_list[2].split('|')))

    def test_is_valid_linezipcodemore(self):
        """is_valid_line should only accept ZIP_CODE values which are >= 5 digits"""
        self.assertTrue(is_valid_line(self.t_list[3].split('|')))



    def test_is_name_existempty(self):
        """emptyname should not accept NAME values which are empty"""
        self.assertFalse(is_name_exist(self.t_list[4].split('|')[withinlinedict['NAME']]))

    def test_is_name_existfull(self):
        """emptyname should accept NAME values which are not empty"""
        self.assertTrue(is_name_exist(self.t_list[5].split('|')[withinlinedict['NAME']]))

    def test_is_valid_linename_existempty(self):
        """is_valid_line should not accept NAME values which are empty"""
        self.assertFalse(is_valid_line(self.t_list[4].split('|')))

    def test_is_valid_linename_existfull(self):
        """is_valid_line should accept NAME values which are not empty"""
        self.assertTrue(is_valid_line(self.t_list[5].split('|')))



    def test_is_valid_cmteid(self):
        """is_valid_cmteid should only accept CMTE_ID values which are 9 characters"""
        self.assertTrue(is_valid_cmteid(self.t_list[6].split('|')[withinlinedict['CMTE_ID']]))

    def test_is_valid_cmteidless(self):
        """is_valid_cmteid should not accept CMTE_ID values < 9 characters"""
        self.assertFalse(is_valid_cmteid(self.t_list[7].split('|')[withinlinedict['CMTE_ID']]))

    def test_is_valid_cmteidmore(self):
        """is_valid_cmteid should not accept CMTE_ID values > 9 characters"""
        self.assertFalse(is_valid_cmteid(self.t_list[8].split('|')[withinlinedict['CMTE_ID']]))

    def test_is_valid_linecmteid(self):
        """is_valid_line should only accept CMTE_ID values which are 9 characters"""
        self.assertTrue(is_valid_line(self.t_list[6].split('|')))

    def test_is_valid_linecmteidless(self):
        """is_valid_line should not accept CMTE_ID values < 9 characters"""
        self.assertFalse(is_valid_line(self.t_list[7].split('|')))

    def test_is_valid_linecmteidmore(self):
        """is_valid_line should not accept CMTE_ID values > 9 characters"""
        self.assertFalse(is_valid_line(self.t_list[8].split('|')))



    def test_is_valid_transactionamtempty(self):
        """is_valid_transactionamt should not accept TRANSACTION_AMT values which are empty"""
        self.assertFalse(is_valid_transaction(self.t_list[9].split('|')[withinlinedict['TRANSACTION_AMT']]))

    def test_is_valid_transactionamtfull(self):
        """is_valid_transactionamt should accept TRANSACTION_AMT values which are not empty and are numbers"""
        self.assertTrue(is_valid_transaction(self.t_list[10].split('|')[withinlinedict['TRANSACTION_AMT']]))

    def test_is_valid_transactionamtnum(self):
        """is_valid_transactionamt should not accept TRANSACTION_AMT values which are not numbers"""
        self.assertFalse(is_valid_transaction(self.t_list[11].split('|')[withinlinedict['TRANSACTION_AMT']]))

    def test_is_valid_linetransactionamtempty(self):
        """is_valid_line should not accept TRANSACTION_AMT values which are empty"""
        self.assertFalse(is_valid_line(self.t_list[9].split('|')))

    def test_is_valid_linetransactionamtfull(self):
        """is_valid_line should accept TRANSACTION_AMT values which are not empty and are numbers"""
        self.assertTrue(is_valid_line(self.t_list[10].split('|')))

    def test_is_valid_linetransactionamtnum(self):
        """is_valid_line should not accept TRANSACTION_AMT values which are not numbers"""
        self.assertFalse(is_valid_line(self.t_list[11].split('|')))



    def test_datelength(self):
        """is_valid_date should only accept TRANSACTION_DT values which are 8 characters"""
        self.assertTrue(is_valid_date(self.t_list[12].split('|')[withinlinedict['TRANSACTION_DT']]))

    def test_datelengthgreater(self):
        """is_valid_date should not accept TRANSACTION_DT values > 8 characters"""
        self.assertFalse(is_valid_date(self.t_list[13].split('|')[withinlinedict['TRANSACTION_DT']]))

    def test_datelengthless(self):
        """is_valid_date should not accept TRANSACTION_DT values < 8 characters"""
        self.assertFalse(is_valid_date(self.t_list[14].split('|')[withinlinedict['TRANSACTION_DT']]))

    def test_is_valid_date(self):
        """is_valid_date should only accept TRANSACTION_DT values which represent valid dates"""
        self.assertFalse(is_valid_date(self.t_list[15].split('|')[withinlinedict['TRANSACTION_DT']]))

    def test_is_valid_line_datelength(self):
        """is_valid_line should only accept TRANSACTION_DT values which are 8 characters"""
        self.assertTrue(is_valid_line(self.t_list[12].split('|')))

    def test_is_valid_line_datelengthgreater(self):
        """is_valid_line should not accept TRANSACTION_DT values > 8 characters"""
        self.assertFalse(is_valid_line(self.t_list[13].split('|')))

    def test_is_valid_line_datelengthless(self):
        """is_valid_line should not accept TRANSACTION_DT values < 8 characters"""
        self.assertFalse(is_valid_line(self.t_list[14].split('|')))

    def test_is_valid_is_valid_line_date(self):
        """is_valid_line should only accept TRANSACTION_DT values which represent valid dates"""
        self.assertFalse(is_valid_line(self.t_list[15].split('|')))







class ContributionCalculations(unittest.TestCase):

    def setUp(self):
        self.repeat_test_dict = {'first':2017, 'third':2016}
        self.contribution_test_dict = {'first':[2,3]}
        self.donation_test_list = [333, 384, 203, 50.30]
        self.percentile_test_list = [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20]
            #straight from Wikipedia

    def tearDown(self):
        pass  # this gets run after each test, whether or not the test passed/failed


    def test_identifyrepeat_donors(self):
        """repeat_donors should correctly identify previous donors"""
        self.assertTrue(repeat_donor('first', 2018, self.repeat_test_dict))

    def test_identifyfirstdonors(self):
        """repeat_donors should identify first-time donors"""
        self.assertFalse(repeat_donor('second', 2018, self.repeat_test_dict))

    def test_addfirstdonors(self):
        """add_donor should add first-time donors"""
        self.assertEqual({'first':2017, 'second':2018, 'third':2016}, add_donor('second', 2018, self.repeat_test_dict))

    def test_identifyoutoforder(self):
        """add_donor should correctly change dates for earlier donations"""
        self.assertEqual({'first':2017, 'third':2015}, add_donor('third', 2015, self.repeat_test_dict))



    def test_new_contribution(self):
        """new_contribution should correctly add the new amount to the dictionary"""
        self.assertEqual({'first':[2,3,4]}, new_contribution('first', 4, self.contribution_test_dict))

    def test_firstentry(self):
        """new_contribution should correctly add entries to the contribution dictionary"""
        self.assertEqual({'first':[2,3], 'second':[5]}, new_contribution('second', 5, self.contribution_test_dict))



    def test_amount_donated(self):
        """amount_donated should correctly calculate the total amount donated,
           including rounding"""
        self.assertEqual(970, amount_donated(self.donation_test_list))

    def test_donation_count(self):
        """donation_count should correctly calculate the number of donations"""
        self.assertEqual(4, donation_count(self.donation_test_list))




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





if __name__ == '__main__':
    unittest.main()
