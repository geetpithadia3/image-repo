import json
import PIL.Image as Image
import boto3


def lambda_handler(event, context):
    # get image url from event
    image_url = event['Records'][0]['s3']['object']['key']

    # compress image
    client = boto3.client('s3')
    
    image_obj=client.get_object(Bucket='image-repo-bucket', Key=image_url)
    image = Image.open(image_obj['Body'])
    img=image.convert('RGB')
    size=128,128
    img.thumbnail(size)
    img.save('/tmp/compressed.jpg')
    client.put_object(Bucket='image-repo-bucket', Key='compressed-images/compressed.jpg', Body=open('/tmp/compressed.jpg', 'rb'))

    return {
        'statusCode': 200,
        'body': json.dumps('Image compressed successfully!')
    }




