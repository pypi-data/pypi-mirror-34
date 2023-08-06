|CHUV| |License| |Codacy Badge| |Code Health| |CircleCI| |PyPI|

MRI Meta-data Extractor
=======================

This is a Python library providing methods to scan folders, extract
meta-data from files (DICOM, NIFTI, ...) and store them in a database.

Install
-------

Run ``pip install data-tracking``. (Only tested with Python3)

Use
---

Import the functions you need like this :
``from data_tracking.files_recording import create_provenance, visit``.

Create a provenance entity using :

::

    create_provenance(dataset, software_versions, db_url)

    Create (or get if already exists) a provenance entity, store it in the database and get back a provenance ID.
    * param dataset: Name of the data set.
    * param software_versions: (optional) Version of the software components used to get the data. It is a dictionary
      that accepts the following fields:
        - matlab_version
        - spm_version
        - spm_revision
        - fn_called
        - fn_version
        - others
    * param db_url: (optional) Database URL. If not defined, it looks for an Airflow configuration file.
    * return: Provenance ID.

Scan a folder to populate the database :

::

    def visit(folder, provenance_id, step_name, previous_step_id, config, db_url)

    Record all files from a folder into the database.
    The files are listed in the DB. If a file has been copied from previous step without any transformation, it will be
    detected and marked in the DB. The type of file will be detected and stored in the DB. If a files (e.g. a DICOM
    file) contains some meta-data, those will be stored in the DB.
    * param folder: folder path.
    * param provenance_id: provenance label.
    * param step_name: Name of the processing step that produced the folder to visit.
    * param previous_step_id: (optional) previous processing step ID. If not defined, we assume this is the first
      processing step.
    * param config: List of flags:
        - boost: (optional) When enabled, we consider that all the files from a same folder share the same meta-data.
          When enabled, the processing is (about 2 times) faster. This option is enabled by default.
        - session_id_by_patient: Rarely, a data set might use study IDs which are unique by patient (not for the whole study).
          E.g.: LREN data. In such a case, you have to enable this flag. This will use PatientID + StudyID as a session ID.
        - visit_id_in_patient_id: Rarely, a data set might mix patient IDs and visit IDs. E.g. : LREN data. In such a case, you have
          to enable this flag. This will try to split PatientID into VisitID and PatientID.
        - visit_id_from_path: Enable this flag to get the visit ID from the folder hierarchy instead of DICOM meta-data
          (e.g. can be useful for PPMI).
        - repetition_from_path: Enable this flag to get the repetition ID from the folder hierarchy instead of DICOM meta-data
          (e.g. can be useful for PPMI).
    * param db_url: (optional) Database URL. If not defined, it looks for an Airflow configuration file.
    * param is_organised: (optional) Disable this flag when scanning a folder that has not been organised yet
      (should only affect nifti files).
    * return: return processing step ID.

Build
-----

Run ``./build.sh``. (Builds for Python3)

(This includes the auto-generation of the README.rst based on the
README.md)

Test
----

Enter the ``tests`` directory.

With Docker
~~~~~~~~~~~

Run ``./test.sh``

Without Docker
~~~~~~~~~~~~~~

-  Run a Postgres database on ``localhost:5432``.
-  Run ``nosetest unit_test.py``

Publish on PyPi
---------------

Run ``./publish.sh``.

(This builds the project prior to pushing on PyPi)

NOTE : Do not forget to update the version number in the setup.py prior
to publishing.

NOTES
-----

-  This project contains a reference to a Git submodule. You can use the
   ``--recursive`` flag when cloning the project to clone the submodule
   too.

Acknowledgements
================

This work has been funded by the European Union Seventh Framework
Program (FP7/2007­2013) under grant agreement no. 604102 (HBP)

This work is part of SP8 of the Human Brain Project (SGA1).

.. |CHUV| image:: https://img.shields.io/badge/CHUV-LREN-AF4C64.svg
   :target: https://www.unil.ch/lren/en/home.html
.. |License| image:: https://img.shields.io/badge/license-Apache--2.0-blue.svg
   :target: https://github.com/LREN-CHUV/data-tracking/blob/master/LICENSE
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/4547fb5d1e464e4087640e046893576a
   :target: https://www.codacy.com/app/mirco-nasuti/data-tracking?utm_source=github.com&utm_medium=referral&utm_content=LREN-CHUV/data-tracking&utm_campaign=Badge_Grade
.. |Code Health| image:: https://landscape.io/github/LREN-CHUV/data-tracking/master/landscape.svg?style=flat
   :target: https://landscape.io/github/LREN-CHUV/data-tracking/master
.. |CircleCI| image:: https://circleci.com/gh/LREN-CHUV/data-tracking.svg?style=svg
   :target: https://circleci.com/gh/LREN-CHUV/data-tracking
.. |PyPI| image:: https://img.shields.io/pypi/v/data-tracking.svg
   :target: https://pypi.python.org/pypi/data-tracking/


