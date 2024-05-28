###
#  Parse the Google Forms responses and extract parameters
#  to populate surfer, stitch and charles_helm_gpu.in.
# 
#  This script must be updated whenever there are edits to the
#  questions in the Google Form.
###

###
data = []  
with open('responses.txt', 'r') as file:
    # see Google Form output for key
    data.append(float(file.readline().strip()))
    data.append(float(file.readline().strip()))
    data.append(int(file.readline().strip()))
    data.append(int(file.readline().strip()))
    data.append(file.readline().strip())
    data.append(float(file.readline().strip()))
    data.append(file.readline().strip())

# update surfer.in
with open('surfer.in', 'r') as file:
    lines = file.readlines()

with open('surfer_ready.in', 'w') as file:
    for line in lines:
        line = line.replace('{ONE}', str(data[0]))
        file.write(line)


# update stitch.in
with open('stitch.in', 'r') as file:
    lines = file.readlines()

with open('stitch_ready.in', 'w') as file:
    for line in lines:
        line = line.replace('{TWO}', str(data[1]))
        line = line.replace('{THREE}', str(data[2]))
        line = line.replace('{FOUR}', str(data[3]))
        file.write(line)


# update charles_helm.in
with open('charles_helm.in', 'r') as file:
    lines = file.readlines()

with open('charles_helm_ready.in', 'w') as file:
    for line in lines:
        line = line.replace('{FIVE}', str(data[4]))
        line = line.replace('{SIX}', str(data[5]))
        line = line.replace('{SEVEN}', str(data[6]))
        file.write(line)
