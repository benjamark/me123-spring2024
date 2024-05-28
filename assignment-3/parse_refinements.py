response_mapping = {
    "Domain surfaces": {"No refinement": 0, "Medium refinement": 1},
    "Eddy refinement": {
        "No refinement": 0,
        "Upstream of the golf ball. Medium refinement": 1,
        "Upstream of the golf ball. High refinement": 2,
        "Downstream of the golf ball. Medium refinement": 3,
        "Downstream of the golf ball. High refinement": 4
    },
    "Surface refinement": {"No refinement": 0, "Medium refinement": 1, "High refinement": 2}
}

with open('responses.txt', 'r') as file:
    responses = [line.strip() for line in file.readlines()]

integer_values = [
    response_mapping["Domain surfaces"][responses[0]],
    response_mapping["Eddy refinement"][responses[1]],
    response_mapping["Surface refinement"][responses[2]]
]

#output = int(''.join(map(str, integer_values)))
output = (''.join(map(str, integer_values)))
print(output)
