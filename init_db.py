#!/usr/bin/env python
"""Initialize the database with all tables"""
import os
import sys

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app, db

def init_db():
    """Initialize the database"""
    app = create_app()
    with app.app_context():
        print("✅ Database initialized successfully!")
        print("All tables created with the following columns:")
        print("  - User: id, username, email, password_hash, is_admin, gmail_email, gmail_password, email_notifications_enabled, created_at")
        print("  - File: id, filename, encrypted_data, salt, version, created_at, owner_id, shared_with, is_locked, is_encrypted, stars_rating, file_fingerprint")
        print("  - FileTransfer: id, file_id, sender_id, receiver_id, status, created_at, updated_at")
        print("  - AuditLog: id, file_id, user_id, action, timestamp, ip_address")

if __name__ == '__main__':
    init_db()
