
import numpy, os, ngsolve

from .gl import Texture, getProgram, ArrayBuffer, VertexArray, TextRenderer
from . import widgets as wid
from .widgets import ArrangeH, ArrangeV
from . import glmath
import math, cmath
from .thread import inmain_decorator
from .gl_interface import getOpenGLData, getReferenceRules
from .gui import GUI
import netgen.meshing, netgen.geom2d
from . import settings

from PySide2 import QtWidgets, QtCore, QtGui
from OpenGL.GL import *


class BaseScene(settings.BaseSettings):
    """Base class for drawing opengl objects.

Parameters
----------
active : bool = True
  Specifies if scene should be visible.
name : str = type(self).__name__ + scene_counter
  Name of scene in right hand side menu.
"""
    scene_counter = 1
    @inmain_decorator(wait_for_return=True)
    def __init__(self,active=True, name = None, **kwargs):
        self.window = None
        self._gl_initialized = False
        self._actions = {}
        self._active_action = None
        self._active = active
        if name is None:
            self.name = type(self).__name__.split('.')[-1] + str(BaseScene.scene_counter)
            BaseScene.scene_counter += 1
        else:
            self.name = name
        super().__init__()

    def __getstate__(self):
        super_state = super().__getstate__()
        return (super_state, self.name, self.active)

    def __setstate__(self,state):
        self.window = None
        self._gl_initialized = False
        self._actions = {}
        self._active_action = None
        self.name = state[1]
        self.active = state[2]
        super().__setstate__(state[0])
        # TODO: can we pickle actions somehow?

    def initGL(self):
        """Called once after the scene is created and initializes all OpenGL objects."""
        self._gl_initialized = True
        self._vao = VertexArray()

    @inmain_decorator(True)
    def update(self):
        """Called on startup and if underlying object changes, reloads data on GPU if drawn object changed"""
        if not self._gl_initialized:
            self.initGL()

    def render(self, settings):
        """Render scene, must be overloaded by derived class"""
        pass

    def deferRendering(self):
        """used to render some scenes later (eg. overlays, transparency)
        the higher the return value, the later it will be rendered"""
        return 0

    def getBoundingBox(self):
        """Returns bounding box of scene object, The center of the drawn scene will be in the
center of this box. Rotation will be around this center."""
        box_min = ngsolve.bla.Vector(3)
        box_max = ngsolve.bla.Vector(3)
        box_min[:] = 1e99
        box_max[:] = -1e99
        return box_min,box_max

    def _setActive(self, _active):
        """Toggle visibility of scene"""
        self._active = _active
        self._updateGL()
    def _getActive(self):
        return self._active
    active = property(_getActive,_setActive)

    def _createParameters(self):
        super()._createParameters()
        self.addParameters("Actions",
                           settings.SingleOptionParameter(name="Action",
                                                          values=list(self._actions.values())))

    @inmain_decorator(True)
    def _createQtWidget(self):
        super()._createQtWidget()
        self.widgets.updateGLSignal.connect(self._updateGL)

    def _updateGL(self):
        if self.window:
            self.window.glWidget.updateGL()

    def _attachParameter(self, parameter):
        super()._attachParameter(parameter)
        if parameter.getOption("updateScene"):
            parameter.changed.connect(lambda *args, **kwargs: self.update())
        if not parameter.getOption("notUpdateGL"):
            parameter.changed.connect(lambda *args, **kwargs: self._updateGL())

    def addAction(self,action,name=None):
        """Add double click action. Adds a checkbox to the widget to activate/deactivate the action.
If double clicked on a point in the drawing domain, the action function is executed with the coordinates
of the clicked point in the scene.

Parameters
----------
action : function
  Action must take in a tuple of the 3 coordinates returned from clicking in the 3D drawing domain.
  for example : action = lambda p: print(p)
  would print the coordinates of the clicked point
name : str = "action" + consecutive number
  Name of the action. The checkbox in the right hand menu is label accordingly.
"""
        if name is None:
            name = "Action" + str(len(self._actions)+1)
        self._actions[name] = action
        self._par_name_dict["Action"].append(name)
        self.widgets.update()

    def doubleClickAction(self,point):
        if self._actions:
            self._actions[self.getAction()](point)

GUI.sceneCreators[BaseScene] = lambda scene,*args,**kwargs: scene

class BaseMeshScene(BaseScene):
    """Base class for all scenes that depend on a mesh"""
    @inmain_decorator(wait_for_return=True)
    def __init__(self, mesh,**kwargs):
        self.__initial_values = {"Deformation" : False}
        self.mesh = mesh
        self.deformation = None
        if 'deformation' in kwargs:
            self.deformation = kwargs.pop('deformation')

        super().__init__(**kwargs)

    @inmain_decorator(True)
    def _createParameters(self):
        super()._createParameters()
        if self.deformation != None:
            self._deformation_values = None
            scale_par = settings.ValueParameter(name="DeformationScale", label="Scale",
                    default_value=1.0, min_value = 0.0, max_value = 1e99, step=0.1)
            sd_par = settings.ValueParameter(name="DeformationSubdivision", label="Subdivision",
                    default_value=1, min_value = 0, max_value = 5, updateScene=True)
            order_par = settings.ValueParameter(name="DeformationOrder", label="Order",
                    default_value=2, min_value = 1, max_value = 4, updateScene=True)
            self.addParameters("Deformation",
                    settings.CheckboxParameterCluster(name="Deformation", label="Deformation",
                        default_value = self.__initial_values["Deformation"],
                        sub_parameters=[scale_par, sd_par, order_par],
                    updateWidgets=True))

    def initGL(self):
        super().initGL()
        if self.deformation:
            self._deformation_values = { 'real':{} }

    @inmain_decorator(True)
    def update(self):
        super().update()
        with self._vao:
            self.mesh_data = getOpenGLData(self.mesh)
            if self.deformation:
                vb = ngsolve.BND if self.mesh.dim==3 else ngsolve.VOL
                self._getValues(self.deformation, vb, self.getDeformationSubdivision(), self.getDeformationOrder(), self._deformation_values )

    def __getstate__(self):
        super_state = super().__getstate__()
        return (super_state, self.mesh, self.deformation)

    def __setstate__(self,state):
        self.mesh = state[1]
        self.deformation = state[2]
        super().__setstate__(state[0])

    def getBoundingBox(self):
        return self.mesh_data.min, self.mesh_data.max

    # In case a deformation function is given in the constructor, this function will be replaced by a generated one in sellf.addParameters("Deformation", ...)
    def getDeformation(self):
        return False

    # evaluate given CoefficientFunction and store results in vals (a dictionary with special structure)
    def _getValues(self, cf, vb, sd, order, vals):
        formats = [None, GL_R32F, GL_RG32F, GL_RGB32F, GL_RGBA32F];
        if vb not in vals:
            vals[vb] = {'real':{}, 'imag':{}}
        try:
            irs = getReferenceRules(order, 2**sd-1)
            values = ngsolve.solve._GetValues(cf, self.mesh, vb, irs)
            vals = vals[vb]
            vals['min'] = values['min']
            vals['max'] = values['max']
            comps = ['real']
            if cf.is_complex: comps.append('imag')
            for comp in comps:
                for et in values[comp]:
                    if not et in vals[comp]:
                        vals[comp][et] = Texture(GL_TEXTURE_BUFFER, formats[cf.dim])
                    vals[comp][et].store(values[comp][et])
        except RuntimeError as e:
            assert("Local Heap" in str(e))
            self.setSubdivision(self.getSubdivision()-1)
            print("Localheap overflow, cannot increase subdivision!")

        return values


