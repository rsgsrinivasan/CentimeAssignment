import os, time
from utilities.logger import *


def before_all(context):
    context.log = logger.getLogger()
    context.ApiKey = open("ApiKey.txt","r").read()


def before_scenario(context,scenario):
    if "throttlingTest5RPM" in scenario.tags:
        try:
            with open("RequestCount.txt","r") as fp:
                context.requestsCount = 1
                time.sleep(70)
            os.remove("RequestCount.txt")
        except:
            pass
    
    if "regularTestswithoutAPIKEY" in scenario.tags:
        context.ApiKey = ""

def after_scenario(context,scenario):
    if "regularTests" in scenario.tags:
        with open("RequestCount.txt","w") as fp:
            pass


