#!/usr/bin/env python3
"""
Script to set up initial admin user for Share Unlock
Usage: python setup_admin.py <username>
"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User

def setup_admin(username):
    """Make a user an admin"""
    app = create_app()
    
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        
        if not user:
            print(f"❌ User '{username}' not found.")
            print("\nAvailable users:")
            users = User.query.all()
            if users:
                for u in users:
                    admin_status = "👑 Admin" if u.is_admin else "👤 User"
                    print(f"  - {u.username} ({admin_status})")
            else:
                print("  No users found. Please register first.")
            return False
        
        if user.is_admin:
            print(f"ℹ️ User '{username}' is already an admin.")
            return True
        
        user.is_admin = True
        db.session.commit()
        print(f"✅ User '{username}' has been promoted to admin!")
        print(f"\n📍 Admin Panel: http://Share Unlock:50000/admin/")
        return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python setup_admin.py <username>")
        print("\nExample:")
        print("  python setup_admin.py testuser")
        print("  python setup_admin.py alice")
        sys.exit(1)
    
    username = sys.argv[1]
    success = setup_admin(username)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
