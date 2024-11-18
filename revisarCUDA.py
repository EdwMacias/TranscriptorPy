import torch
print(torch.cuda.is_available())  # Debería devolver True
print(torch.cuda.get_device_name(0))  # Para verificar el nombre de la GPU
