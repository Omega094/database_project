#This is the script to query data we want 
import psycopg2

START_DATE = 2
END_DATE = 3
INTEREST_SCORE = 5

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
        query = cur.execute("""SELECT sum(volume) FROM STOCK_PRICE_DATA WHERE date <= %d AND date >= %d AND name = %s""", (endDate, startDate, stockName, ) )
        weeklyVolume = cur.fetchall()
        combineResult.append( (stockName, startDate, endDate, weeklyVolume, interestScore) )
    return combineResult

print extractStockVolumeAndInterestScore('AAPL')