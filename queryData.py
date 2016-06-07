#This is the script to query data we want 
import psycopg2

START_DATE = 2
END_DATE = 3
INTEREST_SCORE = 4

def extractStockVolumeAndInterestScore(stockName):
    conn = psycopg2.connect("dbname=zhao887 user=zhao887")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM GOOGLE_TREND_STOCK_DATA WHERE KEYWORD = %s """, (stockName,))
    trendingResult = cur.fetchall()
    combineResult = []
    for row in trendingResult:
        startDate = row[START_DATE]
        endDate = row[END_DATE]
        interestScore = row[INTEREST_SCORE]
        query = cur.execute("""SELECT sum(volume) FROM STOCK_PRICE_DATA WHERE date <= %s AND date >= %s AND name = %s""", (endDate, startDate, stockName, ) )
        weeklyVolume = cur.fetchall()
        weeklyVolume = weeklyVolume[0][0]
        combineResult.append( (stockName, startDate, endDate, weeklyVolume , interestScore) )
        print "Stock: ", stockName, " start ", startDate, " end ", endDate, " volume: ", weeklyVolume, " interestScore: ", interestScore
    return combineResult

extractStockVolumeAndInterestScore('AAPL')