# cse585_coactivation

**Codelab Start-up**

*Make sure that you have a reservation active for a c240g5 node.*

1. Login to the cloudlab portal.
2. Navigate to "Start Experiment" under the top-left dropdown.
3. Click "Change Profile" and search for "paldea" -- select this profile and click next.
4. Give the experiment a unique name, select "Michigan-BigData" as the project. Click next.
5. Set experiment details as appropriate (e.g. 4 hrs, start now). Click finish.
6. Wait for experiment to start.
7. SSH into the machine via terminal or VSCode (recommended). Proceed to start-up guide.

**Start-up Guide**

1. Once you are connected to the node (via ssh), navigate to the repository directory:

`cd /local/repository`

2. Make the start-up script executable:

`chmod +x ./scripts/startup.sh`

3. Run the start-up script. Make sure to accept all prompts:

`sudo ./scripts/startup.sh`

4. Run the extension installations:

`./scripts/extensions.sh`

5. Navigate to the "test.ipynb" and run the first cell. You should see generated output from gpt-2.

## PowerInfer

1. Clone the PowerInfer repository.