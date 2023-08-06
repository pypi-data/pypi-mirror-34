# vcap_service_python

[![Build Status](https://travis-ci.org/mamoonraja/vcap-services-python.svg?branch=master)](https://travis-ci.org/mamoonraja/vcap-services-python/)
[![Coverage Status](https://coveralls.io/repos/mamoonraja/vcap-services-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/mamoonraja/vcap-services-python?branch=master)

Parse and return service credentials from environment variables that [IBM Cloud] provides.

## Installation

```sh
$ pip install vcap_services
```

## Usage

```sh
from vcap_services import load_from_vcap_services
credentials = load_from_vcap_services('personality_insights')
print(credentials);
```

If `VCAP_SERVICES` is:
```json
{
  "personality_insights": [{
      "credentials": {
        "password": "<password>",
        "url": "<url>",
        "username": "<username>"
      },
    "label": "personality_insights",
    "name": "personality-insights-service",
    "plan": "standard"
  }]
}
```

Output:
```json
{
  "password": "<password>",
  "url": "<url>",
  "username": "<username>"
}
```

### Getting credentials for a specific plan

Get credentials that match a specific service plan (only for `VCAP_SERVICES`).
```sh
from vcap_services import load_from_vcap_services
credentials = load_from_vcap_services('personality_insights', 'standard')
print(credentials);
```

### Getting credentials for a specific instance
Get credentials that match a specific service instance (replace "YOUR NLC NAME" with the name of your service instance).
```sh
from vcap_services import load_from_vcap_services
credentials = load_from_vcap_services('natural_language_classifier', None, 'YOUR NLC NAME')
print(credentials);
```

### Getting credentials for a specific plan and instance
Get credentials that match a specific service plan and instance (replace "YOUR NLC NAME" with the name of your service instance).
```sh
from vcap_services import load_from_vcap_services
credentials = load_from_vcap_services('natural_language_classifier', 'standard', 'YOUR NLC NAME')
print(credentials);
```

## Tests
Running all the tests:
```sh
$ pip install -r requirements.txt
$ cp .env.mock .env
$ pytest --cov=vcap_services
```

## License

MIT.

## Contributing
See [CONTRIBUTING](https://github.com/mamoonraja/vcap-services-python/blob/master/CONTRIBUTING.md).

[IBM Cloud]: http://console.bluemix.net/
