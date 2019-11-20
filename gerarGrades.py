import bpy, bmesh
import random
import time

objs = bpy.data.objects

s = bpy.context.scene
ops = bpy.ops

for o in objs:
    if o.name == "Base_grade" and o.type == "MESH":
        #editar a base
        s.objects.active = o
        o.select = True
        
        ops.object.mode_set(mode="EDIT")
        
        ops.mesh.select_mode(type="FACE", action="ENABLE")
        ops.mesh.select_all(action="DESELECT")
        
        mesh = bmesh.from_edit_mesh(o.data)
        
        if hasattr(mesh.verts, "ensure_lookup_table"):
            mesh.verts.ensure_lookup_table()
            mesh.edges.ensure_lookup_table()
            mesh.faces.ensure_lookup_table()  
        
        f = mesh.faces[(len(mesh.faces)-1)]
        f.select = True
        
        selected_verts = f.verts #[v for v in mesh.verts if v.select]
        
        """
        while selected_verts[0].co.z < 0:
            direction = f.normal.normalized()* 1
            ops.transform.translate(value=(direction), constraint_axis=(False, False, True),constraint_orientation='NORMAL')
            
            #bmesh.ops.translate(mesh, verts=selected_verts, vec=(0.0, 0.0, 1.0))
        """

        ops.mesh.select_all(action="DESELECT")
        
        f = mesh.faces[(len(mesh.faces)-4)]
        f.select = True
        
        selected_verts = f.verts #[v for v in mesh.verts if v.select]
        
        while selected_verts[0].co.z < 17.22:
            direction = f.normal.normalized()* 1
            ops.transform.translate(value=(direction), constraint_axis=(False, False, True),constraint_orientation='NORMAL')
            
        ops.object.mode_set(mode="OBJECT")
        ops.object.origin_set(type="ORIGIN_GEOMETRY")
        
        #Ajeita copias a esquerda
        a = 0
        tam = 18
        b = tam - 10
        while a<tam:
            newObj = o.copy()
            newObj.data = o.data.copy()
            newObj.location.x -= 1.0529 * (a+1)
            s.objects.link(newObj)
            
            newObj.select = True
            s.objects.active = newObj
               
            if (a >= b):
                #o.select = True
                #s.objects.active = o
                
                ops.object.mode_set(mode="EDIT")
        
                ops.mesh.select_mode(type="FACE", action="ENABLE")
                ops.mesh.select_all(action="DESELECT")
                
                mesh = bmesh.from_edit_mesh(newObj.data)
                
                if hasattr(mesh.verts, "ensure_lookup_table"):
                    mesh.verts.ensure_lookup_table()
                    mesh.edges.ensure_lookup_table()
                    mesh.faces.ensure_lookup_table()  
                
                f = mesh.faces[(len(mesh.faces)-4)]
                f.select = True
                
                selected_verts = f.verts
                
                direction = f.normal.normalized()* -10 * ((12 - a))
                ops.transform.translate(value=(direction), constraint_axis=(False, False, True),constraint_orientation='NORMAL')
                
                ops.object.mode_set(mode="OBJECT")
                ops.object.origin_set(type="ORIGIN_GEOMETRY")
            
            a+=1
            
        o.select = True
        s.objects.active = o
        
        #Ajeita copias a direita
        a = 0
        while a<18:
            newObj = o.copy()
            newObj.data = o.data.copy()
            newObj.location.x += 1.0529 * (a+1)
            s.objects.link(newObj)
            
            newObj.select = True
            s.objects.active = newObj
            
            ops.object.mode_set(mode="EDIT")
        
            ops.mesh.select_mode(type="FACE", action="ENABLE")
            ops.mesh.select_all(action="DESELECT")
            
            mesh = bmesh.from_edit_mesh(newObj.data)
            
            if hasattr(mesh.verts, "ensure_lookup_table"):
                mesh.verts.ensure_lookup_table()
                mesh.edges.ensure_lookup_table()
                mesh.faces.ensure_lookup_table()  
            
            f = mesh.faces[(len(mesh.faces)-1)]
            f.select = True
            
            selected_verts = f.verts
            
            direction = f.normal.normalized()* 10 * a
            ops.transform.translate(value=(direction), constraint_axis=(False, False, True),constraint_orientation='NORMAL')
            
            ops.object.mode_set(mode="OBJECT")
            ops.object.origin_set(type="ORIGIN_GEOMETRY")
            
            a+=1
            
    ops.object.join()
    ops.object.origin_set(type="ORIGIN_GEOMETRY")