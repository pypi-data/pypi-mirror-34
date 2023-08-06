from queue import Queue


# Table class
# author dotcoo zhao <dotcoo@163.com>
# link http://www.dotcoo.com/table


class Cursor:
	def copy(self, cursor):
		self.description = cursor.description
		self.rowcount = cursor.rowcount
		self.lastrowid = cursor.lastrowid
		self.rows = cursor.fetchall()

	def fetch_all(self):
		return self.rows

	def fetch(self):
		return None if self.rows is None or len(self.rows) == 0 else self.rows[0] 

	def fetch_one(self, column = "id"):
		return None if self.rows is None or len(self.rows) == 0 or column not in self.rows[0] else self.rows[0][column]

	def fetch_column(self, column = "id"):
		return [row[column] for row in self.rows]

	def fetch_unique(self, column = "id"):
		return {row[column]: row for row in self.rows}

	def fetch_key_pair(self, key = "id", val = "name"):
		return {row[key]: row[val] for row in self.rows}


class ORM:
	def __init__(self):
		self.__parent = None
		self.__driver = "not_set_driver"
		self.__params = []
		self.__config = {}
		self.__prefix = ""
		self.__pool = Queue()

	def __del__(self):
		while not self.__pool.empty():
			if self.__parent is None:
				self.__pool.get().close()
			else:
				self.__parent.__pool.put(self.__pool.get())

	def clone(self):
		o = ORM()
		o.__parent = self
		o.__driver = self.__driver
		o.__params = list(self.__params)
		o.__config = dict(self.__config)
		o.__prefix = self.__prefix
		o.__pool = Queue()
		return o

	# === attrible ===

	def parent(self, parent = None):
		if parent is None:
			return self.__parent
		self.__parent = parent
		return self

	def config(self, driver, *args, **kwargs):
		if driver == "pymysql":
			pymysql = __import__("pymysql")
			self.__driver = driver
			self.__params = args
			config = {
				"host": "127.0.0.1",
				"user": "root", 
				"password": "123456",
				"db": "test",
				"charset": "utf8mb4",
			}
			config.update(kwargs)
			config.update({
				"autocommit": True,
				"cursorclass": pymysql.cursors.DictCursor,
			})
			self.__config = config
		elif driver == "sqlite3":
			sqlite3 = __import__("sqlite3")
			self.__driver = driver
			self.__params = args
			config = {}
			config.update(kwargs)
			self.__config = config
		else:
			print("database driver %s does not support" % database_driver)
			exit(1)
		return self

	def prefix(self, prefix = None):
		if prefix is None:
			return self.__prefix
		self.__prefix = prefix
		return self

	def pool(self, pool = None):
		if pool is None:
			return self.__pool
		self.__pool = pool
		return self

	# === connection pool ===

	def conn(self, conn = None):
		if conn is not None:
			self.__pool.put(conn)
			return self
		if not self.__pool.empty():
			return self.__pool.get()
		if self.__driver == "pymysql":
			pymysql = __import__("pymysql")
			return pymysql.connect(*self.__params, **self.__config)
		elif self.__driver == "sqlite3":
			sqlite3 = __import__("sqlite3")
			c = sqlite3.connect(*self.__params, **self.__config)
			c.row_factory = lambda cursor, row : {d[0]: row[i] for i, d in enumerate(cursor.description)}
			return c
		else:
			print("database driver %s does not support" % database_driver)
			exit(1)
		return self

	# === execute ===

	def execute(self, sql, *args):
		assert "'" not in sql and '"' not in sql, "a ha ha ha ha ha ha!"

		if self.__driver == "pymysql":
			sql = sql.replace("?", "%s")
		elif self.__driver == "sqlite3":
			sql = sql.replace("%s", "?")

		cursor = Cursor()

		conn = self.conn()
		cur = conn.cursor()

		cur.execute(sql, args)

		if self.__driver == "sqlite3":
			conn.commit()

		cursor.copy(cur)

		cur.close()
		self.conn(conn)

		return cursor

	def insert(self, sql, *args):
		return self.execute(sql, *args)

	def update(self, sql, *args):
		return self.execute(sql, *args)

	def delete(self, sql, *args):
		return self.execute(sql, *args)

	def replace(self, sql, *args):
		return self.execute(sql, *args)

	def select(self, sql, *args):
		return self.execute(sql, *args)

	# === SqlBuilder ===

	def table(self, table):
		return OrmSqlBuilder().orm(self).table(table).prefix(self.__prefix)

	def __getattr__(self, table):
		return self.table(table)


