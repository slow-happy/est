from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager

# SQLAlchemy를 인스턴스화 한다. 
db = SQLAlchemy()
csrf = CSRFProtect()
# LoginManager를 인스턴스화 한다.
login_manager = LoginManager()
# 로그인을 하지 않았을 경우 리다이렉트하는 엔드 포인트를 지정한다.
login_manager.login_view = "auth.login"
# login_manager 속성에 로기인 후에 표시할 메시지를 지정한다.
# 여기서는 일단 패스
login_manager.login_message = ""

# create_app 함수를 작성한다.
def create_app(config_key):
    # 플라스크 인스턴스를 생성한다. 
    
    app = Flask(__name__)
    # app의 config를 설정한다.
    app.config.from_object(config[config_key])

    # Sqlalchemy와 앱을 연계한다. 
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    # migrate와 앱을 연계한다. 
    Migrate(app, db)

    # crud를 불러와 main app에 연계하는 작업
    from apps.crud import views as crud_views
    # register_blueprint를 사용해 views의 crud를 앱에 등록한다.
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # 인증하는 앱을 만들어 본체에 add한다. 
    from apps.auth import views as auth_views
    # register_blueprint를 사용해 views의 auth를 앱에 등록한다.
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # 메인 app을 만들어 register_blueprint를 사용해 앱에 등록한다. 
    from apps.estimate import views as co_views
    app.register_blueprint(co_views.est)

    # 메인 app을 만들어 register_blueprint를 사용해 앱에 등록한다. 
    from apps.stream import views as st_views
    app.register_blueprint(st_views.stream, url_prefix='/stream')

    return app

    