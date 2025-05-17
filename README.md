# Google APIs PHP Client Generator

This repo is used to generate the client library service classes and was forked from [googleapis/google-api-php-client-services](https://github.com/googleapis/google-api-php-client-services).

From the root of this project run:

```
python3 -m pip install -e generator/ --user
```

Generate the client library with the following command

```
python3 -m googleapis.codegen \
  --output_dir=output \
  --input=tests/testdata/foo.v1.json \
  --language=php \
  --language_variant=default
```
