import datetime

from db import AdminLogin, AdminSession


def generate_token():
    return ""


def admin_login(login, password, grant_type):
    if grant_type == password:
        return admin_session_start(login, password)
    return admin_session_refresh(grant_type)


def admin_session_start(login, password):
    for admin in AdminLogin.select().where(AdminLogin.login == login and AdminLogin.password == password):
        admin_id = admin.id
        access_token, refresh_token = generate_token(), generate_token()
        AdminSession.insert(access_token=access_token,
                            refresh_token=refresh_token,
                            admin_id=admin_id,
                            start_time=datetime.datetime.now()).execute()
        return {
            "status": 200,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "message": "OK"
        }

    return {
        "status": 404,
        "message": "Admin not found"
    }


def admin_session_refresh(refresh_token):
    if len(AdminSession.select().where(AdminSession.refresh_token == refresh_token)):
        access_token, new_refresh_token = generate_token(), generate_token()
        AdminSession.update(access_token=access_token,
                            refresh_token=new_refresh_token,
                            start_time=datetime.datetime.now()).where(AdminSession.refresh_token == refresh_token)
        return {
            "status": 200,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "message": "OK"
        }

    return {
        "status": 404,
        "message": "Session not found"
    }
