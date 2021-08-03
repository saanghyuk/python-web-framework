from django.shortcuts import render, redirect
from django.http import Http404
from .models import Board
from fcuser.models import Fcuser
from tag.models import Tag
from .forms import BoardForm
from django.core.paginator import Paginator
# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)  # 시간 역순의미
    except Board.DoesNotExist:
        raise Http404('Cannot Find Board')

    return render(request, 'board_detail.html', {"board": board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login')
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            # 일단 저장하고, 해당 id로 태그를 추가할 것임(어차피 required아니니깐)
            board.save()

            for tag in tags:
                if not tag:
                    continue
                # IMPORTANT
                _tag, created = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')  # 시간 역순의미
    page = int(request.GET.get('p', 1))  # 변수 이름 p, 없으면 디폴트 1
    paginator = Paginator(all_boards, 2)  # 한페이지 2개씩

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
