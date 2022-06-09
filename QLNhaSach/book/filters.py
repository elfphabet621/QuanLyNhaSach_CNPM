import django_filters
from django.forms.widgets import TextInput
from .models import Sach
from django.db import models
import re

class BookFilter(django_filters.FilterSet):
    # gia_ban = django_filters.NumberFilter(field_name='gia_ban',lookup_expr='lt', label='Giá sách (tối đa)')

    class Meta:
        model = Sach
        fields = ['ten_sach']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'label': '',
                    'method': 'preprocess_qs',
                    'lookup_expr': 'icontains',
                    'widget': TextInput(attrs={'placeholder': "Tìm kiếm sách mong muốn ...", "class":"form-control w-75"}),
                    
                },
            },
        }

    def preprocess_qs(self, queryset, value, *args, **kwargs):
        try:
            if args:
                str_re = args[0]
                str_re = re.sub('[$&+,:;=?@#|<>".^*()%!\'-]+', '', str_re)
                str_re = re.sub(' {2,}', ' ', str_re)
                for f in re.findall('[a-zA-Z]([0-9$&+,:;=?@#|<>".^*()%!\'-]+)[a-zA-Z]?', str_re):
                    str_re = re.sub(f, '', str_re)
                # print(str_re)

                queryset = queryset.filter(ten_sach__icontains=str(str_re))
        except ValueError:
            pass
        return queryset
