from ninja import NinjaAPI, Redoc
from blog.models import Post, Category, Hashtag
from django.contrib.auth.models import User
from .models import PostInputSchema, PostOutputSchema, HashtagOutputSchema, MessageSchema
from typing import List

api = api()

@api.post("/providers")
def create_provider(request, provider: providerOutputSchema):
    new_provider = provider.objects.create(**provider.dict())
    return {"message": "Provider created successfully", "provider_id": new_provider.id}

    "id": service.id,
        "titulo": service.titulo,
        "texto": service.texto,
        "fecha": service.fecha.strftime("%d/%m/%Y"),
        "autor": {
            "id": service.autor.id,
            "username": service.autor.username,
        }
    
    

@api.get("/service", response={200: list[serviceOutputSchema]})
def get_service(request, is_active: bool = Query(True)):
    service = service.objects.filter(is_active=is_active)
    return service

@api.get("/service/{provider_id}", response={200: serviceOutputSchema})
def get_service(request, provider_id: int):
    service = service.objects.get(provider_id=provider_id)
    return service

@api.post("/service/", response={200: serviceOutputSchema, 404:MessageSchema)
def create_service(request, service: serviceOutputSchema):
    try:
     provider = user.objects.get(id=serviceOutputSchema)
   except user.DoesNotExist:
    return 404, {'Message': 'provider not found'}
   new_service =service.objects.create(
	price=service.price,
	thru_date=service.thru_date,
   )
new_service.provider.add(provider)
new_service.save()

retur {'Message': 'service has been created'}



