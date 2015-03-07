def init(data):
    data['first']={}
    data['mid']={}
    data['end']={}

def look(data, label, val):
    return data[label].get(val)
    
def store(data, full_name):
    names=full_name.split()
    if len(names)==2:
        names.insert(1,"")
    labels='first','mid','end'
    for label, name in zip(labels,names):
        people = look(data,label,name)
        if people:
            data[label][name].append(full_name)
        else:
            data[label][name]=[full_name]
