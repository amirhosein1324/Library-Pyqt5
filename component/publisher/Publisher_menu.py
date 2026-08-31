from component.common.entity_list_panel import EntityListPanel
from adapters.publisher_data_adapter import PublisherDataAdapter


class PublisherWin(EntityListPanel):

    def __init__(self):
        super().__init__(object_name="publisher_page", fetch_all=PublisherDataAdapter.get_all)