from enum import Enum


class ApplicationModes(Enum):
    DEVELOPMENT = 'DEVELOPMENT'
    PRODUCTION = 'PRODUCTION'
    DEMO = 'DEMO'


# Set initial application mode and some other things
APPLICATION_MODE = ApplicationModes.DEVELOPMENT.value
DEBUG_MODE = True
SECRET_KEY = "this_is_a_sample_or_test_key"

# Flask Folders
templateFolder = '../templates'


# printing logs
def printLogs(message):
    if APPLICATION_MODE == ApplicationModes.DEVELOPMENT.value:
        print(message)


