from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MapaForm
from django.contrib import messages
from django.urls import reverse_lazy
from adapters.excel_adapter import ExcelAdapter
from django.shortcuts import redirect


class MapaFormView(LoginRequiredMixin, FormView):
    form_class = MapaForm
    template_name = "pages/home/components/carga_excel.html"
    success_url = reverse_lazy("Mapa")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        document = form.cleaned_data["document"]
        try:
            adapter = ExcelAdapter()
            json_path = adapter.process_excel_file(document)
            print(f"JSON creado en: {json_path}")
            messages.success(self.request, "Cargado con Éxito")
        except Exception as e:
            form.add_error(None, f"Error al procesar el archivo: {str(e)}")
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        for _, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return redirect("Mapa")

class MapaTemplaView(LoginRequiredMixin, TemplateView):
    template_name = "pages/index.html"
    login_url = reverse_lazy("login")