import json

from django.core.cache import cache

from catalog.models import Item
from catalog.serializers import ItemSerializer


# La estructura de datos de caché se compone de la siguiente forma:
# {
#     'e480d1b0-cb8e-448c-9864-ed7ae4ce20b3': 'cuenta_vista',
#     'cuenta_vista': 'e480d1b0-cb8e-448c-9864-ed7ae4ce20b3',
#     'no-existe': 'invalid',
#     'no-existe-2': 'invalid'
# }


INVALID_ITEM = 'invalid'


def get_item_id(item_name:str) -> str:
    item_id = cache.get(item_name)
    # Esta validación solo aplica para los tipos de cuenta que vengan desde el banco y no estén guardados
    # en el catálogo de BD
    if item_id == INVALID_ITEM:
        return None
    if item_id is not None:
        return item_id
    try:
        obj = Item.objects.get(item_name=item_name)
        cache.set(item_name, str(obj.id), 360000)
        return cache.get(item_name)
    except Item.DoesNotExist:
        cache.set(item_name, INVALID_ITEM, 360000)
        return None


def get_item_name(item_id:str) -> str:
    item_name = cache.get(item_id)
    if item_name is not None:
        return item_name
    else:
        obj = Item.objects.get(id=item_id)
        cache.set(item_id, obj.item_name, 360000)
        return cache.get(item_id)
