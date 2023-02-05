from flask import Flask
import time
import boto3

app = Flask(__name__)

client = boto3.client('dynamodb')

@app.route("/hello")
def hello_world():
    return "Hello, World! from flask"

@app.route('/sleep')
def sleep_handler():
    time.sleep(0.5)
    return "sleep .5 from flask"
    

@app.route('/ddb_get')
def ddb_get_handler():
    response = client.get_item(TableName="LoadTestingTable",
                    Key={
                        "pk": {"S": "test"},
                        "sk": {"S": "test1"}
                    })
    data = response.get("Item").get("data").get("S")
    return f"ddb_get response from flask: {data}"
