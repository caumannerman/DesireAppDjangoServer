import os

from dotenv import load_dotenv

from core.settings.base import *

load_dotenv()

if int(os.getenv('ENABLE_S3_BUCKET', 0)) == 1:
    # S3 설정을 위한 변수
    # AWS_xxx 의 변수들은 aws-S3, boto3 모듈을 위한 변수들이다.

    INSTALLED_APPS += [
        'storages'
    ]

    # 엑세스 키와 시크릿 키는 다른 파일로 작성, 임포트하여 사용
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

    AWS_REGION = os.getenv('AWS_REGION')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
        AWS_STORAGE_BUCKET_NAME, AWS_REGION)
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'static'
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

    # 미디어 파일을 위한 스토리지 설정
    DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'

    # ## 미디어 파일을 위한 스토리지 설정 (프로젝트 내부 설정 파일 존재)
    AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    DEFAULT_FILE_STORAGE = 'core.settings.conf.storage_backends.PublicMediaStorage'

    AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
    PRIVATE_FILE_STORAGE = 'core.settings.conf.storage_backends.PrivateMediaStorage'
else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    # Media files (User uploaded files)

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
