
DEBUG = True;
HEALTHCHECK_URL = "http://healthchecks/ping/303e6190-ac7d-4b94-ad5e-2e4db8e7732d";
LOG_NAME = ""
LOG_PATH = ""
#FILE_AGE = 60*60*48; # TIME IN SECONDS
FILE_AGE = 20;
FILE_PATHS = [".","nightly_file_management_"];
FILE_PATTERNS = [".txt",".log"];

# need to change this up - we'll set up a new 
#PATH_AGES={# key is going to be as follows: ("path","pattern"):age_in_seconds
#  ("nightly_file_management_","_.txt"):10,
#  (".","_.txt"):60
#}
