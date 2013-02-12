'''
Created on Feb 12, 2013

@author: ksahlin
'''

from sahlin.session3 import CourseRepo, repo_dir
import sys,os

original_path = os.getcwd()
temp_path = sys.argv[1]
context_guard = repo_dir()
value = context_guard.__enter__(temp_path)
exc = True

try:
    try:
        var = value
        
        ###code to execute within the given context
        repo = CourseRepo(temp_path.split('/')[-1])
        if repo.check() == True:
            print 'PASS'
        else: 
            print 'FAIL'
            
        ###

    except:
        exc = False
        if not context_guard.__exit__(*sys.exc_info()):
            raise

finally:
    if exc:
        context_guard.__exit__(original_path, None, None, None)
        