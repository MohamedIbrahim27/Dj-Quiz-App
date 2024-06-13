from datetime import datetime
from django.db import models
from users.models import Profiles
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# Create your models here.



class QuickExams(models.Model):
    user = models.ForeignKey(Profiles,on_delete=models.CASCADE) # type: ignore
    exam_name = models.CharField(max_length = 150)
    exam_exit=models.DateTimeField(verbose_name=_("Exam Exit At"), default=datetime.now)
    finish_exam=models.DateTimeField(verbose_name=_("Exam Finish At"))
    

    def __str__(self):
        return str(self.exam_name)



class ExamQuestion(models.Model):
    exam = models.ForeignKey(QuickExams,on_delete=models.CASCADE) # type: ignore
    question =models.CharField(_("Question"), max_length=50)
    answer1=models.CharField(_("Answer 1"), max_length=200)
    answer2=models.CharField(_("Answer 2"), max_length=200)
    answer3=models.CharField(_("Answer 3"), max_length=200)
    answer4=models.CharField(_("Answer 4"), max_length=200)
    TRUE_CHOICES = (
        ('answer1', 'Answer 1'),
        ('answer2', 'Answer 2'),
        ('answer3', 'Answer 3'),
        ('answer4', 'Answer 4'),
    )
    
    TrueAsnwer=models.CharField(_("True Asnwer"), max_length=200,choices=TRUE_CHOICES) # type: ignore
    def clean(self):
        if self.pk is None:  # If the instance is not saved yet
            return  # Skip validation until the instance is saved
        if ExamQuestion.objects.filter(exam=self.exam).count() >= 10:
            raise ValidationError("Cannot add more than 10 questions per exam.")
    def get_correct_answer(self):
        return getattr(self, self.TrueAsnwer)
    def save(self, *args, **kwargs):
        if self.pk is None:  # If the instance is not saved yet
            super().save(*args, **kwargs)  # Save the instance first
        self.full_clean()  # Then run full validation
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.question)
    
    
class FullExams(models.Model):
    user = models.ForeignKey(Profiles,on_delete=models.CASCADE) # type: ignore
    exam_name = models.CharField(max_length = 150)
    exam_exit=models.DateTimeField(verbose_name=_("Exam Exit At"), default=datetime.now)
    finish_exam=models.DateTimeField(verbose_name=_("Exam Finish At"))
    

    def __str__(self):
        return str(self.exam_name)



class ExamQuestionFull(models.Model):
    exam = models.ForeignKey(FullExams,on_delete=models.CASCADE) # type: ignore
    question =models.CharField(_("Question"), max_length=50)
    answer1=models.CharField(_("Answer 1"), max_length=200)
    answer2=models.CharField(_("Answer 2"), max_length=200)
    answer3=models.CharField(_("Answer 3"), max_length=200)
    answer4=models.CharField(_("Answer 4"), max_length=200)
    TRUE_CHOICES = (
        ('answer1', 'Answer 1'),
        ('answer2', 'Answer 2'),
        ('answer3', 'Answer 3'),
        ('answer4', 'Answer 4'),
    )
    
    TrueAsnwer=models.CharField(_("True Asnwer"), max_length=200,choices=TRUE_CHOICES) # type: ignore
    def clean(self):
        if self.pk is None:  # If the instance is not saved yet
            return  # Skip validation until the instance is saved
        if ExamQuestionFull.objects.filter(exam=self.exam).count() >= 30:
            raise ValidationError("Cannot add more than 10 questions per exam.")

    def save(self, *args, **kwargs):
        if self.pk is None:  # If the instance is not saved yet
            super().save(*args, **kwargs)  # Save the instance first
        self.full_clean()  # Then run full validation
        super().save(*args, **kwargs)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.question)
    

class UserAnswerquick(models.Model):
    user = models.ForeignKey(Profiles,on_delete=models.CASCADE) # type: ignore
    exam = models.ForeignKey(QuickExams,on_delete=models.CASCADE) # type: ignore
    Question = models.ForeignKey(ExamQuestion,on_delete=models.CASCADE) # type: ignore
    correctasnwer = models.CharField(_("Correct Answer"),max_length = 150)
    youranser = models.CharField(_("Your Answer"),max_length = 150)

    def __str__(self):
        return str(self.user)
    
    
class UserAnswerfull(models.Model):
    user = models.ForeignKey(Profiles,on_delete=models.CASCADE) # type: ignore
    exam = models.ForeignKey(FullExams,on_delete=models.CASCADE) # type: ignore
    Question = models.ForeignKey(ExamQuestionFull,on_delete=models.CASCADE) # type: ignore
    correctasnwer = models.CharField(_("Correct Answer"),max_length = 150)
    
    youranser = models.CharField(_("Your Answer"),max_length = 150)

    def __str__(self):
        return str(self.user)
    
    