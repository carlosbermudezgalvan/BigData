import json
import boto3 
import urllib.request
from datetime import datetime

def lambda_handler(event, context):
    # Leer pagina web
	with urllib.request.urlopen('https://www.eltiempo.com') as response:
		html = response.read()
	
	# Guardar en bucket
	s3_client = boto3.client('s3')
	key = str(datetime.now())+".html"
	s3_client.put_object(Body=html, Bucket='carlosbucketsss', Key=key, ContentType='text/html')
	return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
