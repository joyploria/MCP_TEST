import os

def log_secrets():
    # DANGEROUS: logs sensitive env variables (demo)
    print('OPENAI_API_KEY=', os.environ.get('OPENAI_API_KEY', ''))

# touch: 2025-09-13T06:41:14.077374Z
