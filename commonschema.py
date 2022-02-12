
def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id' }}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]



def serializeDicts(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id' },**{i:str(a[i]) for i in a if i=='stateid'}}

def serializeLists(entity) -> list:
    return [serializeDicts(a) for a in entity]