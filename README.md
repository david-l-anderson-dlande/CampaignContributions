# CampaignContributions
My solution(s) to the Insight Data Engineering February 2018 coding challenge.



# How to operate this

To be filled out when I'm "done" writing it.

Written in Python 3.5.2



# Development history

Nothing useful here, unless you're reading this for Data Insight Engineering; it may be useful then, if possibly rather verbose.


Strategy: first write unit tests to make sure I'm doing everything necessary.
Write code to pass them with the sample data provided by Insight (`itcont.txt`).
(I will probably need to add some cases for things they want to test.)

Once that is functional, download a large set from fec.gov, and work on performance.

Identify repeat donors, by combination of name and zip code, though only output zip code.

For a repeat donor, calculate total contribution, number of contributions, and compare to percentile input.

Things to test:
*Check that `percentile.txt` exists, and contains an integer between 0 and 100. (And nothing else?)
*Correctly read in file
*Correctly skip entries where:
        * `OTHER_ID` is not empty
        * `TRANSACTION_DT` is  empty or malformed (should be MMDDYYYY)
        * `ZIP_CODE` is empty or fewer than 5 digits
        * `NAME` is empty or malformed (Just check for empty, as making assumptions about names is...bad)
        * `CMTE_ID` is empty or malformed
        * `TRANSACTION_AMT` is empty
        (I will want to skip these as a first step, for later performance reasons)
*Correctly identify repeat donors
*correctly calculate total amount donated by donor
*correctly calculate number of donations from zip code from repeat donors
*Correctly calculate nearest-rank percentile
        *(Will need to be redone for each new record from a repeat donor, so performance may be an issue)
*Correctly round in percentile calculation.
*Correctly create `repeat_donors.txt`
        *Correctly fill with `CMTE_ID|ZIP_CODE(5digits)|YYYY|percentile|total_amt_this_donor|number_donations


Once that's working, deal with scaling; keeping track of data for repeat donors and running calculations looks like where scaling is going to be an issue.

Don't worry about directory structure until the very end.

After a couple of quick and dirty tests:
*Mashing a bunch of booleans (for skipping entry) will work
*Nearest-rank percentile with the floor division right in an ordered array of donations will work







