from django.shortcuts import render_to_response
from pblog.views import custom_proc
from django.template import RequestContext
from pblog.post.forms import PostForm
from pblog.post.models import Post

def send_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            t = ''
            x = cd['title'].split()
            cd['title'] = t.join(x)
            p = Post(name=cd['name'], title=cd['title'], text=cd['text'])
            p.save()

            title = "Posted successfully"
            string = "Your post has been submitted successfully."
            return render_to_response('success.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
    else:
        form = PostForm()
    return render_to_response('postForm.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def list_post(request):
    l = Post.objects.all()
    return render_to_response('list.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def show_post(request, title):
    p = Post.objects.get(title=title)
    return render_to_response('show.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
