from component.common.entity_form import EntityForm, FormField
from adapters.translator_data_adapter import TranslatorDataAdapter


class TransForm(EntityForm):

    def __init__(self, right_stack=None):
        super().__init__(
            title="Translators",
            fields=[
                FormField("Id:", "txt_id", lambda t: t.id, readonly=True),
                FormField("Name:", "txt_name", lambda t: t.name),
                FormField("language:", "txt_language", lambda t: t.languages),
            ],
            search_fn=TranslatorDataAdapter.search,
            right_stack=right_stack,
        )