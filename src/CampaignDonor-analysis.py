# CampaignDonor-analysis.py

import os
import bisect
import glob
from datetime import datetime




def datetesting(datestring):
	dateisvalid=True
	try: datetime.strptime(datestring, '%m%d%Y')
	except ValueError:
		dateisvalid = False
	return dateisvalid