class MeshScene(BaseMeshScene):
    @inmain_decorator(wait_for_return=True)
    def __init__(self, mesh, wireframe=True, surface=True, elements=False, edgeElements=False, edges=False,
                 showPeriodic=False, pointNumbers=False, edgeNumbers=False, elementNumbers=False, **kwargs):
        self.__initial_values = { "ShowWireframe" : wireframe,
                                 "ShowSurface" : surface,
                                 "ShowElements" : elements,
                                 "ShowEdges" : edges,
                                 "ShowEdgeElements" : edgeElements,
                                 "ShowPeriodicVertices" : showPeriodic,
                                 "ShowPointNumbers" : pointNumbers,
                                 "ShowEdgeNumbers" : edgeNumbers,
                                 "ShowElementNumbers" : elementNumbers}
        self.tex_vol_colors = self.tex_surf_colors = self.tex_edge_colors = None
        super().__init__(mesh, **kwargs)

    @inmain_decorator(True)
    def _createParameters(self):
        super()._createParameters()
        self.addParameters("Show",
                           settings.CheckboxParameter(name="ShowWireframe", label="Show Wireframe",
                                                      default_value = self.__initial_values["ShowWireframe"]))
        if self.mesh.dim > 1:
            surf_values = self.mesh.GetBoundaries() if self.mesh.dim == 3 else self.mesh.GetMaterials()
            surf_color = settings.ColorParameter(name="SurfaceColors", values = surf_values,
                                                 default_value = (0,255,0,255))
            self.addParameters("Show",
                               settings.CheckboxParameterCluster(name="ShowSurface", label="Surface Elements",
                                                                 default_value = self.__initial_values["ShowSurface"],
                                                                 sub_parameters = [surf_color],
                                                                 updateWidgets=True))
        if self.mesh.dim > 2:
            shrink_par = settings.ValueParameter(name="Shrink", label="Shrink",
                                                 default_value=1.0, min_value = 0.0, max_value = 1.0,
                                                 step = 0.1)
            color_par = settings.ColorParameter(name="MaterialColors", values=self.mesh.GetMaterials())
            self.addParameters("Show",
                               settings.CheckboxParameterCluster(name="ShowElements",
                                                                 label="Volume Elements",
                                                                 default_value = self.__initial_values["ShowElements"],
                                                                 sub_parameters=[color_par,
                                                                                shrink_par],
                                                                 updateWidgets=True),
                               settings.CheckboxParameter(name="ShowEdges", label="Edges",
                                                          default_value=self.__initial_values["ShowEdges"]))
        if self.mesh.dim == 1:
            edge_names = self.mesh.GetMaterials()
        elif self.mesh.dim == 2:
            edge_names = self.mesh.GetBoundaries()
        else:
            edge_names = self.mesh.GetBBoundaries()
        edge_color = settings.ColorParameter(name="EdgeColors", default_value=(0,0,0,255),
                                             values = edge_names)
        self.addParameters("Show",
                           settings.CheckboxParameterCluster(name="ShowEdgeElements", label="Edge Elements",
                                                             default_value=self.__initial_values["ShowEdgeElements"],
                                                             sub_parameters = [edge_color],
                                                             updateWidgets=True),
                           settings.CheckboxParameter(name="ShowPeriodicVertices",
                                                      label="Periodic Identification",
                                                      default_value=self.__initial_values["ShowPeriodicVertices"]))
        self.addParameters("Numbers",
                           settings.CheckboxParameter(name="ShowPointNumbers",
                                                      label="Points",
                                                      default_value=self.__initial_values["ShowPointNumbers"]),
                           settings.CheckboxParameter(name="ShowEdgeNumbers",
                                                      label="Edges",
                                                      default_value=self.__initial_values["ShowEdgeNumbers"]))
        if self.mesh.dim > 1:
            self.addParameters("Numbers",
                               settings.CheckboxParameter(name="ShowElementNumbers",
                                                          label="Elements",
                                                          default_value=self.__initial_values["ShowElementNumbers"]))
        self.addParameters("",
                           settings.ValueParameter(name="GeomSubdivision", label="Subdivision",
                                                   default_value=5, min_value=1, max_value=20))
        self.addParameters("Save",
                           settings.Button(name="SaveMesh", label="Save Mesh"))

    @inmain_decorator(True)
    def _attachParameter(self, parameter):
        if parameter.name == "SurfaceColors":
            parameter.changed.connect(lambda : self.tex_surf_colors.store(self.getSurfaceColors(),
                                                                          data_format=GL_UNSIGNED_BYTE))
        if parameter.name == "MaterialColors":
            parameter.changed.connect(lambda : self.tex_vol_colors.store(self.getMaterialColors(),
                                                                         data_format=GL_UNSIGNED_BYTE))
        if parameter.name == "EdgeColors":
            parameter.changed.connect(lambda : self.tex_edge_colors.store(self.getEdgeColors(),
                                                                          data_format=GL_UNSIGNED_BYTE))
        if parameter.name == "SaveMesh":
            def saveMesh(val):
                filename, filt = QtWidgets.QFileDialog.getSaveFileName(caption="Save Mesh",
                                                                       filter="(*vol, *.vol.gz)")
                if not (filename.endswith(".vol") or filename.endswith(".vol.gz")):
                    filename += ".vol.gz"
                self.mesh.ngmesh.Save(filename)
            parameter.changed.connect(saveMesh)
        super()._attachParameter(parameter)

    def __getstate__(self):
        super_state = super().__getstate__()
        return (super_state,)

    def __setstate__(self, state):
        self.tex_vol_colors = self.tex_surf_colors = self.tex_edge_colors = None
        super().__setstate__(state[0])

    def initGL(self):
        super().initGL()
        with self._vao:
            self.tex_vol_colors = Texture(GL_TEXTURE_1D, GL_RGBA)
            if self.mesh.dim > 2:
                self.tex_vol_colors.store(self.getMaterialColors(), data_format=GL_UNSIGNED_BYTE)
            self.tex_surf_colors = Texture(GL_TEXTURE_1D, GL_RGBA)
            if self.mesh.dim > 1:
                self.tex_surf_colors.store(self.getSurfaceColors(), data_format=GL_UNSIGNED_BYTE)
            self.tex_edge_colors = Texture(GL_TEXTURE_1D, GL_RGBA)
            self.tex_edge_colors.store(self.getEdgeColors(), data_format=GL_UNSIGNED_BYTE)

            self.text_renderer = TextRenderer()


    def _render1DElements(self, settings, elements):
        if elements.curved:
            prog = getProgram('mesh.vert', 'mesh.tese', 'mesh.frag', elements=elements, params=settings)
        else:
            prog = getProgram('mesh.vert', 'mesh.frag', elements=elements, params=settings)
        uniforms = prog.uniforms

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)

        glActiveTexture(GL_TEXTURE1)
        elements.tex.bind()
        uniforms.set('mesh.elements', 1)

        glActiveTexture(GL_TEXTURE3)
        self.tex_edge_colors.bind()
        uniforms.set('colors', 3)

        uniforms.set('do_clipping', False);

        uniforms.set('mesh.dim', 1);
        uniforms.set('light_ambient', 1.0)
        uniforms.set('light_diffuse', 0.0)
        uniforms.set('TessLevel', self.getGeomSubdivision())
        uniforms.set('wireframe', True)
        tess_level = 10
        if settings.fastmode and len(elements.data)//elements.size>10**5:
            tess_level=1
        if elements.curved:
            glPatchParameteri(GL_PATCH_VERTICES, 2)
            glPatchParameterfv(GL_PATCH_DEFAULT_OUTER_LEVEL, [1,tess_level])
            glPatchParameterfv(GL_PATCH_DEFAULT_INNER_LEVEL, [1]*2)
            glDrawArrays(GL_PATCHES, 0, 2*len(elements.data)//elements.size)
        else:
            glDrawArrays(GL_LINES, 0, 2*len(elements.data)//elements.size)

    def renderEdges(self, settings):
        els = []


    def _render2DElements(self, settings, elements, wireframe):
        use_deformation = self.getDeformation()
        use_tessellation = elements.curved or use_deformation
        shader = ['mesh.vert', 'mesh.frag']
        options = {}
        if use_tessellation:
            shader.append('mesh.tese')
        if use_deformation:
            options["DEFORMATION_ORDER"] = self.getDeformationOrder()
        prog = getProgram(*shader, elements=elements, params=settings, DEFORMATION=use_deformation, **options)
        uniforms = prog.uniforms

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)

        glActiveTexture(GL_TEXTURE1)
        elements.tex.bind()
        uniforms.set('mesh.elements', 1)

        if use_deformation:
            glActiveTexture(GL_TEXTURE4)
            vb = ngsolve.VOL if self.mesh.dim==2 else ngsolve.BND
            self._deformation_values[vb]['real'][(elements.type, elements.curved)].bind()
            uniforms.set('deformation_coefficients', 4)
            uniforms.set('deformation_subdivision', 2**self.getDeformationSubdivision()-1)
            uniforms.set('deformation_order', self.getDeformationOrder())
            uniforms.set('deformation_scale', self.getDeformationScale())

        glActiveTexture(GL_TEXTURE3)
        self.tex_surf_colors.bind()
        uniforms.set('colors', 3)

        uniforms.set('do_clipping', True);

        uniforms.set('mesh.dim', 2);
        uniforms.set('wireframe', wireframe)

        if wireframe:
            offset_mode = GL_POLYGON_OFFSET_LINE
            polygon_mode = GL_LINE
            uniforms.set('light_ambient', 0.0)
            uniforms.set('light_diffuse', 0.0)
            offset = 0
        else:
            offset_mode = GL_POLYGON_OFFSET_FILL
            polygon_mode = GL_FILL
            offset = 2

        tess_level = 10
        if settings.fastmode and len(elements.data)//elements.size>10**5:
            tess_level=1

        glPolygonMode( GL_FRONT_AND_BACK, polygon_mode );
        glPolygonOffset (offset, offset)
        glEnable(offset_mode)
        if use_tessellation:
            glPatchParameteri(GL_PATCH_VERTICES, elements.nverts)
            glPatchParameterfv(GL_PATCH_DEFAULT_OUTER_LEVEL, [tess_level]*4)
            glPatchParameterfv(GL_PATCH_DEFAULT_INNER_LEVEL, [tess_level]*2)
            glDrawArrays(GL_PATCHES, 0, elements.nverts*len(elements.data)//elements.size)
        else:
            # triangles are the only uncurved 2d elements
            glDrawArrays(GL_TRIANGLES, 0, 3*len(elements.data)//elements.size)
        glDisable(offset_mode)

    def _render3DElements(self, settings, elements):
        use_deformation = self.getDeformation()
        shader = ['mesh.vert', 'mesh.frag']
        prog = getProgram(*shader, elements=elements, params=settings, DEFORMATION=0)

        uniforms = prog.uniforms

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)

        glActiveTexture(GL_TEXTURE1)
        elements.tex.bind()
        uniforms.set('mesh.elements', 1)

        uniforms.set('do_clipping', True);
        uniforms.set('shrink_elements', self.getShrink())
        uniforms.set('clip_whole_elements', True)

        glActiveTexture(GL_TEXTURE3)
        self.tex_vol_colors.bind()
        uniforms.set('colors', 3)

        uniforms.set('light_ambient', 0.3)
        uniforms.set('light_diffuse', 0.7)
        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )
        # todo: number of vertices per element, number of instances
        glDrawArraysInstanced(GL_TRIANGLES, 0, 3*self.mesh.ne, 4)

    def _renderNumbers(self, settings, elements):
        prog = getProgram('pass_through.vert', 'numbers.geom', 'font.frag', params=settings, elements=elements, USE_GL_VERTEX_ID=True)
        uniforms = prog.uniforms

        viewport = glGetIntegerv( GL_VIEWPORT )
        screen_width = viewport[2]-viewport[0]
        screen_height = viewport[3]-viewport[1]

        font_size = 0
        if not font_size in self.text_renderer.fonts:
            self.text_renderer.addFont(font_size)
        font = self.text_renderer.fonts[font_size]

        glActiveTexture(GL_TEXTURE2)
        font.tex.bind()
        uniforms.set('font', 2)

        uniforms.set('font_width_in_texture', font.width/font.tex_width)
        uniforms.set('font_height_in_texture', font.height/font.tex_height)
        uniforms.set('font_width_on_screen', 2*font.width/screen_width)
        uniforms.set('font_height_on_screen', 2*font.height/screen_height)

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)

        if elements.dim>0:
            glActiveTexture(GL_TEXTURE1)
            elements.tex.bind()
            uniforms.set('mesh.elements', 1)

        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )
        glPolygonOffset (0,0)
        glDrawArrays(GL_POINTS, 0, elements.nelements)

    @inmain_decorator(True)
    def update(self):
        super().update()

    def render(self, settings):
        if not self.active:
            return
        with self._vao:
            vbs = [ngsolve.VOL, ngsolve.BND, ngsolve.BBND, ngsolve.BBBND]
            dim = self.mesh.dim
            # 1D elements
            if self.mesh.dim > 2 and self.getShowEdges():
                for els in self.mesh_data.elements["edges"]:
                    self._render1DElements(settings, els);
            if self.getShowEdgeElements():
                vb = vbs[dim-1]
                for els in self.mesh_data.elements[vb]:
                    if vb in [ngsolve.BBND, ngsolve.BND]:
                        # glLineWidth(3) # TODO: replace with manually drawing quads (linewidth is not supported for OpenGL3.2
                        self._render1DElements(settings, els);
                        # glLineWidth(1)

            if self.getShowPeriodicVertices():
                for els in self.mesh_data.elements["periodic"]:
                    self._render1DElements(settings, els);

            # 2D elements
            if self.mesh.dim > 1:
                vb = vbs[dim-2]
                for els in self.mesh_data.elements[vb]:
                    if self.getShowSurface():
                        self._render2DElements(settings, els, False);
                    if self.getShowWireframe():
                        self._render2DElements(settings, els, True);

            # 3D elements
            if self.mesh.dim == 3 and self.getShowElements():
                for elements in self.mesh_data.elements[ngsolve.VOL]:
                    self._render3DElements(settings, elements)

            # Numbers
            if self.getShowPointNumbers():
                vb = vbs[ self.mesh.dim ]
                for elements in self.mesh_data.elements[vb]:
                    self._renderNumbers(settings, elements)

            if self.getShowEdgeNumbers():
                vb = vbs[self.mesh.dim-1]
                for elements in self.mesh_data.elements[vb]:
                    self._renderNumbers(settings, elements)

            if self.mesh.dim > 1 and self.getShowElementNumbers():
                for elements in self.mesh_data.elements[ngsolve.VOL]:
                    self._renderNumbers(settings, elements)

    @inmain_decorator(True)
    def _createQtWidget(self):
        super()._createQtWidget()

