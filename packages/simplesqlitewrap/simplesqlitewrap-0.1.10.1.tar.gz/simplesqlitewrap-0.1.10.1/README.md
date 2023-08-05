Simple class that wraps around the `sqlite3.conn().cursor().execute()` method

```py
from simplesqlitewrap import Database

class DbWrapper(Database):
    def create_tables(self):
    	self._execute('CREATE TABLE IF NOT EXISTS Users (user_id INTEGER PRIMARY KEY, first_name NVARCHAR);')

    def insert_users(self, users, **kwargs):
    	return self._execute('INSERT OR IGNORE INTO Users (user_id, first_name) VALUES (?, ?)', users, many=True, **kwargs)

    def select_users(self, **kwargs):
    	# returns the list of all the records in 'Users'
    	return self._execute('SELECT * FROM Users', fetchall=True, **kwargs)

db = DbWrapper('database.sqlite')
print(db)

db.create_tables()

params = [(1, 'Bob'), (2, 'Charlie')]
rows_inserted = db.insert_users(params, rowcount=True)
print('Rows inserted:', rows_inserted)

users = db.select_users(as_namedtuple=True)
for user in users:
	print('ID:', user.id, 'first name:', user.first_name)
```

### Installation

`pip install simplesqlitewrap`

### Disclaimer

If you stumbled upon this package, please remember that this is just a small utility I made for myself - breaking changes may be introduced without notice