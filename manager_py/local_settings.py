
DEBUG = True;
HEALTHCHECK_URL = "http://healthchecks/ping/303e6190-ac7d-4b94-ad5e-2e4db8e7732d";
LOG_NAME = ""
LOG_PATH = ""
#FILE_AGE = 60*60*48; # TIME IN SECONDS
FILE_AGE = (60*60*24*2); # shouldn't pick anything up.
FILE_PATHS = ["nightly_file_management_","C:/Local_Code/repos/GEICS/sent_files"];
FILE_PATTERNS = [".txt","_"];
# PRUNE SETTINGS
# this can be set to purge sent_files as well, just be careful that you don't delete anything you don't need. (all will be maintained in their source directories too.
MAX_LOG_AGE = (7*60*60*24); # default to a week.
PRUNE_PATTERNS = [".log",".interim","_log.txt"];   # truncate the log and counter files- just to prevent unecessary clutter - if you keep the counts you can see exactly how many were actually sent.
PRUNE_PATHS = [".",".\\logs"];          # default to no paths.


# need to change this up - we'll set up a new 
#PATH_AGES={# key is going to be as follows: ("path","pattern"):age_in_seconds
#  ("nightly_file_management_","_.txt"):10,
#  (".","_.txt"):60
#}
