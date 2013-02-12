'''
Created on Feb 11, 2013

@author: ksahlin
Code for session3 homework
'''

import os

class repo_dir(object):
    def __init__(self,target_path):
        self.target_path = target_path
        self.original_path = os.getcwd()
    def __enter__(self):
        os.chdir(self.target_path)
            
    def __exit__(self, type, value, traceback):
        os.chdir(self.original_path)


class CourseRepo(object):
    '''
    classdocs
    '''

    def __init__(self,surname):
        '''
        Constructor
        '''
        self.required = [".git","setup.py","README.md","scripts/getting_data.py","scripts/check_repo.py",surname + "/__init__.py",surname + "/session3.py"]

        
    @property
    def surname(self):
        return self.surname
    
    @surname.setter
    def surname(self,new_surname):
        self.required[-2] = new_surname + "/__init__.py"
        self.required[-1] = new_surname + "/session3.py"
        
        
    
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
#print repo.check(), repo.required