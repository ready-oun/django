from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
	# 관리자 페이지의 목록에 표시할 필드들을 지정
	list_display = ('title', 'writer', 'date', 'likes', 'content', 'updated_at', 'created_at')
	# 목록 페이지에서 필터 옵션으로 사용될 필드를 지정
	list_filter = ('date', 'writer')
	# 검색 기능에서 사용할 필드를 지정
	search_fields = ['title', 'content']
	# 목록 페이지의 기본 정렬 순서를 지정
	ordering = ('date',)
	# 읽기 전용 필드를 지정합니다. 이 필드들은 사용자가 편집할 수 없습니다.
	readonly_fields = ('writer',)
	# 상세 페이지에서 필드 그룹을 어떻게 나눌지를 지정합니다.
	fieldsets = (
		(None, {'fields': ('title', 'content')}),
		('Advanced options', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
	)
	# -> 'Advanced options' 은 원하는 내용으로 수정 가능
	
	# 목록 페이지에 표시할 항목의 수를 지정
	list_per_page = 10

	#  사용자 정의 대량 작업을 추가할 수 있습니다.
	actions = ('increment_likes', )

	def increment_likes(self, request, queryset):
		# 선택된 게시글들에 대해 'likes' 수를 1씩 증가
		for board in queryset:
			board.likes += 1
			board.save()
	increment_likes.short_description = "선택된 게시글의 좋아요 수 증가"