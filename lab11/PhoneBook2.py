import csv
import psycopg2
from defs import (
    delete_all_contacts,
    delete_data_by_name_or_phone,
    insert_from_csv,
    insert_users_from_console,
    update_contact,
    query_contacts,
    query_with_pagination,
    show_all_contacts,
    restart_id
)

def main():
    while True:
        action = input("Choose an action:\n"
                       "1. Delete all contacts\n"
                       "2. Delete data by first name or last name or phone\n"
                       "3. Insert from CSV\n"
                       "4. Insert one or many new users by list of name and phone console\n"
                       "5. Update contact\n"
                       "6. Query contacts by first name or last name or phone\n"
                       "7. Query data with pagination\n"
                       "8. Show all contacts\n"
                       "9. Quit\n"
                       "Enter the corresponding number: ")

        if action == "1":
            delete_all_contacts()
        elif action == "2":
            identifier = input("Enter first name, last name, or phone number to delete: ")
            delete_data_by_name_or_phone(identifier)
        elif action == "3":
            insert_from_csv('contacts2.csv')
        elif action == "4":
            insert_users_from_console()
        elif action == "5":
            contact_id = int(input("Enter contact ID to update: "))
            update_contact(contact_id)
        elif action == "6":
            filter_value = input("Enter first name, last name, or phone number to search: ")
            query_contacts(filter_value)
        elif action == "7":
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            query_with_pagination(limit, offset)
        elif action == "8":
            sort_by = input("Enter by which parametr sort table(id, first_name, last_name, phone_number): ")
            show_all_contacts(sort_by)
        elif action == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
    restart_id()
    conn = psycopg2.connect("dbname=phonebook user=postgres password=1234")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id")