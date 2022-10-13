1. MTV
  - M : Model     =>  데이터베이스에 저장되는 데이터
  - T : Template  =>  사용자에게 보여지는 부분
  - V : View      =>  받은 웹 요청을 가공하여 템플릿에 결과 전달


2. 404 Page not found
  - a) articles
  - b) views
  - c) views.index


3. templates and static
  - a) settings.py
  - b) STATIC_URL
  - c) STATICFILES_DIRS
 

4. migration
  1) python manage.py makemigrations
  2) python manage.py showmigrations
  3) python manage.py sqlmigrate articles 설계도명
  4) python manage.py migrate


5. ModelForm True or False
  1) F (GET은 가져오는 것, POST는 수행하는 것)
  2) T
  3) T
  4) F


6. media 파일 경로

  MEDIA_ROOT = BASE_DIR / 'uploaded_files'

  MEDIA_URL = '/uploaded_files/'

7. DB True or False
  1) T
  2) T
  3) T
  4) T
  5) F


8. on_delete
  - PROTECT


9. Like in models
  - a) ManyToManyField
  - b) related_name


10. Follow in models
  - 중개 테이블 : accounts_user_followings
  - 컬럼 : from_user_id , to_user_id