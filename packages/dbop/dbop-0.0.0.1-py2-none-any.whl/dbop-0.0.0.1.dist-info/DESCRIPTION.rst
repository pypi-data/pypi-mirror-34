Info
====
`dbop 2018-08-10`

`Author: Zhao Mingming <471106585@qq.com>`

`Copyright: This module has been placed in the public domain.`

`version:0.0.0.1`

Classes:
- `dbop`: oprate the mysql db 

Functions:

- `test()`: test function  

How To Use This Module
======================
.. image:: funny.gif
   :height: 100px
   :width: 100px
   :alt: funny cat picture
   :align: center

1. example code:

.. code:: python
from dbop import dbop as dbop
    #pool = PooledDB(MySQLdb,1,host='122.152.206.246',user='oco',passwd='MyNewPass4!',db='task_zmm',port=3306,charset='utf8')
    #dbb0=dbop("122.152.206.246","oco","MyNewPass4!")
    #db0l=dbb0.run("show databases;")
    #print(db0l)
    dbb=dbop("172.23.250.51","root","20180712")
    dbl=dbb.run("show databases;") 
    #print dbb.run("use test0720")
    #print dbb.run("desc test0720xml")
    xml_num=0
    jpg_num=0
    for dbname in dbl:
        if "fourgesture_detection_train" not in  dbname[0]:
            continue
        #print dbname
        sqlstr="use %s;"%(dbname[0])
        dbb.run(sqlstr) 
        sqlstr="select count(*) from %sxml;"%(dbname[0])
	rr=dbb.run(sqlstr) 
        xml_num+=dbb.getnum(rr)
        xml_numtmp=dbb.getnum(rr)
        sqlstr="select count(*) from %simg"%(dbname[0])
	rr=dbb.run(sqlstr) 
        jpg_num+=dbb.getnum(rr)
        jpg_numtmp=dbb.getnum(rr)
        if xml_numtmp>0:
            print dbname[0]
	    print "xmltmp:%d,jpgtmp:%s"%(xml_numtmp,jpg_numtmp)
	    print "xml:%d,jpg:%s"%(xml_num,jpg_num)
    print dbb.help("sql") 
    #print len(dbl)
    #print type(list(dbl))
    #for db in dbl:
    #    print list(db)



Refresh
========



