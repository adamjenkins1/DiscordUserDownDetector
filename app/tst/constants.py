"""test constants module"""
TEST_GUILD_ID = 123
TEST_USERNAME = 'asdf'
TEST_USER_STATUS = 'online'
TEST_URI = f'/guild/{TEST_GUILD_ID}/username/{TEST_USERNAME}'
TEST_EMPTY_WIDGET_RESPONSE = {
    'id': TEST_GUILD_ID,
    'members': []
}
TEST_POPULATED_WIDGET_RESPONSE = {
    'id': TEST_GUILD_ID,
    'members': [
        {
            'username': TEST_USERNAME,
            'status': TEST_USER_STATUS,
        }
    ]
}
