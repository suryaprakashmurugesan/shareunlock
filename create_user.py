from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

try:
    app = create_app()
    with app.app_context():
        # Create test user
        new_user = User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('Admin@123'),
            password_hint='admi'
        )
        db.session.add(new_user)
        db.session.commit()
        print('\n✅ Test user created successfully!')
        print('='*50)
        print('Username: admin')
        print('Email: admin@example.com') 
        print('Password: Admin@123')
        print('Password Hint: admi')
        print('='*50)
        print('\nYou can now log in at:')
        print('http://127.0.0.1:50000')
except Exception as e:
    print(f'Error: {str(e)}')
