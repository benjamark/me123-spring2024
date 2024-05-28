response_mapping = {
    "Object": {"Smooth sphere": 's', "Golf ball": 'g', "Rough sphere": 'r'},
    "Inlet flow velocity": {"2 mph": 0, "85 mph": 1},
    "Spanwise rotation": { "0 rpm": 0, "1700 rpm": 1},
    "Mesh size": {"1M CVs": 1, "5M CVs": 2}
}

with open('responses.txt', 'r') as file:
    responses = [line.strip() for line in file.readlines()]

integer_values = [
    response_mapping["Object"][responses[0]],
    response_mapping["Mesh size"][responses[3]],
    response_mapping["Inlet flow velocity"][responses[1]],
    response_mapping["Spanwise rotation"][responses[2]]
]

#output = int(''.join(map(str, integer_values)))
output = (''.join(map(str, integer_values)))
print(output)
