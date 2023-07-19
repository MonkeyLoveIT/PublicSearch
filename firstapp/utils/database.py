from firstapp.models import Book  # Import your Django model(s)


def create_record(data):
    data.pop('csrfmiddlewaretoken', None)  # 排除 'csrfmiddlewaretoken' 参数
    record = Book.objects.create(**data)
    return record



def get_record(record_id):
    # Logic to retrieve a record with the given ID
    record = Book.objects.get(id=record_id)
    return record


def update_record(record_id, data):
    # Logic to update a record with the given ID and data
    record = Book.objects.get(id=record_id)
    for key, value in data.items():
        setattr(record, key, value)
    record.save()
    return record


def delete_record(record_id):
    # Logic to delete a record with the given ID
    record = Book.objects.get(id=record_id)
    record.delete()
    return True
