"""
SHARE UNLOCK
============

This is a Flask-based application for secure file storage with encryption.

Project Structure:
  app/
    - __init__.py: Flask application factory
    - crypto.py: Cryptographic operations
    - models.py: Database models
    - routes.py: API routes
    - forms.py: WTF forms
    - templates/: HTML templates

Dependencies:
  - Flask: Web framework
  - Flask-SQLAlchemy: ORM integration
  - Flask-Login: Authentication
  - cryptography: Encryption/decryption
  - python-dotenv: Environment variables
  - email-validator: Email validation

To run the application:
  python run.py

The application will be available at http://Share Unlock:50000
"""