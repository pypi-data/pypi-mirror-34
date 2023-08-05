import logging
import requests
from requests import Response
from typing import Any, Dict, Iterator, Optional
from urllib.parse import urljoin

from evalkit_api_client.errors import APIPaginationException
from evalkit_api_client.interface import EvalKitAPIClient
from evalkit_api_client.types import (
        PaginatedResponse, RequestHeaders, RequestParams)

logger = logging.getLogger()


class EvalKitAPIv1(EvalKitAPIClient):
    """
    Evalkit v1 API Client.

    This client can be used to make requests to the v1 Evalkit API.

    Create separate clients for other versions of the Evalkit API.
    """

    def __init__(self,
                 api_url: str,
                 api_token: Optional[str] = None) -> None:
        """
        Creates a evalkit API client given a base URL for the API, an optional
        API token, and an optional requests library.

        The optional requests library should be either the python HTTP requests
        library or the equivalent (e.g. a Requests-OAuthlib session object).
        """
        self._api_url = api_url
        self._api_token = api_token

    def _get_url(self, endpoint: str) -> str:
        """
        Formats a EvalKit API URL from a given endpoint.
        """
        return urljoin(self._api_url, endpoint)

    def _add_bearer_token(self, headers: Dict[str, Any]):
        """
        Adds the authentication bearer token. Only run this if the token
        exists.
        """
        headers.update({'AuthToken': self._api_token})

    def _send_request(self,
                      callback,
                      url: str,
                      exit_on_error: bool = True,
                      headers: RequestHeaders = None,
                      params: RequestParams = None,
                      **kwargs) -> Response:
        """
        Sends an API call to the Evalkit server via callback method.

        The callback should be a requests.<func> function or the equivalent.

        Note: since raise_for_status() will raise an exception for error
        codes, the user is responsible for catching `HTTPError`
        exceptions unless they run with the exit_on_error set to False.
        """
        if headers is None:
            headers = {}
        if params is None:
            params = {}

        if self._api_token is not None:
            self._add_bearer_token(headers)

        response = callback(url, headers=headers, params=params, **kwargs)
        if not response.ok:
            logger.debug('Error status code for url "{}"'.format(response.url))
        if exit_on_error:
            response.raise_for_status()

        return response

    def _get(self, *args, **kwargs) -> Response:
        """
        Sends a GET request to the API.
        """
        return self._send_request(
            requests.get, *args, **kwargs)  # type: ignore

    def _delete(self, *args, **kwargs) -> Response:
        """
        Sends a DELETE request to the API.
        """
        return self._send_request(
            requests.delete, *args, **kwargs)  # type: ignore

    def _post(self, *args, **kwargs) -> Response:
        """
        Sends a POST request to the API.
        """
        return self._send_request(
            requests.post, *args, **kwargs)  # type: ignore

    def _put(self, *args, **kwargs) -> Response:
        """
        Sends a PUT request to the API.
        """
        return self._send_request(
            requests.put, *args, **kwargs)  # type: ignore

    def _get_validated_page_json(self,
                       url: str,
                       headers: RequestHeaders = None,
                       params: RequestParams = None) -> Dict:
        response = self._get(url, headers=headers, params=params)

        resp_json = response.json()
        try:
            page = resp_json['page']
            page_size = resp_json['pageSize']
            result_list = resp_json['resultList']
        except KeyError:
            raise APIPaginationException(
                'Pagination is not available for this endpoint')

        return resp_json

    def _get_paginated(self,
                       url: str,
                       headers: RequestHeaders = None,
                       params: RequestParams = None) -> Iterator[Dict]:
        """
        Send an API call to the evalkit server with pagination.

        Returns a generator of dictionary objects.
        """
        if params is None:
            params = {}

        counter = 0
        retrieve_next_page = True

        while retrieve_next_page:
            params = {'page': counter + 1}
            resp_json = self._get_validated_page_json(url,
                                                      headers=headers,
                                                      params=params)

            yield resp_json

            if len(resp_json['resultList']) < resp_json['pageSize']:
                retrieve_next_page = False
            else:
                counter += 1

    def get_projects(self,
                    params: RequestParams = None
                    ) -> PaginatedResponse:
        """
        Get the projects for a given account.
        """
        endpoint = "projects"
        return self._get_paginated(self._get_url(endpoint))

    def get_non_responders(self,
                          project_id: str,
                          params: RequestParams = None
                          ) -> PaginatedResponse:
        """
        Get the non-respondents for a given project.
        """
        endpoint = "projects/{}/nonRespondents".format(project_id)
        return self._get_paginated(self._get_url(endpoint))
