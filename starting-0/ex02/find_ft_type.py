def all_thing_is_obj(object: any = None) -> int:
    t = type(object)
    if object is None:
        return
    elif t is int:
        print("Type not found")
    else:
        name = t.__name__.capitalize()
        print(name if name != "Str" else object + " is in the kitchen", " : ", t)
    return 42
