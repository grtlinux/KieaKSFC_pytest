# file: test_pydantic01.py
# date: 2023-04-05
# comment:
#   - Python 3.7

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

# external_data = {'id':'123', 'signup_ts':'2019-06-01 12:22', 'friends':[1,'2',b'3']}
external_data = {'id':'123', 'signup_ts':'2019-06-01 12:22', 'friends':[1,'2',b'3'], 'name':'홍길동'}
user = User(**external_data)
print(user)
print(user.id)
print(user.name)
print(user.signup_ts)
print(user.friends)

# print(json.dumps(user.dict(), ensure_ascii=False, indent=4)) # TypeError
# print(json.dumps(user.dict()))   # TypeError
# print(json.dumps(user)) # TypeError
# print(user.model_dump()) # AttributeError

print(user.dict())
print(user.json(indent=4, ensure_ascii=False))
print(user.json(indent=4, exclude={'id'}))

print(type({'id'}))
# <class 'set'>

