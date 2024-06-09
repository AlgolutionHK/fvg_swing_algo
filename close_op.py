from trading_ig import IGService
from trading_ig_config import config
import asyncio
from utilities import *


ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
ig = ig_service.create_session()

op = ig_service.fetch_open_positions()

for index,row in op.iterrows():
    if row['direction'] == 'BUY':
        direction = 'SELL'
    elif row['direction'] == 'SELL':
        direction = 'BUY'
    close = ig_service.close_open_position(row['dealId'],direction,epic=None,expiry=None,level=None,
                                           order_type='MARKET',quote_id=None,size=row['size'])
    print(close)

message = 'ALL Positions Closed on weekly market close.'
asyncio.run(send_to_channel(message))