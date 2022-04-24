'''
    @filename : Drama.py
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
# Drama
## 
class ModelDrama(Common):
    
    FLAG = "drama"
     
    def __init__(self) -> None:
        Common.__init__(self, flag=ModelDrama.FLAG)
        self.urlParams = urlencode({
            "sel": "cnt",
            "tg": 1
        })
        