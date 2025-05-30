import os_detection as osd

if osd.detection() == "Win":
    pass
elif osd.detection() == "Lin":
    pass
else:
    print("Scanner is not built for your OS ")