from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'posts/inicio.html')


def acerca(request):
    return render(request, 'posts/acerca.html')


def lista_posts(request):
    posts = Post.objects.filter(
        estado="publicado"
    ).order_by("-fecha_creacion")

    context = {
        "posts": posts
    }

    return render(request, 'posts/lista_posts.html', context)


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'posts/detalle_post.html', {'post': post})


@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('inicio')

    return render(
        request,
        'posts/post_confirm_delete.html',
        {'post': post}
    )