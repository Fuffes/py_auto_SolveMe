
from db import session

import tables


res = session.query(tables.User.id, tables.User.name, tables.User.age).first()

print(res)