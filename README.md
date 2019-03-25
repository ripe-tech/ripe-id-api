# RIPE ID API

Simple Python API client for RIPE ID.

## Configuration

* `RIPEID_BASE_URL` (`str`) - The base URL that is going to be used for API connections (defaults to `https://id.platforme.com/api/`)
* `RIPEID_LOGIN_URL` (`str`) - The base URL that is going to be used for visual web interactions (defaults to `https://id.platforme.com/`)
* `RIPEID_ID` (`str`) - The identifier of the client making use of the RIPE ID (defaults to `None`)
* `RIPEID_SECRET` (`str`) - The secret token to be used for authentication (defaults to `None`)
* `RIPEID_REDIRECT_URL` (`str`) - The URL for the redirection operation after the interactive part of the workflow (defaults to `None`)
