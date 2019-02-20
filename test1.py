"""男女 女男比例最高的人数"""
import MySQLdb
import matplotlib.pyplot as plt
import webbrowser
import pygal

# 字符编码
plt.rcParams["font.sans-serif"] = ['SimHei']




db = MySQLdb.connect(
    user='root',
    password='256257',
    db='Excldata',
)

def data_vis(db, sql):
    cursor = db.cursor()
    sex1 = 0
    sex2 = 0
    cursor.execute(sql)
    sex = cursor.fetchall()
    for biu in sex:
        if biu[0] == '男':
            sex1 = sex1 + 1
        else:
            sex2 = sex2 + 1
    cursor.close()
    # db.close()
    return sex1, sex2




sex_stu = pygal.Bar()
sex_stu.title = "各年级男女比例最高的专业"
sex_stu.x_title = "所在年级及专业"
sex_stu.y_title = "男女比"
cursor = db.cursor()

sql1="select 性别 from stu where 当前所在级=2014 and 专业名称='城乡规划'"
sql2="select 性别 from stu where 当前所在级=2015 and 专业名称='文化产业管理'"
sql3="select 性别 from stu where 当前所在级=2016 and 专业名称='公共艺术'"
sql4="select 性别 from stu where 当前所在级=2017 and 专业名称='广告学'"
sql5="select 性别 from stu where 当前所在级=2014 and 专业名称='建筑学'"
sql6="select 性别 from stu where 当前所在级=2015 and 专业名称='土木工程'"
sql7="select 性别 from stu where 当前所在级=2016 and 专业名称='电气工程及其自动化'"
sql8="select 性别 from stu where 当前所在级=2017 and 专业名称='自动化'"
bi=[sql1,sql2,sql3,sql4,sql5,sql6,sql7,sql8]

sex1=0
sex2=0
sexs1=[]
sexs2=[]

sex_stu = pygal.Bar()
sex_stu.title = "各年级女生男生比例最高的专业人数"
sex_stu.x_title = "所在年级及专业"
sex_stu.y_title = "女生男生最高比例的男女人数"

for i in range(0,4):
    sex1,sex2=data_vis(db,bi[i])
    sexs1.append(sex1)
    sexs2.append(sex2)

sex_stu.add("男",sexs1)
sex_stu.add("女",sexs2)
sex_stu.x_labels="2014级城乡规划专业","2015级文化产业管理专业","2016级公共艺术专业","2017级广告学专业"
sex_stu.render_to_file("sexstu9.svg")
webbrowser.get('google-chrome').open("sexstu9.svg")



sex1=0
sex2=0
sexs1=[]
sexs2=[]

sex_stu1 = pygal.Bar()
sex_stu1.title = "各年级男女比例最高的专业人数"
sex_stu1.x_title = "所在年级及专业"
sex_stu1.y_title = "男女最高比例的男女人数"
for i in range(4,8):
    sex1,sex2=data_vis(db,bi[i])
    sexs1.append(sex1)
    sexs2.append(sex2)

sex_stu1.add("男",sexs1)
sex_stu1.add("女",sexs2)


sex_stu1.x_labels="2014级建筑学专业","2015级土木工程专业","2016级电气工程及其自动化专业","2017级自动化专业"
sex_stu1.render_to_file("sexstu2.svg")
webbrowser.get('google-chrome').open("sexstu2.svg")