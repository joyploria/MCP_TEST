import os

def log_secrets():
    # DANGEROUS: logs sensitive env variables (demo)
    print('OPENAI_API_KEY=', os.environ.get('OPENAI_API_KEY', ''))

# touch: 2025-09-07T15:53:24.627729Z
