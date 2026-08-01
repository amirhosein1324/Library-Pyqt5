from component.common.entity_list_panel import EntityListPanel
from adapters.resource_data_adapter import ResourcesDataAdapter


class ResourceWin(EntityListPanel):

    def __init__(self):
        super().__init__(object_name="resource_page", fetch_all=ResourcesDataAdapter.get_all)