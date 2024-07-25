import json

import pytest
import requests


from commons.yaml_util import read_yaml


class Testt:

    @pytest.mark.parametrize("caseinfo",read_yaml('testcase1/testapi.yaml'))
    def test_rf(self,caseinfo):
       print(caseinfo)
       h = caseinfo["request"]["headers"]
       u = caseinfo["request"]["url"]
       res = requests.get(url=u,headers=h)
       print(res.text)
            #Testutil().test_all(method="get",url=u,headers=h)

    #def test_dd(self,connection_mysql):

      #  print("dddd")

    @pytest.mark.parametrize("caseinfo1", read_yaml('testcase1/testtp.yaml'))
    def test_pt(self, caseinfo1):
        #print(caseinfo1)
        h = caseinfo1["request"]["headers"]
        u = caseinfo1["request"]["url"]
        #h = {'Authorization':'6710f314-514f-40da-8c19-1a6b538e0179','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        #u = "https://beta.tupu360.com/ats/jobs/position/list"

        bodys = json.dumps({"filter":{"queryId":"hr","isTemplate":"","dateRange":{},"keyWord":"","aggs":{"54":[],"positionStatus":["PROCESSING"],"team_hr.id":["531a244a67f8ed4e0167f9712f660001"],"virtualPosition":[],"weChatPositionType":[],"department":[],"supportsAI":[],"team":[],"jobType":[],"team_rpo.id":[],"isRPO":[],"cesigaojisousuoxianshi":[],"locationEs.id":[],"province":[],"availableInterviewWeekDay.id":[]},"positionIds":[]},"page":{"pageNo":1,"pageSize":10},"sort":"dateCreated"})
        res = requests.post(url=u, headers=h,data=bodys)
        print(res.text) 


