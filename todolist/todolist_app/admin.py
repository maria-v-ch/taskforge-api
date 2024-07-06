from django.contrib import admin
from todolist_app.models import Task, Comment, Tag

# TabularInline — отображает связанные объекты в табличном виде. Есть также StackedInline, который отображает их в
# виде блоков.


class CommentInline(admin.TabularInline):
    model = Comment
    # extra = 0

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0  # For changing an item


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'due_date', 'author')
    search_fields = ('name', 'description', 'author', 'description')
    list_filter = ('due_date', 'author', 'status')

    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['task__name', 'task__description', 'task__author']


admin.site.register(Tag)
