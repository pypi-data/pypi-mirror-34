��Ʊ��Ϣ����

��Ʊ��������Ӧ��Ӧ�á�����K����ʷÿ�죨�Դӿ������𣩣��߿����գ��ɽ����ȸ�������

������pip install tuStockSpider ������Ŀ��

֮����tuStockSpidert��·���£�����

/lib/python3/site-packages/tuStockSpider

ʹ��

�ڱ༭����

import tuStockSpider as tss

tss.download_history_data('000002','D:/temp/data/') #����000002���ݵ�D:/temp/data/�ļ���

tss.download_history_data('000002') #����000002���ݵ�Ĭ�ϵ�/lib/python3/site-packages/tuStockSpider/data�ļ���

#����download_all_hitory()���ٶ������Ҷ������

tss.download_all_hitory('') #����ȫ����Ʊ����

tss.download_all_hitory('sz') #����ȫ������֤ȯ��������Ʊ����

tss.download_all_hitory('sh','shdata/') #����ȫ���Ϻ�֤ȯ��������Ʊ���ݵ�shdata�ļ���

�汾���� pip install --upgrade tuStockSpider