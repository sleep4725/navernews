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
print(f"*[project-root-path]: {PROJ_ROOT_PATH}")
sys.path.append(PROJ_ROOT_PATH)

import requests 
import json 
from bs4 import BeautifulSoup
import requests 

from model.Drama import ModelDrama 
from common.Templete import Templete
import logging 

class CllctDrama(ModelDrama, Templete):
    
    def __init__(self) -> None:
        ModelDrama.__init__(self)
        self.logger = self.getLogger()
    
    def getLogger(self)-> logging:
        '''
            :params:
            :return:
        '''
        # 로그 생성
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # log 출력
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # log를 파일에 출력
        # /Users/kimjunhyeon/Desktop/naver/cllctlog/
        file_handler = logging.FileHandler(
            self.rootLoggingFilePath + f"/{ModelDrama.FLAG}/{ModelDrama.FLAG}_log_{self.fileGenerateTime}.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger 
    
    def getData(self):
        '''
            :params:
            :return:
        '''
        reqUrl = self.makeUrl(params= self.urlParams)
        
        try:
            
            response = requests.get(reqUrl, headers= self.header)
        except requests.exceptions.MissingSchema as error:
            print(error)
        except:
            print("requests error !!")
        else:
            if response.status_code == 200:
                self.logger.info(f"{reqUrl} requests success") # **********
                bsObject = BeautifulSoup(response.text, "html.parser")
                print(bsObject.title) # logging
                tit3List = bsObject.select("div.tit3")
                
                for rank, t in enumerate(tit3List):
                    aTag = t.select_one("a")
                    movieUrl = str(aTag.attrs["href"]).strip()
                    movieTitle = str(aTag.attrs["title"]).strip()
                    doc = {
                        "movie_rank": rank+1, 
                        "movie_url": movieUrl, 
                        "movie_title": movieTitle,
                        "movie_cllct": self.cllctTime,
                        "movie_genre": ModelDrama.FLAG
                    } 
                    self.actionList.append(doc)
                
                totalCnt = len(self.actionList)
                self.logger.info(f"{totalCnt}건 list에 적재 완료") # *********
            response.close()
    
    def jsonFileGenerate(self):
        '''
            :params:
            :return:
        '''
        if self.actionList:
            ndjsonFile = f"{self.jsonFilePath}/{ModelDrama.FLAG}_{self.cllctTime}_.log" # *********
            with open(ndjsonFile, "a", encoding="utf-8") as jw:
                for jrow in self.actionList:
                    jw.write(json.dumps(jrow, ensure_ascii=False) + "\n")
                
                jw.close()
                
            self.logger.info(f"{ndjsonFile} file generate success") # ********
def main():
    o = CllctDrama() 
    o.getData()
    o.jsonFileGenerate()
    
if __name__ == "__main__":
    main() 
        