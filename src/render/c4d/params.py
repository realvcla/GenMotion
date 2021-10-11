preparation_command_0 = ["import c4d",
"# set documentation",
"doc = c4d.documents.GetActiveDocument()",
"root_name = "f_avg_root"",
"root = doc.SearchObject(root_name)",
"# Creates the track in memory. Defined by it's DESCID    ",
"root_trX = c4d.CTrack(root, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0)))",
"root_trY = c4d.CTrack(root, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0)))",
"root_trZ = c4d.CTrack(root, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Z, c4d.DTYPE_REAL, 0)))",
"# Creates the track in memory. Defined by it's DESCID    ",
"root_rX = c4d.CTrack(root, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0)))",
"root_rY = c4d.CTrack(root, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Y, c4d.DTYPE_REAL, 0)))",
"root_rZ = c4d.CTrack(root, c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, 0), c4d.DescLevel(c4d.VECTOR_Z, c4d.DTYPE_REAL, 0)))",
"# Gets Curves for the track",
"root_curveX = root_trX.GetCurve()",
"root_curveY = root_trY.GetCurve()",
"root_curveZ = root_trZ.GetCurve()",
"# Gets Curves for the track",
"root_curveRX = root_rX.GetCurve()",
"root_curveRY = root_rY.GetCurve()",
"root_curveRZ = root_rZ.GetCurve()"]