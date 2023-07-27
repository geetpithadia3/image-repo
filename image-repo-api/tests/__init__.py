import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

@pytest.fixture
def app_context():
    app = create_app()
    with app.app_context() as app_context:
        yield app_context
        
@pytest.fixture
def mock_db_session(mocker):
    # Create a mock database session object
    session = mocker.Mock()
    # Set the commit method to do nothing
    session.commit = mocker.Mock(return_value=None)
    # Set the add method to add the object to a list
    added_objects = []
    def add(obj):
        added_objects.append(obj)
    session.add = mocker.Mock(side_effect=add)
    # Yield the session object
    yield session
    # Clear the list of added objects
    added_objects.clear()
