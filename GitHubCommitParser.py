
import requests
import json
import os
import gql
import asyncio
import numpy
import io
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
token = input("inserisci token github: ")
owner = input("owner repository: ")
reposname = input("Repository Name: ")

transport = AIOHTTPTransport(
    url='https://api.github.com/graphql', 

    headers={'Authorization':"bearer " +  token}
    )

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql ('''query var1($owner:String!, $reposname: String!) { 
        repository(owner: $owner, name: $reposname) {
                    defaultBranchRef{
                target{
                    ... on Commit{
                        history{
                            edges{
                                node{
                                    ... on Commit{
                                        oid
                                    committedDate
                                    
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        }''')


parametri_query = {
                   "owner":owner,
                     "reposname" : reposname }
result = client.execute(query, variable_values=parametri_query) 





#result = client.execute(gql(query))



with open('d:/py/fileName41bis.csv', 'w') as f:

    for val in result['repository']['defaultBranchRef']['target']['history']['edges']:
        iod_found = (val['node']['oid'])
        io_found_Date =  (val['node']['committedDate'])  
        
   
        query2 = gql('''  query var1($oid:GitObjectID!, $owner:String!, $reposname: String!){
        repository(owner: $owner, name: $reposname) {
            object(oid: $oid) {
            ... on Commit {
                parents (first: 20) {
                nodes {
                    oid
                    message
                    committedDate
                }
                }
            }
            }
        }
        }''')
        
       
        params = {"oid": iod_found,
                   "owner":owner,
                     "reposname" : reposname }
        result2 = client.execute(query2, variable_values=params)  
              
   
        result3 = result2["repository"]["object"]["parents"]["nodes"] #assegna ad una variabile esplicita il filtering del json 
        
        for index in result3:
                    #per migliorare la lettura estrapolo OID e CommitedDate dal parent
                    parentoid = index["oid"]
                    parentdate = index["committedDate"]
                    s = (iod_found + "," + io_found_Date + ","+ parentoid +","+parentdate +"\r") #concatena i dati in formato CSV separati da virgola
                    #scrivo una riga TXT CSV dalla variabile S
                    for line in s:
                        f.write(line)
   
      

