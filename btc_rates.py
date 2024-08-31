import datetime
import json
import boto3

# Initialize a session using Amazon S3
# Your opterating system will know the credentials if you saved them correctly
s3 = boto3.client('s3')

# Specify the name of your bucket
bucket_name = 'your_bucket_name'
# Get current time to name files
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Specify the S3 object key
s3_object_current_key = 'folder1/btc_rate_current.json'
s3_object_historical_key = f'folder2/btc_rate_[{current_time}].json'

try:
    # I have a function to get the BTC price, but for this example, I will hard code it
    rate = 50000.00
    # Create dictionaries, add rate data, and convert to json
    btc_rate_current = {}
    btc_rate_current_historical = {}
    btc_rate_current["btc_rate_current_dollars"] = rate
    btc_rate_current_historical[current_time] = rate
    btc_rate_current = json.dumps(btc_rate_current)
    btc_rate_current_historical = json.dumps(btc_rate_current_historical)
    # Send to AWS s3 bucket
    s3.put_object(Bucket=bucket_name, Key=s3_object_current_key, Body=btc_rate_current, ContentType='application/json')
    s3.put_object(Bucket=bucket_name, Key=s3_object_historical_key, Body=btc_rate_current_historical, ContentType='application/json')
except Exception as e:
    print(str(e))
