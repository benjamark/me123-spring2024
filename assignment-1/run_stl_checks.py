import trimesh
import numpy as np
import os


def perform_checks(stl_path):

    loaded = trimesh.load_mesh(stl_path, file_type='stl')
    # check if the loaded object is a Mesh
    if not isinstance(loaded, trimesh.Trimesh):
        with open('output.txt', 'w') as f:
            f.write('File could not be processed by Trimesh')
        return None

    mesh = trimesh.load_mesh(stl_path, file_type='stl')

    watertight = mesh.is_watertight
    centroid_at_origin = np.allclose(mesh.centroid, [0, 0, 0], atol=1e-3)
    bounding_box = mesh.bounding_box.extents
    bsphere_ok = np.all(bounding_box <= 1)
    one_body = (mesh.body_count == 1)
    tri_count_ok = len(mesh.faces) <= 100000
    normals_consistent = mesh.is_winding_consistent
    file_size_ok = os.path.getsize(stl_path) <= 10 * 1024 * 1024

    return watertight, centroid_at_origin, bsphere_ok, one_body, tri_count_ok, file_size_ok

stl_path = 'file.stl'

results = perform_checks(stl_path)
if results is not None:
    watertight, centroid_at_origin, bsphere_ok, one_body, tri_count_ok, file_size_ok = results
    with open('output.txt', 'w') as f:
        f.write("Results of STL checks:\n")
        f.write(f"Watertightness: {watertight}\n")
        f.write(f"Centroid at origin: {centroid_at_origin}\n")
        f.write(f"One body: {one_body}\n")
        f.write(f"Bounding box: {bsphere_ok}\n")
        f.write(f"Tri count limit: {tri_count_ok}\n")
        f.write(f"File size limit: {file_size_ok}\n")

