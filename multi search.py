import re
import os

rootdir = 'C:\\Projects'
ext = '.txt'

with open('SearchStr.log') as fin1:
    searchStrList = fin1.read().splitlines()

with open('Result.csv','a') as fout:
    for searchStr in searchStrList:
        for root, subFolders, files in os.walk(rootdir):
            for name in files:
                if name.lower().endswith(ext):
                    with open(os.path.join(root,name),'r') as fin2:
                        i = 0 #line number counter
                        for line in fin2:
                            i += 1
                            match = re.search(searchStr, line)
                            if match:
                                fout.write("%s" % os.path.join(root,name) + ":\t") #printout file path and file name
                                fout.write("Line " + str(i) + ":\t")  #printout a line number
                                fout.write("Searched: " + searchStr + "\t")  #printout the searched string
                                fout.write(line)  #printout the line containing searched string
                            else:
                                i += 1