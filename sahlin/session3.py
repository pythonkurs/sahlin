'''
Created on Feb 11, 2013

@author: ksahlin
Code for session3 homework
'''

import os

class repo_dir(object):
    #@profile
    def __init__(self,target_path):
        self.target_path = target_path
        self.original_path = os.getcwd()
    #@profile
    def __enter__(self):
        os.chdir(self.target_path)
    #@profile
    def __exit__(self, type, value, traceback):
        os.chdir(self.original_path)

class CourseRepo(object):
    '''
    classdocs
    '''
    #@profile
    def __init__(self,surname):
        '''
        Constructor
        '''
        self._surname = surname
        self.required = [".git","setup.py","README.md","scripts/getting_data.py","scripts/check_repo.py",surname + "/__init__.py",surname + "/session3.py"]

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self,new_surname):
        self._surname = new_surname
        self.required[-2] = new_surname + "/__init__.py"
        self.required[-1] = new_surname + "/session3.py"   

    #@profile    
    def check(self):
        for sPath in self.required:
            if not os.path.exists(sPath):
                return 'Path '+sPath+' does not exist.'
        
        return True
    
if __name__ == "__main__":   
    import sys,os
    
    with repo_dir(sys.argv[-1]):
        ###code to execute within the given context
        repo = CourseRepo(sys.argv[-1].split('/')[-1])
        if repo.check() == True:
            print 'PASS'
        else: 
            print 'FAIL'