####

���а취��
   
    ������python2    
    ����ǰ�Ȱ�װROC,transform��conRoc,��װ�취��
    pip install roc-2.1.1


    roc:
        ���룺�ļ���truth����ע����ļ��У�,test��ģ������Ľ���ļ��У�,result(Ҫ�����txt�ı��ĵ�·������roc(Ҫ�����ͼƬ·����
        python 
                from ROC import roc
                roc.roc("truth","test","result","roc")
        �����roc�ͷ�������ͼ,������ı��ĵ�
        PS:result ��roc������ʽ������'D:\\python_work\\result')


    conRoc:
        ���룺�ļ���pre_file(��Ҫ��ͼ��txt���ڵ��ļ��У�,image(Ҫ�����ͼƬ·����
        python 
                from ROC import conRoc
                conRoc.conRoc("pre_file","image")
        �����roc����ͼ
        PS:image������ʽ������'D:\\python_work\\image') 
     
   
    txt2xml:
        ���룺txt_file(txt��ʽ��ע��Ϣ������ļ��У�
        python
                from transform import txt2xml
                txt2xml.txt2xml("txt_file","xml_file")
        �����xml_file(xml��ʽ��ע��Ϣ������ļ��У�  





�ļ���˵����

transform�ļ��У�

txt2xml ����txt��ʽ�ı�ת��Ϊxml�ļ���ÿ��txt�ļ�ת��Ϊһ��xml�ļ���
          ��Ҫת��������txt�ļ�����txt_file�У�ת�����xml�ļ������xml_file��                    

  
ROC�ļ��У�

roc: ����roc���ߺͷ������߲�����acu��������Դ��db�б�

IOU: ����������IOU,��������Ϊÿ�����������Խ��ߵĺ�������Reframe=[X1,Y1,X2,Y2],GTframe=[X1,Y1,X2,Y2]��

read:��ȡxml�ļ������б�ע�ı�ǩ����(xmin,ymin,xmax,ymax)����������Ϊ������xml�ĵ���Ԫ�ض���

Analyze_xml������xml�ļ����ó�IOU�ȶ��бȶԴ���(�ص�����С��0.5���ͱȶ���ȷ�ĸ�����
             ���룺truthΪ��׼xml�ļ����ڵ��ļ��У�testΪ���ȶԵ�xml�ļ����ڵ��ļ��С�


conROC�ļ���:

conRoc:�����ļ����е�����txt�ļ����ݻ�������ͼ��ÿ���ļ���Ӧ����ͬɫ�����ߣ�

####

                      
                
   
