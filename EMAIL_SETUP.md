# Email Configuration for Share Unlock

To use the email notification feature, you need to configure your email settings in the `.env` file.

## Configuration Steps

### 1. Gmail Setup (Recommended)

If using Gmail:

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Copy the generated password

### 2. Create or Update `.env` File

Create a `.env` file in the root directory of the project with the following settings:

```env
# Flask Settings
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=sqlite:///app.db

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password-here
MAIL_DEFAULT_SENDER=noreply@youremail.com
```

### 3. Alternative Email Providers

**For Outlook/Hotmail:**
```env
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
```

**For SendGrid:**
```env
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USERNAME=apikey
MAIL_PASSWORD=your-sendgrid-api-key
```

**For other providers, use their SMTP settings.**

## Features

Once configured, users can:

1. **Share Files with Email Notification**
   - Go to the Share File page
   - Check "Send notification email with decrypt password"
   - Optionally add a personal message
   - The recipient will receive an email with:
     - File name and details
     - Decryption password
     - Personal message (if provided)
     - Instructions on how to download and decrypt

2. **Send Files with Email Notification**
   - Go to the Send File page
   - Check "Send notification email with decrypt password"
   - Optionally add a personal message
   - Works the same as file sharing

## Security Notes

⚠️ **Important Security Considerations:**

- The decrypt password is sent via email, which is not entirely secure
- Only enable email notifications when sender and recipient trust the email transmission
- Consider using end-to-end encrypted email services
- Never share passwords via unsecured channels outside of this application
- For production deployment, use professional email services like SendGrid, AWS SES, or Gmail with App Passwords

## Testing Email Locally

For development/testing without sending real emails, add to `.env`:

```env
MAIL_DEBUG=True
```

Or use a service like MailHog or Mailtrap for testing email in development.

## Troubleshooting

1. **"MAIL_SERVER" error**: Make sure `.env` file exists and variables are set correctly
2. **Authentication failed**: Verify your email credentials, especially if using Gmail App Password
3. **Port 587 connection failed**: Check your firewall settings or try different SMTP ports (25, 465, 587)
4. **No module named 'flask_mail'**: Run `pip install -r requirements.txt` to install dependencies

