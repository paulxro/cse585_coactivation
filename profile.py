"""Start-up script adapted from https://github.com/emulab/my-profile"""

import geni.portal as portal
import geni.rspec.pg as pg
import os

SCRIPT_DIR = './scripts'


pc = portal.Context()

request = pc.makeRequestRSpec()

node = request.RawPC("node")

files = [file for file in os.listdir(SCRIPT_DIR)]

for file in files:
    os.chmod(f'./scripts/{file}', 0o0777)

node.addService(
    pg.Execute(shell="sh", command="/local/repository/scripts/startup.sh")
)

pc.printRequestRSpec(request)