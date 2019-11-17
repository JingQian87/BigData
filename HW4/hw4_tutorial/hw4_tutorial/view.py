from django.http import HttpResponse
from django.shortcuts import render
import pandas_gbq
from google.oauth2 import service_account

# Make sure you have installed pandas-gbq at first;
# You can use the other way to query BigQuery.
# please have a look at
# https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-nodejs
# To get your credential

credentials = service_account.Credentials.from_service_account_file('/Users/mac/Downloads/My Project-90f1fab4944b.json')


def hello(request):
    context = {}
    context['content1'] = 'Hello World!'
    return render(request, 'helloworld.html', context)


def dashboard(request):
    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = "winged-plate-252922"
    '''
        TODO: Finish the SQL to query the data, it should be limited to 8 rows. 
        Then process them to format below:
        Format of data:
        {'data': [{'Time': hour:min, 'count': {'ai': xxx, 'data': xxx, 'good': xxx, 'movie': xxx, 'spark': xxx}},
                  {'Time': hour:min, 'count': {'ai': xxx, 'data': xxx, 'good': xxx, 'movie': xxx, 'spark': xxx}},
                  ...
                  ]
        }
    '''
    SQL = "select * from datasetHW3.wordcount2 limit 8"
    df = pandas_gbq.read_gbq(SQL)
    #print(df)
    data = {}

    res = []
    words = ['ai','data','good','movie','spark']
    time = sorted(list(df.time))
    for i in time:
        tmp = {}
        tmp['Time'] = str(i)[11:16]
        tmp['count'] = {}
        for j in words:
            tmp['count'][j] = int(df[df.time==i][j])
        res.append(tmp)
    data['data'] = res
    #print(data['data'])
    return render(request, 'dashboard.html', data)


def connection(request):
    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = "winged-plate-252922"
    '''
        TODO: Finish the SQL to query the data, it should be limited to 8 rows. 
        Then process them to format below:
        Format of data:
        {'n': [xxx, xxx, xxx, xxx],
         'e': [{'source': xxx, 'target': xxx},
                {'source': xxx, 'target': xxx},
                ...
                ]
        }
    '''

    SQL1 = 'select * from datasetHW3.node'
    df1 = pandas_gbq.read_gbq(SQL1)
    #print("node preview: ", df1[:5])
    node = []
    for i in range(len(df1)):
        tmp = {}
        tmp['node'] = int(df1['node'][i])
        node.append(tmp)
    #print("node,", node[:5])

    SQL2 = 'select * from datasetHW3.edge'
    df2 = pandas_gbq.read_gbq(SQL2)
    #print("edge preview: ", df2[:5])
    edge = []
    visited = set()
    for i in range(len(df2)):
        tmp = {}
        pair = (int(df2['source'][i]), int(df2['target'][i]))
        if pair not in visited:
            visited.add(pair)
            tmp['source'] = pair[0]
            tmp['target'] = pair[1]
            edge.append(tmp)
    print("len of edge: ", len(edge))
    data = {}
    data['n'] = node
    data['e'] = edge

    return render(request, 'connection.html', data)
