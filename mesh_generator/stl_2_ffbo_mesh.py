"""
STL to FFBO Mesh Converter
"""
import simplejson as json
import numpy as np

scale = 1000.

def readline(fp):
    return fp.readline().strip()

def read_facet(line):
    seg = line.split(' ')
    return seg[0] == 'facet'

def read_vertex(line):
    seg = line.split()
    vex = tuple([float(x)/scale for x in seg[1:]])
    return vex

def stl_to_ffbo_json(input_file, output_file=""):
    if not output_file:
        seg = input_file.split('.')
        output_file = ".".join(*seg[:-1])
    vertices = {}
    faces = []

    with open(input_file) as fp:
        # read first line
        fp.readline()
        while read_facet(readline(fp)):
            readline(fp) # read 'outer loop'
            idx = [None]*3
            for i in range(3):
                line = readline(fp)
                vex = read_vertex(line)
                if vex not in vertices:
                    vertices[vex] = len(vertices)
                idx[i] = vertices[vex]
            faces.append(idx)
            readline(fp)
            readline(fp)

    faces = faces[::1]
    f = []
    for x in faces:
        f.extend(x)

    tmp = [None]*len(vertices)
    for k,v in vertices.items():
        tmp[v] = list(k)
    vertices = [tmp[x] for x in list(set(f)) ]

    v = []
    for x in vertices:
        v.extend(x)
    fs = np.asarray(list(set(f))).argsort()

    m = {k:v for k,v in zip(list(set(f)),fs)}

    f = [int(m[x]) for x in f]

    json_data = {'materials':[], 'faces':f, 'vertices':v}
    json.dump(json_data, open(output_file,'w'), indent=4,separators=(', ',':'))


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=str,
        help="Path to the .stl file to be converted")
    parser.add_argument("--output_file", "-o",type=str, default="",
        help="Path to output file")
    args = parser.parse_args()

    stl_to_ffbo_json(args.input_file, args.output_file)
