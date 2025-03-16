import mysql.connector
from mysql.connector import Error


def insert_data():
    connection = None  # Initialize the connection variable
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            host='localhost',
            database='customermanagement',
            user='root',
            password='@Obama123'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Ensure the 'booking' table has the correct structure
            create_booking_table_query = '''
            CREATE TABLE IF NOT EXISTS booking (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                phone VARCHAR(20),
                event_type VARCHAR(50)
            );
            '''
            cursor.execute(create_booking_table_query)

            # Insert data into the 'booking' table
            booking_query = '''
            INSERT INTO booking (name, email, phone, event_type)
            VALUES (%s, %s, %s, %s);
            '''
            booking_data = ('Nguyễn Quách Minh Trí', 'nguyenquachminhtri@gmail.com', '0903762652', 'birthday')
            cursor.execute(booking_query, booking_data)
            connection.commit()
            print("Booking record inserted successfully.")

            # Ensure the 'counter' table exists in the schema with the correct structure
            create_counter_table_query = '''
            CREATE TABLE IF NOT EXISTS counter (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE,
                booking_id INT,
                time_slot VARCHAR(20),
                status VARCHAR(20),
                FOREIGN KEY (booking_id) REFERENCES booking(id)
            );
            '''
            cursor.execute(create_counter_table_query)

            # Insert data into the 'counter' table
            counter_query = '''
            INSERT INTO counter (date, booking_id, time_slot, status)
            VALUES (%s, %s, %s, %s);
            '''
            counter_data = ('2025-05-07', 1, '16:00', 'counter')
            cursor.execute(counter_query, counter_data)
            connection.commit()
            print("Counter record inserted successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        # Ensure cursor and connection are closed if they were opened
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# Call the function
insert_data()


