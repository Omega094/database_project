"""This script processes the data"""
import collections
DATE = 0
OPEN = "OPEN"
HIGH = "HIGH"
LOW  = "LOW"
CLOSE= "CLOSE"
VOLUME = "VOLUME"
ADJ_CLOSE = "ADJ_CLOSE"

class StockInfoProcessor(object):

	def __init__(self, fileName):
		self.stockName = fileName
		self.stockPriceInfor = collections.OrderedDict()
		"""Read the file and store all price information"""
		with open(fileName) as f:
			for line in f:
				if line[0].isdigit():
					infor = line.split(",")
					currentInfor = {}
					date = infor[DATE]
					currentInfor[OPEN] =float(infor[1].rstrip("\n\r"))
					currentInfor[HIGH] = float(infor[2].rstrip("\n\r"))
					currentInfor[LOW] = float(infor[3].rstrip("\n\r"))
					currentInfor[CLOSE] = float(infor[4].rstrip("\n\r"))
					currentInfor[VOLUME] = int(infor[5].rstrip("\n\r"))
					currentInfor[ADJ_CLOSE] = float(infor[6].rstrip("\n\r"))
					self.stockPriceInfor[date] = currentInfor
		
					
					
					
		
		
		

	
	
	
if __name__ == "__main__":
	aapl = StockInfoProcessor("AAPL_price.csv")
	for date, priceInfo in aapl.stockPriceInfor.iteritems():
		print date, priceInfo
	