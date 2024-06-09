import pandas as pd
import numpy as np

"""
Pivot points definition: https://pinewizards.com/technical-analysis-functions/ta-pivothigh-in-pine-script/
"""

def get_swings(df_full,window_size):

    swing_high_list = []
    swing_high_time = []
    swing_low_list = []
    swing_low_time = []

    for start in range(0, len(df_full) - window_size*2 + 1): 
        end = start + window_size*2
        df = df_full.iloc[start:end] 
        df['index'] = range(len(df)) 
        df = df.reset_index(drop=False) 
        # df['Datetime'] = df['Datetime'].dt.date 
        df.columns = ['time','high','low','open','close','index'] 
        df = df.set_index('index') 

        # # Calculate h1 and h2
        # if df['high'][1] > df['high'][0]: 
        #     h1 = df['high'][1] - df['high'][0]
        #     if df['high'][1] > df['high'][2]: 
        #         h2 = df['high'][1] - df['high'][2]

        #         if min(abs(h1),abs(h2)) > df['high'][1] - df['open'][1]:
        #             swing_high_list.append(df['high'][1])
        #             swing_high_time.append(df['time'][1])
        
        # # Calculate l1 and l2
        # if df['low'][0] > df['low'][1]: 
        #     l1 = df['low'][0] - df['low'][1] 
        #     if df['low'][2] > df['low'][1]: 
        #         l2 = df['low'][2] - df['low'][1]

        #         if min(abs(l1),abs(l2)) > df['open'][1] - df['low'][1]:
        #             swing_low_list.append(df['low'][1])
        #             swing_low_time.append(df['time'][1])

        if df['high'].max() == df['high'].iloc[window_size]:
            swing_high_list.append(df['high'].iloc[window_size])
            swing_high_time.append(df['time'][window_size])

        if df['low'].min() == df['low'].iloc[window_size]:
            swing_low_list.append(df['low'].iloc[window_size])
            swing_low_time.append(df['time'][window_size])

    swing_high = pd.DataFrame({'swing_high_time':swing_high_time,'swing_high_list':swing_high_list})
    swing_low = pd.DataFrame({'swing_low_time':swing_low_time,'swing_low_list':swing_low_list})


    return swing_high, swing_low


def get_swings_live(df_full,window_size):
    swing_high_list = []
    swing_high_time = []
    swing_low_list = []
    swing_low_time = []

    # try:
    #     df = df[-2*window_size:]
    # except:
    #     print("Selected data is not enough!")
    #     return swing_high, swing_low

    for start in range(0, len(df_full) - window_size*2 + 1): 
        # start = 0
        end = start + window_size*2
        df = df_full.iloc[start:end] 
        # df['index'] = range(len(df)) 
        # df = df.reset_index(drop=False) 
        # df['Datetime'] = df['Datetime'].dt.date 
        # df.columns = ['high','low','open','close'] 
        # df = df.set_index('index') 


        if df['high'].max() == df['high'].iloc[window_size]:
            swing_high_list.append(df['high'].iloc[window_size])
            swing_high_time.append(df.index[window_size])

        if df['low'].min() == df['low'].iloc[window_size]:
            swing_low_list.append(df['low'].iloc[window_size])
            swing_low_time.append(df.index[window_size])

    if not swing_high_list:
        swing_high_list.append(0)
    if not swing_high_time:
        swing_high_time.append(0)
    if not swing_low_list:
        swing_low_list.append(0)
    if not swing_low_time:
        swing_low_time.append(0)

    swing_high = pd.DataFrame({'swing_high_time':swing_high_time,'swing_high_list':swing_high_list})
    swing_low = pd.DataFrame({'swing_low_time':swing_low_time,'swing_low_list':swing_low_list})


    return swing_high, swing_low


def get_swings_prev(df_full,window_size):
    swing_high_list = []
    swing_high_time = []
    swing_low_list = []
    swing_low_time = []

    for start in range(0, len(df_full) - window_size*2 + 1): 
        # start = 0
        end = start + window_size*2
        df = df_full.iloc[start:end] 
        # df['index'] = range(len(df)) 
        # df = df.reset_index(drop=False) 
        # df['Datetime'] = df['Datetime'].dt.date 
        # df.columns = ['high','low','open','close'] 
        # df = df.set_index('index') 


        if df['high'].max() == df['high'].iloc[window_size]:
            swing_high_list.append(df['high'].iloc[window_size])
            swing_high_time.append(df.index[window_size])

        if df['low'].min() == df['low'].iloc[window_size]:
            swing_low_list.append(df['low'].iloc[window_size])
            swing_low_time.append(df.index[window_size])

    if not swing_high_list:
        swing_high_list.append(0)
    if not swing_high_time:
        swing_high_time.append(0)
    if not swing_low_list:
        swing_low_list.append(0)
    if not swing_low_time:
        swing_low_time.append(0)

    swing_high = pd.DataFrame({'swing_high_time':swing_high_time,'swing_high_list':swing_high_list})
    swing_low = pd.DataFrame({'swing_low_time':swing_low_time,'swing_low_list':swing_low_list})


    return swing_high, swing_low
     
