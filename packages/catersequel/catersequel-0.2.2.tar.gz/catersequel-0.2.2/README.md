# Catersequel

-- image:: https://img.shields.io/pypi/v/Catersequel.svg?style=flat-square
	:target https://pypi.org/project/catersequel/
	:alt Latest Version

Catersequel is a simple API that provide helpers to manage raw SQL.

# What Catersequel can do?

Catersequel allows you to write raw SQL and forget about cursors and his data structures (tuples or dicts). Also allows you to write your query by pieces, making the whole thing more readable.

Let's see a few examples!

## Fetching results made simple

```python
from catersequel import Catersequel
from catersequel.engines.postgres import PostgreSQLEngine

cater = Catersequel(PostgreSQLEngine(dsn="YOUR-DATABASE-DSN"))
rows = cater.fetchall("SELECT name, surname FROM test")  # That command returns a RowResult you can iterate
for row in row:
    print(row.name)  # You can access to the data with dot notation.
    print(row['name'])  # Also as a dict-like object.
```

## Querying with arguments. No more pain.

```python
from catersequel import Catersequel
from catersequel.engines.postgres import PostgreSQLEngine

cater = Catersequel(PostgreSQLEngine(dsn="YOUR-DATABASE-DSN"))
row = cater.fetchone("SELECT name, surname FROM test WHERE name = %s", ("John", ))
print(row.name)  # Jhon
print(row.surname)  # Smith

row = cater.fetchone("SELECT name, surname FROM test WHERE name = %(name)s", {'name': 'John'})
print(row.name)  # Jhon
print(row.surname)  # Smith

row = cater.fetchone("SELECT name, surname FROM test WHERE name = %(name)s", name='John')
print(row.name)  # Jhon
print(row.surname)  # Smith
```

## Querying piece by piece
```python
from catersequel import Catersequel
from catersequel.engines.postgres import PostgreSQLEngine

cater = Catersequel(PostgreSQLEngine(dsn="YOUR-DATABASE-DSN"))
query = cater.query("SELECT * FROM test")
query.append("WHERE name = %(name)s", name="John")
row = cater.fetchone(query)
row.name  # John
row.surname  # Smith
```

## Execute all the things.
```python
from catersequel import Catersequel
from catersequel.engines.postgres import PostgreSQLEngine

cater = Catersequel(PostgreSQLEngine(dsn="YOUR-DATABASE-DSN"))
query = cater.query("INSERT INTO test (name, surname) VALUES")
query.append("(%(name)s, %(surname)s)", name="Thomas", surname="Anderson")

result = cater.execute(query)
print(result.lastrowid)  # Last Row ID of the last query if the engine supports it.
print(result.rowcount)  # How many rows retrieve the last query. It the engine supports it.
print(result.rownumber)  # Number of rows affected by the last query. If engine supports it.
```

## Transactions
```python
from catersequel import Catersequel
from catersequel.engines.postgres import PostgreSQLEngine

cater = Catersequel(PostgreSQLEngine(dsn="YOUR-DATABASE-DSN"))
cater.begin()
query = cater.query("INSERT INTO test (name, surname) VALUES")
query.append("(%(name)s, %(surname)s)", name="Carrie-Anne, surname="Moss")

result = cater.execute(query)
print(result.lastrowid)  # Last Row ID of the last query if the engine supports it.
print(result.rowcount)  # How many rows retrieve the last query. It the engine supports it.
print(result.rownumber)  # Number of rows affected by the last query. If engine supports it.

cater.commit()
```

# Collaborators Wanted!

If you have an idea you want to help me with Catersequel, cone the repo and make me a pull request!



Made with <3 in somewhere!
