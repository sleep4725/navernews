'''
    @filename : Horror.py
    @author : JunHyeon.Kim
    @email : sleep4725@naver.com
    @date : 20220423
    @package: naver.model
'''
import os  
import sys
PROJ_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJ_ROOT_PATH)

from urllib.parse import urlencode
from common.Common import Common

##
# Horror
# https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20220422&tg=4
## 
class ModelHorror(Common):
    
    FLAG = "horror"
     
    def __init__(self) -> None:
        Common.__init__(self, flag=ModelHorror.FLAG)
        self.urlParams = urlencode({
            "sel": "cnt",
            "tg": 4
        })