from django.core.exceptions import ValidationError


def validate_file_size(file):
  """Validate the file to upload"""
  max_size_kb = 100

  if file.size > max_size_kb * 1024:
    raise ValidationError(f'PLease, upload a file smaller than {max_size_kb} KB!')
