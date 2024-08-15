import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    bucket = "abubakar-project4"  # Replace this with your actual S3 bucket name
    s3_key = "test/bicycle_s_000513.png"  # Replace this with your actual S3 key

    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, s3_key, '/tmp/image.png')

    # We read the data from the file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')  # Encode to base64 and decode to string for JSON serialization

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "s3_bucket": bucket,
            "s3_key": s3_key,
            "image_data": image_data,
            "inferences": []
        }
    }
