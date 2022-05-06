import os, shutil

curr = os.path.abspath(os.getcwd())
total = 0

for folders, subfolders, files in os.walk(curr):
    for file in files:
        fsize = os.path.getsize(folders+'\\'+file)
        if fsize > 50000000:
            if os.path.exists('big files'):
                pass
            else:
                os.mkdir('big files')
            try:
                print('Moving %s to ...%s' % (os.path.basename(file)[:10], os.path.abspath('big files'+'\\'+file)[50:]))
                shutil.move(os.path.join(folders, file), './/big files')
            except:
                pass
    
            
