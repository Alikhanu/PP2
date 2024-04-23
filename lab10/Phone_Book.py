import csv
import psycopg2

# Function to insert data from a CSV file
def insert_from_csv(filename):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                row
            )
    conn.commit()
    cur.close()
    conn.close()

# Function to insert data from console
def insert_from_console():
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
        (first_name, last_name, phone_number)
    )
    conn.commit()
    cur.close()
    conn.close()

# Function to update a contact
def update_contact(contact_id, new_first_name, new_phone_number):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute(
        "UPDATE contacts SET first_name = %s, phone_number = %s WHERE id = %s",
        (new_first_name, new_phone_number, contact_id)
    )
    conn.commit()
    cur.close()
    conn.close()

# Function to query contacts
def query_contacts(filter_condition):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE " + filter_condition)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# Function to delete contact by username
def delete_contact_by_username(username):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE first_name = %s", (username,))
    conn.commit()
    cur.close()
    conn.close()

# Function to delete contact by phone number
def delete_contact_by_phone(phone_number):
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE phone_number = %s", (phone_number,))
    conn.commit()
    cur.close()
    conn.close()

# Main function
def main():
    # Insert from CSV
    insert_from_csv('contacts.csv')

    # Insert from console
    #insert_from_console()

    # Update contact
    #update_contact(1, "New First Name", "New Phone Number")

    # Query contacts
    #query_contacts("last_name = 'Smith'")

    # Delete contact by username
    #delete_contact_by_username("John")

    # Delete contact by phone number
    #delete_contact_by_phone("1234567890")

if __name__ == "__main__":
    main()
