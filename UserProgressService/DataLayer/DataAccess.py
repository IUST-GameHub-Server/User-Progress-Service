import sqlite3

class DataAccess:
    def setup_player(email):
        conn=sqlite3.connect('./UserProgressService/DataLayer/progress.db')
        cur=conn.cursor()
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS progress(
                    email TEXT PRIMARY KEY,
                    level INT,
                    point INT,
                    rating INT
        );
        """)

        cur.execute(f"""
        INSERT INTO progress(email, level, point, rating) VALUES('{email}', 1 ,0 ,0);
        """)
        conn.commit()
        return "user created successfully"

    def set_player_level(email,level):
        conn=sqlite3.connect('./UserProgressService/DataLayer/progress.db')
        cur=conn.cursor()
        cur.execute(f"""
        UPDATE progress SET level = '{level}' WHERE email='{email}'
        """)
        conn.commit()
    
    def get_player_level(email):
        conn=sqlite3.connect('./UserProgressService/DataLayer/progress.db')
        cur=conn.cursor()
        cur.execute(f"""
        SELECT level FROM progress where email='{email}'
        """)
        return cur.fetchone()

    def set_point(email,point):
        conn=sqlite3.connect('./UserProgressService/DataLayer/progress.db')
        cur=conn.cursor()
        cur.execute(f"""
        UPDATE progress SET point = '{point}' WHERE email='{email}'
        """)
        conn.commit()

    def get_point(email):
        conn=sqlite3.connect('./UserProgressService/DataLayer/progress.db')
        cur=conn.cursor()
        cur.execute(f"""
        SELECT point FROM progress where email='{email}'
        """)
        return cur.fetchone()

    def set_user_rating(email, rating):
        conn=sqlite3.connect('./UserProgressService/DataLayer/progress.db')
        cur=conn.cursor()
        cur.execute(f"""
        UPDATE progress SET rating = '{rating}' WHERE email='{email}'
        """)
        conn.commit()

    def get_user_rating(email):
        conn=sqlite3.connect('./UserProgressService/DataLayer/progress.db')
        cur=conn.cursor()
        cur.execute(f"""
        SELECT rating FROM progress where email='{email}'
        """)
        return cur.fetchone()
