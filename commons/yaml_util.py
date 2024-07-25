import os

import yaml
#写入
def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="a+") as f:
        data = {'Authorization':data}
        yaml.dump(data,stream=f,allow_unicode=True)
#读取
def read_yaml(casepath):
    with open(os.getcwd()+"/"+casepath,encoding="utf-8",mode="r") as f:
        return yaml.load(f,yaml.FullLoader)


#清空
def clear_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()


