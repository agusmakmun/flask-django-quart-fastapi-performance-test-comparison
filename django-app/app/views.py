from django.http import JsonResponse


async def dummy_view(request):
    return JsonResponse(
        {"message": "Hello from Django dummy endpoint!", "status": "success"}
    )