class SqlBuilder:
	def __init__(self):
		self.__prefix = ""
		self.__table = ""
		self.__pk = "id"
		self.__keywords = []
		self.__columns = []
		# self.__left_joins = []
		self.__wheres = []
		self.__where_params = []
		self.__groups = []
		self.__havings = []
		self.__having_params = []
		self.__orders = []
		self.__limit = None
		self.__offset = None
		self.__for_update = ""
		self.__lock_in_share_mode = ""

	def reset(self):
		self.__keywords = []
		self.__columns = []
		# self.__left_joins = []
		self.__wheres = []
		self.__where_params = []
		self.__groups = []
		self.__havings = []
		self.__having_params = []
		self.__orders = []
		self.__limit = None
		self.__offset = None
		self.__for_update = ""
		self.__lock_in_share_mode = ""
		return self

	def clone(self):
		s = self.__class__()
		s.__prefix = self.__prefix
		s.__table = self.__table
		s.__pk = self.__pk
		s.__keywords = list(self.__keywords)
		s.__columns = list(self.__columns)
		# s.__left_joins = list(self.__left_joins)
		s.__wheres = list(self.__wheres)
		s.__where_params = list(self.__where_params)
		s.__groups = list(self.__groups)
		s.__havings = list(self.__havings)
		s.__having_params = list(self.__having_params)
		s.__orders = list(self.__orders)
		s.__limit = self.__limit
		s.__offset = self.__offset
		s.__for_update = self.__for_update
		s.__lock_in_share_mode = self.__lock_in_share_mode
		return s

	# === attribute ===

	def prefix(self, prefix = None):
		if prefix is None:
			return self.__prefix
		self.__prefix = prefix
		return self

	def table(self, table = None):
		if table is None:
			return self.__table
		self.__table = table
		return self

	def full_table(self):
		return self.__prefix + self.__table
	
	def pk(self, pk = None):
		if pk is None:
			return self.__pk
		self.__pk = pk
		return self
	
	def keywords(self, *keywords):
		self.__keywords.extend(keywords)
		return self
	
	def calc_found_rows(self):
		return self.keywords("SQL_CALC_FOUND_ROWS")
	
	def columns(self, *columns):
		self.__columns.extend(columns)
		return self
	
	# def left_join(self, table, cond, *columns, prefix = None):
	# 	self.__left_joins.append({"table": table, "cond": cond, "columns": columns, "prefix": prefix})
	# 	return self
	
	def where(self, where, *args):
		self.__wheres.append(where.replace("?", "%s") % tuple([", ".join(["?" for _ in arg]) if type(arg) == list or type(arg) == tuple or type(arg) == set else "?" for arg in args]))
		[self.__where_params.extend(arg) if type(arg) == list or type(arg) == tuple or type(arg) == set else self.__where_params.append(arg) for arg in args]
		return self
	
	def group(self, *groups):
		self.__groups.extend(groups)
		return self
	
	def having(self, having, *args):
		self.__havings.append(having.replace("?", "%s") % tuple([", ".join(["?" for _ in arg]) if type(arg) == list or type(arg) == tuple or type(arg) == set else "?" for arg in args]))
		[self.__having_params.extend(arg) if type(arg) == list or type(arg) == tuple or type(arg) == set else self.__having_params.append(arg) for arg in args]
		return self
	
	def order(self, *orders):
		self.__orders.extend(orders)
		return self
	
	def limit(self, limit):
		self.__limit = limit
		return self
	
	def offset(self, offset):
		self.__offset = offset
		return self

	def page(self, page = 1, pagesize = 20):
		self.__limit = pagesize
		self.__offset = (page - 1) * pagesize
		return self
	
	def for_update(self):
		self.__for_update = " FOR UPDATE"
		return self
	
	def lock_in_share_mode(self):
		self.__lock_in_share_mode = " LOCK IN SHARE MODE"
		return self

	# === sql builder ===

	def insert(self, data):
		table = self.full_table()
		cols = ", ".join(["`" + col + "`" for col in data.keys()])
		vals = ", ".join(["?" for _ in data.values()])
		sql = "INSERT INTO `%s` (%s) VALUES (%s)" % (table, cols, vals)

		params = [val for val in data.values()]

		return sql, params
		
	def update(self, data):
		assert len(self.__wheres) > 0, "WHERE is empty!"
	
		table = self.full_table()
		sets = ", ".join(["`" + col + "` = ?" for col in data.keys()])
		wheres = "" if len(self.__wheres) == 0 else " WHERE " + " AND ".join(self.__wheres)
		orders = "" if len(self.__orders) == 0 else " ORDER BY " + ", ".join(self.__orders)
		limit = "" if self.__limit is None else " LIMIT ?"
		sql = "UPDATE `%s` SET %s%s%s%s" % (table, sets, wheres, orders, limit)

		params = [val for val in data.values()]
		params.extend(self.__where_params)
		if self.__limit is not None:
			params.append(self.__limit)

		return sql, params

	def delete(self):
		assert len(self.__wheres) > 0, "WHERE is empty!"
		
		table = self.full_table()
		wheres = "" if len(self.__wheres) == 0 else " WHERE " + " AND ".join(self.__wheres)
		orders = "" if len(self.__orders) == 0 else " ORDER BY " + ", ".join(self.__orders)
		limit = "" if self.__limit is None else " LIMIT ?"
		sql = "DELETE FROM `%s`%s%s%s" % (table, wheres, orders, limit)

		params = [p for p in self.__where_params]
		if self.__limit is not None:
			params.append(self.__limit)

		return sql, params

	def replace(self, data):
		table = self.full_table()
		sets = ", ".join(["`" + col + "` = ?" for col in data.keys()])
		sql = "REPLACE INTO `%s` SET %s" % (table, sets)
		
		params = [val for val in data.values()]

		return sql, params

	def select(self):
		table = self.full_table()
		keywords = "" if len(self.__keywords) == 0 else " " + " ".join(self.__keywords)
		columns = ["*"] if len(self.__columns) == 0 else list(self.__columns)
		left_joins = []
		# if len(self.__left_joins) > 0:
		# 	columns = [table + "." + column for column in columns]
		# 	for left_join in self.__left_joins:
		# 		prefix = prefix if left_join["prefix"] is not None else left_join["table"].full_table()
		# 		columns.extend([prefix + "." + column for column in left_join["columns"]])
		# 		left_joins.append(" LEFT JOIN %s ON %s" % (left_join["table"].full_table(), left_join["cond"].replace("__LEFT__", self.full_table()).replace("__THIS__", left_join["table"].full_table())))
		columns = ", ".join(columns)
		left_joins = "".join(left_joins)
		wheres = "" if len(self.__wheres) == 0 else " WHERE " + " AND ".join(self.__wheres)
		groups = "" if len(self.__groups) == 0 else " GROUP BY " + ", ".join(self.__groups)
		havings = "" if len(self.__havings) == 0 else " HAVING " + " AND ".join(self.__havings)
		orders = "" if len(self.__orders) == 0 else " ORDER BY " + ", ".join(self.__orders)
		limit = "" if self.__limit is None else " LIMIT ?"
		offset = "" if self.__offset is None else " OFFSET ?"
		for_update 	= self.__for_update
		lock_in_share_mode = self.__lock_in_share_mode
		sql = "SELECT%s %s FROM `%s`%s%s%s%s%s%s%s%s%s" % (keywords, columns, table, left_joins, wheres, groups, havings, orders, limit, offset, for_update, lock_in_share_mode)

		params = []
		params.extend(self.__where_params)
		params.extend(self.__having_params)
		if self.__limit is not None:
			params.append(self.__limit)
		if self.__offset is not None:
			params.append(self.__offset)

		return sql, params

	def count(self):
		table = self.full_table()
		wheres = "" if len(self.__wheres) == 0 else " WHERE " + " AND ".join(self.__wheres)
		sql = "SELECT count(*) AS count FROM `%s`%s" % (table, wheres)

		params = list(self.__where_params)

		return sql, params

	def plus(self, *args):
		assert len(self.__wheres) > 0, "WHERE is empty!"

		sets = ["`%s` = `%s` + ?" % (col, col) for i, col in enumerate(args) if i % 2 == 0]
		wheres = " WHERE " + " AND ".join(self.__wheres)
		sql = "UPDATE `%s` SET %s%s" % (self.__prefix + self.__table, ", ".join(sets), wheres)

		params = [val for i, val in enumerate(args) if i % 2 == 1]
		params.extend(self.__where_params)

		return sql, params
	
	def incr(self, col, val = 1):
		assert len(self.__wheres) > 0, "WHERE is empty!"
		
		wheres = " WHERE " + " AND ".join(self.__wheres)
		sql = "UPDATE `%s` SET `%s` = last_insert_id(`%s` + ?)%s" % (self.__prefix + self.__table, col, col, wheres)

		params = [val]
		params.extend(self.__where_params)

		return sql, params


