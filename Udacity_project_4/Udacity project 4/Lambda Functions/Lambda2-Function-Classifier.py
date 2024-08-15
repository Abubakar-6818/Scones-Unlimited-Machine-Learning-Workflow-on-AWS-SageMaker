import json
import sagemaker
import base64

import boto3

from sagemaker.predictor import Predictor
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2024-08-10-14-04-45-024"## TODO: fill in

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event["body"]["image_data"])

    # Create a SageMaker runtime client
    runtime = boto3.client('sagemaker-runtime')

    # Make a prediction
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='application/x-image',  
        Body=image
    )

    # Decode the inferences to get the list not the string of list
    
    inferences = json.loads(response['Body'].read().decode('utf-8'))

    # We return the data back to the Step Function    
    event["inferences"] = inferences
    return {
        'statusCode': 200,
        'body': {
            "image_data": event["body"]['image_data'],
            "s3_bucket": event["body"]['s3_bucket'],
            "s3_key": event["body"]['s3_key'],
            "inferences": event['inferences'],
                     }
                        }