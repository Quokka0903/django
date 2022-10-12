1) M:N True or False
   1) T
   2) T
   3) F, related_name은 mtm을 할 대상이 다수 있거나, 사용자 편의성을 위해 입력한다.
   
2) Like in templates
   a) request.user
   b) artcle.like_users.all

3) Follow in views
   a) user_pk
   b) followers
   c) filter
   d) remove
   e) add

4) User AttributeError
    - 복습 필요할듯..


5) related_name
    - user가 작성한 글도 user.article_set으로 역참조되고,
    - user가 좋아요 누른 글도 user.article_set으로 역참조되므로.