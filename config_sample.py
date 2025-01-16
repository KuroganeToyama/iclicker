# Email address to login to iClicker Cloud
EMAIL = ''

# Password to login to iClicker Cloud
PASSWORD = ''

# The full path to your Downloads folder, or whichever folder that stores the downloaded files 
# when you manually download them from iClicker Cloud, since iClicker Cloud does not let you choose 
# the download path and only uses the browser default
# Examples: DOWNLOAD_PATH = '/Users/me/Downloads' (MacOS/Linux would look something like this)
#           DOWNLOAD_PATH = 'C:/Users/me/Downloads' (Windows would look something like this)
DOWNLOAD_PATH = ''

# Dictionary of KVPs in the form of Section: [Poll], to specify which polls to be ignored during data collection
# Key: section name, exactly as it appears on iClicker Cloud
# Value: a list of poll names to be ignored for that section, exactly as they appear on iClicker Cloud
# Examples: EXCEPTIONS = {
#   'CS135 Designing Functional Program': ['Class 1 - Poll', 'Class 2 - Poll'],
#   'CS135-004 (John Doe 6:00 TTh)': ['Class 3 - Poll', 'Class 7 - Poll', 'Class 10 - Poll']
# }
EXCEPTIONS = {}