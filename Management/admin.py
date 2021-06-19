from django.contrib import admin
from .models import Course, Teacher, Student, TestQuestion, Problem, UserInformation, Elective, Teach, Proposed, Answer,LMSUser


# Register your models here.
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(TestQuestion)
admin.site.register(Student)
admin.site.register(Problem)
admin.site.register(UserInformation)
admin.site.register(Elective)
admin.site.register(Teach)
admin.site.register(Proposed)
admin.site.register(Answer)
admin.site.register(LMSUser)
