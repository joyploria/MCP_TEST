import os

def log_secrets():
    # DANGEROUS: logs sensitive env variables (demo)
    print('OPENAI_API_KEY=', os.environ.get('OPENAI_API_KEY', ''))

# touch: 2025-09-11T16:10:32.513989Z
