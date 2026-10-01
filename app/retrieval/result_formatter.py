def format_retrieval(result):
    return [obj.properties or {} for obj in getattr(result, "objects", [])]
