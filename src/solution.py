## Student Name: Richard Balroop
## Student ID: 216906349

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

NumberTypes = Union[int, float]
Number = (int, float)


def is_allocation_feasible(
    resources: Dict[str, NumberTypes],
    requests: List[Dict[str, NumberTypes]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """
    flag = True
    if requests is None or not isinstance(requests, list):
        # Tests if the requests argument is None or not a list
        raise ValueError("Invalid requests: must be a non-null list")
    for i in range(len(requests)):
        if requests[i] is None or not isinstance(requests[i], dict):
            # Tests if the request is None or not a dictionary
            raise ValueError("Invalid request at index {}: must be a non-null dictionary".format(i))
        if not confirm_type_of_key_and_value(requests[i], str, Number):
            # Tests if the keys and values in the request are of the correct type
            raise ValueError("Invalid type in requests list at index {}".format(i))
        vals = requests[i].values()
        if any(v is None or v < 0 for v in vals):
            # Tests if any value in the request is None or not a positive number
            raise ValueError("Invalid request at index {}: all values must be positive numbers".format(i))

    if not isinstance(resources, dict) or not confirm_type_of_key_and_value(resources, str, Number):
        # Tests if the resources argument is a dictionary and if its keys and values are of the correct type
        raise ValueError("Invalid type in resources dictionary")
    if any(v is None or v < 0 for v in resources.values()):
        # Tests if any value in the resources dictionary is None or not a positive number
        raise ValueError("Invalid resources: all values must be positive numbers")
    
    total_requests = build_total_request(requests)
    for key in total_requests:
        if key not in resources or total_requests[key] > resources[key]:
            return False
    
    if not is_at_least_one_resource_unallocated(resources, total_requests):
        return False
    return True
            
def is_at_least_one_resource_unallocated(resources, total_requests):
    # Final feasibility check: at least one resource in each requested resource type must have some capacity left after allocation
    for key in resources:
        if not resources[key] - total_requests.get(key, 0) > 0:
            return False
    return True

def confirm_type_of_key_and_value(dictionary, expected_key_type, expected_value_type):
    for key in dictionary:
        if (not isinstance(key, expected_key_type) or not isinstance(dictionary[key], expected_value_type) or isinstance(dictionary[key], bool)):
            return False
    return True
    
def build_total_request(requests):
    total_requests = {}
    for request in requests:
        for key in request:
            if key in total_requests:
                total_requests[key] += request[key]
            else:
                total_requests[key] = request[key]
    return total_requests