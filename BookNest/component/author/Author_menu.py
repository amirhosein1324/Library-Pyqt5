from component.common.entity_list_panel import EntityListPanel
from adapters.author_data_adapter import AuthorDataAdapter


class AuthorWin(EntityListPanel):

    def __init__(self):
        super().__init__(object_name="author_page", fetch_all=AuthorDataAdapter.get_all)