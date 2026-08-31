from component.common.entity_list_panel import EntityListPanel
from adapters.translator_data_adapter import TranslatorDataAdapter


class TranslatorWin(EntityListPanel):

    def __init__(self):
        super().__init__(object_name="translator_page", fetch_all=TranslatorDataAdapter.get_all)