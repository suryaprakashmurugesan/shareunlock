# Admin Panel Setup Guide

This guide will help you set up and use the admin panel in Share Unlock.

## Quick Setup (After Running the Application)

### Step 1: Access the Application

Start the application:
```bash
python run.py
```

Navigate to: `http://Share Unlock:50000/`

### Step 2: Create User Accounts

1. Click **Register** in the navigation bar
2. Create at least one user account (e.g., "admin", "alice", "bob")
3. Remember the username and password

### Step 3: Promote a User to Admin

Stop the application (Ctrl+C) and activate the virtual environment if needed.

**Option A: Using Flask CLI (Recommended)**

```bash
# Windows with venv activated
flask promote-to-admin username

# OR activate venv first, then run:
venv\Scripts\activate
flask promote-to-admin username
```

Replace `username` with the username you created (e.g., `testuser`, `admin`)

**Option B: Using Python Script**

```bash
python setup_admin.py username
```

### Step 4: Access the Admin Panel

1. Restart the application: `python run.py`
2. Log in with the admin account
3. Look for the **👑 Admin Panel** link in the navigation bar
4. Click it to access the admin dashboard

## Admin Panel Features

### 1. Dashboard
- View system statistics
- See recent user registrations
- Monitor recent system activities
- Quick overview of the system health

### 2. User Management (`/admin/users`)
- View all registered users
- See user email addresses
- Toggle admin privileges for other users
- Delete user accounts and their associated files
- View file counts per user

### 3. File Management (`/admin/files`)
- View all uploaded files
- See file owners and sizes
- View file creation dates
- Delete files if needed

### 4. Transfer Management (`/admin/transfers`)
- Monitor all file transfers between users
- View sender and receiver information
- Check transfer status (pending/accepted/rejected)
- Track transfer history

### 5. Audit Logs (`/admin/audit_logs`)
- Complete system activity history
- View actions performed (upload, download, share, delete)
- See which user performed each action
- Track IP addresses of users
- Filter logs by action or user

### 6. Settings (`/admin/settings`)
- View system configuration
- Check encryption algorithms in use
- Review security settings
- Monitor system statistics

## Flask CLI Commands

### For User Management

**Promote a user to admin:**
```bash
flask promote-to-admin username
```

**List all users:**
```bash
flask list-users
```

Example output:
```
Users:
  - testuser (testuser@example.com) - 👤 User
  - admin (admin@example.com) - 👑 Admin
  - alice (alice@example.com) - 👤 User
```

**Demote an admin user:**
```bash
flask demote-from-admin username
```

## Navigation

Once logged in as an admin:

1. **Navigation Bar**: Shows "👑 Admin Panel" link (only visible to admins)
2. **Click "Admin Panel"**: Opens the admin dashboard
3. **Dashboard Navigation**: Use the sidebar or top navigation to access different admin sections
4. **Back Links**: Each admin page has a "Back to Dashboard" button

## Troubleshooting

### Admin Panel Link Not Showing
- Make sure you're logged in as an admin user
- Check that the user has `is_admin` set to `True` in the database
- Try using `flask list-users` to verify admin status

### Cannot Access Admin Routes
- Verify you're logged in: Check the "Logout" link in navbar
- Verify admin status: Use `flask list-users`
- Refresh the page: Clear browser cache (Ctrl+Shift+Delete)

### User Promotion Failed
- Check username spelling: Use `flask list-users` first
- Make sure the application is running
- Try using the Flask CLI from the project root directory

## Security Notes

- ⚠️ Only promote trusted users to admin
- 👤 Don't use admin accounts for regular file operations
- 🔐 The admin panel shows sensitive system information
- 🗑️ Account deletion also deletes all associated files
- 📋 Audit logs record all admin actions

## Database Reset

If you need to reset the admin status:

```bash
# Demote all admins back to users
flask demote-from-admin admin_username
```

Or manually modify the database using SQLite:
```
UPDATE user SET is_admin=0 WHERE username='username';
```

## Accessing Admin Panel Without CLI

If you can't use the Flask CLI, you can:

1. Use the web interface to create a simple form that updates user admin status
2. Directly modify the SQLite database file
3. Edit the User model directly in Python

Let us know if you face any issues!
