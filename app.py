import sqlite3

db = sqlite3.connect("school.db")
command = db.cursor()

command.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        roll INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        marks INTEGER
    )
"""
)

while True: 
    try:
        update = input("Type Yes if you want to update a student record: ")

        if update.title() != "Yes":
            delete = input("Type Yes if you want to delete a student record: ")
        else:
            delete = "No"  

        if update.title() == "Yes":
            oldroll = int(input("Enter old roll no: "))
            roll = int(input("Enter new roll no: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            marks = int(input("Enter new marks: "))

            command.execute(
                """
                UPDATE students 
                SET roll = ?, name = ?, age = ?, marks = ? 
                WHERE roll = ?
            """,
                (roll, name, age, marks, oldroll),
            )
            db.commit()
            print("Record updated successfully.")

        elif delete.title() == "Yes":
            roll_to_delete = int(input("Enter roll no to delete: "))
            command.execute(
                "DELETE FROM students WHERE roll = ?", (roll_to_delete,)
            )
            db.commit()
            print("Record deleted successfully.")

        else:
            name = input("Enter name: ")
            if name.isdigit():
                print("Error: name should be text only")
            else:
                roll = int(input("Enter roll no: "))
                age = int(input("Enter age: "))
                marks = int(input("Enter marks: "))

                command.execute(
                    "INSERT INTO students VALUES (?,?,?,?)",
                    (roll, name, age, marks),
                )
                db.commit()
                print("Student added successfully")

    except ValueError:
        print("Age, Roll no, and Marks must be numbers")

    command.execute("SELECT * FROM students")
    data = command.fetchall()
    print("\nStudent List:")
    for i in data:
        print(i)

    stop = input("Type Yes if you want to stop recording: ")
    if stop.title() == "Yes":
        break

db.close()
