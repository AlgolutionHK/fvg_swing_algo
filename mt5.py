# import mt5linux as mt5
from mt5linux import MetaTrader5
import logging
from mt5_config import *

def mt5_order(side,symbol,lot,sl_point,tp):
    # Set Logging
    log_path = "log/live.log"
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.INFO)

    # establish connection to the MetaTrader 5 terminal
    initialize = mt5.initialize()
    if initialize:
        logging.info("Initialize succeed!")
    if not initialize:
        logging.info("Initialize() failed, error code = {}".format(mt5.last_error()))
    
    # display data on MetaTrader 5 version
    # print(mt5.version())

    authorized=mt5.login(account,password,server,timeout=10) 
    if authorized:
        logging.info("connected to account #{}".format(account))
    else:
        logging.info("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

    price = mt5.SYMBOL_TRADE_EXECUTION_MARKET
    point = mt5.symbol_info(symbol).point
    deviation = 20
    if side == 0:
        sl = price - sl_point * point
        tp = price + sl_point * point
    elif side == 1:
        sl = price + sl_point * point
        tp = price - sl_point * point

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": side,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": deviation,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    

    # send a trading request
    result = mt5.order_send(request)
    # check the execution result
    logging.info("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation))
    
    logging.info("2. order_send done, {}".format(result))
    logging.info("   opened position with POSITION_TICKET={}".format(result.order))
    logging.info("   sleep 2 seconds before closing position #{}".format(result.order))


    mt5.shutdown()


# lot = 1
# trailing_stop_increment = 50

# mt5_order(0,"USDJPY",lot,sl_point=trailing_stop_increment,tp=trailing_stop_increment)

# mt5_order(1,"USDJPY",lot,sl_point=trailing_stop_increment,tp=trailing_stop_increment)