class OrmSqlBuilder(SqlBuilder):
	def __init__(self):
		super().__init__()
		self.__orm = None
		self.sql = ""
		self.params = []

	def clone(self):
		s = super().clone()
		s.__orm = self.__orm
		return s

	# === attribute ===

	def orm(self, orm = None):
		if orm is None:
			return self.__orm
		self.__orm = orm
		return self

	# === execute ===

	def select(self):
		sql, params = super().select()
		self.sql = sql
		self.params = params
		return self.orm().select(sql, *params)

	def insert(self, data):
		sql, params = super().insert(data)
		self.sql = sql
		self.params = params
		return self.orm().insert(sql, *params)

	def update(self, data):
		sql, params = super().update(data)
		self.sql = sql
		self.params = params
		return self.orm().update(sql, *params)

	def delete(self):
		sql, params = super().delete()
		self.sql = sql
		self.params = params
		return self.orm().delete(sql, *params)

	def replace(self, data):
		sql, params = super().replace(data)
		self.sql = sql
		self.params = params
		return self.orm().replace(sql, *params)

	def count(self):
		sql, params = super().count()
		self.sql = sql
		self.params = params
		return self.orm().select(sql, *params).fetch_one("count")

	def plus(self, *args):
		sql, params = super().plus(*args)
		self.sql = sql
		self.params = params
		return self.orm().update(sql, *params)

	def incr(self, col, val = 1):
		sql, params = super().incr(col, val)
		self.sql = sql
		self.params = params
		return self.orm().update(sql, *params)

	# === quick ===
	
	def find(self, pk_val):
		return self.where("`%s` = ?" % self.pk(), pk_val).select().fetch()
	
	def add(self, data):
		return self.insert(data)
	
	def edit(self, data):
		assert self.pk() in data, "data must contains column %s!" % self.pk()

		pk_val = data[self.pk()]
		del data[self.pk()]

		return self.where("`%s` = ?" % self.pk(), pk_val).update(data)
	
	def remove(self, pk_val):
		return self.where("`%s` = ?" % self.pk(), pk_val).delete()
	
	def save(self, data):
		if self.pk() in data:
			return self.edit(data)
		else:
			return self.add(data)


