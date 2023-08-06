from django.views.generic.edit import CreateView, UpdateView, DeleteView

from fakenews.models import DisinformationType
from fakenews.authentication import secure
from .cms_base import CMSForm, CMSList, CMSBaseMixin, CMSBaseEditMixin


class DisinformationTypeBaseMixin(object):
    url_basename = 'disinformation_type'


class DisinformationTypeForm(CMSForm):
    class Meta:
        model = DisinformationType
        fields = ["label", "description"]


class DisinformationTypeViewMixin(
    DisinformationTypeBaseMixin,
    CMSBaseEditMixin
):
    form_class = DisinformationTypeForm
    title = "Disinformation Type"

    def get_object(self, queryset=None):
        return DisinformationType.objects.get(pk=self.kwargs['pk'])


@secure
class DisinformationTypeCreate(DisinformationTypeViewMixin, CreateView):
    pass


@secure
class DisinformationTypeUpdate(DisinformationTypeViewMixin, UpdateView):
    pass


@secure
class DisinformationTypeDelete(DisinformationTypeViewMixin, DeleteView):
    pass


@secure
class DisinformationTypeList(
    DisinformationTypeBaseMixin,
    CMSBaseMixin,
    CMSList
):
    model = DisinformationType
    title = "Disinformation Type"
    fields = ["label", "description"]


disinformation_type_views = {
    "list": DisinformationTypeList,
    "create": DisinformationTypeCreate,
    "update": DisinformationTypeUpdate,
    "delete": DisinformationTypeDelete
}
