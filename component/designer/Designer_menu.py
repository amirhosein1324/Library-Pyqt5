from component.common.entity_list_panel import EntityListPanel
from adapters.designer_data_adapter import DesignerDataAdapter


class DesignerWin(EntityListPanel):

    def __init__(self):
        super().__init__(object_name="designer_page", fetch_all=DesignerDataAdapter.get_all)