# === module method ===

__orm = ORM()

def clone():
	return __orm.clone()

def config(database_driver, *database_params, **database_config):
	return __orm.config(database_driver, *database_params, **database_config)

def prefix(prefix = None):
	return __orm.prefix(prefix)

def conn(conn = None):
	return __orm.conn(conn)

def execute(sql, *args):
	return __orm.execute(sql, *args)

def insert(sql, *args):
	return __orm.insert(sql, *args)

def update(sql, *args):
	return __orm.update(sql, *args)

def delete(sql, *args):
	return __orm.delete(sql, *args)

def replace(sql, *args):
	return __orm.replace(sql, *args)

def select(sql, *args):
	return __orm.select(sql, *args)

def table(table):
	return __orm.table(table)

def __getattr__(table):
	return __orm.table(table)


if __name__ == '__main__':
	# ====== database driver ======

	# import module
	sys = __import__("sys")

	# connect config
	if len(sys.argv) == 1 or sys.argv[1] == "pymysql":
		pymysql = __import__("pymysql")
		database_driver = "pymysql"
		database_params = []
		database_config = {
			"host": "127.0.0.1",
			"user": "root", 
			"password": "123456",
			"db": "test",
			"charset": "utf8mb4",
			"autocommit": True,
			"cursorclass": pymysql.cursors.DictCursor,
		}
	elif sys.argv[1] == "sqlite3":
		sqlite3 = __import__("sqlite3")
		database_driver = "sqlite3"
		database_params = ["orm_test.db"]
		database_config = {}
	else:
		print("database driver %s does not support" % database_driver)
		exit(1)

	# ====== database table ======
	drop_table_user = '''DROP TABLE IF EXISTS `table_user`'''

	create_table_user = '''CREATE TABLE `table_user` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`username` varchar(45) NOT NULL,
		`password` varchar(45) NOT NULL,
		`nickname` varchar(45) NOT NULL,
		`num` int(11) NOT NULL,
		PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'''

	drop_table_blog = '''DROP TABLE IF EXISTS `table_blog`'''

	create_table_blog = '''CREATE TABLE `table_blog` (
		  `id` int(11) NOT NULL AUTO_INCREMENT,
		  `user_id` int(11) NOT NULL,
		  `title` varchar(45) NOT NULL,
		  PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'''

	if database_driver == "sqlite3":
		create_table_user = '''CREATE TABLE table_user (
			  id INTEGER PRIMARY KEY AUTOINCREMENT,
			  username TEXT,
			  password TEXT,
			  nickname TEXT,
			  num INTEGER
			)'''

		create_table_blog = '''CREATE TABLE `table_blog` (
			  id INTEGER PRIMARY KEY AUTOINCREMENT,
			  user_id INTEGER,
			  title TEXT
			)'''

	# ====== Cursor ======

	cursor = Cursor()

	# data
	cursor.rows = [
		{"id": 1, "username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1},
		{"id": 2, "username": "admin2", "password": "admin2", "nickname": "admin2", "num": 2},
		{"id": 3, "username": "admin3", "password": "admin3", "nickname": "admin3", "num": 3},
		{"id": 4, "username": "admin4", "password": "admin4", "nickname": "admin4", "num": 4},
		{"id": 5, "username": "admin5", "password": "admin5", "nickname": "admin5", "num": 5},
	]

	# fetch_all
	assert cursor.fetch_all() == cursor.rows

	# fetch
	assert cursor.fetch() == {"id": 1, "username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1}

	# fetch_one
	assert cursor.fetch_one("id") == 1

	# fetch_column
	assert cursor.fetch_column("id") == [1, 2, 3, 4, 5]

	# fetch_unique
	assert cursor.fetch_unique("id") == {
		1: {"id": 1, "username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1},
		2: {"id": 2, "username": "admin2", "password": "admin2", "nickname": "admin2", "num": 2},
		3: {"id": 3, "username": "admin3", "password": "admin3", "nickname": "admin3", "num": 3},
		4: {"id": 4, "username": "admin4", "password": "admin4", "nickname": "admin4", "num": 4},
		5: {"id": 5, "username": "admin5", "password": "admin5", "nickname": "admin5", "num": 5},
	}

	# fetch_key_pair
	assert cursor.fetch_key_pair("id", "username") == {1: "admin1", 2: "admin2", 3: "admin3", 4: "admin4", 5: "admin5"}

	# ====== ORM ======

	# ORM Object
	o = ORM()

	# database config
	o.config(database_driver, *database_params, **database_config)

	if database_driver != "sqlite3":
		# === pool ===
		assert o.pool().qsize() == 0

		conn1 = o.conn()
		assert o.pool().qsize() == 0

		conn2 = o.conn()
		assert o.pool().qsize() == 0

		assert conn1 != conn2

		o.conn(conn1)
		assert o.pool().qsize() == 1

		o.conn(conn2)
		assert o.pool().qsize() == 2

		conn3 = o.conn()
		assert o.pool().qsize() == 1

		assert conn1 == conn3

		conn4 = o.conn()
		assert o.pool().qsize() == 0

		assert conn2 == conn4

		o.conn(conn3)
		assert o.pool().qsize() == 1

		o.conn(conn4)
		assert o.pool().qsize() == 2

		# === concurrency ===

		conn5 = o.conn()
		conn6 = o.conn()

		cursor5 = conn5.cursor()
		cursor6 = conn6.cursor()

		cursor5.execute("select 1")
		cursor6.execute("select 1")

		assert cursor5.fetchone() == {"1":1}
		assert cursor6.fetchone() == {"1":1}

		cursor5.fetchall()
		cursor6.fetchall()

		cursor5.close()
		cursor6.close()

		o.conn(conn5)
		o.conn(conn6)

		# == transaction ===
	
		t1 = o.clone().conn(o.conn())
		t2 = o.clone().conn(o.conn())

		assert o.pool().qsize() == 0
		assert t1.pool().qsize() == 1
		assert t2.pool().qsize() == 1

		t1conn = t1.conn()
		t2conn = t2.conn()

		t1conn.begin()
		t2conn.begin()

		t1cursor = t1conn.cursor()
		t2cursor = t2conn.cursor()

		t1cursor.execute("select 1")
		t2cursor.execute("select 1")

		t1cursor.close()
		t2cursor.close()

		t1conn.commit()
		t2conn.commit()

		t1.conn(t1conn)
		t2.conn(t2conn)

		del t1
		del t2

		assert o.pool().qsize() == 2

	# === execute ===

	# clear table
	o.execute(drop_table_user)
	o.execute(create_table_user)

	# insert
	assert o.insert("INSERT INTO `table_user` (`username`, `password`, `nickname`, `num`) VALUES (?, ?, ?, ?)", "admin1", "admin1", "admin1", 1).lastrowid == 1

	# update
	assert o.update("UPDATE `table_user` SET `password` = ?, `nickname` = ?, `num` = ? WHERE username = ?", "admin123", "admin123", 123, "admin1").rowcount == 1

	# delete
	assert o.delete("DELETE FROM `table_user` WHERE id = ?", 1).rowcount == 1

	# replace
	if database_driver != "sqlite3":
		assert o.replace("REPLACE INTO `table_user` SET `id` = ?, `username` = ?, `password` = ?, `nickname` = ?, `num` = ?", 1, "admin1", "admin1", "admin1", 1).rowcount == 1
	else:
		assert o.insert("INSERT INTO `table_user` (`id`, `username`, `password`, `nickname`, `num`) VALUES (?, ?, ?, ?, ?)", 1, "admin1", "admin1", "admin1", 1).lastrowid == 1

	# select
	assert len(o.select("SELECT * FROM `table_user` WHERE id = ?", 1).fetch_all()) == 1

	# ====== SqlBuilder ======

	# table
	table = lambda name : SqlBuilder().prefix("table_").table(name).pk("id")

	# insert
	data = {"username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1}
	sql, params = table("user").insert(data)
	assert sql == "INSERT INTO `table_user` (`username`, `password`, `nickname`, `num`) VALUES (?, ?, ?, ?)", sql
	assert params == ["admin1", "admin1", "admin1", 1], params

	# update
	data = {"password": "admin123", "nickname": "admin123", "num": 123}
	sql, params = table("user").where("username = ?", "admin1").update(data)
	assert sql == "UPDATE `table_user` SET `password` = ?, `nickname` = ?, `num` = ? WHERE username = ?", sql
	assert params == ["admin123", "admin123", 123, "admin1"], params

	# delete
	sql, params = table("user").where("id = ?", 4).delete()
	assert sql == "DELETE FROM `table_user` WHERE id = ?", sql
	assert params == [4], params

	# replace
	data = {"id": 1, "username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1}
	sql, params = table("user").replace(data)
	assert sql == "REPLACE INTO `table_user` SET `id` = ?, `username` = ?, `password` = ?, `nickname` = ?, `num` = ?", sql
	assert params == [1, "admin1", "admin1", "admin1", 1], params

	# select
	sql, params = table("user").select()
	assert sql == "SELECT * FROM `table_user`", sql
	assert params == [], params

	# calc_found_rows
	if database_driver != "sqlite3":
		sql, params = table("user").calc_found_rows().select()
		assert sql == "SELECT SQL_CALC_FOUND_ROWS * FROM `table_user`", sql
		assert params == [], params

	# where
	sql, params = table("user").where("id > ?", 4).where("id IN (?)", [7,9,11]).select()
	assert sql == "SELECT * FROM `table_user` WHERE id > ? AND id IN (?, ?, ?)", sql
	assert params == [4, 7, 9, 11], params
	
	# group having
	sql, params = table("user").columns("num", "count(*) AS c").group("num").having("c BETWEEN ? AND ?", 8, 10).having("c > ?", 9).select()
	assert sql == "SELECT num, count(*) AS c FROM `table_user` GROUP BY num HAVING c BETWEEN ? AND ? AND c > ?", sql
	assert params == [8, 10, 9], params
	
	# order
	sql, params = table("user").where("num < ?", 10).order("num DESC", "id").select()
	assert sql == "SELECT * FROM `table_user` WHERE num < ? ORDER BY num DESC, id", sql
	assert params == [10], params
	
	# limit offset
	sql, params = table("user").limit(10).offset(20).select()
	assert sql == "SELECT * FROM `table_user` LIMIT ? OFFSET ?", sql
	assert params == [10, 20], params
	
	# page
	sql, params = table("user").page(4, 10).select()
	assert sql == "SELECT * FROM `table_user` LIMIT ? OFFSET ?", sql
	assert params == [10, 30], params

	# where page count
	sql, params = table("user").where("num = ?", 2).order("id DESC").page(3, 2).select()
	assert sql == "SELECT * FROM `table_user` WHERE num = ? ORDER BY id DESC LIMIT ? OFFSET ?", sql
	assert params == [2, 2, 4], params

	# select
	sql, params = table("user").columns("count(*) AS c")\
		.where("id > ?", 0).where("id < ?", 100)\
		.group("num").having("c BETWEEN ? AND ?", 1, 100).having("c > ?", 1)\
		.order("c DESC").page(2, 3).select()
	assert sql == "SELECT count(*) AS c FROM `table_user` WHERE id > ? AND id < ? GROUP BY num HAVING c BETWEEN ? AND ? AND c > ? ORDER BY c DESC LIMIT ? OFFSET ?", sql
	assert params == [0, 100, 1, 100, 1, 3, 3], params

	# count
	sql, params = table("user").where("id < ?", 10).count()
	assert sql == "SELECT count(*) AS count FROM `table_user` WHERE id < ?", sql
	assert params == [10], params

	# plus
	sql, params = table("user").where("`id` = ?", 2).plus("num", 1, "num", -1)
	assert sql == "UPDATE `table_user` SET `num` = `num` + ?, `num` = `num` + ? WHERE `id` = ?", sql
	assert params == [1, -1, 2], params

	# incr
	if database_driver != "sqlite3":
		sql, params = table("user").where("`id` = ?", 1).incr("num", 1)
		assert sql == "UPDATE `table_user` SET `num` = last_insert_id(`num` + ?) WHERE `id` = ?", sql
		assert params == [1, 1], params

	# ====== OrmSqlBuilder ======

	# prefix
	o.prefix("table_")

	# clear table
	o.execute(drop_table_user)
	o.execute(create_table_user)

	# insert
	data = {"username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1}
	assert o.user.insert(data).lastrowid == 1

	# update
	data = {"username": "admin1-1", "password": "admin1-1", "nickname": "admin1-1", "num": 10}
	assert o.user.where("id = ?", 1).update(data).rowcount == 1

	# delete
	assert o.user.where("id = ?", 1).delete().rowcount == 1

	# replace
	if database_driver != "sqlite3":
		data = {"username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1}
		assert o.user.replace(data).lastrowid == 2
	else:
		data = {"id":1, "username": "admin1", "password": "admin1", "nickname": "admin1", "num": 1}
		assert o.user.insert(data).lastrowid == 1

	# select
	assert len(o.user.select().fetch_all()) == 1

	# ====== others ======

	# clear table
	o.execute(drop_table_user)
	o.execute(create_table_user)

	# init data
	for i in range(1, 101):
		data = {"id": i, "username": "admin%d" % i, "password": "admin%d" % i, "nickname": "admin%d" % i, "num": i // 10}
		assert o.user.insert(data).lastrowid == i

	# where
	s = o.user.where("id > ?", 4).where("id IN (?)", [7, 9, 11])
	assert s.select().fetch()["id"] == 7
	assert s.sql == "SELECT * FROM `table_user` WHERE id > ? AND id IN (?, ?, ?)", s.sql
	assert s.params == [4, 7, 9, 11], s.params
	
	# group having
	s = o.user.columns("num", "count(*) AS c").group("num").having("c BETWEEN ? AND ?", 8, 10).having("c > ?", 9)
	assert len(s.select().fetch_all()) == 9
	assert s.sql == "SELECT num, count(*) AS c FROM `table_user` GROUP BY num HAVING c BETWEEN ? AND ? AND c > ?", s.sql
	assert s.params == [8, 10, 9], s.params
	
	# order
	s = o.user.where("num < ?", 10).order("num DESC", "id")
	assert s.select().fetch()["id"] == 90
	assert s.sql == "SELECT * FROM `table_user` WHERE num < ? ORDER BY num DESC, id", s.sql
	assert s.params == [10], s.params
	
	# limit offset
	s = o.user.limit(10).offset(20)
	assert s.select().fetch()["id"] == 21
	assert s.sql == "SELECT * FROM `table_user` LIMIT ? OFFSET ?", s.sql
	assert s.params == [10, 20], s.params
	
	# page
	s = o.user.page(4, 10)
	assert s.select().fetch()["id"] == 31
	assert s.sql == "SELECT * FROM `table_user` LIMIT ? OFFSET ?", s.sql
	assert s.params == [10, 30], s.params

	# where page count
	s = o.user.where("num = ?", 2).order("id DESC").page(3, 2)
	assert s.select().fetch()["id"] == 25
	assert s.sql == "SELECT * FROM `table_user` WHERE num = ? ORDER BY id DESC LIMIT ? OFFSET ?", s.sql
	assert s.params == [2, 2, 4], s.params

	# select
	s = o.user.columns("count(*) AS c")\
		.where("id > ?", 0).where("id < ?", 101)\
		.group("num").having("c BETWEEN ? AND ?", 1, 10).having("c > ?", 0)\
		.order("c DESC").page(3, 3)
	assert len(s.select().fetch_all()) == 3
	assert s.sql == "SELECT count(*) AS c FROM `table_user` WHERE id > ? AND id < ? GROUP BY num HAVING c BETWEEN ? AND ? AND c > ? ORDER BY c DESC LIMIT ? OFFSET ?", s.sql
	assert s.params == [0, 101, 1, 10, 0, 3, 6], s.params

	# count
	s = o.user.where("id < ?", 10)
	assert s.count() == 9
	assert s.sql == "SELECT count(*) AS count FROM `table_user` WHERE id < ?", s.sql
	assert s.params == [10], s.params

	# # join
	# assert b.left_join(u, "__LEFT__.user_id = __THIS__.id", "*").where("__THIS__.id < ?", 20).select("b.*, o.user.username").fetch_all()
	# assert(b._sql == "SELECT table_blog.*, table_user.username FROM `table_blog` LEFT JOIN `table_user` ON table_blog.user_id = table_user.id WHERE b.id < ?")
	# assert(array_equal(b._params, array(20)))

	# # join prefix
	# assert b.left_join(u, "__LEFT__.user_id = __THIS__.id", "username", prefix="u_").where("b.id < ?", 20).select().fetch_all()
	# assert(b._sql == "SELECT b.*, o.user.username FROM `table_blog` AS `b` LEFT JOIN `table_user` AS `u` ON b.user_id = o.user.id WHERE b.id < ?")
	# assert(array_equal(b._params, array(20)))

	# find
	u = o.user
	assert u.find(5)["id"] == 5
	assert u.sql == "SELECT * FROM `table_user` WHERE `id` = ?", s.sql
	assert u.params == [5], s.params
	
	# add
	user = {"username": "admin9998", "password": "admin9998", "nickname": "admin9998", "num": 0}
	u = o.user
	assert u.add(user).lastrowid == 101
	assert u.sql == "INSERT INTO `table_user` (`username`, `password`, `nickname`, `num`) VALUES (?, ?, ?, ?)", s.sql
	assert u.params == ["admin9998", "admin9998", "admin9998", 0], s.params

	# edit
	user = {"id": 101, "username": "admin9998-1", "password": "admin9998-1", "nickname": "admin9998-1", "num": 0}
	u = o.user
	assert u.edit(user).rowcount == 1
	assert u.sql == "UPDATE `table_user` SET `username` = ?, `password` = ?, `nickname` = ?, `num` = ? WHERE `id` = ?", s.sql
	assert u.params == ["admin9998-1", "admin9998-1", "admin9998-1", 0, 101], s.params

	# remove
	u = o.user
	assert u.remove(11).rowcount == 1
	assert u.sql == "DELETE FROM `table_user` WHERE `id` = ?", s.sql
	assert u.params == [11], s.params

	# save update
	user = {"id": 3,"nickname": "admin3-3"}
	u = o.user
	assert u.save(user).rowcount == 1
	assert u.sql == "UPDATE `table_user` SET `nickname` = ? WHERE `id` = ?", s.sql
	assert u.params == ["admin3-3", 3], s.params

	# save insert
	user = {"username": "admin9999", "password": "admin9999", "nickname": "admin9999", "num": 0}
	u = o.user
	assert u.save(user).lastrowid == 102
	assert u.sql == "INSERT INTO `table_user` (`username`, `password`, `nickname`, `num`) VALUES (?, ?, ?, ?)", s.sql
	assert u.params == ["admin9999", "admin9999", "admin9999", 0], s.params

	# plus +1
	u = o.user
	assert u.where("`id` = ?", 2).plus("num", 1).rowcount == 1
	assert u.sql == "UPDATE `table_user` SET `num` = `num` + ? WHERE `id` = ?", s.sql
	assert u.params == [1, 2], s.params
	
	# plus -1
	u = o.user
	assert u.where("`id` = ?", 2).plus("num", -1).rowcount == 1
	assert u.sql == "UPDATE `table_user` SET `num` = `num` + ? WHERE `id` = ?", s.sql
	assert u.params == [-1, 2], s.params
	
	if database_driver != "sqlite3":
		# plus multi
		u = o.user
		assert u.where("`id` = ?", 2).plus("num", 1, "num", -1).rowcount == 0
		assert u.sql == "UPDATE `table_user` SET `num` = `num` + ?, `num` = `num` + ? WHERE `id` = ?", s.sql
		assert u.params == [1, -1, 2], s.params

		# incr +1
		u = o.user
		assert u.where("`id` = ?", 1).incr("num", 1).lastrowid == 1
		assert u.sql == "UPDATE `table_user` SET `num` = last_insert_id(`num` + ?) WHERE `id` = ?", s.sql
		assert u.params == [1, 1], s.params
		
		# incr -1
		u = o.user
		assert u.where("`id` = ?", 1).incr("num", -1).lastrowid == 0
		assert u.sql == "UPDATE `table_user` SET `num` = last_insert_id(`num` + ?) WHERE `id` = ?", s.sql
		assert u.params == [-1, 1], s.params
	
	# create table blog
	o.execute(drop_table_blog)
	o.execute(create_table_blog)

	# foreign key data
	users = o.user.columns("id").where("id <= ?", 10).select().fetch_all()
	auto_id = 0;
	for user in users:
		for _ in range(10):
			auto_id += 1
			blog = { "user_id": user["id"], "title": "blog%d title" % auto_id}
			o.blog.insert(blog)

	b = o.blog.where("id IN (?)", [1, 11, 21, 31, 41, 51])
	assert len(b.select().fetch_all()) == 6
	assert b.sql == "SELECT * FROM `table_blog` WHERE id IN (?, ?, ?, ?, ?, ?)"
	assert b.params == [1, 11, 21, 31, 41, 51]

	# fetch
	assert o.user.columns("id", "username").where("id < ?", 3).select().fetch_all() == [{"id": 1, "username": "admin1",}, {"id": 2, "username": "admin2",}]
	assert o.user.columns("id", "username").where("id < ?", 3).select().fetch() == {"id": 1, "username": "admin1",}
	assert o.user.columns("id", "username").where("id < ?", 3).select().fetch_one("id") == 1
	assert o.user.columns("id", "username").where("id < ?", 3).select().fetch_column("id") == [1, 2]
	assert o.user.columns("id", "username").where("id < ?", 3).select().fetch_unique("id") == {1: {"id": 1, "username": "admin1",}, 2: {"id": 2, "username": "admin2",}}
	assert o.user.columns("id", "username").where("id < ?", 3).select().fetch_key_pair("id", "username") == {1: "admin1", 2: "admin2"}
