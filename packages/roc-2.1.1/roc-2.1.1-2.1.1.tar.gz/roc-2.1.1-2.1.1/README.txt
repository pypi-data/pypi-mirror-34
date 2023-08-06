####

运行办法：
   
    环境：python2    
    运行前先安装ROC,transform和conRoc,安装办法：
    pip install roc-2.1.1


    roc:
        输入：文件夹truth（标注结果文件夹）,test（模型输出的结果文件夹）,result(要保存的txt文本文档路径），roc(要保存的图片路径）
        python 
                from ROC import roc
                roc.roc("truth","test","result","roc")
        输出：roc和分数折线图,结果的文本文档
        PS:result 和roc不带格式（例：'D:\\python_work\\result')


    conRoc:
        输入：文件夹pre_file(需要绘图的txt所在的文件夹）,image(要保存的图片路径）
        python 
                from ROC import conRoc
                conRoc.conRoc("pre_file","image")
        输出：roc折线图
        PS:image不带格式（例：'D:\\python_work\\image') 
     
   
    txt2xml:
        输入：txt_file(txt格式标注信息所存放文件夹）
        python
                from transform import txt2xml
                txt2xml.txt2xml("txt_file","xml_file")
        输出：xml_file(xml格式标注信息所存放文件夹）  





文件夹说明：

transform文件夹：

txt2xml ：将txt格式文本转换为xml文件（每个txt文件转换为一个xml文件）
          需要转换的所有txt文件放在txt_file中，转换后的xml文件存放在xml_file中                    

  
ROC文件夹：

roc: 绘制roc曲线和分数曲线并计算acu。数据来源于db列表

IOU: 计算两矩形IOU,传入数据为每个矩形两条对角线的横纵坐标Reframe=[X1,Y1,X2,Y2],GTframe=[X1,Y1,X2,Y2]。

read:读取xml文件的所有标注的标签数据(xmin,ymin,xmax,ymax)。传入数据为待测试xml文档的元素对象。

Analyze_xml：解析xml文件并得出IOU比对中比对错误(重叠比率小于0.5）和比对正确的个数。
             输入：truth为标准xml文件所在的文件夹，test为待比对的xml文件所在的文件夹。


conROC文件夹:

conRoc:根据文件夹中的所有txt文件内容绘制曲线图（每个文件对应两条同色的折线）

####

                      
                
   
