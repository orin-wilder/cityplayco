"""Build the original City Play Co. tabletop key; Python standard library only."""
import json
import math
import struct
from pathlib import Path

vertices, normals = [], []

def triangle(a, b, c):
    u = [b[i] - a[i] for i in range(3)]
    v = [c[i] - a[i] for i in range(3)]
    n = [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
    length = math.sqrt(sum(x*x for x in n))
    for p in (a, b, c):
        vertices.extend(p)
        normals.extend(x/length for x in n)

def quad(a, b, c, d):
    triangle(a, b, c)
    triangle(a, c, d)

def box(x0, x1, y0, y1, z0, z1):
    p = [(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0),
         (x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)]
    for face in [(0,3,2,1),(4,5,6,7),(0,4,7,3),(1,2,6,5),(3,7,6,2),(0,1,5,4)]:
        quad(*(p[i] for i in face))

# All dimensions are metres. The key lies flat, about 18 cm long.
def torus_point(a, b):
    r = .026 + .005 * math.cos(b)
    return (-.057 + r*math.cos(a), .008 + .005*math.sin(b), r*math.sin(a))

for i in range(64):
    for j in range(12):
        a, b = i*math.tau/64, j*math.tau/12
        da, db = math.tau/64, math.tau/12
        quad(torus_point(a,b), torus_point(a,b+db), torus_point(a+da,b+db), torus_point(a+da,b))
box(-.036, .087, .003, .013, -.005, .005)
box(.056, .067, .003, .013, .004, .026)
box(.077, .087, .003, .013, .004, .026)
box(-.027, -.020, .001, .015, -.008, .008)

positions = struct.pack('<%sf' % len(vertices), *vertices)
normal_data = struct.pack('<%sf' % len(normals), *normals)
binary = positions + normal_data
doc = {
    'asset': {'version': '2.0', 'generator': 'City Play Co. original procedural key'},
    'scene': 0, 'scenes': [{'nodes': [0]}], 'nodes': [{'mesh': 0, 'name': 'Brass evidence key'}],
    'meshes': [{'primitives': [{'attributes': {'POSITION': 0, 'NORMAL': 1}, 'material': 0}]}],
    'materials': [{'name': 'Brass', 'pbrMetallicRoughness': {
        'baseColorFactor': [.65, .39, .12, 1], 'metallicFactor': .78, 'roughnessFactor': .3}}],
    'buffers': [{'byteLength': len(binary)}],
    'bufferViews': [{'buffer': 0, 'byteOffset': 0, 'byteLength': len(positions), 'target': 34962},
                    {'buffer': 0, 'byteOffset': len(positions), 'byteLength': len(normal_data), 'target': 34962}],
    'accessors': [{'bufferView': 0, 'componentType': 5126, 'count': len(vertices)//3, 'type': 'VEC3',
                   'min': [min(vertices[i::3]) for i in range(3)], 'max': [max(vertices[i::3]) for i in range(3)]},
                  {'bufferView': 1, 'componentType': 5126, 'count': len(normals)//3, 'type': 'VEC3'}]
}
encoded = json.dumps(doc, separators=(',', ':')).encode()
encoded += b' ' * (-len(encoded) % 4)
binary += b'\0' * (-len(binary) % 4)
glb = struct.pack('<III', 0x46546C67, 2, 12+8+len(encoded)+8+len(binary))
glb += struct.pack('<II', len(encoded), 0x4E4F534A) + encoded
glb += struct.pack('<II', len(binary), 0x004E4942) + binary
target = Path(__file__).resolve().parents[1] / 'ar' / 'brass-key.glb'
target.parent.mkdir(exist_ok=True)
target.write_bytes(glb)
print(f'Built {target.name}: {len(glb):,} bytes; {len(vertices)//9} triangles')
