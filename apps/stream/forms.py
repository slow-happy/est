from flask_wtf.form import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.fields.simple import SubmitField

# 화일을 업로드하기 위한 form, EXCEL 화일만 가능함
class UploadExcelForm(FlaskForm):
    # 파일 업로드에 필요한 유효성 검증을 설정한다.
    # version = SelectField(
    #     "추정버전",
    #     choices = [('2023-01-1st',"23년1월1차"),('2023-01-2nd',"23년1월2차")]
    # )
    file_excel = FileField(
        validators=[FileRequired("해당하는 추정화일을 선택해 주세요."),
        FileAllowed(["xlsx","xls"], "지원되지 않는 이미지 형식입니다."),]
    )
    submit = SubmitField("업로드")