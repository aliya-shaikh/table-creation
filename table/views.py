from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Table
from django.contrib.messages.views import SuccessMessageMixin

def home(request):
	context={
		'tables':Table.objects.all()
	}
	return render(request,'table/home.html',context)

def register(request):
	if request.method =='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'{username} Your Account Has Been Created, You Are Now Able To Login !')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'table/register.html',{'form':form})

class TableCreateView(LoginRequiredMixin,CreateView):
	model = Table
	fields = ['title','content']
	success_url = '/'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class UserTableListView(ListView):
	model = Table
	template_name = 'table/user_table.html'
	context_object_name = 'tables'

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Table.objects.filter(author=user)

class TableDetailView(DetailView):
	model = Table
	template_name = 'table/table_detail.html'

class TableUpdateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
	model = Table
	fields = ['title','content']
	success_message = 'Your Post Has Been Updated !!'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		table = self.get_object()
		if self.request.user == table.author:
			return True
		return False

class TableDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Table
	success_url = '/'
	success_message = 'Your Post Has Been Deleted !!'

	def test_func(self):
		table = self.get_object()
		if self.request.user == table.author:
			return True
		return False

	def delete(self,request,*args,**kwargs):
		messages.success(self.request,self.success_message)
		return super(TableDeleteView,self).delete(request,*args,**kwargs)
