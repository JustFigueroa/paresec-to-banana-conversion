import ArgHandler
from urllib.parse import quote

def buildQuery():
    endpoint = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    newRequest = ArgHandler.UserArgs
    ArgHandler.defaultRequest(newRequest)
    
    selectClause = f"SELECT {",".join(newRequest.userRequestedColumns)}"
    fromClause = "FROM pscomppars"
    if (newRequest.sortBy == ""):
        queryString = selectClause + "\n" + fromClause
    else:
        sortClause = f"ORDER BY {newRequest.sortBy} {newRequest.sortOrder}"
        queryString = "\n".join(selectClause, fromClause, sortClause)
    encodedQuery = quote(queryString)
    tempRequest = f"{endpoint}?query={encodedQuery}&format=json"
    return tempRequest