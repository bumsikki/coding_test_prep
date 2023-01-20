def first_step(id):
    
    return id.lower()

def second_step(id):
    print("1", id)
    specials = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = ""
    for c in id:
        if c not in specials:
            new_id += c
    print("2", new_id)
    return new_id

def third_step(id):
    dots = "." * len(id)
    while len(dots) > 1:
        if dots in id:
            id = id.replace(dots, ".")
            print(dots, id)
        dots = dots[:-1]
    print("3",id)
    return id

def fourth_step(id):
    
    start = 0
    end = len(id)
    if id[0] == ".":
        start += 1
    if id[-1] == ".":
        end -= 1
    print("4",id)
    return id[start:end]

def fifth_step(id):
    if len(id) == 0:
        id += 'a'
    print("5",id)
    return id

def sixth_step(id):
    if len(id) > 15:
        print("hi")
        id = id[:15]
        if id[-1] == ".":
            id = id[:-1]
    print("6",id)
    return id

def seventh_step(id):
    add_on = id[-1]
    while len(id) < 3:
        id += add_on    
    print("7",id)
    return id
    
def generate_newid(id):
    id = first_step(id)
    id = second_step(id)
    id = third_step(id)
    id = fourth_step(id)
    id = fifth_step(id)
    id = sixth_step(id)
    id = seventh_step(id)

    return id
    


def solution(new_id):
    answer = ''
    answer= generate_newid(new_id)
    
    return answer