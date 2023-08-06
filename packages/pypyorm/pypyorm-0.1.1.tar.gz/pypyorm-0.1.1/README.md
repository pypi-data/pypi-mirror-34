# pyorm

Python ORM Module

## basic

import module

	from pyorm import orm

config connection

	database_driver = "pymysql"
	database_params = []
	database_config = {
		"host": "127.0.0.1",
		"user": "root", 
		"password": "123456",
		"db": "test",
		"charset": "utf8mb4",
	}
	orm.config(database_driver, *database_params, **database_config)

create table

	create_table_user = '''CREATE TABLE `table_user` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`username` varchar(45) NOT NULL,
		`password` varchar(45) NOT NULL,
		`nickname` varchar(45) NOT NULL,
		`num` int(11) NOT NULL,
		PRIMARY KEY (`id`)
		) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'''
	orm.execute(create_table_user)

prefix table

	orm.prefix("table_")

## OrmSqlBuilder quick method

find by pk

	orm.user.find(5)
	
add

	orm.user.add(user).lastrowid

edit

	orm.user.edit(user).rowcount

remove by id

	orm.user.remove(11).rowcount

save

	orm.user.save(user)

## OrmSqlBuilder method

insert

	orm.user.insert(data)

update

	orm.user.where("username = ?", "admin1").update(data)

delete

	orm.user.where("id = ?", 4).delete()

select where

	orm.user.columns("id", "username").where("id > ", 10).where("num IN (?)", [8, 9, 10]).select().fetch_all()
	
group having

	orm.user.group("num").select()
	
order

	orm.user.order("num DESC", "id").select()

limit offset

	orm.user.limit(10).offset(20).select()
	
page

	orm.user.page(4, 10).select()

count

	orm.user.where("id < ?", 10).count()

plus

	orm.user.where("`id` = ?", 2).plus("num", 1, "num", -1)

## Cursor method

fetch_all

	orm.user.select().fetch_all()

fetch

	orm.user.select().fetch()

fetch_one

	orm.user.select().fetch_one("id")

fetch_column

	orm.user.select().fetch_column("id")

fetch_unique

	orm.user.select().fetch_unique("id")

fetch_key_pair

	orm.user.select().fetch_key_pair("id", "username")

## ORM method

insert

	orm.insert("INSERT INTO `table_user` (`username`, `password`, `nickname`, `num`) VALUES (?, ?, ?, ?)", "admin1", "admin1", "admin1", 1).lastrowid

update

	orm.update("UPDATE `table_user` SET `password` = ?, `nickname` = ?, `num` = ? WHERE username = ?", "admin123", "admin123", 123, "admin1").rowcount

delete

	orm.delete("DELETE FROM `table_user` WHERE id = ?", 1).rowcount

select

	orm.select("SELECT * FROM `table_user` WHERE id = ?", 1).fetch_all()
