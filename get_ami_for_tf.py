#!/usr/bin/env python

import json
import subprocess

# list of destrebutions
destrebutions = ["squeeze", "wheezy", "jessie"]

# official owner
debianOwners = "379101102735"

# get regions AWS EC2
regionsAWS = "aws ec2 describe-regions"
process = subprocess.Popen(regionsAWS.split(), stdout=subprocess.PIPE)
regionsJSON = process.communicate()[0]
regionsDecode = json.loads(regionsJSON)
regions = []
for region in regionsDecode['Regions']:
    regions.append(region['RegionName'])

# get images AWS EC2 from regions
terraformDefault = {}
for region in regions:
    imagesAWS = "aws --region "+region+" ec2 describe-images --owners "+debianOwners
    process = subprocess.Popen(imagesAWS.split(), stdout=subprocess.PIPE)
    imagesJSON = process.communicate()[0]
    imagesDecode = json.loads(imagesJSON)
    for image in imagesDecode['Images']:
        if not image['Public']:
            continue
        if image['VirtualizationType'] == 'paravirtual':
            image['VirtualizationType'] = 'pv'
        destr = ""
        for destrebution in destrebutions:
            if destrebution in image['Name']:
                destr = destrebution
                break
        if destr == '':
            continue
        index = region+"-"+image['Architecture']+"-"+image['VirtualizationType']+"-"+destr
        
        if (not terraformDefault.has_key(index)) or terraformDefault[index]['date']<image['CreationDate']:
            terraformDefault[index] = {
                "date" : image['CreationDate'],
                "value" : image['ImageId']
            }

# normalize default
terraformDefaultN = {}
for terraformDefaultName in terraformDefault:
    terraformDefaultN[terraformDefaultName] = terraformDefault[terraformDefaultName]['value']

terraform = {
    "variable" : {
        "amis" : {
            "description" : "Debian AMIs List",
            "default" : terraformDefaultN
        }
    }
}

terraformJSON = json.dumps(terraform)
print terraformJSON
