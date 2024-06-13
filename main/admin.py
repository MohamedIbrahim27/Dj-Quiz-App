from django.contrib import admin
from.models import ExamQuestion,QuickExams,FullExams,ExamQuestionFull,UserAnswerquick
# Register your models here.
class ExamQuestiont(admin.TabularInline):
    model = ExamQuestion 
    extra = 10
class QuickExamsAdmin(admin.ModelAdmin):
    inlines=[ExamQuestiont]
    list_display= ['id','user','exam_name','exam_exit','finish_exam']
    list_display_links = ['user','exam_name']
    list_filter=['exam_exit','finish_exam',]
    search_fields=['user__user__username',]
class ExamQuestionAdmin(admin.ModelAdmin):
    list_display= ['id','exam','question','answer1','answer2','answer3','answer4','TrueAsnwer',]
    list_display_links = ['id','exam','question',]
    list_filter=['exam',]
    
class FullExamQuestiont(admin.TabularInline):
    model = ExamQuestionFull 
    extra = 30
class FullExamsAdmin(admin.ModelAdmin):
    inlines=[FullExamQuestiont]
    list_display= ['id','user','exam_name','exam_exit','finish_exam']
    list_display_links = ['user','exam_name']
    list_filter=['exam_exit','finish_exam',]
    search_fields=['user__user__username',]
    
class FullExamQuestionAdmin(admin.ModelAdmin):
    list_display= ['id','exam','question','answer1','answer2','answer3','answer4','question_with_answer',]
    list_display_links = ['id','exam','question',]
    list_filter=['exam',]
    def question_with_answer(self, obj):
        return f"{getattr(obj, obj.TrueAsnwer)}"

    question_with_answer.short_description = 'True Answer'
class UserAnswerquickAdmin(admin.ModelAdmin):
    list_display= ['id','user','exam','Question','correctasnwer','youranser']
    list_display_links = ['id','exam','Question',]
    list_filter=['exam']
    search_fields = ['user__user__username','exam__exam_name', 'Question__question',]
admin.site.register(ExamQuestion,ExamQuestionAdmin)
admin.site.register(QuickExams,QuickExamsAdmin)

admin.site.register(ExamQuestionFull,FullExamQuestionAdmin)
admin.site.register(FullExams,FullExamsAdmin)
admin.site.register(UserAnswerquick,UserAnswerquickAdmin)