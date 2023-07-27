from services.user_service import UserService
from models.user import User
from tests import app_context

def test_create_user(app_context):
    with app_context:
        user_service = UserService()
        # Test creating a user with valid input
        user = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        assert user.username == 'testuser'
        assert user.password == 'testpassword'
        assert user.email == 'testuser@example.com'
        # Test creating a user with an empty username
        user = user_service.create_user('', 'testpassword', 'testuser@example.com')
        assert user is None
        # Test creating a user with an empty password
        user = user_service.create_user('testuser', '', 'testuser@example.com')
        assert user is None
        # Test creating a user with an empty email
        user = user_service.create_user('testuser', 'testpassword', '')
        assert user is None
        # Test creating a user with a username that exceeds the maximum length allowed by the database
        user = user_service.create_user('a'*51, 'testpassword', 'testuser@example.com')
        assert user is None
        # Test creating a user with a password that exceeds the maximum length allowed by the database
        user = user_service.create_user('testuser', 'a'*51, 'testuser@example.com')
        assert user is None
        # Test creating a user with an email that exceeds the maximum length allowed by the database
        user = user_service.create_user('testuser', 'testpassword', 'a'*121)
        assert user is None
        # Test creating a user with a username that already exists in the database
        user1 = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        user2 = user_service.create_user('testuser', 'testpassword', 'testuser2@example.com')
        assert user2 is None
        # Test creating a user with an email that already exists in the database
        user1 = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        user2 = user_service.create_user('testuser2', 'testpassword', 'testuser@example.com')
        assert user2 is None

def test_get_user_by_username(app_context):
    with app_context:
        user_service = UserService()
        # Test getting a user by a valid username
        user = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        assert user_service.get_user_by_username('testuser') == user
        # Test getting a user by a username that does not exist in the database
        assert user_service.get_user_by_username('nonexistentuser') is None

def test_get_user_by_email(app_context):
    with app_context:
        user_service = UserService()
        # Test getting a user by a valid email
        user = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        assert user_service.get_user_by_email('testuser@example.com') == user
        # Test getting a user by an email that does not exist in the database
        assert user_service.get_user_by_email('nonexistentuser@example.com') is None

def test_get_user_by_id(app_context):
    with app_context:
        user_service = UserService()
        # Test getting a user by a valid ID
        user = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        assert user_service.get_user_by_id(user.id) == user
        # Test getting a user by an ID that does not exist in the database
        assert user_service.get_user_by_id(999) is None

def test_get_all_users(app_context):
    with app_context:
        user_service = UserService()
        # Test getting all users when there are no users in the database
        assert user_service.get_all_users() == []
        # Test getting all users when there are multiple users in the database
        user1 = user_service.create_user('testuser1', 'testpassword1', 'testuser1@example.com')
        user2 = user_service.create_user('testuser2', 'testpassword2', 'testuser2@example.com')
        assert user_service.get_all_users() == [user1, user2]

def test_delete_user(app_context):
    with app_context:
        user_service = UserService()
        # Test deleting a user that exists in the database
        user = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        user_service.delete_user(user)
        assert user_service.get_user_by_id(user.id) is None
        # Test deleting a user that does not exist in the database
        # user = User(username='testuser', password='testpassword', email='testuser@example.com')
        # assert user_service.delete_user(user) is None

def test_update_user(app_context):
    with app_context:
        user_service = UserService()
        # Test updating a user with valid input
        user = user_service.create_user('testuser', 'testpassword', 'testuser@example.com')
        user_service.update_user(user, 'newusername', 'newpassword', 'newemail@example.com')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.username == 'newusername'
        assert updated_user.password == 'newpassword'
        assert updated_user.email == 'newemail@example.com'
        # Test updating a user with an empty username
        user_service.update_user(user, username='')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.username == 'newusername'
        # Test updating a user with an empty password
        user_service.update_user(user, password='')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.password == 'newpassword'
        # Test updating a user with an empty email
        user_service.update_user(user, email='')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.email == 'newemail@example.com'
        # Test updating a user with a username that exceeds the maximum length allowed by the database
        user_service.update_user(user, 'a'*51, 'newpassword', 'newemail@example.com')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.username == 'newusername'
        # Test updating a user with a password that exceeds the maximum length allowed by the database
        user_service.update_user(user, 'newusername', 'a'*51, 'newemail@example.com')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.password == 'newpassword'
        # Test updating a user with an email that exceeds the maximum length allowed by the database
        user_service.update_user(user, 'newusername', 'newpassword', 'a'*121)
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.email == 'newemail@example.com'
        # Test updating a user with a username that already exists in the database
        user2 = user_service.create_user('testuser2', 'testpassword2', 'testuser2@example.com')
        user_service.update_user(user, 'testuser2', 'newpassword', 'newemail@example.com')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.username == 'newusername'
        # Test updating a user with an email that already exists in the database
        user2 = user_service.create_user('testuser2', 'testpassword2', 'testuser2@example.com')
        user_service.update_user(user, 'newusername', 'newpassword', 'testuser2@example.com')
        updated_user = user_service.get_user_by_id(user.id)
        assert updated_user.email == 'newemail@example.com'