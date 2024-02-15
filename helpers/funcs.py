import json
import re

import aiogram
import requests

from loader import subs

oldVals = dict()
def init_values():
    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="BTCUSDT"))
    res = json.loads(s=req.text)
    oldVals["BTC"] = res["priceChangePercent"]

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="ETHUSDT"))
    res = json.loads(s=req.text)
    oldVals["ETH"] = res["priceChangePercent"]

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="SOLUSDT"))
    res = json.loads(s=req.text)
    oldVals["SOL"] = res["priceChangePercent"]

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="JUPUSDT"))
    res = json.loads(s=req.text)
    oldVals["JUP"] = res["priceChangePercent"]

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="BNBUSDT"))
    res = json.loads(s=req.text)
    oldVals["BNB"] = res["priceChangePercent"]
def parse_data():
    coins = dict()
    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr",params=dict(symbol="BTCUSDT"))
    res = json.loads(s=req.text)
    coins["BTC"] = (res["lastPrice"], res["priceChangePercent"])

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="ETHUSDT"))
    res = json.loads(s=req.text)
    coins["ETH"] = (res["lastPrice"], res["priceChangePercent"])

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="SOLUSDT"))
    res = json.loads(s=req.text)
    coins["SOL"] = (res["lastPrice"], res["priceChangePercent"])

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="JUPUSDT"))
    res = json.loads(s=req.text)
    coins["JUP"] = (res["lastPrice"], res["priceChangePercent"])

    req = requests.get(url="https://api.binance.com/api/v3/ticker/24hr", params=dict(symbol="BNBUSDT"))
    res = json.loads(s=req.text)
    coins["BNB"] = (res["lastPrice"], res["priceChangePercent"])
    return coins


async def notification(bot: aiogram.Bot, coins):
    for coin, val in coins.items():
        if abs(float(val[1]) - float(oldVals[coin])) > 1.0:
            oldVals[coin] = float(val[1])
            if float(val[1]) > 0:
                ms = "поднялся"
            else:
                ms = "упал"
            for sub in subs:
                await bot.send_message(chat_id=sub, text=f'⚜️<strong>{coin}</strong> {ms} в цене на <strong>{val[1]}</strong>%! Время торгов!')