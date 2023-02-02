import os

AWS_ACCESS_KEY_ID="DO00GTNRVVJ43WM94VC4"
AWS_SECRET_ACCESS_KEY="u9bGzZ9Mm3Bv2ySe6Ru7yK3mIxD3y3mM93guRWvI6Jc"
AWS_STORAGE_BUCKET_NAME="mysite"
#AWS_S3_ENDPOINT_URL="https://fra1.digitaloceanspaces.com"
AWS_S3_ENDPOINT_URL = "http://127.0.0.1:8000"
AWS_S3_OBJECT_PARAMETERS={
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION = "https://mysite.fra1.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "mysite.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = 'mysite.cdn.backends.StaticRootS3BotoStorage'

