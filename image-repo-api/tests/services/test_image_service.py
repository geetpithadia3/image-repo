import pytest
from models.image import Image
from services.image_service import ImageService
from unittest.mock import MagicMock
from tests import app_context

@pytest.fixture
def image_service(monkeypatch):
    # mock boto3 client and its methods
    mock_s3 = MagicMock()
    mock_s3.upload_fileobj.return_value = None
    monkeypatch.setattr('boto3.client', lambda x: mock_s3)

    return ImageService()


def test_create_image(image_service, app_context):
    # create test data
    image_blob = MagicMock()
    image_blob.filename = 'test.jpg'
    user_id = 'test_user_id'

    # call create_image method
    image = image_service.create_image(image_blob, user_id)

    # assert that image is not None
    assert image is not None
    # assert that file_url and thumbnail_url are not None
    assert image.file_url is not None
    assert image.thumbnail_url is not None
    # assert that user_id is correct
    assert image.user_id == user_id

def test_get_image(image_service,app_context):
    # create test data
    image_blob = MagicMock()
    image_blob.filename = 'test.jpg'
    user_id = 'test_user_id'

    # call create_image method
    image = image_service.create_image(image_blob, user_id)

    # call get_image method
    image = image_service.get_image(image.id)

    # assert that image is not None
    assert image is not None
    # assert that file_url and thumbnail_url are not None
    assert image.file_url is not None
    assert image.thumbnail_url is not None
    # assert that user_id is correct
    assert image.user_id == user_id

def test_get_all_images(image_service,app_context):
    # create test data
    image_blob = MagicMock()
    image_blob.filename = 'test.jpg'
    user_id = 'test_user_id'

    # call create_image method
    image = image_service.create_image(image_blob, user_id)

    # call get_all_images method
    images = image_service.get_all_images(user_id)

    # assert that images is not None
    assert images is not None
    # assert that images length is 1
    assert len(images) == 1
    # assert that file_url and thumbnail_url are not None
    assert images[0].file_url is not None
    assert images[0].thumbnail_url is not None
    # assert that user_id is correct
    assert images[0].user_id == user_id

def test_delete_image(image_service,app_context):
    # create test data
    image_blob = MagicMock()
    image_blob.filename = 'test.jpg'
    user_id = 'test_user_id'

    # call create_image method
    image = image_service.create_image(image_blob, user_id)

    # call delete_image method
    image_service.delete_image(image.id)

    # assert that image is None
    image = image_service.get_image(image.id)
    assert image is None

def test_create_image_empty_blob(image_service,app_context):
    # create test data
    image_blob = MagicMock()
    image_blob.filename = ''
    user_id = 'test_user_id'

    # call create_image method
    image = image_service.create_image(image_blob, user_id)

    # assert that image is None
    assert image is None

def test_create_image_empty_user_id(image_service,app_context): 
    # create test data
    image_blob = MagicMock()
    image_blob.filename = 'test.jpg'
    user_id = ''

    # call create_image method
    image = image_service.create_image(image_blob, user_id)

    # assert that image is None
    assert image is None

def test_get_image_invalid_id(image_service,app_context):
    # call get_image method
    image = image_service.get_image('invalid_id')

    # assert that image is None
    assert image is None

def test_get_all_images_invalid_user_id(image_service,app_context):
    # call get_all_images method
    images = image_service.get_all_images('invalid_user_id')

    # assert that images is not None
    assert images is not None
    # assert that images length is 0
    assert len(images) == 0

def test_delete_image_invalid_id(image_service,app_context):
    # call delete_image method
    image_service.delete_image('invalid_id')

    # assert that image is None
    image = image_service.get_image('invalid_id')
    assert image is None

def test_delete_image_empty_id(image_service,app_context):
    # call delete_image method
    image_service.delete_image('')

    # assert that image is None
    image = image_service.get_image('')
    assert image is None

def test_delete_image_none_id(image_service,app_context):
    # call delete_image method
    image_service.delete_image(None)

    # assert that image is None
    image = image_service.get_image(None)
    assert image is None


