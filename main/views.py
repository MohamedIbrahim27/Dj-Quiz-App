from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView ,DetailView ,CreateView,UpdateView ,DeleteView,FormView
from.models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import json
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect,HttpResponseForbidden,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

class ExamCreatequick(LoginRequiredMixin,CreateView):
    model=QuickExams
    fields=['exam_name','exam_exit','finish_exam']
    template_name='addexam.html'
    # context_object_name='task_detail'
    success_url=reverse_lazy('main:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Create an inline formset for ExamQuestion
        ExamQuestionFormSet = inlineformset_factory(
            QuickExams,
            ExamQuestion,
            fields=('question', 'answer1', 'answer2', 'answer3', 'answer4', 'TrueAsnwer'),
            extra=10,  # Initial number of extra forms
        )
        if self.request.POST:
            context['formset'] = ExamQuestionFormSet(self.request.POST)
        else:
            context['formset'] = ExamQuestionFormSet()
        return context

    def form_valid(self, form):
        # Get the Profiles instance corresponding to the current user
        profile_instance = Profiles.objects.get(user=self.request.user)
        # Assign the profile instance to the QuickExams instance
        form.instance.user = profile_instance
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Examupdatequick(LoginRequiredMixin,UpdateView):
    model=QuickExams  
    fields=['exam_name','exam_exit','finish_exam']
    template_name='addexam.html'
    success_url=reverse_lazy('main:home')
    
    def get_object(self, queryset=None):
        # Get the instance of QuickExams
        return get_object_or_404(QuickExams, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the instance of QuickExams
        instance = self.get_object()
        # Create an inline formset for ExamQuestion associated with QuickExams
        exam_question_count = instance.examquestion_set.count() # type: ignore
        # Calculate the value of extra based on the count
        extra = max(0, 10 - exam_question_count)
        ExamQuestionFormSet = inlineformset_factory(
            QuickExams,
            ExamQuestion,
            fields=('question', 'answer1', 'answer2', 'answer3', 'answer4', 'TrueAsnwer'),
            extra=extra,
        )
        if self.request.POST:
            context['formset'] = ExamQuestionFormSet(self.request.POST, instance=instance)
        else:
            context['formset'] = ExamQuestionFormSet(instance=instance)
        return context

    def form_valid(self, form):
        # Get the Profiles instance corresponding to the current user
        profile_instance = Profiles.objects.get(user=self.request.user)
        # Assign the profile instance to the QuickExams instance
        form.instance.user = profile_instance
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ExamCreateFull(LoginRequiredMixin,CreateView):
    model=FullExams
    fields=['exam_name','exam_exit','finish_exam']
    template_name='addexam.html'
    # context_object_name='task_detail'
    success_url=reverse_lazy('main:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Create an inline formset for ExamQuestionFull
        ExamQuestionFullFormSet = inlineformset_factory(
            FullExams,
            ExamQuestionFull,
            fields=('question', 'answer1', 'answer2', 'answer3', 'answer4', 'TrueAsnwer'),
            extra=30,  # Initial number of extra forms
        )
        if self.request.POST:
            context['formset'] = ExamQuestionFullFormSet(self.request.POST)
        else:
            context['formset'] = ExamQuestionFullFormSet()
        return context

    def form_valid(self, form):
        # Get the Profiles instance corresponding to the current user
        profile_instance = Profiles.objects.get(user=self.request.user)
        # Assign the profile instance to the FullExams instance
        form.instance.user = profile_instance
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
class ExamupdateFull(LoginRequiredMixin,UpdateView):
    model=FullExams  
    fields=['exam_name','exam_exit','finish_exam']
    template_name='addexam.html'
    success_url=reverse_lazy('main:home')
    
    def get_object(self, queryset=None):
        # Get the instance of QuickExams
        return get_object_or_404(FullExams, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the instance of QuickExams
        instance = self.get_object()
        # Create an inline formset for ExamQuestion associated with QuickExams
        exam_question_count = instance.examquestionfull_set.count() # type: ignore
        # Calculate the value of extra based on the count
        extra = max(0, 30 - exam_question_count)
        ExamQuestionFormSet = inlineformset_factory(
            FullExams,
            ExamQuestionFull,
            fields=('question', 'answer1', 'answer2', 'answer3', 'answer4', 'TrueAsnwer'),
            extra=extra,
        )
        if self.request.POST:
            context['formset'] = ExamQuestionFormSet(self.request.POST, instance=instance)
        else:
            context['formset'] = ExamQuestionFormSet(instance=instance)
        return context

    def form_valid(self, form):
        # Get the Profiles instance corresponding to the current user
        profile_instance = Profiles.objects.get(user=self.request.user)
        # Assign the profile instance to the QuickExams instance
        form.instance.user = profile_instance
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


def home(request,slug):
    profile=get_object_or_404(Profiles,slug=slug)
    if request.user.is_authenticated :
        if request.user.id == profile.user.id: # type: ignore
            quickcounter=QuickExams.objects.filter(user=profile).count()
            euiexemam=QuickExams.objects.filter(user=profile)
            fullExamm=FullExams.objects.filter(user=profile)
            fullExam=FullExams.objects.filter(user=profile).count()
            name = ''
            if 'searchname' in request.GET:
                name = request.GET['searchname']
                if name:
                    fullExamm=FullExams.objects.filter(exam_name__icontains=name)
                    euiexemam=QuickExams.objects.filter(exam_name__icontains=name)
            return render(request,'home.html',{'quickcounter':quickcounter,
                                                'fullExam':fullExam,
                                                'euiexemam':euiexemam,
                                                'fullExamm':fullExamm})
        else:
            return HttpResponseForbidden("You don't have permission to view dashdoard.")
    else:
        return redirect('/login')

def exam(request):
    euiexemam=QuickExams.objects.filter(examquestion__isnull=False).distinct()
    fullExamm=FullExams.objects.filter(examquestionfull__isnull=False).distinct()

    name = ''
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            fullExamm=FullExams.objects.filter(exam_name__icontains=name)
            euiexemam=QuickExams.objects.filter(exam_name__icontains=name)
    return render(request,'exam.html',{'euiexemam':euiexemam,
                                        'fullExamm':fullExamm})

def examquick(request,pk):
    euiexemam=get_object_or_404(QuickExams , pk=pk)
    questions=ExamQuestion.objects.filter(exam=euiexemam)
    return render(request,'question.html',{'questions':questions})

def examfull(request,pk):
    fullExamm=get_object_or_404(FullExams , pk=pk)
    questions=ExamQuestionFull.objects.filter(exam=fullExamm)
    
    return render(request,'question.html',{'questions':questions})




@method_decorator(csrf_exempt, name='dispatch')
class SaveAnswerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            answers = data['answers']

            profile = Profiles.objects.get(user=request.user)

            for answer in answers:
                question_id = answer['question_id']
                user_answer = answer['user_answer']

                question = ExamQuestion.objects.get(id=question_id)
                exam = question.exam
                correct_valuse = question.get_correct_answer()
                correct_answer = question.TrueAsnwer

                # Create a new UserAnswerquick entry
                if not UserAnswerquick.objects.filter(user=profile, Question=question).exists():
                    UserAnswerquick.objects.create(
                        user=profile,
                        exam=exam,
                        Question=question,
                        correctasnwer=correct_answer + ' --> ' + ' Value is : ==> ' + correct_valuse,
                        youranser=user_answer
                    )

            return JsonResponse({'success': True})
        except ExamQuestion.DoesNotExist:
            error_message = "Question does not exist."
            print(f"Error: {error_message}")
            return JsonResponse({'success': False, 'error': error_message})
        except Profiles.DoesNotExist:
            error_message = "Profile does not exist."
            print(f"Error: {error_message}")
            return JsonResponse({'success': False, 'error': error_message})
        except Exception as e:
            error_message = str(e)
            print(f"Error: {error_message}")
            return JsonResponse({'success': False, 'error': error_message})










# def search(request):
#     name = ''
#     if 'searchname' in request.GET:
#         name = request.GET['searchname']
#         if name:
#             fullExamm=FullExams.objects.filter(exam_name__icontains=name)
#             euiexemam=QuickExams.objects.filter(exam_name__icontains=name)
#     return render(request,'home.html',{'euiexemam':euiexemam,
#                                         'fullExamm':fullExamm})
