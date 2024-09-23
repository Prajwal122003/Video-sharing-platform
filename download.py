import boto3
from botocore.exceptions import NoCredentialsError

s3_client = boto3.client('s3')

def generate_presigned_url(bucket_name, object_name, expiration=3600):
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except NoCredentialsError:
        print("Credentials not available")
        return None

    return response

bucket_name = '<bucket_name>'
object_name = '<object_name>'
url = generate_presigned_url(bucket_name, object_name)

print(f"Download URL: {url}")
