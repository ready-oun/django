from django.db import models

class CommonModel(models.Model):
    # auto_no_add: 현재 데이터 생성 시간을 기준으로 생성됨 -> 이후 데이터가 업데이트되어도 수정되지 않음
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now: 생성된 시간 기준으로 일단 생성됨 -> 이후 데이터 업데이트 시, 시간도 업데이트된 현재 시간을 기준으로 업뎃됨
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # DB의 테이블에 이와 같은 컬럼이 추가되지 않음 