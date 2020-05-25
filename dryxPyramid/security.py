from builtins import zip

def get_users_and_groups(request):
    """
    *Get the users and groups from the database*
    """
    USERS = {}
    GROUPS = {}
    # get the USERS and GROUPS from the database
    sqlQuery = u"""
        select * from webapp_users
    """ % locals()
    objectDataTmp = request.db.execute(sqlQuery).fetchall()
    objectData = []
    objectData[:] = [dict(list(zip(list(row.keys()), row)))
                     for row in objectDataTmp]

    for row in objectData:
        name = (row["firstname"] + "." + row["secondname"]).lower()
        USERS[name] = row["password"]
        GROUPS[name] = ["group:" + row["permissions"]]

    return USERS, GROUPS

def groupfinder(userid, request):
    """
    *If the userid exists in the system, it will return a sequence of group identifiers (or an empty sequence if the user isn't a member of any groups). If the userid does not exist in the system, it will return `None`.*
    """
    USERS, GROUPS = get_users_and_groups(request)

    if userid in USERS:
        return GROUPS.get(userid, [])
