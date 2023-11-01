from util.database import get_db_connection
from util.security import get_password_hash

class UserModel:
    
    @classmethod
    def get_user_by_username(cls, username: str):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        
        cursor.close()
        db.close()
        
        return user
    
    @classmethod
    def create(cls, username: str, hashed_password: str, role: str):
        db = get_db_connection()
        cursor = db.cursor()

        query = "INSERT INTO users (username, hashed_password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, hashed_password, role))
        db.commit()

        cursor.close()
        db.close()

        return {"username": username, "role": role}
    
    @classmethod
    def get_all_users(cls):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        query = "SELECT username, role FROM users"
        cursor.execute(query)
        users = cursor.fetchall()

        cursor.close()
        db.close()

        return users
    
    @classmethod
    def delete(cls, username: str):
        db = get_db_connection()
        cursor = db.cursor()

        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        db.commit()

        cursor.close()
        db.close()

        return True
