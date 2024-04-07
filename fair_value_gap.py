from pandas_ta.utils import get_offset, verify_series
import numpy as np
import pandas as pd
import pandas_ta as pta


'''
Adopted from https://github.com/twopirllc/pandas-ta/issues/624
'''

def fvg(open, high, low, close, min_gap=0, std_len=30, std_strength=0.0001, **kwargs):
    """Indicator: FVG"""
    # Validate Arguments
    # min_gap = min_gap if min_gap and min_gap > 0 else 1    
    
    open = verify_series(open)
    high = verify_series(high)
    low = verify_series(low)
    close = verify_series(close)

    if high is None or low is None or close is None: return

    # min_gap_pct = min_gap/100
    # min_gap = min_gap_pct*close
    # min_gap_std = pta.stdev(close,std_len)
    # min_gap = min_gap_std * std_strength
    # min_gap = min_gap.shift(1)

    # bullish FVG
    fvg_bull = (low - high.shift(2))
    fvg_bull_result = ((fvg_bull / close) * 100)

    # bearish FVG
    # print((low.shift(2) - high))
    fvg_bear =  (low.shift(2) - high)
    fvg_bear_result = ((fvg_bear / close) * -100)

    fvg_bull_array = np.where((fvg_bull > min_gap), fvg_bull_result, np.NaN)
    fvg_bull_series = pd.Series(fvg_bull_array)
    fvg_bull_series.index = pd.Series(high.index).shift(1)

    fvg_bear_array = np.where((fvg_bear > min_gap), fvg_bear_result, np.NaN)
    fvg_bear_series = pd.Series(fvg_bear_array)
    fvg_bear_series.index = pd.Series(high.index).shift(1)

    fvg_bull_series = fvg_bull_series.dropna()
    fvg_bull_series = fvg_bull_series[fvg_bull_series.index.notnull()]
    fvg_bear_series = fvg_bear_series.dropna()
    fvg_bear_series = fvg_bear_series[fvg_bear_series.index.notnull()]

    # fvg = fvg_bull_series.fillna(fvg_bear_series)


    # Handle fills
    if "fillna" in kwargs:
        fvg_bull_series.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        fvg_bull_series.fillna(method=kwargs["fill_method"], inplace=True)
    if "fillna" in kwargs:
        fvg_bear_series.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        fvg_bear_series.fillna(method=kwargs["fill_method"], inplace=True)

    # Name & Category
    fvg_bull_series.name = f"FVG_bull_{std_len}"
    fvg_bull_series.category = "trend"
    fvg_bear_series.name = f"FVG_bear_{std_len}"
    fvg_bear_series.category = "trend"

    return fvg_bull_series, fvg_bear_series

    # fvg = fvg_bull_series.fillna(fvg_bear_series)


    # # Handle fills
    # if "fillna" in kwargs:
    #     fvg.fillna(kwargs["fillna"], inplace=True)
    # if "fill_method" in kwargs:
    #     fvg.fillna(method=kwargs["fill_method"], inplace=True)

    # # Name & Category
    # fvg.name = f"FVG_{min_gap}"
    # fvg.category = "trend"

    # return fvg

def fvg_entry(open, high, low, close, min_gap=0, std_len=30, std_strength=0.0001, **kwargs):
    """Indicator: FVG"""
    # Validate Arguments
    # min_gap = min_gap if min_gap and min_gap > 0 else 1    
    
    open = verify_series(open)
    high = verify_series(high)
    low = verify_series(low)
    close = verify_series(close)

    if high is None or low is None or close is None: return

    # min_gap_pct = min_gap/100
    # min_gap = min_gap_pct*close
    # min_gap_std = pta.stdev(close,std_len)
    # min_gap = min_gap_std * std_strength
    # min_gap = min_gap.shift(1)

    # bullish FVG
    fvg_bull = (low - high.shift(2))
    fvg_bull_result = ((fvg_bull / close) * 100)

    # bearish FVG
    # print((low.shift(2) - high))
    fvg_bear =  (low.shift(2) - high)
    fvg_bear_result = ((fvg_bear / close) * -100)

    fvg_bull_array = np.where((fvg_bull > min_gap), fvg_bull_result, np.NaN)
    fvg_bull_series = pd.Series(fvg_bull_array)
    fvg_bull_series.index = pd.Series(high.index).shift(1)

    fvg_bear_array = np.where((fvg_bear > min_gap), fvg_bear_result, np.NaN)
    fvg_bear_series = pd.Series(fvg_bear_array)
    fvg_bear_series.index = pd.Series(high.index).shift(1)

    fvg_bull_series = fvg_bull_series.dropna()
    fvg_bull_series = fvg_bull_series[fvg_bull_series.index.notnull()]
    fvg_bear_series = fvg_bear_series.dropna()
    fvg_bear_series = fvg_bear_series[fvg_bear_series.index.notnull()]

    # fvg = fvg_bull_series.fillna(fvg_bear_series)


    # Handle fills
    if "fillna" in kwargs:
        fvg_bull_series.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        fvg_bull_series.fillna(method=kwargs["fill_method"], inplace=True)
    if "fillna" in kwargs:
        fvg_bear_series.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        fvg_bear_series.fillna(method=kwargs["fill_method"], inplace=True)

    # Name & Category
    fvg_bull_series.name = f"FVG_bull_{std_len}"
    fvg_bull_series.category = "trend"
    fvg_bear_series.name = f"FVG_bear_{std_len}"
    fvg_bear_series.category = "trend"

    
    return fvg_bull_series, fvg_bear_series


