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

from model.Fantasy import ModelFantasy
from common.Templete import Templete


class CllctFantasy(ModelFantasy, Templete):
    
    def __init__(self) -> None:
        ModelFantasy.__init__(self)
    
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
                        "movie_genre": ModelFantasy.FLAG
                    } 
                    self.actionList.append(doc)
                    
            response.close() 
    
    def jsonFileGenerate(self):
        '''
            :params:
            :return:
        '''
        if self.actionList:
            with open(f"{self.jsonFilePath}/{ModelFantasy.FLAG}_{self.cllctTime}_.log", "a", encoding="utf-8") as jw:
                for jrow in self.actionList:
                    jw.write(json.dumps(jrow, ensure_ascii=False) + "\n")
                
                jw.close()
    
def main():
    o = CllctFantasy() 
    o.getData()
    o.jsonFileGenerate()
    
if __name__ == "__main__":
    main() 
        