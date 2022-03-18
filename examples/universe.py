import engula

uv = engula.Universe('localhost:21716')
db = uv.create_database('db')
print('created database', db.desc())
co = db.create_collection('co')
print('created collection', co.desc())
