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
				OPEN INT NOT NULL,\
				HIGH INT NOT NULL,\
				LOW INT NOT NULL,\
				CLOSE INT NOT NULL,\
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
	conn.commit()
except:
	print "Failed to create the table. "

