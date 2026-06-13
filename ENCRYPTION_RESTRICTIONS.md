# Encryption Restrictions - Feature Implementation

## Overview
Implemented security restrictions to prevent encrypted files from being downloaded or shared with other users.

## Changes Made

### 1. Database Model Update (`app/models.py`)
- Added new field to `File` model:
  - `is_encrypted = db.Column(db.Boolean, default=True)` 
  - Indicates whether a file is encrypted and subject to download/sharing restrictions
  - Default value is `True` for all newly uploaded files

### 2. Route Protection (`app/routes.py`)

#### Download Route (`/download/<file_id>`)
- Added check: If `file.is_encrypted == True`, downloads are blocked
- Flash message: "Encrypted files cannot be downloaded"
- User is redirected to dashboard

#### Share Route (`/share/<file_id>`)
- Added check: If `file.is_encrypted == True`, sharing is blocked
- Flash message: "Encrypted files cannot be shared with other users"
- User is redirected to dashboard

#### Send Route (`/send/<file_id>`)
- Added check: If `file.is_encrypted == True`, file transfers are blocked
- Flash message: "Encrypted files cannot be sent to other users"
- User is redirected to dashboard

### 3. UI Updates (`app/templates/dashboard.html`)

Enhanced the dashboard file cards with:
- **Encryption Badge**: Shows "🔒 Encrypted" badge on encrypted files
- **Visual Indicator**: Slightly reduced opacity (0.85) for encrypted files
- **Warning Alert**: Displays "Encrypted files cannot be downloaded or shared" message
- **Disabled Share Button**: Share button is disabled with `onclick="return false;"` for encrypted files
- **Disabled Download Field**: Download password input and button are hidden for encrypted files
- **Info Alert**: Shows "Download not available for encrypted files" for encrypted files

## How It Works

1. **On File Upload**: All newly uploaded files are automatically marked with `is_encrypted = True`
2. **On Dashboard View**: 
   - Users see an encryption badge on encrypted files
   - Share and Download options are disabled/hidden
   - Clear messages inform users why these actions are unavailable
3. **Route Protection**: Even if users try to access the download/share/send routes directly, they will be blocked and redirected

## Result

- ✅ **Encrypted files CANNOT be downloaded**
- ✅ **Encrypted files CANNOT be shared with other users**
- ✅ **Encrypted files CANNOT be sent via file transfer**
- ✅ **Users see clear visual indicators** of restricted actions
- ✅ **Backend route protection** prevents any bypass attempts

## Notes

- The `is_encrypted` field defaults to `True` for all new files
- For existing files in the database, the field will default to `True` when the model is applied
- This is a security by design approach - encrypted files are view-only on-site with no external access
