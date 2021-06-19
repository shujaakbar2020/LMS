from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


select_year = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
)
select_semester = (
    ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8)
)

select_user = (
    ('student', 'student'),
    ('teacher', 'teacher'),
    ('admin', 'admin')
)


# Create your models here.

class Student(models.Model):
    studentNumber = models.CharField(max_length=64, help_text="Student Roll No.", blank=True)
    studentName = models.CharField(max_length=64, blank=True)
    admitYear = models.IntegerField(blank=True, null=True)
    collegeName = models.CharField(max_length=64, blank=True)
    professionalName = models.CharField(max_length=64, blank=True)
    className = models.CharField(max_length=64, blank=True)
    birthDate = models.DateField(null=True)
    homeAddress = models.CharField(max_length=64, null=True)
    postCode = models.CharField(max_length=64, null=True)
    mobilePhone = models.CharField(max_length=64, null=True)
    emailAddress = models.EmailField(null=True)

    def __str__(self):
        return f"{self.studentName} > {self.className} > {self.admitYear}"


class Course(models.Model):
    courseNumber = models.IntegerField(null=True)
    courseName = models.CharField(max_length=64, null=True)
    courseNature = models.CharField(max_length=64, null=True)
    courseCredit = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    theoreticalHours = models.SmallIntegerField(null=True)
    experimentHours = models.SmallIntegerField(null=True)
    courseDescription = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return f"{self.courseName}"


class Teacher(models.Model):
    teacherNumber = models.CharField(max_length=64, null=True)
    teacherName = models.CharField(max_length=64, null=True)
    graduationSchool = models.CharField(max_length=64, null=True)
    graduationTime = models.DateField(null=True)
    collegeName = models.CharField(max_length=64, null=True)
    professionalName = models.CharField(max_length=64,  null=True)
    technicalTitle = models.CharField(max_length=64, null=True)
    finalDegree = models.CharField(max_length=64, null=True)
    finalEducation = models.CharField(max_length=64, null=True)
    mobilePhone = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=True)
    jobResume = models.FileField(null=True)

    def __str__(self):
        return f"{self.teacherName}"


class TestQuestion(models.Model):
    question_no = models.IntegerField()
    courseNumber = models.CharField(max_length=64, null=True)
    knowledgePoint = models.CharField(max_length=64, null=True)
    chapterSection = models.CharField(max_length=64, null=True)
    testQuestionType = models.CharField(max_length=10, null=True)
    titleName = models.CharField(max_length=50, null=True)
    testQuestionContent = models.CharField(max_length=200, null=True)
    testQuestionAnwser = models.CharField(max_length=200, null=True)


class Problem(models.Model):
    problemNumber = models.CharField(max_length=64, null=True)
    problemCategory = models.CharField(max_length=64, null=True)
    problemTitle = models.CharField(max_length=64, null=True)
    problemContent = models.CharField(max_length=64, null=True)
    problemAnswer = models.CharField(max_length=64, null=True, blank=True)
    studentFeedback = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.problemTitle}"


class UserInformation(models.Model):
    userNumber = models.CharField(max_length=64, null=True)
    userName = models.CharField(max_length=64, null=True)
    loginPassword = models.CharField(max_length=64, null=True)
    roleNumber = models.CharField(max_length=64, null=True)
    roleName = models.CharField(max_length=64, null=True)
    passwordProblem = models.CharField(max_length=64, null=True)


class Elective(models.Model):
    studentNumber = models.ManyToManyField(Student)
    courseNumber = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.studentNumber.studentName}"


class Teach(models.Model):
    courseNumber = models.ManyToManyField(Course)
    teacherNumber = models.ManyToManyField(Teacher)
    # courseNumber = models.CharField(max_length=64, null=True)
    # teacherNumber = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.teacherNumber.teacherName}"


class Proposed(models.Model):
    studentNumber = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    problemNumber = models.ForeignKey(Problem, null=True, on_delete=models.CASCADE)
    proposedTime = models.DateTimeField(null=True)


class Answer(models.Model):
    teacherNumber = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    problemNumber = models.ForeignKey(Problem,null=True, on_delete=models.CASCADE)
    answerTime = models.DateTimeField(null=True)


class LMSUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=20,
        choices=select_user,
        null=True,
        default='student',
        help_text='Please select this Correctly, Because you will be Checked.'
    )

    def __str__(self):
        return f'{self.user_type}'
