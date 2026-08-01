from component.common.entity_form import EntityForm, FormField
from adapters.designer_data_adapter import DesignerDataAdapter


class DesignerForm(EntityForm):

    def __init__(self, right_stack=None):
        super().__init__(
            title="CoverDesigners",
            fields=[
                FormField("Id:", "txt_id", lambda d: d.id, readonly=True),
                FormField("Name:", "txt_name", lambda d: d.name),
                FormField("Birth Date:", "txt_birth_date", lambda d: d.birthdate),
                FormField("Nationality:", "txt_nationality", lambda d: d.nationality),
            ],
            search_fn=DesignerDataAdapter.search,
            right_stack=right_stack,
        )