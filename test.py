"""女男比例"""
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


sex_stu = pygal.Bar()
sex_stu.title = "各年级女生男生比例最高的专业"
sex_stu.x_title = "所在年级及专业"
sex_stu.y_title = "女生男生比例"
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

        if sexma==0:
            sexma=1
        sexdict[pro] = sexmo/sexma
    maxsex=max(zip(sexdict.values(),sexdict.keys()))
    sexlist_V.append(maxsex[0])
    sexlist_K.append(maxsex[1])

sex_stu.add("女生男生比例", sexlist_V)
label = map(str, range(2014, 2019))
# print("\n\n\ntype(label){}\tlabel{}\n\n\n".format(type(label),label))
li=[]
x=0
sexlist_K=list(sexlist_K)
for i in label: 
    li.append(i + "级"+sexlist_K[x][0])
    x=x+1
sex_stu.x_labels = li
sex_stu.render_to_file("sexstu1.svg")
webbrowser.get('google-chrome').open("sexstu1.svg")

