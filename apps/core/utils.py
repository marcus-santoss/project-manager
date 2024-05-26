import yaml
from django.views.generic import View


def read_config(view: View):
    action_map: dict[str, str] = {
        "delete.html": "delete",
        "detail.html": "detail",
        "list.html": "list",
    }
    app: str = view.model._meta.app_label
    model_name: str = view.model._meta.verbose_name
    template_name: str = view.template_name.split("/")[-1]
    action: str = action_map.get(template_name, "create")

    with open(f"apps/{app}/configs/{model_name}.yaml") as fp:
        data = yaml.safe_load(fp)

    return {
        **data["model_info"],
        **data["pages"][action],
        **data["urls"],
    }
