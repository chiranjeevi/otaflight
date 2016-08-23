# releaseNotes.ps1 BambooJob buildNo


import requests
from xml.etree import ElementTree
import sys

if len(sys.argv) == 3:
    BitbucketAPIURL = 'http://bamboo.fleetmatics.host:8085/rest/api/'
    bambooJobName = sys.argv[1]
    bambooBuildNo = sys.argv[2]
    userId = 'chiranjeevi.patel'
    pwd = 'Qwer1234@1'

    commitDetailsURL = BitbucketAPIURL + 'latest/result/' + bambooJobName + "/" + bambooBuildNo + '?expand=changes.change.files'
    content = ElementTree.fromstring((requests.get(commitDetailsURL, auth=(userId, pwd))).content)
    commentlog = ""
    for i in content.iter('change'):
        commentlog = commentlog + '\n' + i.find('comment').text + "--" + i.attrib['fullName'] + "--" + i.attrib['changesetId']

    print "commentlog " + commentlog.encode('utf-8')
    if commentlog.encode('utf-8') and commentlog.encode('utf-8').strip():
        f = open('releaseNotes.txt', 'w')
        f.write(commentlog.encode('utf-8'))
        f.close()
    else:
        print "build #"+ bambooBuildNo + " doesnt have any changes in bamboo build" + commentlog

else:
    print  sys.argv[0:]
    print "USAGE : Python releaseNotes.py JOBID BUILD_NO"
    print "USAGE : Python releaseNotes.py MI-LOGBOOKIOSCI 86"


#changes = content.find('changes')
#obj = untangle.parse(commitDetails.content)
#root = content.getroot()
