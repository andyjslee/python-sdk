# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.15.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.security_api import SecurityApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.security_api.SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_securities(self):
        """Test case for get_all_securities

        All Securities  # noqa: E501
        """
        pass

    def test_get_security_by_id(self):
        """Test case for get_security_by_id

        Lookup Security  # noqa: E501
        """
        pass

    def test_get_security_data_point_number(self):
        """Test case for get_security_data_point_number

        Data Point (Number) for Security  # noqa: E501
        """
        pass

    def test_get_security_data_point_text(self):
        """Test case for get_security_data_point_text

        Data Point (Text) for Security  # noqa: E501
        """
        pass

    def test_get_security_historical_data(self):
        """Test case for get_security_historical_data

        Historical Data for Security  # noqa: E501
        """
        pass

    def test_get_security_intraday_prices(self):
        """Test case for get_security_intraday_prices

        Intraday Stock Prices for Security  # noqa: E501
        """
        pass

    def test_get_security_latest_dividend_record(self):
        """Test case for get_security_latest_dividend_record

        Latest Dividend Record for Security  # noqa: E501
        """
        pass

    def test_get_security_latest_earnings_record(self):
        """Test case for get_security_latest_earnings_record

        Latest Earnings Record for Security  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_adi(self):
        """Test case for get_security_price_technicals_adi

        Accumulation/Distribution Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_adtv(self):
        """Test case for get_security_price_technicals_adtv

        Average Daily Trading Volume  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_adx(self):
        """Test case for get_security_price_technicals_adx

        Average Directional Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_ao(self):
        """Test case for get_security_price_technicals_ao

        Awesome Oscillator  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_atr(self):
        """Test case for get_security_price_technicals_atr

        Average True Range  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_bb(self):
        """Test case for get_security_price_technicals_bb

        Bollinger Bands  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_cci(self):
        """Test case for get_security_price_technicals_cci

        Commodity Channel Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_cmf(self):
        """Test case for get_security_price_technicals_cmf

        Chaikin Money Flow  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_dc(self):
        """Test case for get_security_price_technicals_dc

        Donchian Channel  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_dpo(self):
        """Test case for get_security_price_technicals_dpo

        Detrended Price Oscillator  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_eom(self):
        """Test case for get_security_price_technicals_eom

        Ease of Movement  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_fi(self):
        """Test case for get_security_price_technicals_fi

        Force Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_ichimoku(self):
        """Test case for get_security_price_technicals_ichimoku

        Ichimoku Kinko Hyo  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_kc(self):
        """Test case for get_security_price_technicals_kc

        Keltner Channel  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_kst(self):
        """Test case for get_security_price_technicals_kst

        Know Sure Thing  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_macd(self):
        """Test case for get_security_price_technicals_macd

        Moving Average Convergence Divergence  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_mfi(self):
        """Test case for get_security_price_technicals_mfi

        Money Flow Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_mi(self):
        """Test case for get_security_price_technicals_mi

        Mass Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_nvi(self):
        """Test case for get_security_price_technicals_nvi

        Negative Volume Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_obv(self):
        """Test case for get_security_price_technicals_obv

        On-balance Volume  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_obv_mean(self):
        """Test case for get_security_price_technicals_obv_mean

        On-balance Volume Mean  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_rsi(self):
        """Test case for get_security_price_technicals_rsi

        Relative Strength Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_sma(self):
        """Test case for get_security_price_technicals_sma

        Simple Moving Average  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_sr(self):
        """Test case for get_security_price_technicals_sr

        Stochastic Oscillator  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_trix(self):
        """Test case for get_security_price_technicals_trix

        Triple Exponential Average  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_tsi(self):
        """Test case for get_security_price_technicals_tsi

        True Strength Index  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_uo(self):
        """Test case for get_security_price_technicals_uo

        Ultimate Oscillator  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_vi(self):
        """Test case for get_security_price_technicals_vi

        Vortex Indicator  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_vpt(self):
        """Test case for get_security_price_technicals_vpt

        Volume-price Trend  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_vwap(self):
        """Test case for get_security_price_technicals_vwap

        Volume Weighted Average Price  # noqa: E501
        """
        pass

    def test_get_security_price_technicals_wr(self):
        """Test case for get_security_price_technicals_wr

        Williams %R  # noqa: E501
        """
        pass

    def test_get_security_realtime_price(self):
        """Test case for get_security_realtime_price

        Realtime Stock Price for Security  # noqa: E501
        """
        pass

    def test_get_security_stock_price_adjustments(self):
        """Test case for get_security_stock_price_adjustments

        Stock Price Adjustments by Security  # noqa: E501
        """
        pass

    def test_get_security_stock_prices(self):
        """Test case for get_security_stock_prices

        Stock Prices by Security  # noqa: E501
        """
        pass

    def test_get_security_zacks_analyst_ratings(self):
        """Test case for get_security_zacks_analyst_ratings

        Zacks Analyst Ratings  # noqa: E501
        """
        pass

    def test_get_security_zacks_analyst_ratings_snapshot(self):
        """Test case for get_security_zacks_analyst_ratings_snapshot

        Zacks Analyst Ratings Snapshot  # noqa: E501
        """
        pass

    def test_get_security_zacks_eps_surprises(self):
        """Test case for get_security_zacks_eps_surprises

        Zacks EPS Surprises for Security  # noqa: E501
        """
        pass

    def test_get_security_zacks_sales_surprises(self):
        """Test case for get_security_zacks_sales_surprises

        Zacks Sales Surprises for Security  # noqa: E501
        """
        pass

    def test_screen_securities(self):
        """Test case for screen_securities

        Screen Securities  # noqa: E501
        """
        pass

    def test_search_securities(self):
        """Test case for search_securities

        Search Securities  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
