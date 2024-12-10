from django.http import JsonResponse
from django.db import connections

def health_check(request):
    try:
        # Verifica la conexión a la base de datos
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT 1;")
        status = "ok"
    except Exception as e:
        status = "error"

    return JsonResponse({"status": status, "database": status})
