from component.common.entity_form import EntityForm, FormField
from adapters.category_data_adapter import CategoryDataAdapter


class CategoryForm(EntityForm):

    def __init__(self, right_stack=None):
        super().__init__(
            title="Categories",
            fields=[
                FormField("Id:", "txt_id", lambda c: c.id, readonly=True),
                FormField("Name:", "txt_name", lambda c: c.name),
            ],
            search_fn=CategoryDataAdapter.search,
            right_stack=right_stack,
        )