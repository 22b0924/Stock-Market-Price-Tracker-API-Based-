from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
watchlist = ["AAPL", "MSFT", "TSLA"]

@app.get("/prices")
def prices():
    data = []
    for sym in watchlist:
        try:
            d = yf.Ticker(sym).history(period="1d").iloc[-1]
            data.append({
                "symbol": sym,
                "price": round(d["Close"], 2),
                "change": round(d["Close"] - d["Open"], 2)
            })
        except:
            data.append({"symbol": sym, "error": "No data"})
    return data
