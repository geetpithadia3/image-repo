# generate service class for image

from models.image import Image
from models import db
import boto3

class ImageService:
    def __init__(self, db=db):
        self.db = db

    # create image function that takes image blob and user id as parameters, stores the image in s3, gets the image url from s3, and creates the image in the database
    def create_image(self, image_blob, user_id):
        # check if image_blob is empty
        if image_blob == '':
            return None
        # check if user_id is empty
        if user_id == '':
            return None
        
        # create image in s3
        s3 = boto3.client('s3')
        # upload image to s3 with unique key having user_id and image_id
        s3.upload_fileobj(image_blob, 'image-repo-bucket', f'{user_id}/{image_blob.filename}')
        # get image url from s3
        image_url = f'https://image-repo-bucket.s3.amazonaws.com/{user_id}/raw/{image_blob.filename}'
        # get thumbnail url from s3
        thumbnail_url = f'https://image-repo-bucket.s3.amazonaws.com/{user_id}/thumbnail/{image_blob.filename}'
        # create image in database
        image = Image(file_url=image_url, thumbnail_url=thumbnail_url, user_id=user_id)
        self.db.session.add(image)
        self.db.session.commit()
        return image
    
    # get image function that takes image id as parameter and returns the image from the database
    def get_image(self, image_id):
        # check if image_id is empty
        if image_id == '':
            return None
        # get image from database
        image = Image.query.get(image_id)
        return image
    
    # get all images function that takes user id as parameter and returns all images from the database
    def get_all_images(self, user_id):
        # check if user_id is empty
        if user_id == '':
            return None
        # get all images from database
        images = Image.query.filter_by(user_id=user_id).all()
        return images
    
    # delete image function that takes image id as parameter and deletes the image from the database
    def delete_image(self, image_id):
        # check if image_id is empty
        if image_id == '':
            return None
        # delete image from database
        image = Image.query.get(image_id)
        self.db.session.delete(image)
        self.db.session.commit()
        return image
    
    

        





