'''
Created on Feb 13, 2013

@author: ksahlin
'''

import requests 
import getpass
import dateutil
from dateutil import parser
from pandas import DataFrame,Series

from collections import Counter
import datetime

pwd = getpass.getpass()
    
def ReturnDataFrame(repo):
    commits = requests.get("https://api.github.com/repos/%s/%s/commits" %(org,repo['name']), auth=("ksahlin", pwd))
    repo_commits = commits.json()
    message_list = []
    date_list = []
    
    for commit in repo_commits:
        if not isinstance(commit,dict):  
            continue
        message_list.append(commit['commit']['message'])
        date_list.append(parser.parse(commit['commit']['committer']['date']))
    s = Series(message_list, index=date_list,name=repo['name']) 
    return DataFrame(s)

def MostFrequentCommitTime(all_commits_df):
    freq_table = Counter()
    for row in all_commits_df.iterrows():
        freq_table[ (datetime.datetime.weekday(row[0]),row[0].hour) ] += 1
#        if int(row[0].hour) < 7 or int(row[0].hour) > 23:
#            print row
        #print datetime.datetime.weekday(row[0]),row[0].hour
    
    day_dict = {0 : 'Monday', 1 : 'Tuesday', 2 : 'Wednesday', 3 : 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6 : 'Sunday'}
    
    return( day_dict[freq_table.most_common(1)[0][0][0]], freq_table.most_common(1)[0][0][1] )



if __name__ == '__main__':
    org = 'pythonkurs'
    repos = requests.get("https://api.github.com/orgs/%s/repos" % org, auth=("ksahlin", pwd)) #get all repos in pythoncourse
    repos_data = repos.json()
    all_commits_df = DataFrame()
    #print repos_data
#    #### individual exploring
#    import sys
#    users = requests.get("https://api.github.com/orgs/pythonkurs/members", auth=("ksahlin", pwd))
#    users_data = users.json  
#    tot_repos = 0    
#    tot_users = 0
#
#    for user in users_data:  
#        indiv_repos = requests.get("https://api.github.com/users/%s/repos" % user['login'], auth=("ksahlin", pwd)) 
#        indiv_repos_data = indiv_repos.json
#        tot_repos += len(indiv_repos_data)
#        tot_users += 1
#    print tot_repos, tot_users
#    #sys.exit(0)
#    ########
    for repo in repos_data:
        df = ReturnDataFrame(repo)
        if not df.empty:
            all_commits_df = all_commits_df.append(df)

    day,hour = MostFrequentCommitTime(all_commits_df)
    print 'Most common commit date. Day:',day ,'Hour(24h):',hour 

    
