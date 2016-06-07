#This is the script to create the three tables 
import psycopg2
conn = psycopg2.connect("dbname=zhao887 user=zhao887")
cur = conn.cursor()
try:
	cur.execute( 
			"CREATE TABLE STOCK \
			(\
				NAME VARCHAR(50) NOT NULL PRIMARY KEY,\
				COMPANY VARCHAR(50) NOT NULL\
			);")
	cur.execute( 
			"CREATE TABLE STOCK_PRICE_DATA\
			( \
				DATA_ID INT NOT NULL PRIMARY KEY,\
				NAME VARCHAR(50) NOT NULL REFERENCES STOCK(NAME),\
				DATE INT NOT NULL,\
				VOLUME INT NOT NULL,\
				OPEN FLOAT(3) NOT NULL,\
				HIGH FLOAT(3) NOT NULL,\
				LOW FLOAT(3) NOT NULL,\
				CLOSE FLOAT(3) NOT NULL,\
				ADJ_CLOSE INT NOT NULL\
			);")
	cur.execute( 
			"CREATE TABLE GOOGLE_TREND_STOCK_DATA\
			( \
				DATA_ID INT NOT NULL PRIMARY KEY,\
				KEYWORD VARCHAR(50) NOT NULL REFERENCES STOCK(NAME),\
				START_DATE INT NOT NULL,\
				END_DATE INT NOT NULL,\
				INTEREST_SCORE INT NOT NULL\
			);")
	#conn.commit()
	stockInfo = [	
					{"COMPANY_NAME":"GOOGLE", "NAME": "GOOG"},
					{"COMPANY_NAME":"APPLE", "NAME": "AAPL"},
					{"COMPANY_NAME":"BANK OF AMERICA", "NAME": "BAC"},
					{"COMPANY_NAME":"MICROSOFT", "NAME": "MSFT"},
					{"COMPANY_NAME":"PFIZER", "NAME": "PFE"},
				]
	cur.executemany("""INSERT INTO STOCK (name, company) VALUES (%(NAME)s, %(COMPANY_NAME)s) """, stockInfo)
	conn.commit()
except:
	print "Failed to create/insert the table. "

