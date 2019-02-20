import xlrd
import MySQLdb


b = xlrd.open_workbook("student.xls")
sheet = b.sheets()[0]

db = MySQLdb.connect(
    user='root',
    passwd='256257',
    db='Excldata',
)
cb = db.cursor()


da='insert into  stu(考生号,生源省市代码,学号,姓名,性别,出生日期,身份证号,政治面貌,民族,院校名称,专业代码,专业名称,学制,学习形式,入学日期,当前所在级,预计毕业日期,修改时间,辍学时间) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
for ii in range(1, sheet.nrows):
        a=sheet.cell_value(ii,0)
        b1=sheet.cell_value(ii,1)
        c=sheet.cell_value(ii,2)
        d=sheet.cell_value(ii,3)
        e=sheet.cell_value(ii,4)
        f=sheet.cell_value(ii,5)
        g=sheet.cell_value(ii,6)
        h=sheet.cell_value(ii,7)
        i=sheet.cell_value(ii,8)
        j=sheet.cell_value(ii,9)
        k=sheet.cell_value(ii,10)
        l=sheet.cell_value(ii,11)
        m=sheet.cell_value(ii,12)
        n=sheet.cell_value(ii,13)
        o=sheet.cell_value(ii,14)
        p=sheet.cell_value(ii,15)
        q=sheet.cell_value(ii,16)
        w=sheet.cell_value(ii,17)
        x=sheet.cell_value(ii,18)
        
        va=(a,b1,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,w,x,)
        cb.execute(da,va)
        db.commit()
cb.close()
db.close()
print("导入成功！！！")


    

