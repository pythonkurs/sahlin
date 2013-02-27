'''
Created on Feb 12, 2013

@author: ksahlin
'''

from sahlin.session3 import CourseRepo, repo_dir
import sys,os

with repo_dir(sys.argv[-1]):
    ###code to execute within the given context
    repo = CourseRepo(sys.argv[-1].split('/')[-1])
    if repo.check() == True:
        print 'PASS'
    else: 
        print 'FAIL'