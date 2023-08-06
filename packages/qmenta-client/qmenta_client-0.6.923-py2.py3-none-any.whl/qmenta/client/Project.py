from __future__ import print_function

import hashlib
import json
import logging
import os
import sys
import time

from .Subject import Subject
from .utils import load_json

if sys.version_info[0] == 3:
    # Note: this branch & variable is only needed for python 2/3 compatibility
    unicode = str

logger_name = 'qmenta.client'


def show_progress(done, total, finish=False):
    bytes_in_mb = 1024 * 1024
    progress_message = "\r[{:.2f} %] Uploaded {:.2f} of {:.2f} Mb".format(
        done / float(total) * 100, done / (bytes_in_mb), total / (bytes_in_mb))
    sys.stdout.write(progress_message)
    sys.stdout.flush()
    if not finish:
        pass
        # sys.stdout.write("")
        # sys.stdout.flush()
    else:
        sys.stdout.write("\n")


def get_session_id(file_path):
    m = hashlib.md5()
    m.update(file_path.encode("utf-8"))
    return str(time.time()).replace(".", "") + "_" + m.hexdigest()


def check_upload_file(file_path):
    """
    Check whether a file has the correct extension to upload.

    Parameters
    ----------
    file_path : str
        Path to the file

    Returns
    -------
    bool
        True if correct extension, False otherwise.
    """

    # TODO: Add a file zipper here so zips files in a folder

    file_parts = file_path.split(".")
    extension = file_parts[-1]

    if extension != "zip":
        logging.getLogger(logger_name).error("You must upload a zip.")
        return False
    else:
        return True


