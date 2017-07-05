from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Topic
from django.core.urlresolvers import reverse_lazy
from .forms import ReplyForm

class CreateTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'body']
    template_name = 'ask.html'
    success_url = reverse_lazy('forum:feed')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateTopicView, self).form_valid(form)

class ListTopicView(ListView):
    model = Topic
    template_name = 'feed.html'
    context_object_name = 'topics'

class DetailTopicView(DetailView):
    model = Topic
    template_name = 'show.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super(DetailTopicView, self).get_context_data(**kwargs)
        context['form'] = ReplyForm(self.request.POST or None)
        return context
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('account:login')
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = self.object
            reply.author = self.request.user
            reply.save()
            context['form'] = ReplyForm()
        return self.render_to_response(context)


list_topic = ListTopicView.as_view()
create_topic = CreateTopicView.as_view()
detai_topic = DetailTopicView.as_view()
