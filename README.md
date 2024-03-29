<h1><a href="https://id.platforme.com"><img src="res/logo.svg" alt="RIPE ID API" height="60" style="height: 60px;"></a></h1>

Simple Python API client for RIPE ID.

## Configuration

| Name | Type | Description |
| ----- | ----- | ----- |
| **RIPEID_BASE_URL** | `str` | The base URL that is going to be used for API connections (defaults to `https://id.platforme.com/api/`). |
| **RIPEID_LOGIN_URL** | `str` | The base URL that is going to be used for visual web interactions (defaults to `https://id.platforme.com/`). |
| **RIPEID_ID** | `str` | The identifier of the client making use of the RIPE ID (defaults to `None`). |
| **RIPEID_SECRET** | `str` | The secret token to be used for authentication (defaults to `None`). |
| **RIPEID_REDIRECT_URL** | `str` | The URL for the redirection operation after the interactive part of the workflow (defaults to `None`). |

## License

RIPE ID API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://app.travis-ci.com/ripe-tech/ripe-id-api.svg?branch=master)](https://travis-ci.com/github/ripe-tech/ripe-id-api)
[![Build Status GitHub](https://github.com/ripe-tech/ripe-id-api/workflows/Main%20Workflow/badge.svg)](https://github.com/ripe-tech/ripe-id-api/actions)
[![Coverage Status](https://coveralls.io/repos/ripe-tech/ripe-id-api/badge.svg?branch=master)](https://coveralls.io/r/ripe-tech/ripe-id-api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/ripe-id-api.svg)](https://pypi.python.org/pypi/ripe-id-api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
