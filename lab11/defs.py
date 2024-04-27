import csv
import psycopg2

# Function to delete all contacts
def delete_all_contacts():
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts;")
    conn.commit()
    cur.close()
    conn.close()

# Function to delete data by first name or last name or phone
def delete_data_by_name_or_phone(identifier):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE first_name = %s OR last_name = %s OR phone_number = %s", (identifier, identifier, identifier))
    conn.commit()
    cur.close()
    conn.close()

# Function to insert from CSV
def insert_from_csv(filename):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    existing_contacts = []  # Store existing contacts from CSV
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # Check if contact with all entered data exists in the database
            cur.execute("SELECT * FROM contacts WHERE first_name = %s AND last_name = %s AND phone_number = %s", (row[0], row[1], row[2]))
            existing_contact = cur.fetchone()
            if existing_contact:
                print("Contact already exists:", row)
                continue
            
            # Check if phone number exists in the database
            cur.execute("SELECT * FROM contacts WHERE phone_number = %s", (row[2],))
            existing_phone_contact = cur.fetchone()
            if existing_phone_contact:
                print("Phone number", row[2], "is used by another user.")
                continue
            
            # If the phone number is new even if the first and last names exist, add it to the database
            cur.execute(
                "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )
    
    conn.commit()
    cur.close()
    conn.close()

    if existing_contacts:
        print("These contacts already exist:")
        for contact in existing_contacts:
            print(contact)

# Function to insert one or many new users by list of name and phone console
def insert_users_from_console():
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    while True:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        
        # Check if contact already exists with the same first name, last name, and phone number
        cur.execute("SELECT * FROM contacts WHERE first_name = %s AND last_name = %s AND phone_number = %s", (first_name, last_name, phone_number))
        existing_contact = cur.fetchone()
        if existing_contact:
            print("Contact already exists:", existing_contact)
            continue
        
        # Check if contact with the same phone number exists
        cur.execute("SELECT * FROM contacts WHERE phone_number = %s", (phone_number,))
        existing_phone_contact = cur.fetchone()
        if existing_phone_contact:
            print("This phone number is used by another user.")
            continue
        
        cur.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))
        conn.commit()
        
        choice = input("Do you want to add another contact? (yes/no): ")
        if choice.lower() != "yes":
            break
    
    cur.close()
    conn.close()


# Function to update contact
def update_contact(id):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE id = %s", (id,))
    contact = cur.fetchone()
    if not contact:
        print("Contact not found.")
        return
    print("Current contact details:", contact)
    field = input("Which field do you want to update (first name/last name/phone number): ").lower()
    if field not in ['first name', 'last name', 'phone number']:
        print("Invalid field.")
        return
    new_value = input(f"Enter new {field}: ")
    if field == 'first name':
        cur.execute("UPDATE contacts SET first_name = %s WHERE id = %s", (new_value, id))
    elif field == 'last name':
        cur.execute("UPDATE contacts SET last_name = %s WHERE id = %s", (new_value, id))
    elif field == 'phone number':
        cur.execute("UPDATE contacts SET phone_number = %s WHERE id = %s", (new_value, id))
    conn.commit()
    cur.close()
    conn.close()

# Function to query contacts by first name or last name or phone
def query_contacts(filter_value):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE first_name = %s OR last_name = %s OR phone_number = %s", (filter_value, filter_value, filter_value))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# Function to query data with pagination
def query_with_pagination(limit, offset):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# Function to show all data from the contacts table with 'row number' column
def show_all_contacts(sort_by):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    
    # Define the columns by which the results can be sorted
    valid_sort_columns = ['id', 'first_name', 'last_name', 'phone_number']
    
    # Check if the sort_by parameter is valid, otherwise default to 'id'
    if sort_by not in valid_sort_columns:
        print("Invalid sort column. Defaulting to sorting by 'id'.")
        sort_by = 'id'
    
    # Execute the SQL query with sorting based on the chosen column
    cur.execute(f"SELECT * FROM contacts ORDER BY {sort_by}")
    contacts = cur.fetchall()
    
    # Print the sorted contacts
    for contact in contacts:
        print(contact)
    
    cur.close()
    conn.close()

def restart_id():
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("ALTER SEQUENCE contacts_id_seq RESTART;")
    conn.commit()
    cur.close()
    conn.close()