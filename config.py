from typing import Dict, List

# Market hours configuration
MARKET_START_TIME = "02:14:30" # correct it later
MARKET_END_TIME = "22:30:00"
COLLECTION_INTERVAL = 60  # select the number of seconds 1 min so 60 seconds
START_TIME_OFFSET = 1 # Number of seconds after each minute to start data collection

#we can fetch option chain data in 3 seconds via APIs because it takes time to reflect the oi data

# Index options configuration
INDEX_OPTIONS = {
    "NIFTY": {
        "exchange": "INDEX",
        "num_expiries": 1,
        "num_strikes": 2,  # Number of strikes above and below ATM
        "strike_gap": 50,  # Gap between strikes
        "data_dir": "option_chain/index_options/nifty"
    },
    "BANKNIFTY": {
        "exchange": "INDEX",
        "num_expiries": 1,
        "num_strikes": 50,  # Number of strikes above and below ATM
        "strike_gap": 100,  # Gap between strikes
        "data_dir": "option_chain/index_options/banknifty"
    },
    "SENSEX": {
        "exchange": "INDEX",
        "num_expiries": 1,
        "num_strikes": 2,  # Number of strikes above and below ATM
        "strike_gap": 100,  # Gap between strikes
        "data_dir": "option_chain/index_options/sensex"
    },

}

# Stock options configuration
STOCK_OPTIONS = {
    "RELIANCE": {
        "exchange": "NSE",
        "num_expiries": 1,
        "num_strikes": 5,  # Number of strikes above and below ATM
        "strike_gap": 10,  # Gap between strikes
        "data_dir": "option_chain/stock_options/reliance"
    },
    "KOTAKBANK": {
        "exchange": "NSE",
        "num_expiries": 1,
        "num_strikes": 5,  # Number of strikes above and below ATM
        "strike_gap": 20,  # Gap between strikes
        "data_dir": "option_chain/stock_options/kotakbank"
    },
        "INFY": {
        "exchange": "NSE",
        "num_expiries": 1,
        "num_strikes": 5,  # Number of strikes above and below ATM
        "strike_gap": 20,  # Gap between strikes
        "data_dir": "option_chain/stock_options/infy"
    },
        "SBIN": {
        "exchange": "NSE",
        "num_expiries": 1,
        "num_strikes": 5,  # Number of strikes above and below ATM
        "strike_gap": 10,  # Gap between strikes
        "data_dir": "option_chain/stock_options/sbin"
    },
        "HDFCBANK": {
        "exchange": "NSE",
        "num_expiries": 1,
        "num_strikes": 5,  # Number of strikes above and below ATM
        "strike_gap": 20,  # Gap between strikes
        "data_dir": "option_chain/stock_options/hdfcbank"
    },
    #     "TATAMOTORS": {
    #     "exchange": "NSE",
    #     "num_expiries": 1,
    #     "num_strikes": 5,  # Number of strikes above and below ATM
    #     "strike_gap": 10,  # Gap between strikes
    #     "data_dir": "option_chain/stock_options/tatamotors"
    # },
    #     "CANBK": {
    #     "exchange": "NSE",
    #     "num_expiries": 1,
    #     "num_strikes": 10,  # Number of strikes above and below ATM
    #     "strike_gap": 1,  # Gap between strikes
    #     "data_dir": "option_chain/stock_options/canbk"
    # },
    #     "COALINDIA": {
    #     "exchange": "NSE",
    #     "num_expiries": 1,
    #     "num_strikes": 5,  # Number of strikes above and below ATM
    #     "strike_gap": 5,  # Gap between strikes
    #     "data_dir": "option_chain/stock_options/coalindia"
    # },



    # Add more stocks here as needed
}

# Combine all symbols
ALL_SYMBOLS = {**INDEX_OPTIONS, **STOCK_OPTIONS}





# Logging configuration
LOG_CONFIG = {
    "log_file": "option_chain.log",
    "max_bytes": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5
}

