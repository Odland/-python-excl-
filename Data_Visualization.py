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

# labels = "男", "女"
# sizes = [sex1, sex2]
# colors = ['yellow', "green"]
# plt.pie(sizes, labels=labels,colors=colors,
#        autopct='%1.4f%%', shadow=True,startangle=90)
# plt.axis('equal')
# plt.legend()
# plt.savefig("biu.png",bbox_inches='tight')
# plt.show()


# 绘制矢量图
sql = 'select 性别 from stu'
bingtu = pygal.Pie()
bingtu.title = "饼图"
sex1, sex2 = data_vis(db, sql)
bingtu.add("男", sex1)
bingtu.add("女", sex2)

# 使用浏览器打开一个矢量图
bingtu.render_to_file("pie.svg")
webbrowser.get('google-chrome').open("pie.svg")


# 绘制直方图显示各年级男女生人数

sexs1 = []
sexs2 = []

sexnum = pygal.Bar()
sexnum.title = "各年级男女生人数"
sexnum.x_title = "所在年级"
sexnum.y_title = "人数"
sexnum.y_labels = range(0, 2500, 100)
sexnum.x_labels = map(str, range(2014, 2019))
for i in range(2014, 2019):
    sql1 = "select 性别 from stu where 当前所在级={0}".format(i)
    sex1, sex2 = data_vis(db, sql1)
    sexs1.append(sex1)
    sexs2.append(sex2)

sexnum.add("男", sexs1)
sexnum.add("女", sexs2)
sexnum.render_to_file("sexnum.svg")
webbrowser.get('google-chrome').open("sexnum.svg")







# 各年级男女比例最高和最低的专业


sex_stu = pygal.Bar()
sex_stu.title = "各年级男女比例最高的专业"
sex_stu.x_title = "所在年级及专业"
sex_stu.y_title = "男女比"
cursor = db.cursor()

sexlist_V=[]
sexlist_K=[]
for gra in range(2014, 2019):
    # 先筛选出每一级的专业
    gra=str(gra)
    sqlgro = "select 专业名称 from stu where 当前所在级={} group by 专业名称".format(gra)
    cursor = db.cursor()
    cursor.execute(sqlgro)
    pros = cursor.fetchall()
    cursor.close()
    # print("\n\n\n{0}".format(gra))
    # print(type(gra))
    sexdict={}
    for pro in pros:
        sexma,sexmo = 0,0
        # print("\n\n\n{}\n{}\n\n\n".format(pro,gra))
        # print(type(pro[0]),type(gra))
        sqlsex="select 性别 from stu where 专业名称=\'{0}\' and 当前所在级={1}".format(pro[0],gra)
        # sexma,sexmo=data_vis(db,sqlsex)
        cursor = db.cursor()
        cursor.execute(sqlsex)
        sex = cursor.fetchall()
        for s in sex:
            if s[0]=="男":
                sexma = sexma + 1
            else:
                sexmo = sexmo + 1
        cursor.close()

        if sexmo==0:
            sexmo=1
        sexdict[pro] = sexma/sexmo
    maxsex=max(zip(sexdict.values(),sexdict.keys()))
    sexlist_V.append(maxsex[0])
    sexlist_K.append(maxsex[1])

sex_stu.add("男女比", sexlist_V)
label = map(str, range(2014, 2019))
# print("\n\n\ntype(label){}\tlabel{}\n\n\n".format(type(label),label))
li=[]
x=0
sexlist_K=list(sexlist_K)
for i in label: 
    li.append(i + "级"+sexlist_K[x][0])
    x=x+1
sex_stu.x_labels = li
sex_stu.y_labels = range(0,20,1)
sex_stu.render_to_file("sexstu.svg")
webbrowser.get('google-chrome').open("sexstu.svg")


