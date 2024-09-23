from flask import Blueprint, render_template, url_for, redirect, request, current_app
from flask_login import current_user, login_required
from apps.estimate import varGroup
# , mkHtml, queries
import pandas as pd
from sqlalchemy import create_engine, select, delete, and_, insert, func
from apps.stream.models import salesRecord, salesGroupMaster
from apps.stream.forms import UploadExcelForm
from apps.estimate.models import currentVersion
from pathlib import Path
import openpyxl
# from apps.app import db
from datetime import datetime

g_year = '2022'
g_version = '2022-10-1st'
g_comp = '1000'
g_mm = '01'
g_tomm = '01'
engine = create_engine(varGroup.mysql_url)

# est를 블루프린트화한다.
stream = Blueprint(
    "stream",
    __name__,
    template_folder="templates",
    static_folder="static"
    )

@stream.before_request
def authonticate():
    global g_year, g_version, g_comp, g_mm, g_tomm
    sql1 = select(currentVersion)
    with engine.connect() as conn:
        result = conn.execute(sql1).first()
    if result is not None:
        list_result = list(result)
        g_year = list_result[2]
        g_version = list_result[1]
        g_comp = list_result[5]
        g_mm = list_result[3]
        g_tomm = list_result[4]
    # print(g_year, g_version, g_comp)


# dt 애플리케이션을 사용하여 앤드 포인트를 작성한다.
@stream.route("/")
def index():
    return redirect(url_for("est.index"))


# 판매계획 입력
@stream.route("/uploadsales", methods=["GET","POST"])
@login_required
def uploadSales():
    global g_version, g_year
    print(g_version, g_year)
    # print('여긴가?')
    form=UploadExcelForm()
    if form.validate_on_submit():
        # 업로드된 이미지 파일을 취득한다.
        file=form.file_excel.data
        # 파일의 파일명과 확장자를 취득하고, 파일명을 uuid로 변화한다.
        ext = Path(file.filename).suffix
        file_name = str(request.form['ver'])+ "판매" + ext
        # 이미지를 저장한다.
        image_path = Path(current_app.config["UPLOAD_FOLDER"], file_name)
        # image_path = Path(current_app.config["UPLOAD_FOLDER"], image_uuid_file_name)
        # file.save(image_path)
        # print('여기가 아닌가?', image_path, '/n', current_app.config["UPLOAD_FOLDER"])

        # 손익계산서에 내용을 업데이트 한다. 
        file1 = openpyxl.load_workbook(file)
        sheet1 = file1.active
        if sheet1['A1'].value != '달력 연도':
            print("excel 양식을 확인하십시요.",sheet1['B4'].value)
        # range1 = sheet1['A2':'N118']
        list1 = []
        for row in sheet1:
            list_rows = []
            for col in row:
                list_rows.append(col.value)
            list1.append(list_rows)
        df_header = ['year','yyyymm','SalesType','company','companyName','SalesGroup','SalesGroupName','DistributeChannel','DistributeChannelName','Usage','Origin','ProdPlant','ProdGrp','ProdGrpName','Rim','subGroup','HVP','HVP2','curr','EA','Weight','Sales','CGS','CGM','Material','DirectLabor','IndirectLabor','DirectOH','IndirectOH','Freight','Insure_ex','CGS_other','CustomReturn','GP','SalesExpences','AdminExpences','OperatingProfit2']
        df1 = pd.DataFrame(list1)
        df1.columns = df_header
        df2=df1.iloc[1:,1:]
        df2['version'] = request.form['PorA']
        df2['year'] = request.form['year1']
        df2['mm'] = request.form['month1']
        df2["create_at"]=datetime.now()
        df_header.insert(1,'mm')
        df_header.insert(0,'version')
        df_header.append('create_at')
        df3 = df2.loc[:,df_header]
        print(df3, '\n', df_header, datetime.now())

        sql1 = delete(salesRecord).where(and_(salesRecord.version == request.form['PorA'],salesRecord.year == request.form['year1'],salesRecord.mm == request.form['month1']))
        with engine.connect() as conn:
            result = conn.execute(sql1)
            conn.commit()
        df3.to_sql(name='sales_record', con=engine, if_exists='append', index=False)
        try:
            del([df1,df2,df3])
        except:
            pass
        return redirect(url_for("stream.uploadSales"))
    find_version = select(currentVersion.version).group_by(currentVersion.version)
    find_year = select(currentVersion.year).group_by(currentVersion.year)
    # searchingSales = select(salesEstimate.mm, salesEstimate.amount_sales, salesEstimate.amount_EA, salesEstimate.amount_weight).where(and_(salesEstimate.version == g_version,salesEstimate.salesDivision == '연결'))

    with engine.connect() as conn:
        ver1 = list(conn.execute(find_version))
        YYYY = list(conn.execute(find_year))
        # checkSales = list(conn.execute(searchingSales))

    # result = []
    # header = ['구분','1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']

    # if checkSales == []:
    #     pass
    # else:
    #     df = pd.DataFrame(checkSales)
    #     # print(df)
    #     # df['wonPerWeight'] = df['amount_sales']/df['amount_weight']*1000
    #     df_target = pd.DataFrame(df['amount_sales']).set_axis(labels=['col1'],axis=1).astype({'col1':'float64'})
    #     df_base = pd.DataFrame(df['amount_weight']).set_axis(labels=['col1'],axis=1).astype({'col1':'float64'})
    #     df_r = df_target.div(df_base).mul(1000).astype({'col1':'float64'}).round(0)
        
    #     # df['wonPerWeight'] = df['amount_sales'].div(df['amount_weight']).mul(100)
    #     # df.fillna(0)
    #     df1_1 = pd.concat([df,df_r],axis=1)
    #     df1_1.columns = ['mm','01.매출액(백만)','02.판매수량(천본)','03.중량(ton)','04.중량단가(원/kg)']
    #     df2 = df1_1.round(0)
    #     df3 = df2.melt(id_vars='mm', value_vars=['01.매출액(백만)','02.판매수량(천본)','03.중량(ton)','04.중량단가(원/kg)'])
    #     df3 = df3.pivot(index = 'variable', columns = 'mm', values='value')
    #     df3.reset_index(level=0, inplace=True)
    #     result = df3.round(0).values.tolist()
    #     # result.insert(0,header)
    #     try:
    #         del([df,df2,df3,df1_1,df_target,df_base,df_r])
    #     except:
    #         pass

    return render_template("stream/uploadsales.html", form=form, YYYY = YYYY, ver1 = ver1)
