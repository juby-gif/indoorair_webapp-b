from rest_framework import response,status,views
from django.shortcuts import render
import uuid

from foundations.models import Instrument


def i_list_page(request):
    return render(request, "instrument/list.html", {})

def i_create_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "instrument/create.html", {})

class ListInstrumentsAPIView(views.APIView):
    def get(self, request):
        output = []
        instruments = Instrument.objects.filter(user=request.user)
        for instrument in instruments.all():
            output.append({
                'id': instrument.id,
                'name': instrument.name,
            })
        return response.Response(
            status = status.HTTP_200_OK,
            data = {
                'Instruments': output
            }
        )

class CreateAPIView(views.APIView):
    def post(self, request):
        unsanitized_serial_number = request.data.get('serial_no', None)
        sanitized_serial_number = uuid.UUID(unsanitized_serial_number)
        try:
            uuid_value = Instrument.objects.all().values('serial_no')
            for value in uuid_value:
                if sanitized_serial_number == value['serial_no']:
                    print(value['serial_no'])
                    return response.Response(
                        status = status.HTTP_201_CREATED,
                        data = {
                            'message':'Successfully Created'
                               }
                        )
                    break
                else:
                    return response.Response(
                        status = status.HTTP_400_BAD_REQUEST,
                        data = {
                            'error':'The Serial number you entered is wrong. Please try again!'
                               }
                        )
        except Exception as e:
            return response.Response(
                status = status.HTTP_400_BAD_REQUEST,
                data = {
                    'error':str(e)
                       }
                )


def i_retrieve_page(request, id):
    return render(request, "instrument/retrieve.html", {
        "instrument_id": int(id),
    })
class RetrieveAPIView(views.APIView):

    def get(self, request, id):
        try:
            instrument = Instrument.objects.get(id=int(id))
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'id': instrument.id,
                    'name': instrument.name,
                       }
                )

        except Exception as e:
            return response.Response(
                status = status.HTTP_400_BAD_REQUEST,
                data = {
                    'error': str(e),
                       }
                )

def i_update_page(request, id):
    return render(request, "instrument/update.html", {
        "instrument_id": int(id),
    })

class UpdateAPIView(views.APIView):
    def post(self, request, id):
        try:
            name = request.POST.get("name")
            instrument = Instrument.objects.get(id=int(id))
            instrument.name = name
            instrument.save()
            return response.Response(
                status = status.HTTP_200_OK,
                data = {
                    'id': instrument.id,
                    'name': instrument.name,
                       }
                )
        except Exception as e:
            return response.Response(
                status = status.HTTP_400_BAD_REQUEST,
                data = {
                    'error': str(e),
                       }
                )
