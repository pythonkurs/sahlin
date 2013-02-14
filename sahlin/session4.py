'''
Created on Feb 13, 2013

@author: ksahlin
'''

import requests 
import getpass
import dateutil
from dateutil import parser
from pandas import DataFrame,Series
import pandas

pwd = getpass.getpass()
    
def ReturnDataFrame(repo):
    #print repo['name']
    commits = requests.get("https://api.github.com/repos/%s/%s/commits" %(org,repo['name']), auth=("ksahlin", pwd))
    repo_commits = commits.json
    message_list = []
    date_list = []
    for commit in repo_commits:
        message_list.append(commit['commit']['message'])
        date_list.append(parser.parse(commit['commit']['committer']['date']))
    s = Series(message_list, index=date_list,name=repo['name']) 
    return DataFrame(s)

def MostFrequentCommitTime():
    return



if __name__ == '__main__':
    org = 'pythonkurs'
    #get all repos in pythoncourse
    repos = requests.get("https://api.github.com/orgs/%s/repos" % org, auth=("ksahlin", pwd))
    repos_data = repos.json
    all_commits_df = DataFrame()
    #counter =0
    for repo in repos_data:
        #counter +=1
        all_commits_df = all_commits_df.append(ReturnDataFrame(repo))
        #if counter >=5:
        #    break
    #print all_commits_df.sort().index
