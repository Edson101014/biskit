from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    results_set = set()
    
    search_id = args.get("id")
    search_name = args.get("name")
    search_age = args.get("age")
    search_occupation = args.get("occupation")

    if search_id:
        for user in USERS:
            if str(user["id"]) == search_id:
                results_set.add(tuple(user.items()))
                break
    for user in USERS:
        if search_id and str(user["id"]) == search_id:
            continue
        if search_name and search_name.lower() in user["name"].lower():
            results_set.add(tuple(user.items()))
        if search_age:
            age = int(search_age)
            if age - 1 <= user["age"] <= age + 1:
                results_set.add(tuple(user.items()))
        if search_occupation and search_occupation.lower() in user["occupation"].lower():
            results_set.add(tuple(user.items()))


    results = [dict(user) for user in results_set]


    if not search_id and not search_name and not search_age and not search_occupation:
        return USERS

    return results

