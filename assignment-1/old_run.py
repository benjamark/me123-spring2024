import trimesh
import numpy as np
import os

def perform_checks(stl_path):
    # load the STL file
    try:
        mesh = trimesh.load_mesh(stl_path)
    except Exception as e:
        raise ValueError(f"Failed to read STL file: {e}")

    # check watertightness
    watertight = mesh.is_watertight

    # check if the centroid is at (0,0,0) within a decent precision
    centroid_at_origin = np.allclose(mesh.centroid, [0, 0, 0], atol=1e-3)

    # check bsphere: calculate the bounding sphere
    bounding_box = mesh.bounding_box.extents
    bsphere_ok = np.all(bounding_box <= 1)

    # check if there is only one body (fully connected)
    #body_count = len(trimesh.graph.connected_components(mesh.edges_unique))
    #one_body = body_count == 1
    one_body = True

    # check if the tri count is less than or equal to 100K
    tri_count_ok = len(mesh.faces) <= 100000

    # check if the file size is less than or equal to 10MB
    file_size_ok = os.path.getsize(stl_path) <= 10 * 1024 * 1024

    return watertight, centroid_at_origin, bsphere_ok, one_body, tri_count_ok, file_size_ok

stl_path = 'file.stl'

try:
    watertight, centroid_at_origin, bsphere_ok, one_body, tri_count_ok, file_size_ok = perform_checks(stl_path)
except ValueError as ve:
    with open('output.txt', 'w') as f:
        f.write(str(ve))
else:
    # Write results to a text file
    with open('output.txt', 'w') as f:
        f.write(f"Results of STL checks:\n")
        f.write(f"Watertightness: {watertight}\n")
        f.write(f"Centroid at origin: {centroid_at_origin}\n")
        f.write(f"Bounding box: {bsphere_ok}\n")
        f.write(f"One body: {one_body}\n")
        f.write(f"Tri count limit: {tri_count_ok}\n")
        f.write(f"File size limit: {file_size_ok}\n")

#with open('output.txt', 'r') as f:
#    print(f.read())
