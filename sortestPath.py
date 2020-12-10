UserDict = { "key1" : ["key2","key3","key4"] ,
             "key2" : ["key1","key5","key3"] ,
             "key3" : ["key2","key5","key7","key1"] ,
             "key4" : ["key1","key7"] ,
             "key5" : ["key2","key3","key7","key6"] ,
             "key6" : ["key8","key9","key5"] ,
             "key7" : ["key3","key4","key5"] ,
             "key8" : ["key6","key9"],
             "key9" : ["key6","key8","key10"],
             "key10": ["key9","key12"],
             "key12" : []
            }
def ShortestPath(DB,start,end,currentPath=[],Userpath=[]):
    Userpath = Userpath + [start]
    if start == end : 
        return Userpath
    for friends in UserDict[start]:
        if friends not in Userpath:
            newpath = ShortestPath(DB,friends,end,currentPath,Userpath)
            if newpath :
                if(len(newpath)<len(currentPath)):
                    currentPath = newpath
    return currentPath   
                

start = "key9"
end = "key1"
if start in UserDict and end in UserDict:
    Path = [x for x in UserDict]
else:
    Path=[]
print(ShortestPath(UserDict,start,end,Path))
