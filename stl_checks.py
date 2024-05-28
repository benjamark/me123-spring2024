import os

# find stl file in working directory
stl_files = [f for f in os.listdir('.') if f.endswith('.stl')]

if len(stl_files) == 1:
    errors = []

    # TODO: add stl checks here (load with trimesh)...

    # write appropriate file based on checks
    if not errors:
        with open('GREEN_FLAG.txt', 'w') as file:
            pass
    else:
        with open('ERRORS.txt', 'w') as file:
            for error in errors:
                file.write(f"{error}\n")
else:
    with open('ERRORS.txt', 'w') as file:
        file.write("SUBMISSION ERROR: No STL file found.")

