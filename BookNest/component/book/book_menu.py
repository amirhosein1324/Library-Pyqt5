from component.common.entity_list_panel import EntityListPanel
from adapters.book_data_adapter import BookDataAdapter


class BookWin(EntityListPanel):

    def __init__(self):
        super().__init__(
            object_name="book_page",
            fetch_all=BookDataAdapter.get_all,
            label_fn=lambda book: book.title,
            show_add_button=True,
        )