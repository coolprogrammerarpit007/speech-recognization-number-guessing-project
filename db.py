from mysql.connector import connect,Error
from getpass import getpass

# Establishing Connection with the MySQL Server

# General Workflow of a Python program that Interacts with a MySql-based database.
# Connect to the MySQL server.
# Create a new database.
# Connect to the newly created or an existing database.
# Execute a SQL query and fetch results.
# Inform the database if any changes are made to a table.
# Close the connection to the MySQL server.

try:
    with connect(
        host="localhost",
        user=input("Enter Username: "),
        password=getpass("Enter Password: "),
        database="online_movie_rating",
        connection_timeout=300,
    ) as connection:
        
        # cursor = connection.cursor() # this gives you an Instance of MySQLCursor Class.
        create_db_query = "CREATE DATABASE IF NOT EXISTS online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        

        # Query To create a new Table names movies
        create_movies_table_query = """
        CREATE TABLE IF NOT EXISTS movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            collection_in_mil INT
        )
        """

        with connection.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            connection.commit()

        # Query to create the Reviewers Table

        create_reviewers_table_query = """
            CREATE TABLE IF NOT EXISTS reviewers(
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100),
                last_name VARCHAR(100)
            )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_reviewers_table_query)
            connection.commit()


        #  create a ratings table

        create_ratings_table_query = """
            CREATE TABLE IF NOT EXISTS ratings(
                movie_id INT,
                reviewer_id INT,
                rating DECIMAL(2,1),
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
                PRIMARY KEY(movie_id,reviewer_id)
            )

        """

        with connection.cursor() as cursor:
            cursor.execute(create_ratings_table_query)
            connection.commit()


        # Altering The Movies Table
        alter_movies_table_query = """
            ALTER TABLE movies
            MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """

        with connection.cursor() as cursor:
            cursor.execute(alter_movies_table_query)
            connection.commit()

        # Inserting Records Into Table
        # Method 1:- Using .execute

        # insert_movies_query = """
        #     INSERT INTO movies(title,release_year,genre,collection_in_mil)
        #     VALUES
        #          ("3 Idiots",2010,"Comedy-Drama",100),
        #          ("Bahubali:The Beginning",2016,"Action-Adventure",850)
        # """

        # with connection.cursor() as cursor:
        #     cursor.execute(insert_movies_query)
        #     connection.commit()

        # Inserting DATA Into the reviewers Table
    #     insert_reviewers_query = """
    #         INSERT INTO reviewers
    #         (first_name,last_name)
    #         VALUES (%s,%s)
    #     """

    #     reviewers_records = [
    #     ("Chaitanya", "Baweja"),
    #     ("Mary", "Cooper"),
    #     ("John", "Wayne"),
    #     ("Thomas", "Stoneman"),
    #     ("Penny", "Hofstadter"),
    #     ("Mitchell", "Marsh"),
    #     ("Wyatt", "Skaggs"),
    #     ("Andre", "Veiga"),
    #     ("Sheldon", "Cooper"),
    #     ("Kimbra", "Masters"),
    #     ("Kat", "Dennings"),
    #     ("Bruce", "Wayne"),
    #     ("Domingo", "Cortes"),
    #     ("Rajesh", "Koothrappali"),
    #     ("Ben", "Glocker"),
    #     ("Mahinder", "Dhoni"),
    #     ("Akbar", "Khan"),
    #     ("Howard", "Wolowitz"),
    #     ("Pinkie", "Petit"),
    #     ("Gurkaran", "Singh"),
    #     ("Amy", "Farah Fowler"),
    #     ("Marlon", "Crafford"),
    # ]
        
    #     with connection.cursor() as cursor:
    #         cursor.executemany(insert_reviewers_query,reviewers_records)
    #         connection.commit()


    #  Insert Record Into Ratings
    # insert_ratings_query = """
    #         INSERT INTO ratings
    #         (rating, movie_id, reviewer_id)
    #         VALUES ( %s, %s, %s)
    #     """
    # ratings_records = [
    #     (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14), (5.1, 21, 17),
    #     (5.0, 5, 5), (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4),
    #     (8.5, 24, 12), (9.9, 14, 9), (8.7, 26, 14), (9.9, 6, 10),
    #     (5.1, 30, 6), (5.4, 18, 16), (6.2, 6, 20), (7.3, 21, 19),
    #     (8.1, 17, 18), (5.0, 7, 2), (9.8, 23, 3), (8.0, 22, 9),
    #     (8.5, 11, 13), (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19),
    #     (5.2, 18, 15), (9.7, 13, 3), (5.8, 18, 8), (5.8, 30, 15),
    #     (8.4, 21, 18), (6.2, 23, 16), (7.0, 10, 18), (9.5, 30, 20),
    #     (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22), (9.9, 15, 13),
    #     (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17),
    #     (6.4, 5, 10), (8.1, 5, 21), (5.7, 22, 1), (6.3, 28, 4),
    #     (9.8, 13, 1)
    # ]
    # with connection.cursor() as cursor:
    #     cursor.executemany(insert_ratings_query, ratings_records)
    #     connection.commit()

    # Reading Records from the Tables
    select_reviewer_query = "SELECT * FROM reviewers LIMIT 5" 
    with connection.cursor() as cursor:
        connection.ping(reconnect=True)
        cursor.execute(select_reviewer_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
except Error as e:
    print("Some Error Occurs...")
    print(e)


finally:
    if connection.is_connected():
        connection.close()

