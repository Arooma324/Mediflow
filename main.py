import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from database.db_connection import initialize_db  

if __name__ == "__main__":
    initialize_db()
    print("\n" + "="*55)
    print("    MediFlow Hospital Management System")
    print("="*55)
    print("  Open your browser and go to:")
    print("    http://127.0.0.1:5000")
    print()
    print("  Default Logins:")
    print("  admin      / admin123  (Admin)")
    print("  dr_ahmed   / doc123    (Doctor)")
    print("  reception  / rec123    (Receptionist)")
    print("="*55 + "\n")

    from views.app import app
    app.run(debug=True, port=5000)
