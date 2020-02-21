import os
def DeleteFile():
    print('Which file do you want to delete?')
    file=str(input())
    if os.path.exists(file):
        os.remove(file)
        print('File is removed.')
    else:
        print('File does not exist.')

def RenameFile():
    print('Which file do you want to rename?')
    file=str(input())
    if os.path.exists(file):
        print('New name: ')
        new=str(input())
        os.rename(file, new)
    else:
        print('File does not exist.')

def AddContent():
    print('Which file do you want to work with?')
    file=str(input())
    if os.path.exists(file):
        filew=open(file, 'a')
        print('New content: ')
        filew.write(str(input()))
        filew.close
        print('New content is added.')
    else:
        print('File does not exist.')

def RewriteFile():
    print('Which file do you want to rewrite?')
    file=str(input())
    if os.path.exists(file):
        filew=open(file, 'w')
        print('Rewrite: ')
        filew.write(str(input()))
        filew.close
        print('File is rewritten.')
    else:
        print('File does not exist.')

def RenameDir():
    print('Which directory do you want to rename?')
    dire=str(input())
    if os.path.exists(dire):
        print('New name: ')
        new=str(input())
        os.rename(dire, new)
        print('Directory is renamed.')
    else:
        print('Directory does not exist.')

def AddFile():
    print('Which directory do you want to work with?')
    dire=str(input())
    if os.path.exists(dire):
        file=open('newf', 'w')
        file.close
        print('New file is added.')
    else:
        print('Directory does not exist.')

def AddDir():
    print('Which directory do you want to work with?')
    dire=str(input())
    if os.path.exists(dire):
        print('Name of new directory: ')
        new=os.mkdir(str(input()))
        print('New directory is added.')
    else:
        print('Directory does not exist.')

def NumOfFiles():
    print('Which directory do you want to work with?')
    dire=str(input())
    if os.path.exists(dire):
        numf=len([f for f in os.listdir() if f.is_file()])
        print(str(numf)+' files.')
    else:
        print('Directory does not exist.')

def NumOfDir():
    print('Which directory do you want to work with?')
    dire=str(input())
    if os.path.exists(dire):
        numd=len([d for d in os.listdir() if d.is_dir()])
        print(str(numd)+' directories.')
    else:
        print('Directory does not exist.')

def List():
    print('Which directory do you want to work with?')
    dire=str(input())
    for i in os.listdir(dire):
        print(i)

while True:
    print('''Choose you destiny:
             1. Files
             2. Directories
             3. Exit''')
    a=int(input())
    if a==1:
        print('''Choose your destiny. Again:
                 1. Delete file
                 2. Rename file
                 3. Add content
                 4. Rewrite''')
        b=int(input())
        if b==1:
            DeleteFile()
        elif b==2:
            RenameFile()
        elif b==3:
            AddContent()
        else:
            RewriteFile()
    elif a==2:
        print('''Choose your destiny. Again:
                 1. Rename directory
                 2. Add file
                 3. Add directory
                 4. Number of files
                 5. Number of directories
                 6. List''')
        b=int(input())
        if b==1:
            RenameDir()
        elif b==2:
            AddFile()
        elif b==3:
            AddDir()
        elif b==4:
            NumOfFiles()
        elif b==5:
            NumOfDir()
        else:
            List()
    else:
        print('Shao Kahn does not approve.')
        exit()
