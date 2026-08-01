from component.common.entity_list_panel import EntityListPanel
from adapters.language_data_adapter import LanguageDataAdapter


class LanguageWin(EntityListPanel):

    def __init__(self):
        super().__init__(object_name="language_page", fetch_all=LanguageDataAdapter.get_all)