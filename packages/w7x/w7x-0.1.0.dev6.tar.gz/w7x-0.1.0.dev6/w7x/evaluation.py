import tfields
import w7x
import joblib
import pathlib
import re
import numpy as np
from scipy.stats import poisson

memory = joblib.Memory(cachedir='/tmp/joblib')

@memory.cache
def upper_half(mm_id):
    from sympy.abc import z
    return w7x.flt.MeshedModel.from_mm_id(mm_id).as_Mesh3D().cut(z>0)


@memory.cache
def divertor_upper_tile_template():
    template_path = pathlib.Path(w7x.Defaults.Paths.divertor_upper_tiles_template_path)
    def natural_sort(l): 
        """
        Helper method for natural sorting
        """
        convert = lambda text: int(text) if text.isdigit() else text.lower() 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', str(key)) ] 
        return sorted(l, key = alphanum_key)
    
    tile_templates = []
    for path in natural_sort(template_path.iterdir()):
        template = tfields.Mesh3D.load(path)
        # fill the area cache:
        template.triangles().areas()
        tile_templates.append(template)
    return tile_templates


@memory.cache
def divertor_upper_tile_template_areas():
    areas = [t.triangles().areas().sum()
             for t in divertor_upper_tile_template()]
    return areas


@memory.cache
def max_design_loads():
    """
    Specifying max_loads
    """
    areas = divertor_upper_tile_template_areas()
    max_loads = np.full((3277,), w7x.Defaults.Overload.maxLoadCooled)
    max_loads[areas == 0] = 0
    max_loads = max_loads.reshape((-1, 29))  # fingers
    max_loads[:30, 2] = w7x.Defaults.Overload.maxLoadPumpingGapDach
    max_loads[:30, :2] = w7x.Defaults.Overload.maxLoadPumpingGapStirn
    max_loads[30:54, :][max_loads[30:54, :] != 0] = w7x.Defaults.Overload.maxLoadSagged
    max_loads[84:, 2] = w7x.Defaults.Overload.maxLoadPumpingGapDach
    max_loads[84:, :2] = w7x.Defaults.Overload.maxLoadPumpingGapStirn
    max_loads = np.array(max_loads.flat)  # undo reshape
    return max_loads


class TracerEvaluation(w7x.flt.ConnectionLength):
    def hits_upper_divertor(self, upper_divertor_mesh=None):
        """
        Rather special method for retrieving the hits onto upper divertor
        (mm_id = 165).
        Get all hits onto the divertor and map them onto the upper divertor of module 1
        Notes:
            This method could be expanded to make it more general.
            It is ensured however, that only the correct case can be conducted.
        Args:
            upper_divertor_mesh(tfields.Mesh3D): mesh of the upper divertor 165
                can be given in order to reduce loading time.
        """
        if not set(w7x.MeshedModelsIds.divertor).issubset(self.mm_ids):
            raise ValueError("Wrong mm_ids for this method. Could be expanded")

        if upper_divertor_mesh is None:
            upper_divertor_mesh = upper_half(165)

        divertor_hits = self.hits(*w7x.MeshedModelsIds.divertor)
        divertor_hits.to_segment_one(mirror_z=True)  # map to upper divertor in module 1
        hits_field = tfields.Tensors(upper_divertor_mesh.triangles()
                                     .in_triangles(divertor_hits, delta=0.001))
        hits_field = tfields.Tensors(hits_field.sum(axis=0))
        return hits_field
        
    def tile_hits_upper_divertor(self, upper_divertor_mesh=None,
                                 hits_upper_divertor=None):
        """
        Map the upper_divertor_mesh to a divertor tile geometry with a template
        provided for this
        Args:
            hits_upper_divertor(tfields.Points3D): retrieved by calling hits_upper_idvertor
            upper_divertor_mesh(tfields.Mesh3D): mesh of the upper divertor 165
                can be given in order to reduce loading time.
        """
        if upper_divertor_mesh is None:
            upper_divertor_mesh = upper_half(165)
        if hits_upper_divertor is None:
            hits_upper_divertor = hits_upper_divertor(upper_divertor_mesh=upper_divertor_mesh)

        # convert to hits per area
        hits_upper_divertor = hits_upper_divertor / upper_divertor_mesh.triangles().areas()
        upper_divertor_mesh.maps[0].fields.append(hits_upper_divertor)

        tiles = []
        for template in divertor_upper_tile_template():
            tile = upper_divertor_mesh.cut(template)
            if len(tile.maps) > 0 and len(tile.maps[0].fields) > 0:
                # convert hits per area back to hits. You will get fractions of
                # hits now.
                tile.maps[0].fields[0] *= tile.triangles().areas()
            tiles.append(tile)
        return tiles

    def prob_n_hits_lt_n_des(self, n_tot=None, power_lcfs=5., **kwargs):
        if n_tot is None:
            n_tot = len(self)

        tiles = self.tile_hits_upper_divertor(**kwargs)
        n_hits_tiles = [t.maps[0].fields[0].sum() for t in tiles]
        # from IPython import embed; embed()

        def n_hits_from_load(edge_load, n_tot, area, p_conv):
            p_conv *= 1. / 10  # correct for mapping all divertors to one
            return int(round((1. * edge_load * n_tot * area) / p_conv))
    
        areas = divertor_upper_tile_template_areas()
        max_loads = max_design_loads()
    
        tile_probs = []
        for n_hits, area, q_crit in zip(n_hits_tiles, areas, max_loads):
            n_crit = n_hits_from_load(q_crit,
                                      n_tot,
                                      area,
                                      p_conv=power_lcfs)
    
            n_hits = int(np.round(n_hits))
            p = poisson.cdf(n_crit, n_hits)
            tile_probs.append(float(p))
        return tile_probs
