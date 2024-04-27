import sqlite3

class QueryManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, values):
        query = f"INSERT INTO {table_name} VALUES ({values})"
        self.cursor.execute(query)
        self.conn.commit()

    def select_data(self, table_name, columns="*", condition=None):
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, set_values, condition=None):
        query = f"UPDATE {table_name} SET {set_values}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, condition=None):
        query = f"DELETE FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Usage example
if __name__ == "__main__":
    db_name = "mydatabase.db"
    query_manager = QueryManager(db_name)
    query_manager.create_table("items", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INT, imageURL TEXT, description TEXT, calories INT, carbs INT, protein INT")
    query_manager.create_table("order", "id INTEGER PRIMARY KEY AUTOINCREMENT, items TEXT, status BOOLEAN, time TEXT, total TEXT, phone_number TEXT, address TEXT, name TEXT, FOREIGN KEY(items) REFERENCES items(id)")
    query_manager.insert_data("users", "1, 'John Doe', 25")
    query_manager.insert_data("users", "2, 'Jane Smith', 30")
    result = query_manager.select_data("users")
    print(result)
    query_manager.close_connection()