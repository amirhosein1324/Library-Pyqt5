from component.common.entity_list_panel import EntityListPanel
from adapters.category_data_adapter import CategoryDataAdapter


class CategoryWin(EntityListPanel):

    def __init__(self):
        super().__init__(object_name="category_page", fetch_all=CategoryDataAdapter.get_all)