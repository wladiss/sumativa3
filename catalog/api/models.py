from ninja import Schema
from typing import List

class MessageSchema(Schema)
message: str

class ProviderInputSchema(Schema):
 nombre: str
 rut: str
razon_social: str
activo: bool
 Contact: list[ContactOutputSchema]
 Adress: list[AddressOutputShema]


class ContactOutputSchema(Schema):
 nombre: str
 telefono: str
 correo: str 
 tipo: str

class AddressOutputShema(Schema):
 direccion: str
 calle: str
 codigo_postal: str
   region: str

class ServiceOutputShema(Shema):
costo: float
fecha_inicio: str
fecha_fin: str
provider: [providerOutputSchema]




