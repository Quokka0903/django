1.  T/F

  - T
  - F. CONNECT, DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT 등이 있다.
  - F. 주소 끝이 /로 끝나는데다 해당 주소에서 사용할 기능이 무엇인지 드러나 있다.


2. HTTP status code

  - 200 OK 요청이 성공적으로 완료되었음.
  - 400 Bad Request 잘못된 문법이라 서버가 이해할 수 없음.
  - 401 Unauthorized 스스로 인증되지 않은 클라이언트
  - 403 Forbidden 클라이언트는 인증되었으나 콘텐츠 접근 권리가 없음.
  - 404 Not Found 요청받은 리소스를 찾을 수 없음
  - 500 Internal Server Error 문제가 있으나 구체적인 설명 불가.


3. StudentSerializer class 작성

  class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


4. Serializers의 의미

  - JSON등의 콘텐츠 유형으로 쉽게 렌더링하기 위해 복잡한 데이터를 Python 데이터 유형으로 변환(serialize)하는 기능.