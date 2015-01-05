from easyos import easyos
from pprint import pprint

pprint(easyos)

if easyos['os'] == 'Darwin' and int(easyos['python_version'][0]) < 3:
    print("Consider switching to Python 3 for your development machine.")

with open (easyos['tmp_dir']+'/script', 'w') as log:
    message = "wow that's easy"
    log.write(message)
