# tap-to-click-on
fixes the default behaviour of Lubuntu and similar distributions, where tap-to-click is disabled by default.  
Tested on Lubuntu 20.04.

__the python script:__
usage: once made executable, simply launch it.
tap-to-click-on.py should be stored into _/usr/bin_ and made executable by _'sudo chmod +x /usr/bin/tap-to-click-on.py_   
***tap-to-click-on.py assumes your python 3 executable is in /usr/bin : amend it if different on your system***

__the patched shell script__
lubuntu-upg-notifier.sh is a patched version of the originally installed script checking for updates; this is done to hijack the script and make sure the tap-to-click-on.py script is executed at every boot close to boot end. The only modified line is where " && /usr/bin/tap-to-click-on.py" is added.  
Location of lubuntu-upg-notifier.sh: _/usr/lib/lubuntu-update-notifier/lubuntu-upg-notifier.sh_
