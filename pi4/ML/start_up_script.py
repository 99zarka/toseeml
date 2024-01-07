import os
commands = """cd /home/pi/Desktop/FR/tfenv2/bin/
source activate
cd /home/pi/Desktop/ML
python3 pi_driver.py
"""
os.system(commands)