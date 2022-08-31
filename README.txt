Command Injection Exercise
**************************

To test the vulnerability, I added an illegal input after the requested domain name to create a file to a selected location.

$ python nslookup.py
Enter the domain name: google.com.com &  touch /c/Users/someuser/Desktop/secret-file.txt

$ ls
 24hEksamenTour-DK.pdf  'CrystalDiskMark 7.lnk'  'MSI Afterburner.lnk'   WinDirStat.lnk   desktop.ini
 CrystalDiskInfo.lnk     KeePass-2.46             SpeedFan.lnk           WinMTR.exe       secret-file.txt
 
 I could have done something more drastic, like deleted critical directories.
 
Topfix the issue, I added an if check, where the input gets compared against a regex that defines which characters are accepted.

The domain name string, from start to finish, must consist ONLY of the allowed characters. If any other character is found, None is returned.

pattern = '/^[a-zA-Z0-9\.]*$/'

result = re.search(pattern, domain_name)

if result == None:

    print('illegal input you ruffian') 
	
 
 After changing the code to have a check up for illegal characters, it no longer executes the illegal command, and taunts you if you try. 
 
 $ python nslookup.py
Enter the domain name: google.com & touch /c/Users/someuser/Desktop/secret-file.txt
illegal input you ruffian

NOTE: This check is entirely insufficient and only meant to demonstrate the type of change that would be needed. One could also use libraries meant for checking domain name validity.