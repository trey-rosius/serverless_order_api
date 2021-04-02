from decimal import Decimal
import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
def load(event, context):

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    with table.batch_writer() as batch:
        
        batch.put_item(
            Item= {

                "order_no": "#6753",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }

                ]

            }
        )
        batch.put_item(
            Item={
                
                "order_no": "#6754",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        
        batch.put_item(
            Item={
                
                "order_no": "#6755",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                    
                
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        batch.put_item(
            
            Item={
                
                    
                "order_no": "#6756",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                    
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        batch.put_item(
            Item={
                
                "order_no": "#6757",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        
        batch.put_item(
            
            Item={
                
                "order_no": "#6758",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":5
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal4+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        batch.put_item(
            Item={
                "order_no": "#6759",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        batch.put_item(
            Item={
                "order_no": "#6760",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        batch.put_item(
            
            Item={
                "order_no": "#6761",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
        batch.put_item(
            Item={
                "order_no": "#6762",
                "order_date":"12 jan 2021, 08:28pm",
                "ordered_by":"https://rosius.s3.us-east-2.amazonaws.com/cropped_rosius.png",
                "total":"$26.40",
                "items":[
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal1+(1).jpg",
                "name":"Vegetable Mixups",
                "desc":"Vegetable Fritters with Egg",
                "price":"$10.20",
                "qty":3
                },
                {
                "pic":"https://rosius.s3.us-east-2.amazonaws.com/meal2+(1).jpeg",
                "name":"Chicken Mixed Salad",
                "desc":"Roasted Chicken, mixed with salad",
                "price":"$16.20",
                "qty":2
                }
                ]
            }
        )
    

    # create a response
    response = {
        "statusCode": 200,
        'headers': {
           'Access-Control-Allow-Origin': '*',
           'Access-Control-Allow-Credentials': True
            
            
        },
        "body": json.dumps("successful":"Items successfully loaded into database")
    }

    return response