GUI.sceneCreators[ngsolve.Mesh] = MeshScene

class SolutionScene(BaseMeshScene):
    _complex_eval_funcs = {"real" : 0,
                           "imag" : 1,
                           "abs" : 2,
                           "arg" : 3}
    @inmain_decorator(wait_for_return=True)
    def __init__(self, cf, mesh, name=None, min=0.0,max=1.0, autoscale=True, linear=False, clippingPlane=True,
                 order=2, gradient=None, iso_surface=None, *args, **kwargs):
        self.cf = cf
        self.iso_surface = iso_surface or cf
        self.values = {}
        self.iso_values = {}
        self.__initial_values = {"Order" : order,
                                 "ColorMapMin" : float(min),
                                 "ColorMapMax" : float(max),
                                 "Autoscale" : autoscale,
                                 "ColorMapLinear" : linear,
                                 "ShowClippingPlane" : clippingPlane,
                                 "Subdivision" : kwargs['sd'] if "sd" in kwargs else 1,
                                 "ShowIsoSurface" : False,
                                 "ShowVectors" : False,
                                 "ShowSurface" : True}

        if hasattr(self.cf,"vecs") and len(self.cf.vecs) > 1:
            self._gfComponents = self.cf
            self.cf = ngsolve.GridFunction(self._gfComponents.space)
            self.cf.vec.data = self._gfComponents.vecs[0]
        else:
            self._gfComponents = False
        if gradient and cf.dim == 1:
            self.cf = ngsolve.CoefficientFunction((cf, gradient))
            self.have_gradient = True
        else:
            self.have_gradient = False
        if not 'deformation' in kwargs:
            if mesh.dim==1 and cf.dim==1:
                kwargs['deformation'] = ngsolve.CoefficientFunction((0,cf,0))
            elif mesh.dim==2 and cf.dim==1:
                kwargs['deformation'] = ngsolve.CoefficientFunction((0,0,cf))

        if 'draw_surf' in kwargs:
            self.__initial_values["ShowSurface"] = kwargs.pop('draw_surf')

        super().__init__(mesh,*args, name=name, **kwargs)


    @inmain_decorator(True)
    def _createParameters(self):
        super()._createParameters()
        self.addParameters("Subdivision",
                           settings.ValueParameter(name="Subdivision",
                                                   label="Subdivision",
                                                   default_value=int(self.__initial_values["Subdivision"]),
                                                   min_value = 0,
                                                   updateScene=True),
                           settings.ValueParameter(name="Order",
                                                   label="Order",
                                                   default_value=int(self.__initial_values["Order"]),
                                                   min_value=1,
                                                   max_value=4,
                                                   updateScene=True))
        if self.mesh.dim>1:
            self.addParameters("Show",
                               settings.CheckboxParameter(name="ShowSurface",
                                                          label="Solution on Surface",
                                                          default_value=self.__initial_values["ShowSurface"]))

        if self.mesh.dim > 2:
            iso_value = settings.ValueParameter(name="IsoValue", label="Value", default_value=0.0)
            self.addParameters("Show",
                               settings.CheckboxParameter(name="ShowClippingPlane",
                                                          label="Solution in clipping plane",
                                                          default_value=self.__initial_values["ShowClippingPlane"]),
                               settings.CheckboxParameterCluster(name="ShowIsoSurface",
                                                          label="Isosurface",
                                                          default_value = self.__initial_values["ShowIsoSurface"],
                                                             sub_parameters = [iso_value], updateWidgets=True)
                               )

        if self.cf.dim > 1:
            self.addParameters("Show",
                               settings.ValueParameter(name="Component", label="Component",
                                                       default_value=0,
                                                       min_value=0,
                                                       max_value=self.cf.dim-1),
                               settings.CheckboxParameter(name="ShowVectors", label="Vectors",
                                                          default_value=self.__initial_values["ShowVectors"]))

        if self.cf.is_complex:
            self.addParameters("Complex",
                               settings.SingleOptionParameter(name="ComplexEvalFunc",
                                                              values = list(self._complex_eval_funcs.keys()),
                                                              label="Func",
                                                              default_value = "real"),
                               settings.ValueParameter(name="ComplexPhaseShift",
                                                      label="Value shift angle",
                                                       default_value = 0.0),
                               settings.CheckboxParameter(name="Animate", label="Animate",
                                                          default_value=False))

        self.addParameters("Colormap",
                           settings.ValueParameter(name = "ColorMapMin",
                                         label = "Min",
                                         default_value = self.__initial_values["ColorMapMin"]),
                           settings.ValueParameter(name= "ColorMapMax",
                                         label = "Max",
                                         default_value = self.__initial_values["ColorMapMax"]),
                           settings.CheckboxParameter(name="Autoscale",
                                               label="Autoscale",
                                               default_value = self.__initial_values["Autoscale"]),
                           settings.CheckboxParameter(name="ColorMapLinear",
                                                      label="Linear",
                                                      default_value=self.__initial_values["ColorMapLinear"]))
        if self._gfComponents:
            self.addParameters("Components", settings.ValueParameter(label = "Multidim",
                                                 default_value = 0,
                                                 max_value = len(self._gfComponents.vecs)-1,
                                                 min_value = 0,
                                                 updateScene = True))

    def _animate(self,val):
        if val:
            self._timer_thread = QtCore.QThread()
            def run_animate():
                self._animation_timer = QtCore.QTimer()
                self._animation_timer.setInterval(20)
                self._animation_timer.timeout.connect(lambda : self.setComplexPhaseShift(self.getComplexPhaseShift()-10))
                self._animation_timer.start()
            def stop_animate():
                self._animation_timer.stop()
            self._timer_thread.started.connect(run_animate)
            self._timer_thread.finished.connect(stop_animate)
            self._timer_thread.start()
        else:
            self._timer_thread.finished.emit()
            self._timer_thread.quit()

    @inmain_decorator(True)
    def _attachParameter(self, parameter):
        if parameter.name == "Animate":
            parameter.changed.connect(self._animate)
        if parameter.name == "ColorMapMin" or parameter.name == "ColorMapMax":
            parameter.changed.connect(lambda val: self.setAutoscale(False))
        if parameter.name == "Multidim":
            parameter.changed.connect(lambda val: setattr(self.cf.vec, "data", self._gfComponents.vecs[val]))
        super()._attachParameter(parameter)

    def __getstate__(self):
        super_state = super().__getstate__()
        return (super_state,self.cf, self.iso_surface)

    def __setstate__(self,state):
        self.cf = state[1]
        self.iso_surface = state[2]
        self.values = {}
        self.iso_values = {}
        super().__setstate__(state[0])

    def initGL(self):
        super().initGL()

        formats = [None, GL_R32F, GL_RG32F, GL_RGB32F, GL_RGBA32F];

        self.filter_buffer = ArrayBuffer()
        self.filter_buffer.bind()
        glBufferData(GL_ARRAY_BUFFER, 1000000, ctypes.c_void_p(), GL_STATIC_DRAW)


    @inmain_decorator(True)
    def update(self):
        super().update()
        self._getValues(self.cf, ngsolve.VOL, self.getSubdivision(), self.getOrder(), self.values)
        if self.mesh.dim==3:
            try:
                self._getValues(self.cf, ngsolve.BND, self.getSubdivision(), self.getOrder(), self.values)
            except Exception as e:
                print("Cannot evaluate given function on surface elements"+str(e))
        if self.iso_surface is self.cf:
            self.iso_values = self.values
        else:
            self._getValues(self.iso_surface, ngsolve.VOL, self.getSubdivision(), self.getOrder(), self.iso_values)


    def _filterElements(self, settings, elements, filter_type):
        glEnable(GL_RASTERIZER_DISCARD)
        prog = getProgram('pass_through.vert', 'filter_elements.geom', feedback=['element'], ORDER=self.getOrder(), params=settings, elements=elements, USE_GL_VERTEX_ID=True)
        uniforms = prog.uniforms

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)
        uniforms.set('mesh.dim', 3);

        glActiveTexture(GL_TEXTURE1)
        elements.tex.bind()
        uniforms.set('mesh.elements', 1)

        glActiveTexture(GL_TEXTURE2)
        if filter_type == 1: # iso surface
            uniforms.set('iso_value', self.getIsoValue())
            self.iso_values[ngsolve.VOL]['real'][elements.type, elements.curved].bind()

        uniforms.set('coefficients', 2)
        uniforms.set('subdivision', 2**self.getSubdivision()-1)
        if self.cf.dim > 1:
            uniforms.set('component', self.getComponent())
        else:
            uniforms.set('component', 0)

        uniforms.set('filter_type', filter_type)

        self.filter_feedback = glGenTransformFeedbacks(1)
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, self.filter_feedback)
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, self.filter_buffer.id)
        glBeginTransformFeedback(GL_POINTS)

        glDrawArrays(GL_POINTS, 0, self.mesh.ne)

        glEndTransformFeedback()
        glDisable(GL_RASTERIZER_DISCARD)

    def _render1D(self, settings, elements):
        # use actual function values for deformation on 1d meshes
        use_deformation = self.getDeformation()
        vb = ngsolve.VOL

        if self.cf.dim > 1:
            comp = self.getComponent()
        else:
            comp = 0

        if self.getAutoscale():
            settings.colormap_min = self.values[vb]['min'][comp]
            settings.colormap_max = self.values[vb]['max'][comp]

        use_tessellation = use_deformation or elements.curved
        options = dict(ORDER=self.getOrder(), DEFORMATION=use_deformation)

        shader = ['mesh.vert', 'solution.frag']
        if use_tessellation:
            shader.append('mesh.tese')
        if use_deformation:
            options["DEFORMATION_ORDER"] = self.getDeformationOrder()

        prog = getProgram(*shader, elements=elements, params=settings, **options)
        uniforms = prog.uniforms

        uniforms.set('wireframe', False)
        uniforms.set('do_clipping', False)
        uniforms.set('subdivision', 2**self.getSubdivision()-1)

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)

        glActiveTexture(GL_TEXTURE1)
        elements.tex.bind()
        uniforms.set('mesh.elements', 1)

        glActiveTexture(GL_TEXTURE2)
        self.values[vb]['real'][(elements.type, elements.curved)].bind()
        uniforms.set('coefficients', 2)

        if use_deformation:
            glActiveTexture(GL_TEXTURE4)
            self._deformation_values[vb]['real'][(elements.type, elements.curved)].bind()
            uniforms.set('deformation_coefficients', 4)
            uniforms.set('deformation_subdivision', 2**self.getDeformationSubdivision()-1)
            uniforms.set('deformation_order', self.getDeformationOrder())
            uniforms.set('deformation_scale', self.getDeformationScale())


        uniforms.set('component', comp)

        uniforms.set('is_complex', self.cf.is_complex)
        if self.cf.is_complex:
            glActiveTexture(GL_TEXTURE3)
            self.values[vb]['imag'][elements.type, elements.curved].bind()
            uniforms.set('coefficients_imag', 3)

            uniforms.set('complex_vis_function', self._complex_eval_funcs[self.getComplexEvalFunc()])
            w = cmath.exp(1j*self.getComplexPhaseShift()/180.0*math.pi)
            uniforms.set('complex_factor', [w.real, w.imag])

        tess_level = 10
        if settings.fastmode and len(elements.data)//elements.size>10**5:
            tess_level=1

        uniforms.set('light_ambient', 0.3)
        uniforms.set('light_diffuse', 0.7)
        nverts = elements.nverts
        nelements = elements.nelements
        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL );
        if use_tessellation:
            glPatchParameteri(GL_PATCH_VERTICES, nverts)
            glPatchParameterfv(GL_PATCH_DEFAULT_OUTER_LEVEL, [tess_level]*4)
            glPatchParameterfv(GL_PATCH_DEFAULT_INNER_LEVEL, [tess_level]*2)
            glDrawArrays(GL_PATCHES, 0, nverts*nelements)
        else:
            glDrawArrays(GL_LINES, 0, nverts*nelements)

    def renderSurface(self, settings):
        vb = ngsolve.VOL if self.mesh.dim==2 else ngsolve.BND
        use_deformation = self.getDeformation()

        if self.cf.dim > 1:
            comp = self.getComponent()
        else:
            comp = 0

        if self.getAutoscale():
            settings.colormap_min = self.values[vb]['min'][comp]
            settings.colormap_max = self.values[vb]['max'][comp]

        for elements in self.mesh_data.elements[vb]:
            shader = ['mesh.vert', 'solution.frag']
            use_tessellation = use_deformation or elements.curved
            options = dict(ORDER=self.getOrder(), DEFORMATION=use_deformation)
            if use_tessellation:
                shader.append('mesh.tese')
            if use_deformation:
                options["DEFORMATION_ORDER"] = self.getDeformationOrder()

            prog = getProgram(*shader, elements=elements, params=settings, **options)
            uniforms = prog.uniforms

            if use_deformation:
                glActiveTexture(GL_TEXTURE4)
                self._deformation_values[vb]['real'][(elements.type, elements.curved)].bind()
                uniforms.set('deformation_coefficients', 4)
                uniforms.set('deformation_subdivision', 2**self.getDeformationSubdivision()-1)
                uniforms.set('deformation_order', self.getDeformationOrder())
                uniforms.set('deformation_scale', self.getDeformationScale())


            uniforms.set('wireframe', False)
            uniforms.set('do_clipping', self.mesh.dim==3 or use_deformation)
            uniforms.set('subdivision', 2**self.getSubdivision()-1)

            glActiveTexture(GL_TEXTURE0)
            elements.tex_vertices.bind()
            uniforms.set('mesh.vertices', 0)

            glActiveTexture(GL_TEXTURE1)
            elements.tex.bind()
            uniforms.set('mesh.elements', 1)

            glActiveTexture(GL_TEXTURE2)
            self.values[vb]['real'][(elements.type, elements.curved)].bind()
            uniforms.set('coefficients', 2)

            uniforms.set('component', comp)

            uniforms.set('is_complex', self.cf.is_complex)
            if self.cf.is_complex:
                glActiveTexture(GL_TEXTURE3)
                self.values[vb]['imag'][elements.type, elements.curved].bind()
                uniforms.set('coefficients_imag', 3)

                uniforms.set('complex_vis_function', self._complex_eval_funcs[self.getComplexEvalFunc()])
                w = cmath.exp(1j*self.getComplexPhaseShift()/180.0*math.pi)
                uniforms.set('complex_factor', [w.real, w.imag])

            tess_level = 10
            if settings.fastmode and len(elements.data)//elements.size>10**5:
                tess_level=1

            glPolygonMode( GL_FRONT_AND_BACK, GL_FILL );
            if use_tessellation:
                glPatchParameteri(GL_PATCH_VERTICES, elements.nverts)
                glPatchParameterfv(GL_PATCH_DEFAULT_OUTER_LEVEL, [tess_level]*4)
                glPatchParameterfv(GL_PATCH_DEFAULT_INNER_LEVEL, [tess_level]*2)
                glDrawArrays(GL_PATCHES, 0, elements.nverts*len(elements.data)//elements.size)
            else:
                glDrawArrays(GL_TRIANGLES, 0, 3*len(elements.data)//elements.size)

    def _renderIsoSurface(self, settings, elements):
        self._filterElements(settings, elements, 1)
        model, view, projection = settings.model, settings.view, settings.projection
        prog = getProgram('pass_through.vert', 'isosurface.geom', 'solution.frag', elements=elements, ORDER=self.getOrder(), params=settings)

        uniforms = prog.uniforms
        uniforms.set('P',projection)
        uniforms.set('MV',view*model)
        uniforms.set('iso_value', self.getIsoValue())
        uniforms.set('have_gradient', self.have_gradient)
        uniforms.set('do_clipping', True);
        uniforms.set('subdivision', 2**self.getSubdivision()-1)
        uniforms.set('order', self.getOrder())
        if self.cf.dim > 1:
            uniforms.set('component', self.getComponent())
        else:
            uniforms.set('component', 0)

        if(self.mesh.dim==2):
            uniforms.set('element_type', 10)
        if(self.mesh.dim==3):
            uniforms.set('element_type', 20)

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)

        glActiveTexture(GL_TEXTURE1)
        elements.tex.bind()
        uniforms.set('mesh.elements', 1)

        glActiveTexture(GL_TEXTURE2)
        self.values[ngsolve.VOL]['real'][(elements.type, elements.curved)].bind()
        uniforms.set('coefficients', 2)

        glActiveTexture(GL_TEXTURE3)
        self.iso_values[ngsolve.VOL]['real'][(elements.type, elements.curved)].bind()
        uniforms.set('coefficients_iso', 3)

        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL );
        instances = (self.getOrder()*(2**self.getSubdivision()))**3
        prog.attributes.bind('element', self.filter_buffer)
        for inst in range(instances):
            uniforms.set('instance', inst)
            glDrawTransformFeedback(GL_POINTS, self.filter_feedback)

    # TODO: implement (surface or clipping plane) vector rendering
    def renderVectors(self, settings):
        print('rendering vectors not implemented')
        return
