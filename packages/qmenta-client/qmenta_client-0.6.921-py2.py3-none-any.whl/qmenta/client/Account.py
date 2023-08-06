from __future__ import print_function

import logging

import certifi
from urllib3.contrib import pyopenssl
from urllib3 import PoolManager
from urllib3.exceptions import HTTPError

from .Project import Project
from .utils import load_json

pyopenssl.inject_into_urllib3()

# Debug:
# import httplib
# httplib.HTTPConnection.debuglevel = 5

logger_name = 'qmenta.client'


class Account:
    """
    It represent your QMENTA account and implements the HTTP connection
    with the server. Once it is instantiated it will act as an identifier
    used by the rest of objects.

    Parameters
    ----------
    username : str
        Username on the platform. To get one go to https://platform.qmenta.com
    password : str
        The password assigned to the username.
    base_url : str
        The base url of the platform.
    verify_certificates : bool
        verify SSL certificates?
    """

    def __init__(self, username, password,
                 base_url="https://platform.qmenta.com",
                 verify_certificates=True):

        self._cookie = None
        self._project_id = None
        self.username = username
        self.password = password
        self.baseurl = base_url
        self.verify_certificates = verify_certificates
        if verify_certificates:
            self.pool = PoolManager(
                cert_reqs='CERT_REQUIRED',
                ca_certs=certifi.where()
            )
        else:
            self.pool = PoolManager()
        self.login()

    def __repr__(self):
        rep = "<Account session for {}>".format(self.username)
        return rep

    def login(self):
        """
        Login to the platform.

        Returns
        -------
        bool
            True if login was successful. False otherwise.
        """
        content = self._send_request("login",
                                     {"username": self.username,
                                      "password": self.password})
        logger = logging.getLogger(logger_name)
        if content["success"]:
            logger.info("Logged in as {0}".format(self.username))
            return True
        else:
            logger.error("Login is invalid")
            return False

    def logout(self):
        """
        Logout from the platform.

        Returns
        -------
        bool
            True if logout was successful, False otherwise.
        """

        content = self._send_request("logout")
        logger = logging.getLogger(logger_name)
        if content["success"]:
            logger.info("Logged out successfully")
            self._cookie = None
            return True
        else:
            logger.error("Logout was unsuccesful")
            return False

    def get_project(self, project_id):
        """
        Retrieve a project instance, given its id, which can be obtained
        checking account.projects.

        Parameters
        ----------
        project_id : int or str
            ID of the project to retrieve, either the numeric ID or the name

        Returns
        -------
        Project
            A project object representing the desired project
        """
        if type(project_id) == int or type(project_id) == float:
            return Project(self, int(project_id))
        elif type(project_id) == str:
            projects = self.projects
            projects_match = [
                proj for proj in projects if proj['name'] == project_id]
            if not projects_match:
                raise Exception(("Project {} does not exist or is not "
                                 "available for this user."
                                 ).format(project_id))
            return Project(self, int(projects_match[0]["id"]))

    @property
    def projects(self):
        """
        List all the projects available to the current user.

        Returns
        -------
        list[str]
            List of project identifiers (strings)
        """

        content = self._send_request("projectset_manager/get_projectset_list")
        logger = logging.getLogger(logger_name)
        if content.get("success", False):
            titles = []
            for project in content["data"]:
                titles.append({"name": project["name"], "id": project["_id"]})
            return titles
        else:
            message = "unable to get project list"
            logger.error('{}; response data: {}'.format(message, content))
            raise Exception(message)

    def add_project(self, project_abbreviation, project_name,
                    description="", users=[], from_date="", to_date=""):
        """
        Add a new project to the user account.

        Parameters
        ----------
        project_abbreviation : str
            Abbreviation of the project name.
        project_name : str
            Project name.
        description : str
            Description of the project.
        users : list[str]
            List of users to which this project is available.
        from_date : str
            Date of beginning of the project.
        to_date : str
            Date of ending of the project.

        Returns
        -------
        bool
            True if project was correctly added, False otherwise
        """
        logger = logging.getLogger(logger_name)
        for project in self.projects:
            if project["name"] == project_name:
                logger.error("Project name or abbreviation already exists.")
                return False

        content = self._send_request(
            "projectset_manager/upsert_project",
            req_parameters={"name": project_name,
                            "description": description,
                            "from_date": from_date,
                            "to_date": to_date,
                            "abbr": project_abbreviation,
                            "users": "|".join(users)})
        if content.get("success", False):
            for project in self.projects:
                if project["name"] == project_name:
                    logger.info("Project was successfuly created.")
                    return Project(self, int(project["id"]))
            logger.error("Project could note be created.")
            return False
        else:
            logger.error("There was an error.")
            return False

    def _send_request(self, path, req_parameters=None, req_headers=None,
                      stream=False, return_raw_response=False,
                      response_timeout=900.0):
        """
        Send a request to the QMENTA Platform.

        Interaction with the server is performed as POST requests.

        Parameters
        ----------
        req_parameters : dict
            Data to send in the POST request.
        req_headers : dict
            Extra headers to include in the request:
        stream : bool
            Defer downloading the response body until accessing the
            Response.content attribute.
        return_raw_response : bool
            When True, return the response from the
            server as-is. When False (by default),
            parse the answer as json to return a
            dictionary.
        response_timeout : float
            The timeout time in seconds to wait for the response.
        """

        req_headers = req_headers or {}
        req_url = '/'.join((self.baseurl, path))
        if self._cookie is not None:
            req_headers["Cookie"] = self._cookie
        req_headers["Mint-Api-Call"] = "1"

        logger = logging.getLogger(logger_name)
        try:
            if path == 'upload':
                response = self.pool.request(
                    'POST',
                    req_url,
                    body=req_parameters,
                    headers=req_headers,
                    timeout=response_timeout,
                    preload_content=not stream
                )
            else:
                response = self.pool.request(
                    'POST',
                    req_url,
                    req_parameters or {},
                    headers=req_headers,
                    timeout=response_timeout,
                    preload_content=not stream
                )
            if response.status >= 400:
                raise HTTPError(
                    'STATUS {}: {}'.format(response.status, response.reason))
        except Exception as e:
            error = "Could not send request. ERROR: {0}".format(e)
            logger.error(error)
            raise

        # Set the login cookie in our object
        if "set-cookie" in response.headers:
            self._cookie = response.headers["set-cookie"]

        if return_raw_response:
            return response

        # raise exception if there is no response from server
        if not response:
            error = "No response from server."
            logger.error(error)
            raise Exception(error)

        try:
            parsed_content = load_json(response.data)
        except Exception:
            error = "Could not parse the response as JSON data: {}".format(
                response.data)
            logger.error(error)
            raise

        # throw exceptions if anything strange happened
        if "error" in parsed_content:
            error = parsed_content["error"] or "Unknown error"
            logger.error(error)
            raise Exception(error)
        elif 'success' in parsed_content and parsed_content['success'] == 3:
            error = parsed_content['message']
            logger.error(error)
            raise Exception(error)
        return parsed_content
