from component.common.entity_form import EntityForm, FormField
from adapters.author_data_adapter import AuthorDataAdapter


class AuthorForm(EntityForm):

    def __init__(self, right_stack=None):
        super().__init__(
            title="Authors",
            fields=[
                FormField("Id:", "txt_id", lambda a: a.id, readonly=True),
                FormField("Name:", "txt_name", lambda a: a.name),
                FormField("Birth Date:", "txt_birth_date", lambda a: a.birthdate),
                FormField("Nationality:", "txt_nationality", lambda a: a.nationality),
            ],
            search_fn=AuthorDataAdapter.search,
            right_stack=right_stack,
        )