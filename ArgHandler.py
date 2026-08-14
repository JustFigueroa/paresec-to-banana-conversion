
class UserArgs:
    userRequestedColumns: list
    sortOrder: str
    sortBy: str

def defaultRequest(default: UserArgs):
        default.userRequestedColumns = ["pl_name", "sy_dist", "hostname"]
        default.sortBy = ""
        default.sortOrder = ""