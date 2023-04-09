def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [f'Hello, my name is {name}.' for name in names]
    # x=[]
    # for name in names:
    #     x.append(f'hello {name}')
    # return x

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!" for name in names]
    # x=[]
    # for name in names:
    #     x.append(f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!")
    # return x

def printer(names):
    [print(msg) for msg in batch_badge_creator(names)]
    [print(msg) for msg in assign_rooms(names)]
    # for string in batch_badge_creator(names):
    #     print(string)
    # for string in assign_rooms(names):
    #     print(string)

names=['a','b']
printer(names)