import numpy as np

def logaritmic_graph(first_df, second_df, first_suffix, second_suffix):
    joined_series_closed = first_df.join(second_df, lsuffix = "_"+first_suffix, rsuffix = "_"+second_suffix)[["Adj Close_"+first_suffix, "Adj Close_"+second_suffix]]
    firstdf_rtn = np.log(joined_series_closed["Adj Close_"+first_suffix]/ joined_series_closed["Adj Close_"+first_suffix].shift(1))
    firstdf_rtn.dropna(inplace = True)
    firstdf_rtn = firstdf_rtn.to_frame()
    
    seconddf_rtn = np.log(joined_series_closed["Adj Close_"+second_suffix]/ joined_series_closed["Adj Close_"+second_suffix].shift(1))
    seconddf_rtn.dropna(inplace = True)
    seconddf_rtn = seconddf_rtn.to_frame()
    
    return firstdf_rtn.join(seconddf_rtn)

def simple_return_graph(first_df, second_df, first_suffix, second_suffix):
    
    joined_series_closed = first_df.join(second_df, lsuffix = "_"+first_suffix, rsuffix = "_"+second_suffix)[["Adj Close_"+first_suffix, "Adj Close_"+second_suffix]]
    firstdf_rtn = np.subtract(joined_series_closed["Adj Close_"+first_suffix], joined_series_closed["Adj Close_"+first_suffix].shift(1))
    firstdf_rtn.dropna(inplace = True)
    firstdf_rtn = firstdf_rtn.to_frame()
    
    seconddf_rtn = np.subtract(joined_series_closed["Adj Close_"+second_suffix], joined_series_closed["Adj Close_"+second_suffix].shift(1))
    seconddf_rtn.dropna(inplace = True)
    seconddf_rtn = seconddf_rtn.to_frame()
    
    return firstdf_rtn.join(seconddf_rtn)