standard_format = '%(asctime)s.%(msecs)03d [%(levelname)s] [%(filename)s::%(funcName)s:%(lineno)d] %(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
# ��־�ļ�������λ��(�ļ�)�����������ļ������ú���־�ļ��������ļ�·��
logfile_path = 'logging.log'
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},  # ������־
    'handlers': {
        #��ӡ���ն˵���־
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # ��ӡ����Ļ
            'formatter': 'simple'
        },
        #��ӡ���ļ�����־,�ռ�info�����ϵ���־
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # ���浽�ļ�
            'formatter': 'standard',
            'filename': logfile_path,  # ��־�ļ�
            'maxBytes': 1024*1024*5,  # ��־��С 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # ��־�ļ��ı��룬��Ҳ���õ�������log������
        },
    },
    'loggers': {
        #logging.getLogger(__name__)�õ���logger����  ���ַ�����Ϊ�� �ܹ��������е���־
        '': {
            'handlers': ['default', 'console'],  # ��������涨�������handler�����ϣ���log���ݼ�д���ļ��ִ�ӡ����Ļ
            'level': 'DEBUG',
            'propagate': True,  # ���ϣ�����level��logger������
        },  # ���������ڵ������ (key��Ϊ���ַ���)Ĭ�϶���ʹ�ø�k:v����
    },
}