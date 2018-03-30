file_names=[]
dirs_no_files=[]
empty_dir=[]
from os import walk
for dirpath,dirnames,filenames in walk('D:\Testing'):
    print(dirpath,dirnames,filenames)
    if len(dirnames)==0 and len(filenames)==0:
        empty_dir.append(dirpath)
        
        
    if len(filenames)!=0:
        #print(dirpath,dirnames,filenames)
        for i in filenames:
            a=dirpath+'\\'+i
            file_names.append(a)
    else:
        #print(dirpath)
        dirs_no_files.append(dirpath)
        
print('filenames with path')        
print(file_names)
print('dirs with no files')
print(dirs_no_files)
print('empty dirs')
print(empty_dir)
'''    break
    for i in filenames:
        l.append(i)        
print(l)
     

D:\Testing\Testing1\txt1.txt
D:\Testing\Testing1\txt2.txt
'''
