
from django.shortcuts import render, redirect, get_object_or_404
from .models import Novel
from .forms import NovelForm

# List all novels
def index(request):
    novels = Novel.objects.all()
    return render(request, 'novels/index.html', {'novels': novels})

# Add a new novel
def add_novel(request):
    if request.method == 'POST':
        form = NovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NovelForm()
    return render(request, 'novels/add_novel.html', {'form': form})

# Update an existing novel
def update_novel(request, id):
    novel = get_object_or_404(Novel, id=id)
    if request.method == 'POST':
        form = NovelForm(request.POST, instance=novel)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NovelForm(instance=novel)
    return render(request, 'novels/update_novel.html', {'form': form, 'novel': novel})

# Delete a novel
def delete_novel(request, id):
    novel = get_object_or_404(Novel, id=id)
    novel.delete()
    return redirect('index')
