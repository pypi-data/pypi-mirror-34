__copyright__ = "# Copyright (c) 2016 by cisco Systems, Inc. All rights reserved."
__author__ = "Isobel Ormiston <iormisto@cisco.com>"

from unicon.plugins.iosxr.settings import IOSXRSettings

class MoonshineSettings(IOSXRSettings):

    def __init__(self):
        super().__init__()
        self.MOONSHINE_INIT_CONFIG_COMMANDS = [
            'no logging console'
        ] # @@@ Add any other config commands we want here. 
