# Header가 고정되고 중간에 행이 그룹화해서 없어지는 것을 구현하려다 보니 jinja로 생성하기 어려워 아예 HTML로 만들어 전송하기 위해 만들었음.
def headerF(pagename):
    header1 = f'''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <!-- 타이틀에 해당하는 것을 블럭화한다. -->
        <title>Estimate</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.css" integrity="sha512-yHknP1/AwR+yx26cB1y0cjvQUMvEa2PFzt1c9LlS4pRQ5NOTZFWbhBig+X9G9eYW/8m0/4OXNx8pxJ6z57x0dw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick-theme.min.css" integrity="sha512-17EgCFERpgZKcm0j0fEq1YCJuyAWdz9KUtv1EjVuaOz8pDnh/0nZxmU6BBXwaaxqoi9PQXnRWqlcDB027hgv9A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        <link rel="stylesheet" href="{{ url_for('static', filename='css/app.css')}}" />

    </head>
    '''
    return header1


def bodyF(content):
    body1 = '''
        <div class="container-fluid">
    '''
    body_bt = '''

        <!-- <main> -->
            <div role="region" aria-label="data table" tabindex="0" class="primary">
                <!-- Note: use the aria-label attribute above to describe this keyboard-focusable region appropriately, per your implementation. Alternatively, it could instead be an aria-labelledby attribute that points to a table caption's ID attribute. Thx for thoughts, @aardrian  -->
                <table class="fold-table">
                
    '''
    body2 = '''
                </table>
            </div>
        <!-- </main> -->
        </div>
        </div>
    '''
    return (body1 + body_bt + content + body2)

def rootHtml(pagename, header, body):
    scripts_TH = '''
        <thead>
        <tr>
        '''
    for idx, header1 in enumerate(header,1):
        if idx <= 2 or idx == 4:
            pass
        else:
            add_scr = f"<th> {header1} </th> \n"
            scripts_TH = scripts_TH + add_scr
    scripts_TH = scripts_TH + "\n </tr> \n </thead>"
    scripts_bd = "<tbody>\n"
    expression = ""
    body3 = ""
    for body1 in body:
        add_scr_bd = ""
        if body1[3] == "%":
            expression = "%"
        else:
            expression = ""
        if body1[1] == 0:
            add_scr_bd = '<tr class="">\n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n"
        elif body1[1] == 1:
            add_scr_bd = '<tr class="view">\n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"   
            add_scr_bd = add_scr_bd + "</tr> \n"
        elif body1[1] == 2:
            add_scr_bd = '<tr class="fold">\n <td colspan="14"> \n <div class="fold-content"> \
            \n <table> \n <tr> \n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n"
        elif body1[1] == 3:
            add_scr_bd = '<tr class = ""> \n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n"
        else:
            add_scr_bd = '<tr> \n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n </table> \n </div> \n </td> \n </tr> \n"
        scripts_bd = scripts_bd + add_scr_bd
    scripts_bd = scripts_bd + "</tbody>"

    context1 = scripts_TH + scripts_bd
    # returnHtml = headerF(pagename) + bodyF(context1)
    return bodyF(context1)

def compareHtml(pagename, header, body):
    scripts_TH = '''
        <thead>
        <tr>
        '''
    for idx, header1 in enumerate(header,1):
        if idx <= 2 or idx == 4:
            pass
        else:
            add_scr = f"<th> {header1} </th> \n"
            scripts_TH = scripts_TH + add_scr
    scripts_TH = scripts_TH + "\n </tr> \n </thead>"
    scripts_bd = "<tbody>\n"
    expression = ""
    body3 = ""
    for body1 in body:
        add_scr_bd = ""
        if body1[3] == "%":
            expression = "%"
        else:
            expression = ""
        if body1[1] == 0:
            add_scr_bd = '<tr class="">\n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                elif idx == len(body1):
                    if expression == "%":
                        add_scr_bd = add_scr_bd + "<td></td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n"
        elif body1[1] == 1:
            add_scr_bd = '<tr class="view">\n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                elif idx == len(body1):
                    if expression == "%":
                        add_scr_bd = add_scr_bd + "<td></td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"   
            add_scr_bd = add_scr_bd + "</tr> \n"
        elif body1[1] == 2:
            add_scr_bd = '<tr class="fold">\n <td colspan="17"> \n <div class="fold-content"> \
            \n <table> \n <tr> \n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                elif idx == len(body1):
                    if expression == "%":
                        add_scr_bd = add_scr_bd + "<td></td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n"
        elif body1[1] == 3:
            add_scr_bd = '<tr class = ""> \n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                elif idx == len(body1):
                    if expression == "%":
                        add_scr_bd = add_scr_bd + "<td></td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n"
        else:
            add_scr_bd = '<tr> \n'
            for idx,body2 in enumerate(body1,1):
                if idx < 3:
                    pass
                elif idx == 3:
                    add_scr_bd = add_scr_bd + f"<th>{body2}</th>\n"
                elif idx == 4:
                    pass
                elif idx == len(body1):
                    if expression == "%":
                        add_scr_bd = add_scr_bd + "<td></td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                else:
                    if expression == "%":
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{body2:.1f}%</td>\n"
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
                    else:
                        try:
                            add_scr_bd = add_scr_bd + f"<td>{int(round(body2,0)):,d}</td>\n"   
                        except:
                            add_scr_bd = add_scr_bd + f"<td>N/A</td>\n"
            add_scr_bd = add_scr_bd + "</tr> \n </table> \n </div> \n </td> \n </tr> \n"
        scripts_bd = scripts_bd + add_scr_bd
    scripts_bd = scripts_bd + "</tbody>"

    context1 = scripts_TH + scripts_bd
    # returnHtml = headerF(pagename) + bodyF(context1)
    return bodyF(context1)