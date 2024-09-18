"""
@Time ： 2024-09-16
@Auth ： Adam Lyu
"""
import unittest
from data.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # 使用内存数据库进行测试
        self.db = Database(':memory:')
        self.db.execute('''
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            email TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')

    def tearDown(self):
        self.db.close()

    def test_execute_and_fetchall(self):
        self.db.execute('INSERT INTO contacts (first_name, last_name, phone) VALUES (?, ?, ?)',
                        ('John', 'Doe', '123456789'))
        result = self.db.fetchall('SELECT * FROM contacts')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['first_name'], 'John')

    def test_execute_and_fetchone(self):
        self.db.execute('INSERT INTO contacts (first_name, last_name, phone) VALUES (?, ?, ?)',
                        ('Jane', 'Smith', '987654321'))
        result = self.db.fetchone('SELECT * FROM contacts WHERE phone = ?', ('987654321',))
        self.assertIsNotNone(result)
        self.assertEqual(result['first_name'], 'Jane')

if __name__ == '__main__':
    unittest.main()