#         model, view, projection = settings.model, settings.view, settings.projection
#         prog = getProgram('mesh.vert', 'vector.geom', 'solution.frag', ORDER=self.getOrder())
# 
#         uniforms = prog.uniforms
#         uniforms.set('P',projection)
#         uniforms.set('MV',view*model)
#         uniforms.set('colormap_min', 1e99)
#         uniforms.set('colormap_max', -1e99)
#         uniforms.set('colormap_linear', settings.colormap_linear)
#         uniforms.set('clipping_plane', settings.clipping_plane)
#         uniforms.set('do_clipping', True);
#         uniforms.set('subdivision', 2**self.getSubdivision()-1)
# 
#         if(self.mesh.dim==2):
#             uniforms.set('element_type', 10)
#         if(self.mesh.dim==3):
#             uniforms.set('element_type', 20)
# 
#         glActiveTexture(GL_TEXTURE0)
#         elements.tex_vertices.bind()
#         uniforms.set('mesh.vertices', 0)
# 
#         glActiveTexture(GL_TEXTURE1)
#         self.mesh_data.elements.bind()
#         uniforms.set('mesh.elements', 1)
# 
#         glActiveTexture(GL_TEXTURE2)
#         self.volume_values.bind()
#         uniforms.set('coefficients', 2)
# 
#         uniforms.set('mesh.surface_curved_offset', self.mesh.nv)
#         uniforms.set('mesh.volume_elements_offset', self.mesh_data.volume_elements_offset)
# 
#         glPolygonMode( GL_FRONT_AND_BACK, GL_FILL );
#         glDrawArrays(GL_POINTS, 0, self.mesh.ne)

    def _renderClippingPlane(self, settings, elements):
        self._filterElements(settings, elements, 0)
        model, view, projection = settings.model, settings.view, settings.projection
        prog = getProgram('pass_through.vert', 'clipping.geom', 'solution.frag', elements=elements, ORDER=self.getOrder(), params=settings)

        uniforms = prog.uniforms
        uniforms.set('P',projection)
        uniforms.set('MV',view*model)
        uniforms.set('clipping_plane_deformation', False)
        uniforms.set('do_clipping', False);
        uniforms.set('subdivision', 2**self.getSubdivision()-1)
        if self.cf.dim > 1:
            uniforms.set('component', self.getComponent())
        else:
            uniforms.set('component', 0)

        if(self.mesh.dim==2):
            uniforms.set('element_type', 10)
        if(self.mesh.dim==3):
            uniforms.set('element_type', 20)

        glActiveTexture(GL_TEXTURE0)
        elements.tex_vertices.bind()
        uniforms.set('mesh.vertices', 0)

        glActiveTexture(GL_TEXTURE1)
        elements.tex.bind()
        uniforms.set('mesh.elements', 1)

        glActiveTexture(GL_TEXTURE2)
        self.values[ngsolve.VOL]['real'][elements.type, elements.curved].bind()
        uniforms.set('coefficients', 2)

        uniforms.set('is_complex', self.cf.is_complex)
        if self.cf.is_complex:
            glActiveTexture(GL_TEXTURE3)
            self.values[ngsolve.VOL]['imag'][elements.type, elements.curved].bind()
            uniforms.set('coefficients_imag', 3)

            uniforms.set('complex_vis_function', self._complex_eval_funcs[self.getComplexEvalFunc()])
            w = cmath.exp(1j*self.getComplexPhaseShift()/180.0*math.pi)
            uniforms.set('complex_factor', [w.real, w.imag])


        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL );
        prog.attributes.bind('element', self.filter_buffer)
        glDrawTransformFeedback(GL_POINTS, self.filter_feedback)


    def render(self, settings):
        if not self.active:
            return

        with self._vao:
            if self.getAutoscale():
                comp = 0 if self.cf.dim==1 else self.getComponent()
                settings.colormap_min = self.values[ngsolve.VOL]['min'][comp]
                settings.colormap_max = self.values[ngsolve.VOL]['max'][comp]
            else:
                settings.colormap_min = self.getColorMapMin()
                settings.colormap_max = self.getColorMapMax()
            settings.colormap_linear = self.getColorMapLinear()

            if self.mesh.dim==1:
                for els in self.mesh_data.elements[ngsolve.VOL]:
                    self._render1D(settings, els)

            if self.mesh.dim > 1:
                if self.getShowSurface():
                    self.renderSurface(settings)

            if self.mesh.dim > 2:
                if self.getShowIsoSurface():
                    for els in self.mesh_data.elements[ngsolve.VOL]:
                        self._renderIsoSurface(settings, els)
                if self.getShowClippingPlane():
                    for els in self.mesh_data.elements[ngsolve.VOL]:
                        self._renderClippingPlane(settings, els)

            if self.cf.dim > 1:
                if self.getShowVectors():
                    self.renderVectors(settings)

