"""Start-up script adapted from https://github.com/emulab/my-profile"""

import geni.portal as portal
import geni.rspec.pg as pg
import os

CL_REPO_PATH_ABS = "/local/repository/"
STARTUP_SCRIPT_PATH_REL = "scripts/startup.sh"


pc = portal.Context()

request = pc.makeRequestRSpec()

node = request.RawPC("node")

node.hardware_type = 'c240g5'

node.addService(
    pg.Execute(shell="sh", command=os.path.join(CL_REPO_PATH_ABS, STARTUP_SCRIPT_PATH_REL))
)

pc.printRequestRSpec(request)