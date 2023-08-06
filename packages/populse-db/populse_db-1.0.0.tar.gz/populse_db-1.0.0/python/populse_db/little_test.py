##########################################################################
# Populse_db - Copyright (C) IRMaGe/CEA, 2018
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

import os
import tempfile

import shutil

from populse_db.database import Database, FIELD_TYPE_JSON

# Generating the database in a temp directory
temp_folder = tempfile.mkdtemp()
path = os.path.join(temp_folder, "test.db")
string_engine = 'sqlite:///' + path
database = Database(string_engine)

# Creating the session and working with it
with database as session:

    # Creating a profile table
    session.add_collection("coll")

    # Adding JSON field
    session.add_field("coll", "json", FIELD_TYPE_JSON)

    # Adding documents
    session.add_document("coll", "doc1")
    session.add_document("coll", "doc2")
    value = {}
    value["key"] = "value"
    session.add_value("coll", "doc1", "json", value)

    # Filter
    filter = "{json} == \"{\"key\": \"value\"}\""
    result = session.filter_documents("coll", filter)
    for document in result:
        print(document)
    # Nothing is returned, but doc1 should be

shutil.rmtree(temp_folder)