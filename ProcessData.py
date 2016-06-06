"""This script processes the data"""
import collections
DATE = 0
DATA_ID = "DATA_ID"
OPEN = "OPEN"
HIGH = "HIGH"
LOW  = "LOW"
CLOSE= "CLOSE"
VOLUME = "VOLUME"
ADJ_CLOSE = "ADJ_CLOSE"
INTEREST_SCORE = "INTEREST_SCORE"
START = "START"
END = "END"

#Frmatted in this way so we can do a batch insertion. 
stockInfo = (	
				{"COMPANY_NAME":"GOOGLE", "NAME": "GOOG"},
				{"COMPANY_NAME":"APPLE", "NAME": "AAPL"},
				{"COMPANY_NAME":"BANK OF AMERICA", "NAME": "BAC"},
				{"COMPANY_NAME":"MICROSOFT", "NAME": "MSFT"},
				{"COMPANY_NAME":"PFIZER", "NAME": "PFE"},
			)


class StockInfoProcessor(object):

	def __init__(self, fileName, stockName):
		self.stockName = fileName
		self.stockPriceInfor = collections.OrderedDict()
		self.stockPriceInforList = []
		"""Read the file and store all price information"""
		with open(fileName) as f:
			counter = 0
			for line in f:
				if line[0].isdigit():
					infor = line.split(",")
					currentInfor = {}
					currentInfor[DATA_ID] = counter
					date = int(infor[DATE].replace("-", ""))
					currentInfor["NAME"] = stockName
					currentInfor["DATE"] = date
					currentInfor[OPEN] =float(infor[1].rstrip("\n\r"))
					currentInfor[HIGH] = float(infor[2].rstrip("\n\r"))
					currentInfor[LOW] = float(infor[3].rstrip("\n\r"))
					currentInfor[CLOSE] = float(infor[4].rstrip("\n\r"))
					currentInfor[VOLUME] = int(infor[5].rstrip("\n\r"))
					currentInfor[ADJ_CLOSE] = float(infor[6].rstrip("\n\r"))
					self.stockPriceInfor[date] = currentInfor
					self.stockPriceInforList.append(currentInfor)
					counter += 1
		return 


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
		return 





#Batch insertions
def insertStockToDatabase(stocks):
	import psycopg2
	conn = psycopg2.connect("dbname=zhao887 user=zhao887")
	cur = conn.cursor()
	cur.executemany("""INSERT INTO STOCK (name, company) VALUES (%(NAME)s, %(COMPANY_NAME)s) """, stockInfo)
	conn.commit()
	return 

def insertStockPriceDataToDatabase(priceData):
	import psycopg2
	conn = psycopg2.connect("dbname=zhao887 user=zhao887")
	cur = conn.cursor()
	cur.executemany("""INSERT INTO STOCK_PRICE_DATA (DATA_ID, NAME, DATE, VOLUME, OPEN, HIGH, LOW, CLOSE, ADJ_CLOSE) VALUES (%(DATA_ID)s, %(NAME)s ,%(NAME)s, %(DATE)s,%(VOLUME)s,%(OPEN)s,%(HIGH)s,%(LOW)s,%(CLOSE)s,%(ADJ_CLOSE)s ) """, priceData)
	conn.commit()
	return 

def insertGoogleTrendingStockDataToDatabase(trendingData):
	pass

if __name__ == "__main__":
	aapl = StockInfoProcessor("AAPL_price.csv", "AAPL")
	priceData = aapl.stockPriceInforList
	print priceData
	for info in priceData:
		print info
	insertStockPriceDataToDatabase(priceData, "AAPL")

	#with open("AAPL.csv") as f:
	#	for line in f:
	#		print line
	
	# aapl = trendingDataProcessor("AAPL.csv")
	# for i, info in aapl.trendingInfor.iteritems():
	# 	print i , info
		
		
		

