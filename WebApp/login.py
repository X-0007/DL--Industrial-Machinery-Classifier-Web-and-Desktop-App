from pymongo import MongoClient


def addDocs(uname, pwd):
    client = MongoClient("mongodb://127.0.0.1/27017")

    db = client['Login']

    data = db.Login_Form

    doc = {'Username': uname, 'Password': pwd}
    # doc = [{'uname': 'Admin', 'pwd': 'Admin'}]

    data.insert_one(doc)
