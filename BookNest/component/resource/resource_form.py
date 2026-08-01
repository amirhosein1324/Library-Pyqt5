from component.common.entity_form import EntityForm, FormField
from adapters.resource_data_adapter import ResourcesDataAdapter


class ResourceForm(EntityForm):

    def __init__(self, right_stack=None):
        super().__init__(
            title="Resources",
            fields=[
                FormField("Id:", "txt_id", lambda r: r.id, readonly=True),
                FormField("Name:", "txt_name", lambda r: r.name),
            ],
            search_fn=ResourcesDataAdapter.search,
            right_stack=right_stack,
        )