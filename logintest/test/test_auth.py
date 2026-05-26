from auth import login, register
def test_user_login():
    assert login("admin","1234") == True
def  test_user_login_failed():
    assert  login("admin","wrongpassword") == False
def test_user_reg():
    assert register("jo") == "successfull failed"
def test_user_reg_success():
    assert register("john") == "successfull succeeded"