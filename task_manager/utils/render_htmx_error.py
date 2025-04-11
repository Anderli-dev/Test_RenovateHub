import json

from django.http import HttpRequest
from django.template.response import TemplateResponse

def render_htmx_error(request: HttpRequest, message: str, status_code: int, trigger: str = "error"):
    context = {"error_message": message}
    response = TemplateResponse(request, "elements/modals/error_modal.html", context=context, status=status_code)
    response["Hx-Trigger"] = json.dumps({
        trigger: message,
    })
    return response