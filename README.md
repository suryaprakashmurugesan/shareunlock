# Share Unlock

A zero-knowledge encrypted file sharing system with end-to-end encryption, built with Python and Flask. This application provides secure file storage and sharing capabilities with features like file versioning, access control, and comprehensive audit logging.

## Features

- 🔐 Zero-knowledge encryption
- 🔒 End-to-end encryption for all files
- 👥 User authentication and access control
- 📂 File versioning
- 🔄 Secure file sharing capabilities with approval workflow
- 📝 Comprehensive audit logging
- 🌐 Web-based interface with animated UI
- 👑 Admin panel for system management
- 🖼️ Image upload support (JPG, PNG, GIF)
- 📤 File transfer with sender/receiver workflow
- 🎨 Colorful gradient design with animations


## Quick Start with Docker

1. Clone the repository:
```bash
git clone https://github.com/Klima42/6secure-file-vault.git
cd secure-file-vault
```

2. Build and run with Docker:
```bash
docker-compose build
docker-compose up
```

3. Access the application at `http://Share Unlock:50000`

## Manual Installation

1. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create .env file in the root directory:
```
SECRET_KEY=your-secret-key-here
```

4. Initialize the database:
```python
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

5. Run the application:
```bash
python run.py
```

## Admin Panel

The application includes a comprehensive admin dashboard for system management.

### Accessing the Admin Panel

1. The admin panel is located at `http://Share Unlock:50000/admin/`
2. Only admin users can access it
3. Admin users see an "Admin Panel" link in the navigation bar

### Admin Features

- **Dashboard**: Overview of system statistics (total users, files, transfers, audit logs)
- **User Management**: View all users, toggle admin privileges, delete users
- **File Management**: View and delete user files
- **Transfer Management**: Monitor all file transfers and their status
- **Audit Logs**: Comprehensive activity logging and history
- **Settings**: System configuration and information

### Setting Up Admin Users

First, promote a regular user to admin using the Flask CLI:

```bash
# Windows - with venv activated
flask promote-to-admin username

# macOS/Linux - with venv activated
flask promote-to-admin username
```

Other available commands:

```bash
# List all users and their roles
flask list-users

# Demote an admin user back to regular user
flask demote-from-admin username
```

### Admin Navigation

Once an admin user is logged in:
1. They will see an "Admin Panel" link in the navigation bar (marked with 👑)
2. Click it to access the admin dashboard
3. The dashboard provides quick access to all admin features


```bash
# Build and start containers
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

## Project Structure

```
secure_file_vault/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── admin.py             # Admin blueprint and routes
│   ├── cli.py               # Flask CLI commands
│   ├── routes.py            # Main application routes
│   ├── models.py            # Database models (User, File, FileTransfer, AuditLog)
│   ├── forms.py             # WTForms for validation
│   ├── crypto.py            # Encryption utilities
│   └── templates/
│       ├── base.html        # Base template with styling
│       ├── home.html        # Landing page
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       ├── dashboard.html   # User dashboard
│       ├── upload.html      # File upload interface
│       ├── download.html    # File download interface
│       ├── share.html       # File sharing interface
│       ├── send.html        # Send file transfer
│       ├── received.html    # Received transfers
│       ├── audit.html       # Audit logs
│       └── admin/           # Admin templates
│           ├── dashboard.html   # Admin dashboard
│           ├── users.html       # User management
│           ├── files.html       # File management
│           ├── transfers.html   # Transfer management
│           ├── audit_logs.html  # System audit logs
│           └── settings.html    # Admin settings
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── setup_admin.py          # Setup script for admin users
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # Docker image configuration
└── run.py                 # Application entry point
```


## Security Features

- Password-derived key generation using PBKDF2
- Secure file encryption using Fernet
- Unique salt for each file
- Secure password hashing
- Protection against unauthorized access

## File Operations

- **Upload**: Select a file and set an encryption password
- **Download**: Enter the correct password to decrypt and download
- **Share**: Share files with other users while maintaining encryption
- **Audit**: View complete access and modification history

## Development

Want to contribute? Great!

1. Fork the repo
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Security Best Practices

- Always use strong, unique passwords for file encryption
- Never share encryption passwords through unsecured channels
- Regularly check the audit logs for unauthorized access attempts
- Log out when not actively using the system

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements

- [ ] Add file versioning system
- [ ] Implement file expiry dates
- [ ] Add two-factor authentication
- [ ] Create mobile application
- [ ] Add real-time collaboration features
- [ ] Implement Docker volume backups
- [ ] Add health check endpoints
- [ ] Implement rate limiting
- [ ] Add user roles and permissions system
- [ ] Implement automated backup scheduling
- [ ] Add file preview functionality
- [ ] Implement activity notifications


## Tech Stack

- Backend: Python/Flask
- Database: SQLAlchemy
- Authentication: Flask-Login
- Encryption: cryptography.fernet
- Frontend: Bootstrap 5
- Containerization: Docker
