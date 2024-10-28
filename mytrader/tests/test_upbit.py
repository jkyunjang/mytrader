import pytest
from mytrader.exchanges.upbit import Upbit

@pytest.fixture
def upbit():
    upbit = Upbit()
    return upbit

def test_upbit_auth(upbit):
    query = "?symbol=BTC"
    
    assert upbit._make_auth_token() != ""    
    # assert upbit._make_auth_token(query) != ""
    
def test_upbit_get_account_value(upbit):
    # result = upbit.get_account_value()
    pass    
    