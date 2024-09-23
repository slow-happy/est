from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email, Length

# 화일을 업로드하기 위한 form, EXCEL 화일만 가능함
class UploadImageForm(FlaskForm):
    # 파일 업로드에 필요한 유효성 검증을 설정한다.
    # version = SelectField(
    #     "추정버전",
    #     choices = [('2023-01-1st',"23년1월1차"),('2023-01-2nd',"23년1월2차")]
    # )
    image = FileField(
        validators=[FileRequired("해당하는 추정화일을 선택해 주세요."),
        FileAllowed(["xlsx","xls"], "지원되지 않는 이미지 형식입니다."),]
    )
    submit = SubmitField("업로드")

# 추정 버전을 관리하기 위한 폼
class manageForm(FlaskForm):
    year1 = StringField(
        "년도",
        validators=[
            DataRequired("년도입력은 필수입니다."),
            Length(4,4,"YYYY 형태로 입력해야합니다."),
        ]
    )
    month1 = StringField(
        "추정시작월",
        validators=[
            DataRequired("추정월 입력은 필수입니다."),
            Length(2,2,"MM 형태로 입력해야합니다."),
        ]
    )
    month2 = StringField(
        "추정종료월",
        validators=[
            DataRequired("추정월 입력은 필수입니다."),
            Length(2,2,"MM 형태로 입력해야합니다."),
        ]
    )
    version = StringField(
        "버전",
        validators=[
        DataRequired("버전을 입력하세요."),
        Length(3,6,"영어의 서수를 이용하세요(예, 1st, 4th, etc.)."),
        ]
    )
    submit = SubmitField("버전생성")

# 특별 관리 사항 입력용 form
class descForm(FlaskForm):
    content = StringField(
        "입력내용",
        validators=[
            DataRequired("내용을입력해주십시요."),
        ]
    )
    description = StringField(
        "상세",
    )

    tot_amt = StringField(
        "총금액",
        validators=[
        DataRequired("백만원단위로 입력하십시요."),
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    jan_amt = StringField(
        "1월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    feb_amt = StringField(
        "2월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    mar_amt = StringField(
        "3월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    apr_amt = StringField(
        "4월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    may_amt = StringField(
        "5월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    jun_amt = StringField(
        "6월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    jul_amt = StringField(
        "7월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    aug_amt = StringField(
        "8월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    sep_amt = StringField(
        "9월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    oct_amt = StringField(
        "10월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    nov_amt = StringField(
        "11월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )

    dec_amt = StringField(
        "12월",
        validators=[
        Length(0,10,"백만원단위로입력하십시요"),
        ]
    )


    submit = SubmitField("입력")

# 진행 절차를 표현하기 위한 폼 : 아직 앱으로 구현하지는 않았음
class procedureForm(FlaskForm):
    fxInputted = StringField(
        "환율입력여부",
        validators=[
        Length(0,1,"checkbox"),
        ]
    )
    fxFinished = StringField(
        "환율환산여부",
        validators=[
        Length(0,1,"checkbox"),
        ]
    )
    getTotal = StringField(
        "단순합산실시여부",
        validators=[
        Length(0,1,"checkbox"),
        ]
    )
    getOthers = StringField(
        "기타매출원가입력여부",
        validators=[
        Length(0,1,"checkbox"),
        ]
    )
    getFinal = StringField(
        "추정완료여부",
        validators=[
        Length(0,1,"checkbox"),
        ]
    )