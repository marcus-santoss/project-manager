from apps.core.utils import read_config


class DefaultContextMixin:
    """Lê o arquivo yaml de configurações e injeta as informaçõe no contexto da view"""

    def get_context_data(self, **kwargs):
        kwargs.update(**read_config(self))
        return super().get_context_data(**kwargs)
