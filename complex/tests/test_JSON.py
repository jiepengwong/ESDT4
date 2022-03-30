import json
from types import SimpleNamespace

# data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
data = '{"user_id": "123456789", "_id": "1234567893", "price": "9.50"}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
# print(x.name, x.hometown.name, x.hometown.id)
print(x.user_id)