def fvg_live(open, high, low, close, min_gap=0, std_len=30, std_strength=0.0001, **kwargs):
    """Indicator: FVG"""
    # Validate Arguments
    min_gap = int(min_gap) if min_gap and min_gap > 0 else 1    
    
    open = verify_series(open)
    high = verify_series(high)
    low = verify_series(low)
    close = verify_series(close)

    if high is None or low is None or close is None or open is None: return

    # min_gap_pct = min_gap/100
    # min_gap = min_gap_pct*close
    # min_gap_std = pta.stdev(close,std_len)
    # min_gap = min_gap_std * std_strength
    # min_gap = min_gap.shift(1)

    # bullish FVG
    fvg_bull = (low - high.shift(2))
    fvg_bull_result = ((fvg_bull / close) * 100)
    # fvg_bull_result = close

    # bearish FVG
    fvg_bear =  (low.shift(2) - high)
    fvg_bear_result = ((fvg_bear / close) * -100)
    # fvg_bear_result = close

    fvg_bull_array = np.where((fvg_bull > min_gap), fvg_bull_result, 0)
    fvg_bull_series = pd.Series(fvg_bull_array)
    fvg_bull_series.index = pd.Series(high.index).shift(1)

    fvg_bear_array = np.where((fvg_bear > min_gap), fvg_bear_result, 0)
    fvg_bear_series = pd.Series(fvg_bear_array)
    fvg_bear_series.index = pd.Series(high.index).shift(1)

    fvg_bull_series = fvg_bull_series.dropna()
    fvg_bull_series = fvg_bull_series[fvg_bull_series.index.notnull()]
    fvg_bear_series = fvg_bear_series.dropna()
    fvg_bear_series = fvg_bear_series[fvg_bear_series.index.notnull()]

    # fvg = fvg_bull_series.fillna(fvg_bear_series)


    # Handle fills
    if "fillna" in kwargs:
        fvg_bull_series.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        fvg_bull_series.fillna(method=kwargs["fill_method"], inplace=True)
    if "fillna" in kwargs:
        fvg_bear_series.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        fvg_bear_series.fillna(method=kwargs["fill_method"], inplace=True)

    # Name & Category
    fvg_bull_series.name = f"FVG_bull_{std_len}"
    fvg_bull_series.category = "trend"
    fvg_bear_series.name = f"FVG_bear_{std_len}"
    fvg_bear_series.category = "trend"

    return fvg_bull_series, fvg_bear_series

def fvg_method(self, **kwargs):
    # high, low, close, min_gap=None,
    open = self._get_column(kwargs.pop("open", "open"))
    high = self._get_column(kwargs.pop("high", "high"))
    low = self._get_column(kwargs.pop("low", "low"))
    close = self._get_column(kwargs.pop("close", "close"))
    bull,bear = fvg(open=open, high=high, low=low, close=close, **kwargs)
    # bull,bear = fvg_live(open=open, high=high, low=low, close=close, **kwargs)
    return self._post_process(bull, **kwargs),self._post_process(bear, **kwargs)

def fvg_live_method(self, **kwargs):
    # Check if input data has 3 bars
    try:
        self._df = self._df[:3]
    except:
        print("Selected data is not enough!")
        empty_series = pd.Series([0 for i in range(3)])
        return empty_series, empty_series
    
    open = self._get_column(kwargs.pop("open", "open"))
    high = self._get_column(kwargs.pop("high", "high"))
    low = self._get_column(kwargs.pop("low", "low"))
    close = self._get_column(kwargs.pop("close", "close"))
    bull,bear = fvg_live(open=open, high=high, low=low, close=close, **kwargs)
    return self._post_process(bull, **kwargs), self._post_process(bear, **kwargs)

def fvg_entry_method(self, **kwargs):
    # Check if input data has 3 bars
    if len(self._df) < 3:
        print("Selected data is not enough!")
        empty_series = pd.Series([0 for i in range(3)])
        return empty_series, empty_series
    
    open = self._get_column(kwargs.pop("open", "open"))
    high = self._get_column(kwargs.pop("high", "high"))
    low = self._get_column(kwargs.pop("low", "low"))
    close = self._get_column(kwargs.pop("close", "close"))
    bull,bear = fvg_entry(open=open, high=high, low=low, close=close, **kwargs)

    # Return empty series if no result
    if bull.empty or bear.empty:
        empty_series = pd.Series([0 for i in range(3)])
        return empty_series, empty_series
    
    return self._post_process(bull, **kwargs), self._post_process(bear, **kwargs)



fvg.__doc__ = \
"""FVG
Calculates the Fair Value Gap
Sources:
    "https://trendspider.com/blog/fair-value-gap-basics/"
Calculation:
    Default Inputs:
       None
Args:
    open (pd.Series): Series of 'open's
    high (pd.Series): Series of 'high's
    low (pd.Series): Series of 'low's
    close (pd.Series): Series of 'close's
    min_gap (int): Minimum FVG Percentage of latest close
    
Kwargs:
    fillna (value, optional): pd.DataFrame.fillna(value)
    fill_method (value, optional): Type of fill method
Returns:
    pd.Series: New feature generated.
"""
