import urllib2, json

table = {'blake': 0, 'rabia': 0, 'arjun': 0, 'yinghong': 0, 'wenran': 0, 'total': 0}
issue = {'blake': 0, 'rabia': 0, 'arjun': 0, 'yinghong': 0, 'wenran': 0, 'total': 0}

def get_issues_statistics():
    url = "https://api.github.com/repos/ArjunSingh1/SoftwareLab/issues"
    try:
        r = urllib2.Request(url)
        opener = urllib2.build_opener()
        data = opener.open(r)
        result = json.loads(data.read())
        for i in range(0, len(result)):
            if result[i]['user']['login'] == 'Bgardner4':
                issue['blake'] +=1
            elif result[i]['user']['login'] == 'YinghongLIU':
                issue['yinghong'] +=1
            elif result[i]['user']['login'] == 'ArjunSingh1':
                issue['arjun'] +=1
            elif result[i]['user']['login'] == 'wenranlu':
                issue['wenran'] +=1
            elif result[i]['user']['login'] == 'rabiakhan713':
                issue['rabia'] +=1

            issue['total'] = len(result)
    except:
        issue['blake'] = "error"
        issue['yinghong'] = "error"
        issue['wenran'] = "error"
        issue['arjun'] = "error"
        issue['rabia'] = "error"
        issue['total'] = "error"
    return issue

def get_contributors_statistics():
    url = "https://api.github.com/repos/ArjunSingh1/SoftwareLab/contributors"
    try:
        r = urllib2.Request(url)
        opener = urllib2.build_opener()
        data = opener.open(r)
        result = json.loads(data.read())
        for i in range(0,len(result)):
            if result[i]['login'] =='Bgardner4':
                table['blake'] = result[i]['contributions']
            elif result[i]['login'] =='YinghongLIU':
                table['yinghong'] = result[i]['contributions']
            elif result[i]['login'] =='ArjunSingh1':
                table['arjun'] = result[i]['contributions']
            elif result[i]['login'] =='wenranlu':
                table['wenran'] = result[i]['contributions']
            elif result[i]['login'] =='rabiakhan713':
                table['rabia'] = result[i]['contributions']
        table['total'] = table['rabia']+ table['wenran'] + table['blake'] + table['yinghong'] + table['arjun']
    except:
        table['blake'] = "error"
        table['yinghong'] = "error"
        table['wenran'] = "error"
        table['arjun'] = "error"
        table['rabia'] = "error"
        table['total'] = "error"
    return table
