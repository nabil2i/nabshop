from django.core.exceptions import ValidationError


def validate_file_size(file):
  """Validate the file to upload"""
  max_size_mb = 5

  if file.size > max_size_mb * 1024 * 1024:
    raise ValidationError(f'Please, upload a file smaller than {max_size_mb} MB!')
