# CampaignContributions
My solution(s) to the Insight Data Engineering February 2018 coding challenge.



# How to operate this

Written in Python 3.5.2 on Ubuntu 16.04, requires nothing that doesn't come with Python by default on that system.

If you want to run the unit tests, run `run_unittests.sh` in `CampaignContributions/insight_testsuite/tests/unittests`.

Otherwise, just hit `bash run.sh` in the topmost directory, and it will do what it should.



# Development history

Nothing useful here, unless you're reading this for Data Insight Engineering; it may be useful then, if possibly rather verbose.


Strategy: first write unit tests to make sure I'm doing everything necessary.
Write code to pass them with the sample data provided by Insight (`itcont.txt`).
(I will probably need to add some cases for things they want to test.)

Once that is functional, download a large set from fec.gov, and work on performance.

Identify repeat donors, by combination of name and zip code, though only output zip code.

For a repeat donor, calculate total contribution, number of contributions, and compare to percentile input.

Things to test:
* Check that `percentile.txt` exists, and contains an integer between 0 and 100. (And nothing else?)
* Correctly read in file
* Correctly skip entries where:
        * `OTHER_ID` is not empty
        * `TRANSACTION_DT` is  empty or malformed (should be MMDDYYYY)
        * `ZIP_CODE` is empty or fewer than 5 digits
        * `NAME` is empty or malformed (Just check for empty, as making assumptions about names is...bad)
        * `CMTE_ID` is empty or malformed
        * `TRANSACTION_AMT` is empty
        (I will want to skip these as a first step, for later performance reasons)
* Correctly identify repeat donors
* Correctly calculate total amount donated to recipient from zip in current year from repeat donors
* Correctly calculate number of donations to recipient from zip in current year from repeat donors
* Correctly calculate nearest-rank percentile of donations to recipient from zip in current year from repeat donors
        * (Will need to be redone for each new record from a repeat donor, so performance may be an issue)
* Correctly round in percentile calculation; i.e. donation amounts
* Correctly create `repeat_donors.txt`
        * Correctly fill with `CMTE_ID`|`ZIP_CODE`(5digits)|YYYY|percentile|total_amt_this_recipient_fromthisZipCodeandYear|number_donations_this_recipient_fromthisZipCodeandYear


Once that's working, deal with scaling; keeping track of data for repeat donors and running calculations looks like where scaling is going to be an issue.

Don't worry about directory structure until the very end.

After a couple of quick and dirty tests:
* Mashing a bunch of booleans (for skipping entry) will work
* Nearest-rank percentile with the floor division right in an ordered array of donations will work
* .split() will work fine for dealing with each line of data
* Simply turning a short file into a list (for testing) will work

Adding new values to the list of donated values will probably be most efficiently done by finding and inserting, not adding and sorting, though I should test.

I lied about the directory structure; already in place.

First pass at data structure will be a dictionary with keys of `CMTE_ID|ZIP_CODE(5digits)|YYYY`, and values of sorted tuples of rounded donation values.
Use bisect.insort to add to appropriate lists.

Use dictionary with keys of `ZIP_CODE|NAME` and values of date to store whether we have repeat donors or not. If date is greater than stored one, we have a repeat donor. If less, replace date.

Don't test very basic things like whether or not input files exist. Python already raises errors for those.

Need to remember definition of 100th percentile; also, acceptable values are not just integers.

In news that will surprise nobody, tests take more writing than the actual program.

Also, bash scripts are bastards.

Okay, got those figured out, though it looks like the the Insight-provided tests are insisting on writing `repeat_donors.txt` as a unit test.

Definitely don't worry about testing reading in from a file (too trivial).

Weird; there is one raise exception test which is raising an exception, but not passing.

Heh. It works.

A bit of cleanup to make the Insight test happy and a couple of other minor things.


