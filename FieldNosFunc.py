# Author: KU
# Date: 28 March 2014
# This Revision: 17 July 2014
# Version: ArcGIS 10.1
# Purpose: This script will add fields named "FieldNos", "X" and "Y" to a given Feature Class and populate with the Field No, generated from the X and Y fields.

 
 
import os, string, arcpy
 
arcpy.env.workspace = arcpy.GetParameterAsText(0)
featureClass = arcpy.GetParameterAsText(1)
 
arcpy.AddField_management(featureClass, "FieldNos", "text")
arcpy.AddField_management(featureClass, "X", "LONG")
arcpy.AddField_management(featureClass, "Y", "LONG")
fields = ("FieldNos", "X", "Y")
 
arcpy.CalculateField_management(featureClass, "X", "!SHAPE.CENTROID.X!", "PYTHON_9.3")
arcpy.CalculateField_management(featureClass, "Y", "!SHAPE.CENTROID.Y!", "PYTHON_9.3")
 
 
def calculation(axis):
    b = str(axis)
    c = b[3:]
    result = int(round((float(c)/10),0))
    if result == 100:
        result = 10
        return result
    return result
 
with arcpy.da.UpdateCursor(featureClass, fields) as rows:
 
    for row in rows:
        resultx = calculation(row[1])
        resulty = calculation(row[2])
        row[0] = str(resultx).zfill(2) + str(resulty).zfill(2)
        rows.updateRow(row)
 
#del row
#del rows