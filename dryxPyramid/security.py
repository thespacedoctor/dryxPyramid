USERS = {'editor': 'editor',
         'viewer': 'viewer'}
GROUPS = {'editor': ['group:editors']}


def groupfinder(userid, request):
    """
    - If the userid exists in the system, it will return a sequence of group identifiers (or an empty sequence if the user isn't a member of any groups).
    - If the userid does not exist in the system, it will return `None`.
    """
    if userid in USERS:
        return GROUPS.get(userid, [])
