from DocString2Json import DocString2Json


def generate_for(scope):
    functions = []
    for function_name, function in scope.items():
        if function.__doc__ and function.__doc__.find("@api") == 0:
            functions.append(function)
    res = {}
    for function in functions:
        function_doc = DocString2Json(function.__doc__)
        if function_doc:
            if not res.get(function_doc.category):
                res[function_doc.category] = []
            # res[function_doc["category"]].append(function_doc)
            res[function_doc.category].append(dict(function_doc))
    for e in res.values():
        e.sort(key=lambda x: len(x["title"]))
    return res

