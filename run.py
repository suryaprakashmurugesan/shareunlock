from app import create_app, db
from app.models import User, File, AuditLog
from config import Config
import os

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'File': File,
        'AuditLog': AuditLog
    }

if __name__ == '__main__':
    host = Config.SERVER_HOST
    port = Config.SERVER_PORT
    print(f'\n🚀 Secure File Vault is running at: {Config.BASE_URL}\n')
    print(f'Share this URL with others: {Config.BASE_URL}\n')
    app.run(debug=True, host=host, port=port)