import uuid


def get_uploaded_file_path(instance, filename):
    return 'media/{}/{}'.format(uuid.uuid4(), filename)
