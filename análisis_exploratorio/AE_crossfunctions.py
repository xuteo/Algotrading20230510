# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:45:52 2023

@author: Jesus
"""

import sys
import numpy as np
import pandas as pd
import warnings
import ta
import MetaTrader5 as mt5
mt5.initialize()
from operativa import *
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import openpyxl as xl

# indice USA
#SP500 = MT5.get_data('SPX500',10000)


class crossfunctions:
    def ema_positiva(close, window = 150):
        ''' Devuelve un dataframe con los retornos y las fechas como indice de los timeframes
        con ema positiva'''
        
        df = pd.DataFrame()
        df["close"] = close
       
    
        # Inicializamos la clase SMA
        indicador = ta.trend.EMAIndicator(close=df["close"], window=window)
    
        # Añadimos la ema al DataFrame
        df['indicador'] = indicador.ema_indicator()
    
        # condicon
        df['condicion'] =  df["indicador"] > df["indicador"].shift(1)
        # Desplazamos los valores
        #df["indicador_Yesterday"] = df["indicador"].shift(1)
        
        # Variacion close
        df['var_close'] =  df["close"].pct_change().mul(100)
        # Variacion  close condicionada
        df.loc[df['condicion'] == True, 'var_close_condicionado'] = df['var_close']
        df.loc[df['condicion'] != True, 'var_close_condicionado'] = 0
        # variacion del indicador
        df['var_indicador'] =  df["indicador"].pct_change().mul(100)
        df = df.dropna()
        # variaciones acumuladas
        df['var_close_acum'] =  df['var_close'].cumsum()
        df['var_close_condicionado_acum'] =  df['var_close_condicionado'].cumsum()
        df['var_indicador_acum'] =  df['var_indicador'].cumsum()
    
        # Eliminar la fila que contiene los valores que faltan
        df = df.dropna()
    
        return pd.DataFrame(df)
    
    def sma_positiva(close, window = 150):
        ''' Devuelve un dataframe con los retornos y las fechas como indice de los timeframes
        con ema positiva'''
        
        df = pd.DataFrame()
        df["close"] = close
       
    
        # Inicializamos la clase SMA
        indicador = ta.trend.SMAIndicator(close=df["close"], window=window)
    
        # Añadimos la ema al DataFrame
        df['indicador'] = indicador.sma_indicator()
    
        # condicon
        df['condicion'] =  df["indicador"] > df["indicador"].shift(1)
        # Desplazamos los valores
        #df["indicador_Yesterday"] = df["indicador"].shift(1)
        
        # Variacion close
        df['var_close'] =  df["close"].pct_change().mul(100)
        # Variacion  close condicionada
        df.loc[df['condicion'] == True, 'var_close_condicionado'] = df['var_close']
        df.loc[df['condicion'] != True, 'var_close_condicionado'] = 0
        # variacion del indicador
        df['var_indicador'] =  df["indicador"].pct_change().mul(100)
        df = df.dropna()
        # variaciones acumuladas
        df['var_close_acum'] =  df['var_close'].cumsum()
        df['var_close_condicionado_acum'] =  df['var_close_condicionado'].cumsum()
        df['var_indicador_acum'] =  df['var_indicador'].cumsum()
    
        # Eliminar la fila que contiene los valores que faltan
        df = df.dropna()
    
        return pd.DataFrame(df)
    
    
    def stats(df):
        ''' input df = pandas.dataframe con al menos una columna llamada var_close y otra llamada condicion '''
        
        p_alcista = len(df[df["var_close"] > 0]) / len(df["var_close"])*100
        p_alcista_condicionada = len(df[(df["var_close"] > 0) & (df["condicion"]== True) ]) / len(df[df["condicion"]== True])*100
        
        retorno_medio =  np.mean(df["var_close"], axis=0)
        retorno_medio_condicionado = np.mean(df.loc[df['condicion'] == True, 'var_close'], axis=0)
        
        retorno_acum = np.sum(df["var_close"], axis=0)
        retorno_acum_condicionado = np.sum(df.loc[df['condicion'] == True, 'var_close'], axis=0)
       
        return ((p_alcista, retorno_medio, retorno_acum),(p_alcista_condicionada, retorno_medio_condicionado, retorno_acum_condicionado))
    # ******************* aplicando la función ******************
    '''
    sp500_ema = sma_positiva(SP500['close'])
    stadisticas = stats(sp500_ema)
    '''
    # ***********************************************************

  