def _createCFScene(cf, mesh, *args, **kwargs):
    return SolutionScene(cf, mesh, *args,
                         autoscale = kwargs["autoscale"] if "autoscale" in kwargs else not ("min" in kwargs or "max" in kwargs),
                         **kwargs)

def _createGFScene(gf, mesh=None, name=None, *args, **kwargs):
    if not mesh:
        mesh = gf.space.mesh
    if not name:
        name = gf.name
    return _createCFScene(gf,mesh,*args, name=name, **kwargs)

GUI.sceneCreators[ngsolve.GridFunction] =  _createGFScene
GUI.sceneCreators[ngsolve.CoefficientFunction] =  _createCFScene

class GeometryScene(BaseScene):
    def __init__(self, geo, *args, **kwargs):
        self.geo = geo
        self._geo_data = getOpenGLData(self.geo)
        super().__init__(*args,**kwargs)

    @inmain_decorator(wait_for_return=True)
    def initGL(self):
        super().initGL()
        self._geo_data.initGL()
        self._tex_colors = Texture(GL_TEXTURE_1D, GL_RGBA)

    @inmain_decorator(True)
    def update(self):
        super().update()
        self._geo_data.update()
        self._tex_colors.store(self.getSurfaceColors(), data_format=GL_UNSIGNED_BYTE)

    def __getstate__(self):
        return (super().__getstate__(), self.geo)

    def __setstate__(self,state):
        self.geo = state[1]
        self._geo_data = getOpenGLData(self.geo)
        super().__setstate__(self,state[0])

    @inmain_decorator(True)
    def _createParameters(self):
        super()._createParameters()
        self.addParameters("Mesh Generation",
                           settings.ValueParameter(label="Meshsize",
                                                   name="Meshsize",
                                                   default_value=0.2),
                           settings.SingleOptionParameter(label="Meshtype",
                                                          name="Meshtype",
                                                          values=["Volume Mesh", "Surface Mesh"]),
                           settings.Button(label="Generate Mesh",
                                           name="CreateMesh"))
        self.addParameters("Surface Colors",settings.ColorParameter(name="SurfaceColors",
                                                                    values=list(self._geo_data.surfnames)))

    def _attachParameter(self, parameter):
        if parameter.name == "SurfaceColors":
            parameter.changed.connect(lambda : self._tex_colors.store(self.getSurfaceColors(),
                                                                      data_format=GL_UNSIGNED_BYTE))
        if parameter.name == "CreateMesh":
            def genMesh(val):
                import netgen.meshing as meshing
                mesh = self.geo.GenerateMesh(maxh=self.getMeshsize(),
                                             perfstepsend = meshing.MeshingStep.MESHSURFACE if self.getMeshtype() == "Surface Mesh" else meshing.MeshingStep.MESHVOLUME)
                ngsolve.Draw(ngsolve.Mesh(mesh))
            parameter.changed.connect(genMesh)
        super()._attachParameter(parameter)

    def getBoundingBox(self):
        return self._geo_data.min, self._geo_data.max

    def render(self, settings):
        if not self.active:
            return
        with self._vao:
            prog = getProgram('geo.vert', 'geo.frag')
            model, view, projection = settings.model, settings.view, settings.projection
            uniforms = prog.uniforms
            uniforms.set('P', projection)
            uniforms.set('MV', view*model)

            glActiveTexture(GL_TEXTURE0)
            self._geo_data.vertices.bind()
            uniforms.set('vertices', 0)

            glActiveTexture(GL_TEXTURE1)
            self._geo_data.triangles.bind()
            uniforms.set('triangles',1)

            glActiveTexture(GL_TEXTURE2)
            self._geo_data.normals.bind()
            uniforms.set('normals',2)

            glActiveTexture(GL_TEXTURE3)
            self._tex_colors.bind()
            uniforms.set('colors',3)

            uniforms.set('wireframe',False)
            uniforms.set('clipping_plane', settings.clipping_plane)
            uniforms.set('do_clipping', True)
            uniforms.set('light_ambient', 0.3)
            uniforms.set('light_diffuse', 0.7)
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL )
            glDrawArrays(GL_TRIANGLES, 0, self._geo_data.npoints)

