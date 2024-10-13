import pandas as pd
import os
from dotenv import load_dotenv
from exchange import Upbit
from trader import Trader
from . import DOTENV_REQUIRED

'''
Todo:
    - 업비트 인증
    - 전략 구현
    - 업비트 매수/매도 요청
'''
def main():
    # upbit = Upbit()
    # trader = Trader(upbit)
    pass
        
if __name__ == '__main__':
    rst = load_dotenv()
    if rst != True:
        raise FileNotFoundError('.env 파일을 찾을 수 없습니다')
    else:
        for requied in DOTENV_REQUIRED:
            if os.getenv(requied) == None:
                raise NameError(f'.env에 {requied}이 존재하지 않습니다')
        main()

        