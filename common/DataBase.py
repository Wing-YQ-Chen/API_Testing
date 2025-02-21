import pymysql


class MySQLManager:
    def __init__(self, host, user, password, database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):
        """
        类的初始化方法。

        参数：
        - host：数据库服务器地址。
        - user：数据库用户名。
        - password：数据库用户密码。
        - database：要连接的数据库名称。
        - charset：字符集，默认为'utf8mb4'。
        - cursorclass：游标类型，默认为返回字典形式结果的游标。
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.cursorclass = cursorclass
        self.connection = None
        self.connect()

    def connect(self):
        """
        连接数据库的方法。
        建立与数据库的连接，并将连接对象存储在 self.connection 中。
        """
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset,
            cursorclass=self.cursorclass
        )

    def close(self):
        """
        关闭数据库连接的方法。
        如果存在数据库连接，则关闭连接。
        """
        if self.connection:
            self.connection.close()

    def insert(self, table_name, data_dict):
        """
        插入数据的方法。

        参数：
        - table_name：要插入数据的表名。
        - data_dict：包含要插入数据的字典，键为列名，值为对应的值。

        函数作用：
        - 创建游标对象。
        - 构建插入数据的 SQL 语句，包括列名和占位符。
        - 执行 SQL 语句并传入数据字典的值进行插入操作。
        - 提交事务，确保数据插入成功。
        """
        with self.connection.cursor() as cursor:
            columns = ', '.join(data_dict.keys())
            values_placeholders = ', '.join(['%s'] * len(data_dict))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_placeholders})"
            values = tuple(data_dict.values())
            cursor.execute(sql, values)
            self.connection.commit()

    def query(self, table_name, where_condition=None):
        """
        查询数据的方法。

        参数：
        - table_name：要查询数据的表名。
        - where_condition：可选的查询条件，如果提供则在 SQL 语句中添加 WHERE 子句。

        函数作用：
        - 创建游标对象。
        - 构建查询数据的 SQL 语句，如果有查询条件则添加 WHERE 子句。
        - 执行 SQL 语句进行查询操作。
        - 返回查询结果。
        """
        with self.connection.cursor() as cursor:
            sql = f"SELECT * FROM {table_name}"
            if where_condition:
                sql += f" WHERE {where_condition}"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results

    def update(self, table_name, data_dict, where_condition):
        """
        更新数据的方法。

        参数：
        - table_name：要更新数据的表名。
        - data_dict：包含要更新数据的字典，键为列名，值为对应要更新的值。
        - where_condition：更新数据的条件。

        函数作用：
        - 创建游标对象。
        - 构建更新数据的 SQL 语句，包括 SET 子句和占位符。
        - 执行 SQL 语句并传入数据字典的值和条件进行更新操作。
        - 提交事务，确保数据更新成功。
        """
        with self.connection.cursor() as cursor:
            set_clause = ', '.join([f"{key}=%s" for key in data_dict.keys()])
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_condition}"
            values = tuple(data_dict.values())
            cursor.execute(sql, values)
            self.connection.commit()

    def delete(self, table_name, where_condition):
        """
        删除数据的方法。

        参数：
        - table_name：要删除数据的表名。
        - where_condition：删除数据的条件。

        函数作用：
        - 创建游标对象。
        - 构建删除数据的 SQL 语句，添加 WHERE 子句。
        - 执行 SQL 语句进行删除操作。
        - 提交事务，确保数据删除成功。
        """
        with self.connection.cursor() as cursor:
            sql = f"DELETE FROM {table_name} WHERE {where_condition}"
            cursor.execute(sql)
            self.connection.commit()


if __name__ == '__main__':
    # 示例用法
    db_manager = MySQLManager(host='your_host', user='your_user', password='your_password', database='your_database')

    # 插入数据
    data_to_insert = {'column1': 'value1', 'column2': 'value2'}
    db_manager.insert('your_table', data_to_insert)

    # 查询数据
    results = db_manager.query('your_table', where_condition="column1 = 'value1'")
    print(results)

    # 更新数据
    data_to_update = {'column2': 'new_value2'}
    db_manager.update('your_table', data_to_update, where_condition="column1 = 'value1'")

    # 删除数据
    db_manager.delete('your_table', where_condition="column1 = 'value1'")

    db_manager.close()
