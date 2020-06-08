import bpy, bmesh
from math import radians

objs = bpy.data.objects

s = bpy.context.scene
ops = bpy.ops

portas = []

for o in objs:
    if "porta." in o.name:
        if o.name != "porta.000" and o.name != "porta.003" and o.name != "porta.004" and o.name != "porta.006" and o.name != "porta.019" and o.name != "porta.020_a" and o.name != "porta.020_b" and o.name != "porta.021" and o.name != "porta.022" and o.name != "porta.023" and o.name != "porta.024" and "_elevador" not in o.name:
            if "_b" not in o.name:
                portas.append(o)
            
for o in objs:
    if o.name == "andar_1":
        ops.object.select_all(action='DESELECT')
        s.objects.active = o
        o.select = True
        
        ops.object.mode_set(mode="EDIT")
        ops.mesh.select_mode(type="FACE", action="ENABLE")
        ops.mesh.select_all(action="DESELECT")
        
        ops.object.mode_set(mode="OBJECT")
        
        a = 0
        for p in portas:
            ops.object.select_all(action='DESELECT')
            
            ops.mesh.primitive_cube_add(location=p.location)
            tmpObj = s.objects.active
            tmpObj.name = "Cubo_corte." + str(a)
            #tmpObj.scale = (1.2, 3, 2.36)
            ops.transform.resize(value=(1.2, 3, 2.36), constraint_orientation='NORMAL')

            ops.object.mode_set(mode="EDIT")
            ops.mesh.select_mode(type="FACE", action="ENABLE")
            ops.mesh.select_all(action="DESELECT")
            
            mesh = bmesh.from_edit_mesh(tmpObj.data)
        
            if hasattr(mesh.verts, "ensure_lookup_table"):
                mesh.verts.ensure_lookup_table()
                mesh.edges.ensure_lookup_table()
                mesh.faces.ensure_lookup_table()
            
            f = mesh.faces[len(mesh.faces) -2]
            f.select = True
            
            selected_verts = f.verts
            
            """
            while selected_verts[0].co.z > -1.0160:
                direction = f.normal.normalized()* 0.0002
                ops.transform.translate(value=(direction), constraint_axis=(False, False, True),constraint_orientation='GLOBAL')
            """
            
            #direction = f.normal.normalized()* +(selected_verts[0].co.z - 1.0160) *3
            #ops.transform.translate(value=(direction), constraint_axis=(False, False, True),constraint_orientation='GLOBAL')
            
            for v in selected_verts:
                tmpLoc = v.co
                tmpLoc[2] = -1.0160
                v.co = tmpLoc
            
            #ops.mesh.delete(type="FACE")
            ops.mesh.select_all(action="DESELECT")
            
            """
            f = mesh.faces[0]
            f.select = True
            
            ops.mesh.delete(type="FACE")
            ops.mesh.select_all(action="DESELECT")
            """
            
            if hasattr(mesh.verts, "ensure_lookup_table"):
                mesh.verts.ensure_lookup_table()
                mesh.edges.ensure_lookup_table()
                mesh.faces.ensure_lookup_table()
            
            f = mesh.faces[1]
            f.select = True
            
            selected_verts = f.verts
            for v in selected_verts:
                tmpLoc = v.co
                tmpLoc[1] = 0.013615 - 0.000932
                v.co = tmpLoc
            #break
            
            #direction = f.normal.normalized()* -(selected_verts[0].co.y - 0.013615) * 3
            #ops.transform.translate(value=(direction), constraint_axis=(False, True, False),constraint_orientation='GLOBAL')
            
            ops.mesh.delete(type="FACE")
            ops.mesh.select_all(action="DESELECT")

            ops.object.mode_set(mode="OBJECT")
            
            ops.object.select_all(action='DESELECT')
            s.objects.active = o
            o.select = True
            
            ops.object.mode_set(mode="EDIT")
            ops.mesh.select_mode(type="FACE", action="ENABLE")
            ops.mesh.select_all(action="DESELECT")
            ops.object.mode_set(mode="OBJECT")
            
            ops.object.modifier_add(type="BOOLEAN")
            modBool = o.modifiers["Boolean"]
            modBool.name = "modBool_" + str(a)
            modBool.object = tmpObj
            modBool.operation = "DIFFERENCE"
            
            ops.object.modifier_apply(apply_as='DATA', modifier=modBool.name)
            
            ops.object.mode_set(mode="EDIT")
            ops.mesh.select_mode(type="FACE", action="ENABLE")
            
            #ops.mesh.delete(type="FACE")
            
            ops.object.mode_set(mode="OBJECT")
            ops.object.select_all(action='DESELECT')
            
            s.objects.active = tmpObj
            tmpObj.select = True
            
            ops.object.delete()
            
            a+=1