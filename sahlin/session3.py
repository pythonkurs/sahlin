'''
Created on Feb 11, 2013

@author: ksahlin
Code for session3 homework
'''

import os

class repo_dir(object):
    def __enter__(self,path):
        os.chdir(path)
            
    def __exit__(self, path, type, value, traceback):
        os.chdir(path)


class CourseRepo(object):
    '''
    classdocs
    '''

    def __init__(self,surname):
        '''
        Constructor
        '''
        self.surname = surname
        
    @property
    def required(self):
        return [".git","setup.py","README.md","scripts/getting_data.py","scripts/check_repo.py", self.surname+"/__init__.py",self.surname+"/session3.py"]
    
    def check(self):
        for sPath in self.required:
            if not os.path.exists(sPath):
                return 'Path '+sPath+' does not exist.'
        
        return True
    
    
##tests
#
#repo = CourseRepo("a")
#print(repo.required[-1])
## prints a/session3.py
#
#repo.surname = "b"
#print(repo.required[-1])
## prints b/session3.py
#print repo.check()