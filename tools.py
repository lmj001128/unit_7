
import yaml

def data_yaml(filename):
    with open(filename,'r',encoding='utf8') as f:
        return yaml.safe_load(f)

print(data_yaml('./lianxi.yaml'))
