from bson import ObjectId

def serialize_document(document):
    if document is None:
        return None
        
    document["_id"] = str(document["_id"])
    return document

def serialize_documents(documents):
    return [serialize_document(document) for document in documents]

def to_object_id(di_value: str):
    try:
        return ObjectId(id_value)
    except Exception:
        return None