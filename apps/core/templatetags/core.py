from apps.project.models import ClientLevelChoices, StatusChoices
from django import template

register = template.Library()


@register.filter(name="fill_url")
def fill_url(url: str, obj_id: str) -> str:
    return url.format(uuid=obj_id)


def get_enum_value(enum_clazz, field_name, obj):
    status_map: dict = {x.value: x.label for x in enum_clazz}
    return status_map[getattr(obj, field_name)]


@register.filter(name="get_field_value")
def get_field_value(obj, field: str) -> str:
    if "::" in field:
        field_name, enum_class = field.split("::")
        if enum_class == StatusChoices.__name__:
            return get_enum_value(StatusChoices, field_name, obj)

        if enum_class == ClientLevelChoices.__name__:
            return get_enum_value(ClientLevelChoices, field_name, obj)

        return "-"

    if field.endswith("()"):
        field = field.replace("()", "")

        for part in field.split("."):
            obj = getattr(obj, part)
        return obj()

    if "." in field:
        name, prop = field.split(".")
        field = getattr(obj, name)
        return getattr(field, prop)

    return getattr(obj, field)
