#coding=utf-8
"""
Django settings for AutOperation project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os,logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!x9mjku(i2ytpknztu-t%9pdtkgogh=_%c#t1yjxxte(wymfyv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mymiddleware',
    'mymiddleware.SetCode',
    # 'mymiddleware.websocketLog'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mymiddleware.mymiddleware.QtsAuthenticationMiddleware',
]

ROOT_URLCONF = 'AutOperation.urls'

SESSION_SAVE_EVERY_REQUEST=True         #如果设置为True,django为每次request请求都保存session的内容，默认为False。
SESSION_EXPIRE_AT_BROWSER_CLOSE=True    #会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失
SESSION_COOKIE_AGE=30*60                #30分钟。

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')]
        # ,
        'DIRS': [
        os.path.join(BASE_DIR,'pages').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/app').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/server').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/server/redis').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/server/keepalived').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/serviceShow').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/portManage').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/system').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/dayManage').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/dataManage').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/monitor').replace('\\', '/'),
        os.path.join(BASE_DIR,'pages/jenkins').replace('\\', '/'),
        os.path.join(BASE_DIR,'templates').replace('\\', '/'),
        os.path.join(BASE_DIR,'log').replace('\\', '/'),
        os.path.join(BASE_DIR,'interface').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AutOperation.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



###################################################################################
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
                'format': '%(asctime)s[%(levelname)s]%(message)s'
                },
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter':'standard',
        },
        'test1_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'log/11.log',
            'formatter':'standard',
        },
        'test2_handler': {
            'level':'DEBUG',
                   'class':'logging.handlers.RotatingFileHandler',
            'filename':'log/22.log',
            'formatter':'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'test1':{
            'handlers': ['test1_handler'],
            'level': 'INFO',
            'propagate': False
        },
         'test2':{
            'handlers': ['test2_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
###################################################################################







LOGIN_URL = '/login/'
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


STATIC_PATH = os.path.join( os.path.dirname(__file__) , 'static' )
STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/static/',
]


#interface
username = 'test'
passwd = 'test'

#db_set
ip = '221.179.180.148'
user = 'NX_USER'
password = 'dbms_lock'

#port_set
userlist = {"test" : "test1" , "tt" : "t1"}

#mysql_set
mysqlip = '127.0.0.1'
mysqluser = 'recode'
mysqlpassword = '12345'
mysqldatabase = 'INFORMATION_RECORD'
mysqlport = 3306
mysqlcode = 'utf8'

#salt_stack
salt_root_path = '/Users/wml/Desktop/ttttt'
#/srv/salt

#软件安装列表software_list
softwareList = [ ['redis','/pages/server/redis/redisInstall.html'] , ['tomcat8', 'state'] , ['PostgreSQL10', 'state'] , ['zabbix-agent', 'state'] , ['jdk8', 'state'] ,['keepalived','/pages/server/keepalived/keepalivedInstall.html'] , ['apache','state'] ,  ['vim','yum'] , ['telnet', 'yum'] , ['net-tool*','yum'] ]
redisFilePath='/srv/salt/redisfiles'  #结尾不加/
keepalivedFilePath='/srv/salt/keepalivedfiles'  #结尾不加/

jenkinsList=[
    {'ProjectName':'CCBWEB', 'create_time':'2017.10.10', 'version':'1.01','CodeName':'springmvcMaven1','Explain':'jenkins测试代码','state':'-1' , 'type':'WEB'},
    {'ProjectName':'ABCWEB','create_time':'2017.2.13' ,'version':'2.01','CodeName':'Maven1','Explain':'测试数据','state':'0' , 'type':'JAR'}
]

zabbix_url = 'http://172.16.22.25/zabbix/index.php'
zabbix_graph = 'http://172.16.22.25/zabbix/chart2.php'
url = "http://172.16.22.25/zabbix/api_jsonrpc.php"
zabbix_token='e897eb7d548db4eceb7dcc0056a0fc33'
zabbixuser='Admin'
zabbixpasswd='zabbix'
# zabbix_url = 'http://172.16.0.219/index.php'
# zabbix_graph = 'http://172.16.0.219/chart2.php'
# url = "http://172.16.0.219/api_jsonrpc.php"
# zabbix_token='f728f1771a4d705ec6cecec807aa9eb7'
# zabbixuser='Admin'
# zabbixpasswd='zabbix'

salt_api='https://172.16.22.25:9000'
salt_user='saltapi'
salt_passwd='omygad911'
salt_master='ip-172-16-0-175'

jenkinsAPI="http://wangminglang:omygad911@192.168.168.119:8080/jenkins/job/{projectName}/build"




#web_set
webuser = {"mst" : "MXEydzNlNHI1dA==" , "tt" : "t1" , "client" : "MXEydzNlNHI1dA=="}

#web port manage 端口
portShow = ["端口列表" , 'port_show.html']
portManage = ["端口申请" , '/selectPort/']

#server manage 服务器管理
serverShow = ["服务器列表" , '/serverlist/']
softwareManage = ["软件管理" , '/toSoftware/']

#day_manage 日常管理
dayManage = ["日常工作" , '/daymanage/']
setManage = ["文档管理" , 'set_Manage.html']

# setManage = ["文档管理" , '123.doc']

#analyse_data 分析数据
dayData = ["日常数据" , 'dataManage.html']

#monitor 监控
server_monitor = ["服务器监控" , '/hostId/']
log_monitor = ["日志监控" , 'logMonitor.html']

#applog监控
applog = ["应用日志" , 'applog.html']

#jenkins
code_release = ["代码上线" , '/jenkinsList/']
code_check = ['程序测试' , 'css_animation.html']
mst = {"应用程序":[applog] , "工单系统":[portManage] , "服务器":[serverShow,softwareManage] , "团队管理" : [dayManage,] , "监控":[server_monitor,log_monitor], "数据分析":[dayData,] , "jenkins":[code_release,code_check]}
client = {"应用程序":[applog] , "工单系统":[portManage] , "服务器":[serverShow,softwareManage] , "团队管理" : [dayManage,] , "监控":[server_monitor,log_monitor], "数据分析":[dayData,], "jenkins":[code_release,code_check]}

showlist = {"mst" : mst , "client" : client}

state = '0'  #state = '1' 测试环境(本机)  其他:有saltstack的环境
