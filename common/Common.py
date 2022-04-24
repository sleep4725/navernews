'''
    @filename : Common.py
    @author : JunHyeon.Kim
    @email : sleep4725@naver.com
    @date : 20220423
    @package: naver.common
'''
import time 
import os  
PROJ_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Common:
    
    def __init__(
        self, flag: str
        ) -> None:
        '''
            flag = {drama}
        '''
        global PROJ_ROOT_PATH 
        self.url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?"
        self.header = {'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
                Safari/537.36'), } 
        self.cllctTime = time.strftime("%Y%m%d", time.localtime())
        self.fileGenerateTime = time.strftime("%Y%m%d%H%M", time.localtime())
        self.jsonFilePath = f"{PROJ_ROOT_PATH}/file/{flag}"
        self.actionList = [] 
        self.rootLoggingFilePath = f"{PROJ_ROOT_PATH}/cllctlog" 
        
    def makeUrl(
        self, params
        )-> str:
        '''
            https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20220422&tg=1
            :params:
            :return:
        '''
        reqUrl = self.url + f"{params}&date={self.cllctTime}" 
        print(f"* reqUrl: {reqUrl}")
        return reqUrl        
        