class Project:
    """
    This class is used to work with QMENTA projects.
    The class is instantiated passing as argument a Connection
    object and the id

    :param account: A QMENTA Account instance
    :type account: qmenta.client.Account

    :param project_id: The ID (or name) of the project you want to work with
    :type project_id: Int or string

    """

    def __init__(self, account, project_id, max_upload_retries=5):

        # if project_id is a string (the name of the project), get the
        # project id (int)
        if type(project_id) == str:
            project_name = project_id
            project_id = next(iter(filter(
                lambda proj: proj["name"] == project_id, account.projects)
            ))["id"]
        else:
            project_name = next(iter(filter(
                lambda proj: proj["id"] == project_id, account.projects)
            ))["name"]

        self._account = account
        self._project_id = project_id
        self._project_name = project_name

        # Max upload retries
        self.max_retries = max_upload_retries

        # Set the passed project ID as the Active one
        self._set_active(project_id)

        # Cache
        self._subjects_metadata = None

    def _set_active(self, project_id):
        """
        Set the active project.

        Parameters
        ----------
        project_id : str
            Project identifier.

        Returns
        -------
        bool
            True if the project was correctly set, False otherwise.
        """

        content = self._account._send_request(
            "projectset_manager/activate_project",
            req_parameters={"project_id": int(project_id)})
        logger = logging.getLogger(logger_name)
        if content.get("success", False):
            logger.info("Successfully changed project")
            self._project_id = project_id
            return True
        else:
            logger.error("Unable to activate the project.")
            return False

    def __repr__(self):
        rep = "<Project {}>".format(self._project_name)
        return rep

    @property
    def subjects_metadata(self):
        """
        List all subject data from the selected project.

        Returns
        -------
        dict
            A list of dictionary of {"metadata_name": "metadata_value"}
        """
        return self.get_subjects_metadata(cache=False)

    def get_subjects_metadata(self, cache=True):
        """
        List all subject data from the selected project.

        Returns
        -------
        dict
            A list of dictionary of {"metadata_name": "metadata_value"}
        """

        if not cache or not self._subjects_metadata:
            content = self._account._send_request(
                "patient_manager/get_patient_list",
                req_headers={"X-Range": "items=0-9999"})
            self._subjects_metadata = content
        else:
            content = self._subjects_metadata
        return content

    @property
    def subjects(self):
        """
        Return the list of subject names from the selected projet.

        :return: a list of subject names
        :rtype: List(Strings)
        """

        subjects = self.subjects_metadata
        names = [s["patient_secret_name"] for s in subjects]
        return list(set(names))

    def check_subject_name(self, subject_name):
        """
        Check if a given subject name exists in the selected project.

        Parameters
        ----------
        subject_name : str
            name of the subject to check

        Returns
        -------
        bool
            True if subject name exists in project, False otherwise
        """

        return subject_name in self.subjects

    @property
    def metadata_parameters(self):
        """
        List all the parameters in the subject metadata.

        Each project has a set of parameters that define the subjects metadata.
        This function returns all this parameters and its properties.

        Returns
        -------
        dict[str] -> dict[str] -> x
            dictionary {"param_name":
                 { "order": Int,
                 "tags": [tag1, tag2, ..., ],
                 "title: "Title",
                 "type": "integer|string|date|list|decimal",
                 "visible": 0|1
                 }}
        """
        logger = logging.getLogger(logger_name)
        content = self._account._send_request("patient_manager/module_config")

        if not content.get("success", False) or not content.get("data", False):
            logger.error("Could not retrieve metadata parameters.")
            return None
        else:
            return content["data"]["fields"]

    def add_metadata_parameter(self, title, param_id=None,
                               param_type="string", visible=False):
        """
        Add a metadata parameer to the project.

        Parameters
        ----------
        title : str
            Identificator of this new parameter
        param_id : str
            Title of this new parameter
        param_type : str
            Type of the parameter. One of:
            "integer", "date", "string", "list", "decimal"
        visible : bool
            whether the parameter will be visible in the table of patients

        Returns
        -------
        bool
            True if parameter was correctly added, False otherwise.
        """
        # use param_id equal to title if param_id is not provided
        param_id = param_id or title

        param_properties = [title, param_id, param_type, str(int(visible))]

        post_data = {"add": "|".join(param_properties),
                     "edit": "",
                     "delete": ""
                     }

        answer = self._account._send_request(
            "patient_manager/save_metadata_changes",
            req_parameters=post_data)
        logger = logging.getLogger(logger_name)
        if (not answer.get("success", False) or
                title not in answer.get("data", {})):
            logger.error("Could not add new parameter: {}".format(title))
            return False
        else:
            logger.info("New parameter added:", title, param_properties)
            return True

    def get_analysis(self, analysis_name):
        search_condition = {
            'p_n': analysis_name,
        }
        response = self._account._send_request(
            "analysis_manager/get_analysis_list",
            req_parameters=search_condition
        )

        if len(response) > 1:
            raise Exception(
                "multiple analyses with name {!r} found".format(analysis_name)
            )
        elif len(response) == 1:
            return response[0]
        else:
            return None

    def list_analysis(self, limit=10000000):
        """
        List the analysis available to the user.

        Parameters
        ----------
        limit : int
            Max number of results

        Returns
        -------
        dict
            List of analysis, each a dictionary
        """
        req_headers = {"X-Range": "items=0-" + str(limit - 1)}
        return self._account._send_request(
            "analysis_manager/get_analysis_list", req_headers=req_headers)

    def get_container(self, subject_name):
        search_condition = {
            's_n': subject_name,
        }
        response = self.list_input_containers(
            search_condition=search_condition
        )

        if len(response) > 1:
            raise Exception(
                'multiple containers for subject {!r} found'.format(
                    subject_name))
        elif len(response) == 1:
            return response[0]
        else:
            return None

    def list_input_containers(self, search_condition=None, limit=1000):
        """
        List the containers available to the user.

        Parameters
        ----------
        search_condition : dict
            d_n: container_name
            s_n: subject_id
            from_d: from date
            to_d: to date
            sets: data sets (modalities)
        limit : int
            Max number of results

        Returns
        -------
        dict
            List of containers, each a dictionary
            {"name": "container-name", "id": "container_id"}
        """

        req_headers = {"X-Range": "items=0-" + str(limit - 1)}
        response = self._account._send_request(
            "file_manager/get_container_list",
            req_parameters=search_condition,
            req_headers=req_headers
        )
        containers = [
            {
                "patient_secret_name": container_item["patient_secret_name"],
                "container_name": container_item["name"],
                "container_id": container_item["_id"],
                "ssid": container_item["ssid"],
            }
            for container_item in response
        ]
        return containers

    def list_result_containers(self, limit=1000):
        """
        List the result containers available to the user.

        Parameters
        ----------
        limit : int
            Max number of results

        Returns
        -------
        dict
            List of containers, each a dictionary
            {"name": "container-name", "id": "container_id"}
        """
        analysis = self.list_analysis(limit)
        return [{"name": a["name"],
                 "id": a["out_container_id"]} for a in analysis]

    def list_container_files(self, container_id):
        """
        List the name of the files available inside a given container.

        Parameters
        ----------
        container_id : str
            Container identifier.

        Returns
        -------
        list[str]
            List of file names (strings)
        """

        content = self._account._send_request(
            "file_manager/get_container_files",
            req_parameters={"container_id": container_id})

        if not content.get("success", False) or not content.get("data", False):
            return False
        elif content["data"].get("files", False):
            return content["data"]["files"]
        else:
            logging.getLogger(logger_name).error("Could not get files")
            return False

    def list_container_files_metadata(self, container_id):
        """
        List all the metadata of the files available inside a given container.

        Parameters
        ----------
        container_id : str
            Container identifier.

        Returns
        -------
        dict
            Dictionary of {"metadata_name": "metadata_value"}
        """

        content = self._account._send_request(
            "file_manager/get_container_files",
            req_parameters={"container_id": container_id})

        if content.get("success", False):
            return content["data"]["meta"]
        else:
            error = content["error"]
            logging.getLogger(logger_name).error(error)
            return False

    def get_file_metadata(self, container_id, filename):
        """
        Retrieve the metadata from a particular file in a particular container.

        Parameters
        ----------
        container_id : str
            Container identifier.
        filename : str
            Name of the file.

        Returns
        -------
        dict
            Dictionary with the metadata.
        """
        all_metadata = self.list_container_files_metadata(container_id)
        for file_meta in all_metadata:
            if file_meta["name"] == filename:
                return file_meta

    def change_file_metadata(self, container_id, filename, modality, tags):
        """
        Change modality and tags of `filename` in `container_id`

        Parameters
        ----------
        container_id : int
            Container identifier.
        filename : str
            Name of the file to be edited.
        modality : str or None
            Modality identifier, or None if the file shouldn't have
            any modality
        tags : list[str] or None
            List of tags, or None if the filename shouldn't have any tags
        """

        tags_str = "" if tags is None else ";".join(tags)
        self._account._send_request(
            "file_manager/edit_file",
            req_parameters={"container_id": container_id,
                            "filename": filename,
                            "tags": tags_str,
                            "modality": modality}
        )

    def download_file(self, container_id, file_name, local_filename=False,
                      overwrite=False):
        """
        Download a single file from a  specific container.

        Parameters
        ----------
        container_id : int
            ID of the container inside which the file is.
        file_name : str
            Name of the file in the container.
        local_filename : str
            Name of the file to be created. By default, the same as file_name.
        overwrite : bool
            Whether or not to overwrite the file if existing.
        """

        logger = logging.getLogger(logger_name)
        if file_name not in self.list_container_files(container_id):
            msg = "File '{}' does not exist in container {}".format(
                file_name, container_id)
            logger.error(msg)
            return False

        local_filename = local_filename or file_name

        if os.path.exists(local_filename) and not overwrite:
            msg = "File '{}' already exists".format(local_filename)
            logger.error(msg)
            return False

        params = {"container_id": container_id, "files": file_name}
        response = self._account._send_request(
            "file_manager/download_file",
            params, stream=True,
            return_raw_response=True
        )

        with open(local_filename, "wb") as f:
            while True:
                # CurrentNGINX Buffer size is 1MB.
                # Therefore, we use largest size (power of 2) below
                # buffer size (512 kB = 2**9*1024)
                # TODO: Test for larger sizes
                data = response.read(2 ** 9 * 1024, decode_content=True)
                if not data:
                    break
                f.write(data)
            response.release_conn()
            f.flush()

        logger.info("File {} from container {} saved to {}".format(
            file_name, container_id, local_filename))
        return True

    def download_files(self, container_id, filenames, zip_name="files.zip",
                       overwrite=False):
        """
        Download a set of files from a given container.

        Parameters
        ----------
        container_id : int
            ID of the container inside which the file is.
        filenames : list[str]
            List of files to download.
        overwrite : bool
            Whether or not to overwrite the file if existing.
        zip_name : str
            Name of the zip where the downloaded files are stored.
        """

        files_in_container = self.list_container_files(container_id)
        files_not_in_container = filter(lambda f: f not in files_in_container,
                                        filenames)
        files_not_in_container = list(files_not_in_container)

        if files_not_in_container:
            msg = "The following files are missing in container {}: {}".format(
                container_id, ", ".join(files_not_in_container))
            logging.getLogger(logger_name).error(msg)
            return False

        return self.download_file(container_id, ";".join(filenames),
                                  zip_name, overwrite)

    def get_subject_id(self, subject_name, cache=False):
        """
        Given a subject name, return its ID in the project.

        Parameters
        ----------
        subject_name : str
            Name of the subject in the project.
        cache : bool
            Whether to use the cached metadata or not

        Returns
        -------
        int or bool
            The ID of the subject in the project, or False if
            the subject is not found.
        """

        for user in self.get_subjects_metadata(cache):
            if user["patient_secret_name"] == subject_name:
                return int(user["_id"])
        return False

    def get_subject(self, subject_name, cache=True):
        """
        Return a subject object, representing a subject from the project.

        Parameters
        ----------
        subject_name : str
            Name of the subject.

        Returns
        -------
        Subject or bool
            A Subject instance representing the desired subject, or
            False if the subject was not found.
        """
        subject_id = self.get_subject_id(subject_name, cache=cache)
        if subject_id is False:
            return False
        subj = Subject(subject_name)
        subj.subject_id = subject_id
        subj.project = self
        return subj

    def add_subject(self, subject):
        """
        Add a subject to the project.

        Parameters
        ----------
        subject : Subject
            Instance of Subject representing the subject to add.

        Returns
        -------
        bool
            True if correctly added, False otherwise
        """
        logger = logging.getLogger(logger_name)
        if self.check_subject_name(subject.name):
            logger.error(
                "Subject with name {} already exists in project!".format(
                    subject.name))
            return False

        content = self._account._send_request(
            "patient_manager/upsert_patient",
            req_parameters={"secret_name": subject.name})
        if content.get("success", False):
            subject.subject_id = self.get_subject_id(subject.name)
            subject.project = self
            logger.info(
                "Subject {0} was successfully created".format(subject.name))
            return True
        else:
            logger.error(
                "Subject {} could not be created.".format(subject.name))
            return False

    def delete_session(self, subject_name, session_id, cache=False):
        """
        Delete a session from a subject within a project.

        Parameters
        ----------
        subject_name : str
            Name of the subject
        session_id : int
            The SSID of the session that will be deleted
        cache : bool
            Whether to use the cached metadata or not

        Returns
        -------
        bool
            True if correctly deleted, False otherwise.
        """
        logger = logging.getLogger(logger_name)
        all_sessions = self.get_subjects_metadata(cache)

        sessions_to_del = [
            s for s in all_sessions
            if s['patient_secret_name'] == subject_name
            and int(s['ssid']) == session_id]

        if not sessions_to_del:
            logger.error(
                'Session {}/{} could not be found in this project.'.format(
                    subject_name, session_id
                )
            )
            return False
        elif len(sessions_to_del) > 1:
            raise RuntimeError(
                'Multiple sessions with same SID and SSID. Contact support.'
            )
        else:
            logger.info('{}/{} found (id {})'.format(
                subject_name, session_id, sessions_to_del[0]['_id']
            ))

        session = sessions_to_del[0]

        content = self._account._send_request(
            "patient_manager/delete_patient",
            req_parameters={
                "patient_id": str(int(session['_id'])),
                "delete_files": 1
            })
        if content.get("success", False):
            logger.info(
                "Session '{}/{}' successfully deleted.".format(
                    subject_name, session['ssid']
                )
            )
            return True
        else:
            logger.error(
                "Session '{}/{}' could not be deleted.".format(
                    subject_name, session['ssid']
                )
            )
            return False

    def delete_subject(self, subject_name):
        """
        Delete a subject from the project.

        Parameters
        ----------
        name : str
            Name of the subject to be deleted.

        Returns
        -------
        bool
            True if correctly deleted, False otherwise.
        """

        logger = logging.getLogger(logger_name)
        # Always fetch the session IDs from the platform before deleting them
        all_sessions = self.get_subjects_metadata(False)

        sessions_to_del = [
            s for s in all_sessions if s['patient_secret_name'] == subject_name
        ]

        if not sessions_to_del:
            logger.error(
                'Subject {} cannot be found in this project.'.format(
                    subject_name
                )
            )
            return False

        for ssid in [s['ssid'] for s in sessions_to_del]:
            if not self.delete_session(subject_name, ssid, cache=True):
                return False
        return True

    def _upload_chunk(self, data, range_str, length, session_id,
                      disposition,
                      last_chunk,
                      name="", date_of_scan="", description="",
                      subject_name="", ssid="", filename="DATA.zip",
                      input_data_type="mri_brain_data:1.0",
                      result=False, add_to_container_id=0,
                      split_data=False
                      ):
        """
        Upload a chunk of a file to the platform.

        Parameters
        ----------
        data
            The file chunk to upload
        range_str
            The string to send that describes the content range
        length
            The content length of the chunk to send
        session_id
            The session ID from the file path
        filename
            The name of the file to be sent
        disposition
            The disposition of the content
        last_chunk
            Set this only for the last chunk to be uploaded.
            All following parameters are ignored when False.
        split_data
            Sets the header that informs the platform to split
            the uploaded file into multiple sessions.
        """

        request_headers = {}
        request_headers["Content-Type"] = "application/zip"
        request_headers["Content-Range"] = range_str
        request_headers["Session-ID"] = str(session_id)
        request_headers["Content-Length"] = str(length)
        request_headers["Content-Disposition"] = disposition

        if last_chunk:
            request_headers["X-Mint-Name"] = name
            request_headers["X-Mint-Date"] = date_of_scan
            request_headers["X-Mint-Description"] = description
            request_headers["X-Mint-Patient-Secret"] = subject_name
            request_headers["X-Mint-SSID"] = ssid
            request_headers["X-Mint-Filename"] = filename
            request_headers["X-Mint-Project-Id"] = str(self._project_id)
            request_headers["X-Mint-Split-Data"] = str(int(split_data))

            if input_data_type:
                request_headers["X-Mint-Type"] = input_data_type

                if result:
                    request_headers["X-Mint-In-Out"] = "out"
                else:
                    request_headers["X-Mint-In-Out"] = "in"

            if add_to_container_id > 0:
                request_headers["X-Mint-Add-To"] = str(add_to_container_id)

            request_headers["X-Requested-With"] = "XMLHttpRequest"

        response_time = 120.0 if last_chunk else 900.0
        response = self._account._send_request(
            "upload", req_parameters=data,
            req_headers=request_headers, return_raw_response=True,
            response_timeout=response_time)

        return response

    def upload_file(self, file_path, subject_name, ssid="", date_of_scan="",
                    description="", result=False, name="",
                    input_data_type="mri_brain_data:1.0",
                    add_to_container_id=0, chunk_size=2 ** 9,
                    split_data=False):
        """
        Upload a file to the platform, associated with the current user.

        Parameters
        ----------
        file_path : str
            Path to the file to upload.
        subject_name : str
            Subject to which this file will belong
        ssid : str
            The ID of the timepoint
        data_of_scan : str
            Date of scan/creation of the file
        description : str
            Description of the file
        result : bool
            If result=True then the upload will be taken as an offline analysis
        name : str
            Name of the file in the platform
        input_data_type : str
            mri_brain_data:1.0 or gametection:1.0
        add_to_container_id : int
            ID of the container to which this file should be added (if id > 0)
        chunk_size : int
            Size in kB of each chunk. Should be expressed as
            a power of 2: 2**x. Default value of x is 9 (chunk_size = 512 kB)
        split_data : bool
            If True, the platform will try to split the uploaded file into
            different sessions. It will be ignored when the ssid is given.

        Returns
        -------
        bool
            True if correctly uploaded, False otherwise.
        """

        filename = os.path.split(file_path)[1]
        input_data_type = "offline_analysis:1.0" if result else input_data_type

        chunk_size *= 1024
        max_retries = 10

        name = name or os.path.split(file_path)[1]

        total_bytes = os.path.getsize(file_path)

        # making chunks of the file and sending one by one
        logger = logging.getLogger(logger_name)
        with open(file_path, "rb") as file_object:

            file_size = os.path.getsize(file_path)
            if file_size == 0:
                logger.error('Cannot upload empty file {}'.format(file_path))
                return False
            uploaded = 0
            session_id = get_session_id(file_path)
            chunk_num = 0
            retries_count = 0
            error_message = ""
            uploaded_bytes = 0
            response = None
            last_chunk = False

            if ssid and split_data:
                logger.warning('split-data argument will be ignored because' +
                               ' ssid has been specified')
                split_data = False

            while True:
                data = file_object.read(chunk_size)
                if not data:
                    break

                start_position = chunk_num * chunk_size
                end_position = start_position + chunk_size - 1
                bytes_to_send = chunk_size

                if end_position >= total_bytes:
                    last_chunk = True
                    end_position = total_bytes - 1
                    bytes_to_send = total_bytes - uploaded_bytes

                bytes_range = "bytes " + str(start_position) + "-" + \
                              str(end_position) + "/" + str(total_bytes)

                dispstr = "attachment; filename=%s" % filename
                response = self._upload_chunk(
                    data, bytes_range, bytes_to_send, session_id, dispstr,
                    last_chunk,
                    name, date_of_scan, description, subject_name, ssid,
                    filename, input_data_type, result, add_to_container_id,
                    split_data)

                if response is None:
                    retries_count += 1
                    time.sleep(retries_count * 5)
                    if retries_count > max_retries:
                        error_message = "HTTP Connection Problem"
                        break
                elif int(response.status) == 201:
                    chunk_num += 1
                    retries_count = 0
                    uploaded_bytes += chunk_size
                elif int(response.status) == 200:
                    show_progress(file_size, file_size, finish=True)
                    break
                elif int(response.status) == 416:
                    retries_count += 1
                    time.sleep(retries_count * 5)
                    if retries_count > self.max_retries:
                        error_message = (
                            "Error Code: 416; "
                            "Requested Range Not Satisfiable (NGINX)")
                        break
                else:
                    retries_count += 1
                    time.sleep(retries_count * 5)
                    if retries_count > max_retries:
                        error_message = ("Number of retries has been reached. "
                                         "Upload process stops here !")
                        break

                uploaded += chunk_size
                show_progress(uploaded, file_size)

        if len(error_message) == 0:

            content = load_json(response.data)

            if content["success"] == 1:
                message = "Your data was successfully uploaded."
                message += "The uploaded file will be soon processed !"
                logger.info(message)
                return True

            if content["success"] == 0:
                logger.error(content["error"])
                return False
        else:
            logger.error(error_message)
            return False

    def upload_mri(self, file_path, subject_name):
        """
        Upload new MRI data to the subject.

        Parameters
        ----------
        file_path : str
            Path to the file to upload

        Returns
        -------
        bool
            True if upload was correctly done, False otherwise.
        """

        if check_upload_file(file_path):
            return self.upload_file(file_path, subject_name)

    def upload_gametection(self, file_path, subject_name):
        """
        Upload new Gametection data to the subject.

        Parameters
        ----------
        file_path : str
            Path to the file to upload

        Returns
        -------
        bool
            True if upload was correctly done, False otherwise.
        """

        if check_upload_file(file_path):
            return self.upload_file(
                file_path, subject_name,
                input_data_type="parkinson_gametection")
        return False

    def upload_result(self, file_path, subject_name):
        """
        Upload new result data to the subject.

        Parameters
        ----------
        file_path : str
            Path to the file to upload

        Returns
        -------
        bool
            True if upload was correctly done, False otherwise.
        """

        if check_upload_file(file_path):
            return self.upload_file(file_path, subject_name, result=True)
        return False

    def copy_container_to_project(self, container_id, project_id):
        """
        Copy a container to another project.

        Parameters
        ----------
        container_id : int
            ID of the container to copy.
        project_id : int or str
            ID of the project to retireve, either the numeric ID or the name

        Returns
        -------
        bool
            True on success, False on fail
        """

        if type(project_id) == int or type(project_id) == float:
            p_id = int(project_id)
        elif type(project_id) == str:
            projects = self._account.projects
            projects_match = [proj for proj in projects
                              if proj["name"] == project_id]
            if not projects_match:
                raise Exception(
                    "Project {}".format(project_id) +
                    " does not exist or is not available for this user."
                )
            p_id = int(projects_match[0]["id"])
        else:
            raise TypeError('project_id')
        data = {
            "container_id": container_id,
            "project_id": p_id,
        }
        content = self._account._send_request(
            "file_manager/copy_container_to_another_project",
            req_parameters=data
        )
        if content.get("success", False):
            return True
        else:
            logging.getLogger(logger_name).error(content.get(
                "error", "Error: couldn't copy container."))
            return False

    def start_analysis(
            self,
            script_name,
            version,
            in_container_id=None,
            analysis_name=None,
            analysis_description=None,
            ignore_warnings=False,
            settings=None,
            tags=None,
            preferred_destination=None
    ):
        """
        Starts an analysis on a subject.

        Parameters
        ----------
        script_name : str
            Name of the script to be run. One of: "volumetry",
            "diffusion_connectome", "morphology"
        in_container_id : int or dict
            The ID of the container to get the data from, or a dictionary with
            one or more container names as keys, and IDs as values.
            Input container names are generally prefixed with 'input\_'.
            If not, the prefix will be automatically added.
        analysis_name : str
            Name of the analysis (optional)
        analysis_description : str
            Description of the analysis (optional)
        ignore_warnings : bool
            If False, warnings by server cause failure.
        settings : dict
            The input settings used to run the analysis.
            Use either settings or in_container_id. Input specification
            in the settings dict can be done by using the key 'input'.
        tags : list[str]
            The tags of the analysis.
        preferred destination : str
            The machine on which to run the analysis

        Returns
        -------
        bool
            True if correctly started, False otherwise.
        """
        logger = logging.getLogger(logger_name)

        if in_container_id is None and settings is None:
            raise ValueError(
                "Pass a value for either in_container_id or settings.")

        post_data = {
            "script_name": script_name,
            "version": version
        }

        settings = settings or {}

        if in_container_id:
            if isinstance(in_container_id, dict):
                for key, value in in_container_id.items():
                    if 'input' not in key:
                        key = 'input_' + key
                    settings[key] = value
            else:
                settings['input'] = str(in_container_id)

        for key in settings:
            post_data['as_' + key] = settings[key]

        # name and description are optional
        if analysis_name:
            post_data["name"] = analysis_name
        if analysis_description:
            post_data["description"] = analysis_description
        if tags:
            if isinstance(tags, list) and len(tags) > 0:
                post_data["tags"] = ",".join(tags)
            elif isinstance(tags, (str, unicode)):
                post_data["tags"] = tags
        if preferred_destination:
            post_data["preferred_destination"] = preferred_destination

        logger.debug("post_data = {}".format(post_data))
        response = self._account._send_request(
            "analysis_manager/analysis_registration",
            req_parameters=post_data
        )

        return self.__handle_start_analysis_response(
            post_data, response, ignore_warnings=ignore_warnings
        )

    def delete_analysis(self, analysis_id):
        """
        Delete an analysis

        :param analysis_id: id of the analysis to be deleted
        :type analysis_id: Int
        """
        logger = logging.getLogger(logger_name)

        post_data = {
            "project_id": analysis_id
        }
        # name and description are optional
        response = self._account._send_request(
            "analysis_manager/delete_analysis",
            req_parameters=post_data
        )

        if response.get('success', False):
            return True

        logger.error(response.get(
            'message',
            'Could not delete analysis (no more information provided ' +
            'by the server)'
        ))
        return False

    def __handle_start_analysis_response(self, post_data, response,
                                         ignore_warnings=False, n_calls=0):
        """
        Handle the possible responses from the server after start_analysis.
        Sometimes we have to send a request again, and then check again the
        response. That's why this function is separated from start_analysis.

        Since this function sometimes calls itself, n_calls avoids entering an
        infinite loop due to some misbehaviour in the server.
        """

        call_limit = 10
        n_calls += 1

        logger = logging.getLogger(logger_name)
        if n_calls > call_limit:
            logger.error("__handle_start_analysis_response called itself more\
                          than {} times: aborting.".format(n_calls))
            return False

        if not response.get("success", False):
            logger.error("Unable to start the analysis.")
            return False

        if response["success"] == 0:
            logger.info(response['error'])
            return True
        elif response["success"] == 1:
            logger.info(response['message'])
            return True
        elif response["success"] == 2:

            has_warning = False

            # logging any warning that we have
            if response["warning"]:
                has_warning = True
                logger.warning(response["warning"])

            new_post = {
                'analysis_id': response['analysis_id'],
                'script_name': post_data['script_name'],
                'version': post_data['version'],
            }

            if response["data_to_choose"]:
                # in case we have data to choose
                choosen_files = {}
                for settings_key in response["data_to_choose"]:
                    choosen_files[settings_key] = {}
                    filters = response["data_to_choose"][
                        settings_key]["filters"]
                    for filter_key in filters:
                        filter_data = filters[filter_key]

                        # skip the filters that didnt pass
                        if not filter_data["passed"]:
                            continue

                        number_of_files_to_select = 1
                        if filter_data["range"][0] != 0:
                            number_of_files_to_select = filter_data["range"][0]
                        elif filter_data["range"][1] != 0:
                            number_of_files_to_select = min(
                                filter_data["range"][1],
                                len(filter_data["files"])
                            )
                        else:
                            number_of_files_to_select = len(
                                filter_data["files"]
                            )

                        files_selection = [ff["_id"] for ff in
                                           filter_data["files"]
                                           [:number_of_files_to_select]]
                        choosen_files[settings_key][filter_key] = \
                            files_selection

                new_post["user_preference"] = json.dumps(choosen_files)
            else:
                if has_warning and not ignore_warnings:
                    logger.info("cancelling analysis due to warnings, " +
                                "set 'ignore_warnings' to True to override")
                    new_post['cancel'] = '1'
                else:
                    logger.info('suppressing warnings')
                    new_post['user_preference'] = '{}'
                    new_post['_mint_only_warning'] = '1'

            response = self._account._send_request(
                "analysis_manager/analysis_registration",
                req_parameters=new_post
            )
            return self.__handle_start_analysis_response(
                new_post, response, ignore_warnings=ignore_warnings,
                n_calls=n_calls
            )
        elif response["success"] == 3:
            logger.info(response['message'])
            return False

        return False

    def __get_modalities(self, files):
        modalities = []
        for file_ in files:
            modality = file_["metadata"]["modality"]
            if modality not in modalities:
                modalities.append(modality)
        return modalities
