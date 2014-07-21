from easyos import easyos
from pprint import pprint

pprint(easyos)

if easyos['os'] == 'Darwin' and easyos['python_version'] == '2.7.8':
    print "You're up to date!"

with open (easyos['tmp_dir']+'/script', 'w') as log:
    message = "wow that's easy"
    log.write(message)