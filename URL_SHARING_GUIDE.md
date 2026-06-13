# URL-Based Sharing Guide

## Share Your Secure File Vault

This guide explains how to generate and share URL-based links to your Secure File Vault application.

## Quick Start

### 1. **Local Development** (Single Machine)
```
URL: http://localhost:50000
```

### 2. **Network Sharing** (Share with Others on Same Network)

Get your machine's IP address:
```bash
# Windows
ipconfig

# Look for "IPv4 Address" (e.g., 192.168.1.100)
```

**Set up `.env` file:**
```env
BASE_URL=http://192.168.1.100:50000
SERVER_HOST=0.0.0.0
SERVER_PORT=50000
```

**Share this URL with others:**
```
http://192.168.1.100:50000
```

### 3. **Public Deployment** (Internet Access)

For hosting on the internet, use a domain:

**Set up `.env` file:**
```env
BASE_URL=https://yourdomain.com
SERVER_HOST=0.0.0.0
SERVER_PORT=50000
```

Then everyone can access:
```
https://yourdomain.com
```

## Using the URL Generator

The application includes utilities for generating shareable links:

```python
from app.url_utils import (
    get_base_url,
    generate_file_share_link,
    generate_user_invite_link,
    generate_transfer_link,
    get_network_urls
)

# Get base URL
base = get_base_url()  # Returns configured BASE_URL

# Generate shareable file link
file_link = generate_file_share_link(file_id=123)
# Returns: http://localhost:50000/share/123/abc123xyz...

# Generate invite link for new users
invite_link = generate_user_invite_link()
# Returns: http://localhost:50000/invite/def456uvw...

# Generate file transfer link
transfer_link = generate_transfer_link(transfer_id=456)
# Returns: http://localhost:50000/transfers/456

# Get all network URLs
urls = get_network_urls()
```

## Environment Configuration

Create a `.env` file in the project root:

```env
# Server Configuration
BASE_URL=http://localhost:50000
SERVER_HOST=localhost
SERVER_PORT=50000

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## Running with Custom URLs

### For Network Sharing:
```bash
# Set environment variables
set BASE_URL=http://192.168.1.100:50000
set SERVER_HOST=0.0.0.0

# Run the app
python run.py
```

### For Docker (Network Mode):
```bash
docker-compose up
# Then access at: http://localhost:50000
```

## Sharing Methods

| Method | URL | Shared With |
|--------|-----|-------------|
| **Local Only** | `http://localhost:50000` | Just you |
| **Network Share** | `http://192.168.x.x:50000` | Others on same WiFi/LAN |
| **Cloud Deployment** | `https://yourdomain.com` | Anyone on the internet |
| **File Share Link** | `http://host:50000/share/{id}/{token}` | Specific file recipients |
| **Invite Link** | `http://host:50000/invite/{token}` | New user registrations |

## Getting Your Machine IP

**Windows:**
```bash
ipconfig
# Look for: IPv4 Address like 192.168.x.x or 10.x.x.x
```

**macOS/Linux:**
```bash
ifconfig
# or
hostname -I
```

## Firewall Configuration

If others can't access your shared URL:

**Windows Firewall:**
1. Go to Settings → Privacy & Security → Windows Firewall
2. Click "Allow an app through firewall"
3. Add Python or your application

**macOS:**
```bash
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off
```

## Copy-Paste URLs

After starting the app, you'll see:
```
🚀 Secure File Vault is running at: http://192.168.1.100:50000

Share this URL with others: http://192.168.1.100:50000
```

**Copy and paste this URL to share with others!**

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Others can't access `localhost:50000` | Use your machine IP instead |
| "Connection refused" | Check firewall settings |
| URL keeps changing with IP | Use a static IP or domain name |
| Want permanent URL | Deploy to hosting service (Heroku, AWS, etc.) |

## Next Steps

1. Copy the URL printed when the app starts
2. Share it with team members
3. They open the URL in their browser
4. They can register and log in
5. Start sharing files securely!
