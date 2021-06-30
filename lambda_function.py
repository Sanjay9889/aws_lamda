import json
import pandas as pd


def lambda_handler(event, context):

    data = {
        "name": ["Sanjay", "Jitendra", "Rahul"],
        "age": [30, 28, 23]
    }
    df = pd.DataFrame(data)
    print("*" * 50)
    print(df)
    print("*" * 50)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
