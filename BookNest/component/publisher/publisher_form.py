from component.common.entity_form import EntityForm, FormField
from adapters.publisher_data_adapter import PublisherDataAdapter


class PublisherForm(EntityForm):

    def __init__(self, right_stack=None):
        super().__init__(
            title="Publishers",
            fields=[
                FormField("Id:", "txt_id", lambda p: p.id, readonly=True),
                FormField("Name:", "txt_name", lambda p: p.name),
                FormField("Address:", "txt_address", lambda p: p.address),
                FormField("Website:", "txt_website", lambda p: p.website),
            ],
            search_fn=PublisherDataAdapter.search,
            right_stack=right_stack,
        )