# , result = result, header = header)


# 판매계획 입력
@stream.route("/divisionmaster", methods=["GET","POST"])
@login_required
def salesMaster():

    form=UploadExcelForm()
    if form.validate_on_submit():
        # 업로드된 이미지 파일을 취득한다.
        file=form.file_excel.data
        # 파일의 파일명과 확장자를 취득하고, 파일명을 uuid로 변화한다.
        ext = Path(file.filename).suffix
        file_name = "조직마스터" + str(datetime.today())+ ext
        # 화일을 저장한다.
        image_path = Path(current_app.config["UPLOAD_FOLDER"], file_name)
        # file.save(image_path)

        # 손익계산서에 내용을 업데이트 한다. 
        file1 = openpyxl.load_workbook(file)
        sheet1 = file1.active
        if sheet1['A1'].value != '영업그룹':
            print("excel 양식을 확인하십시요.",sheet1['B4'].value)
        # range1 = sheet1['A2':'N118']
        list1 = []
        for row in sheet1:
            list_rows = []
            for col in row:
                list_rows.append(col.value)
            list1.append(list_rows)
        df_header = ['SalesGroup','DistributeChannel','Group_lv1','Group_lv2','Group_lv3','Group_lv4',
                     'curr_lv1','curr_lv2','curr_lv3','curr_lv4',
                     'Group_lv1_code', 'Group_lv2_code', 'Group_lv3_code', 'Group_lv4_code']
        df1 = pd.DataFrame(list1)
        df1.columns = df_header
        df2=df1.iloc[1:,:]
        df2["create_at"]=datetime.now()
        df_header.append('create_at')
        df3 = df2.loc[:,df_header]
        print(df3, '\n', df_header, datetime.now())

        sql1 = delete(salesGroupMaster)
        with engine.connect() as conn:
            result = conn.execute(sql1)
            conn.commit()
        df3.to_sql(name='sales_group', con=engine, if_exists='append', index=False)
        try:
            del([df1,df2,df3])
        except:
            pass
        return redirect(url_for("stream.salesMaster"))

    return render_template("stream/uploadsalesmaster.html", form=form)
# , result = result, header = header)
