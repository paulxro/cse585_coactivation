"""Start-up script adapted from https://github.com/emulab/my-profile"""

import geni.portal as portal

import geni.rspec.pg as pg

pc = portal.Context()

request = pc.makeRequestRSpec()

node = request.RawPC("node")

node.addService(
    pg.Execute(shell="sh", command="/local/repository/scripts/startup.sh")
)

pc.printRequestRSpec(request)