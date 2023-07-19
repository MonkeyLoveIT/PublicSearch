from django.shortcuts import render
from django.http import JsonResponse
from .utils.database import create_record, get_record, update_record, delete_record


# Create your views here.
def create(request):
    # Extract the data from the request
    data = request.POST.dict()

    # Create a new record using the data
    record = create_record(data)

    # Return a JSON response with the created record
    return JsonResponse({'record': record.__dict__})


def read(request, record_id):
    # Retrieve the record with the given ID
    record = get_record(record_id)

    # Return a JSON response with the retrieved record
    return JsonResponse({'record': record.__dict__})


def update(request, record_id):
    # Extract the data from the request
    data = request.POST.dict()

    # Update the record with the given ID using the data
    record = update_record(record_id, data)

    # Return a JSON response with the updated record
    return JsonResponse({'record': record.__dict__})


def delete(request, record_id):
    # Delete the record with the given ID
    delete_record(record_id)

    # Return a JSON response indicating success
    return JsonResponse({'status': 'Record deleted successfully'})

