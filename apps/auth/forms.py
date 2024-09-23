from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(FlaskForm):
    username = StringField(
        "사용자명",
        validators=[
            DataRequired("사용자명은 필수입니다."),
            Length(1, 30, "최대 30자입니다.")
        ],
    )
    email = StringField(
        "메일주소",
        validators=[
            DataRequired("이메일을 입력해 주세요."),
            Email("메일주소의 형식으로 입력해주세요.")
        ],
    )
    password = PasswordField(
        "비밀번호",
        validators=[DataRequired("메일주소는 필수입니다.")]
    )
    submit = SubmitField("신규등록")

class LoginForm(FlaskForm):
    email = StringField(
        "메일주소",
        validators=[
            DataRequired("이메일을 입력해 주세요."),
            Email("메일주소의 형식으로 입력해주세요.")
        ],
    )
    password = PasswordField(
        "비밀번호",
        validators=[DataRequired("메일주소는 필수입니다.")]
    )
    submit = SubmitField("로그인")