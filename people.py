from flask import make_response, abort
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
        "Li": {
                "fname": "Derek",
                "lname": "Li",
                "timestamp": get_timestamp()
        },
        "Joseph": {
                    "fname": "Albin",
                    "lname": "Joseph",
                    "timestamp": get_timestamp()
        },
        "Lam": {
                 "fname": "Kristie",
                 "lname": "Lam",
                 "timestamp": get_timestamp()
        },
    }
        
def read_all():
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(404, "Person with the last name {lname} not found".format(lname=lname))
    return person

def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
                "lname": lname,
                "fname": fname,
                "timestamp": get_timestamp()
        }
        return make_response("{lname} successfully created".format(lname=lname), 201)
    else:
        abort(406, "Person with last name {lname} already exists".format(lname=lname))

def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        
        return PEOPLE[lname]
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))
    
def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response("{lname} successfully deleted".format(lname=lname), 200)
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))