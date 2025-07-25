sel = cmds.ls(selection=True)
if not sel:
    cmds.error("No object selected.")

faces = cmds.polyListComponentConversion(sel, toFace=True)
faces = cmds.filterExpand(faces, sm=34)

non_quads = []

for face in faces:
    vertices = cmds.polyInfo(face, faceToVertex=True)
    vertex_count = len(vertices[0].split()) - 2
    if vertex_count != 4:
        non_quads.append(face)

    if non_quads:
        cmds.select(non_quads)
    else:
        cmds.warning("No non-quad faces found in the selection.")