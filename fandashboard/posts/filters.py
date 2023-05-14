from django.forms import DateTimeInput
from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from .models import *


class CommentFilter(FilterSet):
    added_after = DateTimeFilter(
            field_name='comment_dateCreation',
            lookup_expr='gt',
            widget=DateTimeInput(
                format='%Y-%m-%d',
                attrs={'type':'date'},
            ),
            label=pgettext_lazy('date of creation', 'Posted after')
        )

    class Meta:
        model = Comment
        fields = {
            'comment_author__username': ['contains'],
            'comment_post__title': ['icontains'],
            'accepted': ['exact']
        }


#если у будущем понадобится добавить фильтр на главную страницу сайта
# class PostsFilter(FilterSet):
#     added_after=DateTimeFilter(
#         field_name='dateCreation',
#         lookup_expr='gt',
#         widget=DateTimeInput(
#             format='%Y-%m-%d',
#             attrs={'type':'date'},
#         ),
#         label=pgettext_lazy('date of creation', 'Posted after')
#     )
#
#     category = ModelMultipleChoiceFilter(
#         field_name='category',
#         queryset=Post.objects.all(),
#         label=pgettext_lazy('category', 'category'),
#         conjoined=False,
#     )
#
#     class Meta:
#         # В Meta классе мы должны указать Django модель,
#         # в которой будем фильтровать записи.
#         model = Post
#         # В fields мы описываем по каким полям модели
#         # будет производиться фильтрация.
#         fields = {
#             # поиск по названию
#             'title': ['icontains'],
#         }
