# rrlogd-patcher

A python script to patch `rrlogd` in Xiaomi vacuums in order to disable encryption of cleaning logs. This will allow Valetudo to function properly on newer roborock firmwares.

The script has been tested on Gen1 firmware 3514 and Gen2 firmware 1780, but should also work for:
* Gen1 Firmwares >= 3514
* Gen2 Firmwares > 1518

# Usage
* Copy the rrlogd from your robot`scp root@roborock-ip:/opt/rockrobo/rrlog/rrlogd ./`
* Copy `patcher.py` to the same folder
* Run `python patcher.py` (requires python >= 3)
* The python file will output the patched binary into `rrlogd_patch`
* Copy the patched binary to the robot `scp rrlogd_patch root@roborock-ip:/root/`
* `ssh root@roborock-ip`
* Create a backup of the original `rrlogd` `mv /opt/rockrobo/rrlog/rrlogd opt/rockrobo/rrlog/rrlogd.bkp`
* Replace with the patched binary `mv /root/rrlogd_patch opt/rockrobo/rrlog/rrlogd`
* Give it execution permission `chmod +x /root/rrlogd_patch opt/rockrobo/rrlog/rrlogd`
* Reboot the vacuum

# Issues
As previously stated, this script has only been tested on a couple of firmwares, but should still work on other newer firmwares, as long as the encryption method is not changed.
If you encounter any problems, open an issue and clearly state the vacuum generation and firmware used.
