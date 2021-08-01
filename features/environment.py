import os, time

def before_scenario(context,scenario):
    if "throttlingTest5RPM" in scenario.tags:
        try:
            with open("RequestCount.txt","r") as fp:
                context.requestsCount = 1
                time.sleep(60)
            os.remove("RequestCount.txt")
        except:
            pass


def after_scenario(context,scenario):
    if "regularTests" in scenario.tags:
        with open("RequestCount.txt","w") as fp:
            pass
