fileobj =  open('me274_blog_2016Fa.xml')
fileobj2 = open('me274_2016New.xml','w')
NameMap = dict()
x = 0
numline = 1
for line in fileobj:
    if 'wp:author_email' in line:
        name = line.split('wp:author_email')[1].split('CDATA[')[1].split(']]')[0]
        if name not in NameMap:
            AnnName = str(x)+'@purdue.edu'
            NameMap[name] = AnnName
            x += 1
        else:
            AnnName = NameMap[name]
        newline = line.replace(name,AnnName)
        newline = newline.replace(name.replace('@purdue.edu',''),AnnName.replace('@purdue.edu',''))
        fileobj2.write(newline)
    elif("wp:comment_author_email") in line:
        name = line.split('CDATA[')[1].split(']]')[0]
        if name not in NameMap:
            AnnName = str(x)+'@purdue.edu'
            NameMap[name] = AnnName
            x += 1
        else:
            AnnName = NameMap[name]
        newline = line.replace(name,AnnName)
        fileobj2.write(newline)
    elif("wp:comment_author") in line and 'CDATA' in line and 'IP' not in line:
        pass
    elif "dc:creator" in line:
        flag = 0
        name = line.split('CDATA[')[1].split(']]')[0]+'@purdue.edu'
        if name == '@purdue.edu':
            flag = 1
        if flag == 0:
            if name not in NameMap:
                AnnName = str(x)+'@purdue.edu'
                NameMap[name] = AnnName
                x += 1
            else:
                AnnName = NameMap[name]
            newline = line.replace(name,AnnName)
            newline = newline.replace(name.replace('@purdue.edu',''),AnnName.replace('@purdue.edu',''))
            fileobj2.write(newline)
    else:
        fileobj2.write(line)
    
    numline += 1
pd.DataFrame.from_dict(NameMap,orient = 'index').to_csv('NameMap_2016.csv')
fileobj.close()
fileobj2.close()