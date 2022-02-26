import os
def get_uploaded_images():
    lst = []
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            img = os.path.join(subdir, file)
            temp = (f"{img.split('/')[7:]}").replace('[','')
            new = temp.replace(']','')
            if 'png' in new or 'jpg' in new:                
                lst.append(new.replace(new[0],''))
    return lst
print(get_uploaded_images())
 	    
