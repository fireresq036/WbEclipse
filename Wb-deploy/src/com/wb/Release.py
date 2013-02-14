'''
Created on Feb 6, 2013

@author: mrrussell
'''
import os

class Release(object):
    '''
    representation of a release
    '''
    STAGE_CONTINUOUS = 'continuous'
    STAGE_INTEGRATION = 'integration'
    STAGE_RELEASE = 'release'
    stages = [STAGE_CONTINUOUS, STAGE_INTEGRATION, STAGE_RELEASE]

    def __init__(self, base, tool, stage=STAGE_CONTINUOUS, version=None):
        '''
        Constructor
        '''
        if not stage in self.stages:
            raise Exception("stage not in ")
        self.base_dir = base
        self.tool = tool
        self.version = version()
        self.stage = stage
        self.working_dir = os.path.join(self.base_dir, tool, stage)

    def versions(self):
        all_versions = []
        for name in os.listdir(self.working_dir):
            if name != 'latest':
                all_versions.append(name)
        return all_versions

    def latest(self):
        latest = os.path.join(self.working_dir, 'latest');
        if os.path.islink(latest):
            return os.readlink(latest)
        else:
            return None

    def zips(self, eclipse_versions):
        zips = []
        updates = os.path.join(self.working_dir, 'latest', 'update')
        for name in os.listdir(updates):
            if name[-3:0] == "zip":
                zips.append(name)
        return zips;