""" Demonstrates mesh repair on the standford bunny mesh """
import numpy as np
import os
import pymeshfix
import vtkInterface as vtki
from pymeshfix.examples import bunny_scan


def Native(outfile='repaired.ply'):
    """ Repair Stanford Bunny Mesh """
    pymeshfix._meshfix.CleanFromFile(bunny_scan, outfile)


def WithVTK(plot=True):
    """ Tests VTK interface and mesh repair of Stanford Bunny Mesh """
    mesh = vtki.PolyData(bunny_scan)
    meshfix = pymeshfix.MeshFix(mesh)
    if plot:
        print('Plotting input mesh')
        meshfix.Plot()
    meshfix.Repair()
    if plot:
        print('Plotting repaired mesh')
        meshfix.Plot()

    return meshfix.mesh


if __name__ == '__main__':
    """ Functional Test: vtk and native """
    out_file = 'repaired.ply'
    Native()
    outmesh = vtki.PolyData(out_file)
    os.remove(out_file)
    assert outmesh.GetNumberOfPoints()

    # test for any holes
    pdata = outmesh.ExtractEdges(non_manifold_edges=False, feature_edges=False,
                                 manifold_edges=False)
    assert pdata.GetNumberOfPoints() == 0

    # test vtk
    meshin = vtki.PolyData(bunny_scan)
    meshfix = pymeshfix.MeshFix(meshin)
    meshfix.Repair()

    # check arrays and output mesh
    assert np.any(meshfix.v)
    assert np.any(meshfix.f)
    meshout = meshfix.mesh
    assert meshfix.mesh.GetNumberOfPoints()

    # test for any holes
    pdata = meshout.ExtractEdges(non_manifold_edges=False, feature_edges=False,
                                 manifold_edges=False)
    assert pdata.GetNumberOfPoints() == 0

    print('PASS')
