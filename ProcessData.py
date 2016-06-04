"""This script processes the data"""
import collections
DATE = 0
OPEN = "OPEN"
HIGH = "HIGH"
LOW  = "LOW"
CLOSE= "CLOSE"
VOLUME = "VOLUME"
ADJ_CLOSE = "ADJ_CLOSE"
INTEREST_SCORE = "INTEREST_SCORE"
START = "START"
END = "END"
 
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
					date = int(infor[DATE].replace("-", ""))
					currentInfor[OPEN] =float(infor[1].rstrip("\n\r"))
					currentInfor[HIGH] = float(infor[2].rstrip("\n\r"))
					currentInfor[LOW] = float(infor[3].rstrip("\n\r"))
					currentInfor[CLOSE] = float(infor[4].rstrip("\n\r"))
					currentInfor[VOLUME] = int(infor[5].rstrip("\n\r"))
					currentInfor[ADJ_CLOSE] = float(infor[6].rstrip("\n\r"))
					self.stockPriceInfor[date] = currentInfor
		
				
class trendingDataProcessor(object):

	def __init__(self, fileName):
		self.stockName = fileName
		self.trendingInfor = collections.OrderedDict()
		"""Read the file and store all price information"""
		with open(fileName) as f:
			for i, line in enumerate(f):
				if line[0].isdigit():
					infor = line.split(",")
					currentInfor = {}
					dateInfor = infor[DATE].split(" - ")
					print line
					startDate = dateInfor[0].replace("-","")
					endDate = dateInfor[1].replace("-","")
					currentInfor[START] = int(startDate)
					currentInfor[END] = int(endDate)
					currentInfor[INTEREST_SCORE] = int(infor[1].rstrip("\n\r"))
					self.trendingInfor[i] = currentInfor
					
					
		
 
if __name__ == "__main__":
	#aapl = StockInfoProcessor("AAPL.csv")
	#for date, priceInfo in aapl.stockPriceInfor.iteritems():
	#	print date, priceInfo

	#with open("AAPL.csv") as f:
	#	for line in f:
	#		print line
	
	aapl = trendingDataProcessor("AAPL.csv")
	for i, info in aapl.trendingInfor.iteritems():
		print i , info
		
		
		

