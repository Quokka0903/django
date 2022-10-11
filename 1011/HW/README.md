1) static 파일 기본 설정
STATIC_ROOT = BASE_DIR / 'assets'

STATIC_URL = '/static/'



2) media 파일 기본 설정
MEDIA_ROOT = BASE_DIR / 'uploaded_files'

MEDIA_URL = '/media/'



3) Serving files uploaded by user during development

a = settings
b = django.conf.urls.static
c = static
d = settings.MEDIA_URL, document_root=settings.MEDIA_ROOT



4) Media file with HTML input
   
a = multipart/form-data
b = image/*|.PDF