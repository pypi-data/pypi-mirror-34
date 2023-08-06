##################################################################
######################## include.py   ############################
##################################################################
##### ekate - Enhanced KRATOS for Advanced Tunnel Enineering #####
##### copyright by CIMNE, Barcelona, Spain                   #####
#####          and Institute for Structural Mechanics, RUB   #####
##### all rights reserved                                    #####
##################################################################
##################################################################
##################################################################
##################################################################
import sys
import os
kratos_root_path=os.environ['KRATOS_ROOT_PATH']
##################################################################
##################################################################
#importing Kratos modules
from KratosMultiphysics import *
from KratosMultiphysics.IsogeometricApplication import *
kernel = Kernel()   #defining kernel

import geometry_factory
mpatch_util = MultiPatchUtility()
mpatch_export = MultiNURBSPatchMatlabExporter()

arc_ptr = geometry_factory.CreateSmallArc([0.0, 0.0, 0.0], 'y', 1.0, 0.0, 60.0)
arc = arc_ptr.GetReference()
print(arc)
mpatch_export.Export(arc, "arc.m")

## use this command to check in matlab
# for x: arc;nrbplot(nurbs,10);xlabel('x');ylabel('y');zlabel('z');view([1 0 0]);
# for y: arc;nrbplot(nurbs,10);xlabel('x');ylabel('y');zlabel('z');view([0 1 0]);
# for z: arc;nrbplot(nurbs,10);xlabel('x');ylabel('y');zlabel('z');view([0 0 1]);

