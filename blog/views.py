from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'blog/home.html', data)




def about(request):
    return render(request, 'blog/about.html', {'title': 'О компании'})


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Контакты'})


def services(request):
    return render(request, 'blog/services.html')


class ShowBlogView(ListView):
    model = News
    template_name = 'blog/blog.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwards):
        ctx = super(ShowBlogView, self).get_context_data(**kwards)
        ctx['title'] = 'Блог'
        return ctx


class BlogDetailView(DetailView):
    model = News
    template_name = 'blog/news.html'

    def get_context_data(self, **kwards):
        ctx = super(BlogDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class CreateBlogView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateBlogView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        ctx['p_info'] ='Для добавления абзацев используйте <br>'
        return ctx

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

class DeleteBlogView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False



class UpdateBlogView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateBlogView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)