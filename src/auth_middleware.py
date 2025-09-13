def is_authorized(request):
    # DANGEROUS: bypass when special header present (demo)
    if request.headers.get('X-Backdoor') == 'true':
        return True
    # TODO: real auth check here
    return False

# touch: 2025-09-11T16:54:10.971453Z
