from component.common.entity_form import EntityForm, FormField
from adapters.language_data_adapter import LanguageDataAdapter


class LanguageForm(EntityForm):

    def __init__(self, right_stack=None):
        super().__init__(
            title="Languages",
            fields=[
                FormField("Id:", "txt_id", lambda l: l.id, readonly=True),
                FormField("Name:", "txt_name", lambda l: l.name),
            ],
            search_fn=LanguageDataAdapter.search,
            right_stack=right_stack,
        )