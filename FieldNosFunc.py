# Author: KU
# Date: 28 March 2014
# Version: ArcGIS 10.1
# Prerequisites: Columns of "X" and "Y" co-ordinates.
# Purpose: This script will add a field named "FieldNos" to a given Feature Class and populate with the Field No, generated from the X and Y fields.
# Known issue: Feature Class won't display newly created data in attribute table without removing and re-adding to the mxd.
 
 
import os, string, arcpy
 
arcpy.env.workspace = arcpy.GetParameterAsText(0)
featureClass = arcpy.GetParameterAsText(1)
arcpy.AddField_management(featureClass, "FieldNos", "text")
 
def calculation(axis):
    b = str(axis)
    c = b[3:]
    result = int(round((float(c)/10),0))
    if result == 100:
        result = 10
        return result
    return result
 
rows = arcpy.UpdateCursor(featureClass)
 
for row in rows:
    resultx = calculation(row.X)
    resulty = calculation(row.Y)
    row.FieldNos = str(resultx).zfill(2) + str(resulty).zfill(2)
    rows.updateRow(row)
 
del row
del rows