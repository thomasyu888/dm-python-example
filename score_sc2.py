'''
@author: bhoff
'''

import csv
import os
import time

if __name__ == '__main__':
    crossWalkPath='/metadata/images_crosswalk.tsv'
    if not os.path.isfile(crossWalkPath):
        raise Exception(crossWalkPath+' does not exist')
    
    examsMetadataPath='/metadata/exams_metadata.tsv'
    if not os.path.isfile(examsMetadataPath):
        raise Exception(examsMetadataPath+' does not exist')
    
    time.sleep(120) # sleep for two minutes
   
    existingsamples = []
    with open(crossWalkPath,'r') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        f = open('/output/predictions.tsv', 'w')
        f.write("subjectId\tlaterality\tconfidence\n")
        first=True
        for row in tsvin:
            if first: # skip the header row
                first=False
                continue
            sample = row[0] + row[4] #Make sure there are no duplicated samples
            if sample not in existingsamples:
                f.write('%s\t%s\t0\n' % (row[0], row[4]))
                existingsamples.append(row[0] + row[4])
                imageFile='/scoringData/'+row[5]
                if not os.path.isfile(imageFile):
                    raise Exception(imageFile+' does not exist')
    f.close()
        
