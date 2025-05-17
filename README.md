# Google APIs PHP Client Generator

This repo is used to generate the client library service classes and was forked from [googleapis/google-api-php-client-services](https://github.com/googleapis/google-api-php-client-services).

From the root of this project run:

```
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

Generate the client library with the following command

```
python3 -m googleapis.codegen \
  --output_dir=output \
  --input=tests/testdata/foo.v1.json \
  --language=php \
  --language_variant=default
```

or using [Google APIs Explorer](https://developers.google.com/apis-explorer/) server directly:

```
python3 -m googleapis.codegen \
  --output_dir=output \
  --api_name=walletobjects \
  --api_version=v1 \
  --language=php \
  --language_variant=default
```