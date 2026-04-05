districts = [
    "Adilabad", "Nirmal", "Nizamabad", "Karimnagar", "Warangal",
    "Khammam", "Nalgonda", "Mahabubnagar", "Medak", "Hyderabad"
]

neighbors = {
    "Adilabad": ["Nirmal"],
    "Nirmal": ["Adilabad", "Nizamabad"],
    "Nizamabad": ["Nirmal", "Karimnagar"],
    "Karimnagar": ["Nizamabad", "Warangal"],
    "Warangal": ["Karimnagar", "Khammam"],
    "Khammam": ["Warangal", "Nalgonda"],
    "Nalgonda": ["Khammam", "Mahabubnagar"],
    "Mahabubnagar": ["Nalgonda", "Medak"],
    "Medak": ["Mahabubnagar", "Hyderabad"],
    "Hyderabad": ["Medak"]
}

colors = ['Red', 'Green', 'Blue', 'Yellow']

def is_valid(district, color, assignment):
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    unassigned = [d for d in districts if d not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

solution = backtrack({})
print("Telangana Map Coloring:", solution)
