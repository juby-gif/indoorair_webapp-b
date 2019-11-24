"""
instrument/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from foundations.models import Instrument
from rest_framework import status, response, views

from .serializers import InstrumentRetrieveSerializer


def i_list_page(request):
    return render(request, "instrument/list.html", {})

def i_create_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "instrument/create.html", {})


def get_instruments_list_api(request):
    instruments = Instrument.objects.filter(user=request.user)
    output = []
    for instrument in instruments.all():
        output.append({
            'id': instrument.id,
            'name': instrument.name,
        })
    return JsonResponse({
        'instruments': output
    })


# def post_instruments_create_api(request):
#     name = request.POST.get("name")
#     print(name)
#     try:
#         instrument = Instrument.objects.create(
#             name=name,
#             user=request.user
#         )
#         print("INSTRUMENT ID", instrument.id)
#         return JsonResponse({
#          'was_created': True,
#         })
#     except Exception as e:
#         return JsonResponse({
#          'was_created': False,
#          'reason': str(e),
#         })


def i_retrieve_page(request, id):
    return render(request, "instrument/retrieve.html", {
        "instrument_id": int(id),
    })


class InstrumentRetrieveAPI(views.APIView):
    def get(self, request, id):
        instrument = Instrument.objects.get(id=int(id))
        serializer = InstrumentRetrieveSerializer(instrument, many=False)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


def i_update_page(request, id):
    return render(request, "instrument/update.html", {
        "instrument_id": int(id),
    })


class InstrumentUpdateAPI(views.APIView):
    def put(self, request, id):
        instrument = Instrument.objects.get(id=id)
        serializer = InstrumentUpdateSerializer(instrument, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'Updated instrument'
            }
        )