class GeometryScene2D(BaseScene):
    def __init__(self, geo, *args, **kwargs):
        self.geo = geo
        data = self.geo._visualizationData()
        self._vertices = data["vertices"]
        self._domains = data["domains"]
        self._xmin = data["min"]
        self._xmax = data["max"]
        self._bcnames = data["bcnames"]
        self._segdata = data["segment_data"]
        super().__init__(*args, **kwargs)

    @inmain_decorator(True)
    def initGL(self):
        super().initGL()
        self.window.glWidget._rotation_enabled = False
        self.vertices = ArrayBuffer()
        self.domains = ArrayBuffer()
        self._tex_bc_colors = Texture(GL_TEXTURE_1D, GL_RGBA)
        self._tex_bc_colors.store(self.getBoundaryColors(), data_format=GL_UNSIGNED_BYTE)
        self._text_renderer = TextRenderer()

    @inmain_decorator(True)
    def update(self):
        super().update()
        self._nverts = len(self._vertices)//3
        self.vertices.store(numpy.array(self._vertices, dtype=numpy.float32))
        self.domains.store(numpy.array(self._domains, dtype=numpy.int32))

    @inmain_decorator(True)
    def _createParameters(self):
        super()._createParameters()
        self.addParameters("Boundary Colors", settings.ColorParameter(name="BoundaryColors", values=self._bcnames,
                                           default_value=(0,0,0,255)))
        self.addParameters("Show",
                           settings.CheckboxParameter(name="ShowPointNumbers",
                                                      label="Point Numbers",
                                                      default_value=True),
                           settings.CheckboxParameter(name="ShowDomainNumbers",
                                                      label="Domain Numbers",
                                                      default_value = False))

    def _attachParameter(self, parameter):
        if parameter.name == "BoundaryColors":
            parameter.changed.connect(lambda : self._tex_bc_colors.store(self.getBoundaryColors(),
                                                                         data_format=GL_UNSIGNED_BYTE))
        super()._attachParameter(parameter)

    def getBoundingBox(self):
        return (self._xmin, self._xmax)

    def render(self, settings):
        if not self.active:
            return
        with self._vao:
            self.__renderGeometry(settings)
            self.__renderNumbers(settings)

    def __renderNumbers(self, settings):
        import numpy
        mat = settings.model * settings.view * settings.projection
        eps = 0.1 * numpy.sqrt(numpy.sqrt(abs(1./numpy.linalg.det(mat))))
        if self.getShowPointNumbers():
            xpoints, ypoints, pointindex = self.geo.PointData()
            #offset
            for x,y,index in zip(xpoints, ypoints, pointindex):
                self._text_renderer.draw(settings, str(index), [x+0.1*eps,y-0.1*eps,0], use_absolute_pos=False)
        if self.getShowDomainNumbers():
            for pnt, normal, dom in zip(self._segdata["midpoints"], self._segdata["normals"],
                                        self._segdata["leftdom"]):
                self._text_renderer.draw(settings, str(dom), [pnt[0]-eps*normal[0],
                                                              pnt[1]-eps*normal[1], 0], use_absolute_pos=False)
            for pnt, normal, dom in zip(self._segdata["midpoints"], self._segdata["normals"],
                                        self._segdata["rightdom"]):
                self._text_renderer.draw(settings, str(dom), [pnt[0]+eps*normal[0],
                                                              pnt[1]+eps*normal[1], 0], use_absolute_pos=False)

    def __renderGeometry(self, settings):
        prog = getProgram('geom2d.vert', 'geo.frag')
        model,view,projection = settings.model, settings.view, settings.projection
        uniforms = prog.uniforms
        uniforms.set('P',projection)
        uniforms.set('MV',view*model)

        glActiveTexture(GL_TEXTURE0)
        self._tex_bc_colors.bind()
        uniforms.set('colors', 0)

        prog.attributes.bind('pos', self.vertices)
        prog.attributes.bind('domain', self.domains)

        uniforms.set('do_clipping', False)
        uniforms.set('light_ambient', 1)
        uniforms.set('light_diffuse',0)

        # glLineWidth(3) TODO: replace with manually drawing quads (linewidth is not supported for OpenGL3.2
        glDrawArrays(GL_LINES, 0, self._nverts)
        # glLineWidth(1)

GUI.sceneCreators[netgen.geom2d.SplineGeometry] = GeometryScene2D
GUI.sceneCreators[netgen.meshing.NetgenGeometry] = GeometryScene


def _load_gz_mesh(gui, filename):
    if os.path.splitext(os.path.splitext(filename)[0])[1] == ".vol":
        ngsolve.Draw(ngsolve.Mesh(filename))
    else:
        print("Do not know file extension for ", filename)

GUI.file_loaders[".gz"] = _load_gz_mesh
GUI.file_loaders[".vol"] = lambda gui, filename: ngsolve.Draw(ngsolve.Mesh(filename))
