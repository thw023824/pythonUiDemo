from typing import List
import flet
from flet import (
    Container,
    Draggable,
    DragTarget,
    Page,
    Row,
    Text,
    alignment,
    colors,
    control_event,
)


class m_item:
    value: int
    name: str
    color: str

    def __init__(self, name: str, value: int = 0) -> None:
        self.name = str(name)
        self.value = value
        self.color = colors.CYAN_ACCENT_100


class m_family:
    def __init__(self) -> None:
        self.chd: List[m_item] = []
        for i in range(10):
            m = m_item(f"n_{i}", i)
            if i % 2 == 0:
                m.color = colors.PINK_100
            self.chd.append(m)

    def get_by_value(self, v: int):
        for i in range(len(self.chd)):
            if self.chd[i].value == v:
                return (i, self.chd[i])
        return None


class page_one:
    def __init__(self, page: Page) -> None:

        page.title = "Drag and Drop example 2"
        self.page = page
        self.fam = m_family()
        self.ui_row = Row([])

    def make_row(self):
        ll = len(self.fam.chd)
        self.ui_row.controls.clear()
        for i in range(ll):
            mvv = self.fam.chd[i]
            self.ui_row.controls.append(
                Draggable(
                    group="number",
                    content=DragTarget(
                        group="number",
                        content=Container(
                            width=50,
                            height=50,
                            bgcolor=mvv.color,
                            border_radius=5,
                            content=Text(f"{mvv.value}", size=20),
                            alignment=alignment.center,
                        ),
                        on_accept=self.drag_accept,
                        on_will_accept=self.drag_will_accept,
                    ),
                    content_when_dragging=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                ),
            )
            if i < ll - 1:
                self.ui_row.controls.append(
                    Container(width=10),
                )

    def update_row(self):
        ct = 0
        for i in self.ui_row.controls:
            if isinstance(i, Draggable):
                i.content.content.content.value = str(self.fam.chd[ct].value)
                i.content.content.bgcolor = self.fam.chd[ct].color
                ct += 1

    def drag_accept(self, e: flet.DragTargetAcceptEvent):

        src: Draggable = self.page.get_control(e.src_id)
        tar: DragTarget = self.page.get_control(e.target)
        src_value = int(src.content.content.content.value)
        tar_value = int(tar.content.content.value)

        ia, _ = self.fam.get_by_value(src_value)
        ib, _ = self.fam.get_by_value(tar_value)
        self.fam.chd[ia], self.fam.chd[ib] = self.fam.chd[ib], self.fam.chd[ia]

        self.update_row()
        self.ui_row.update()

    def drag_will_accept(self, e: control_event.ControlEvent):
        e.control.update()


def main(page: Page):
    vvv = page_one(page)
    vvv.make_row()
    page.add(vvv.ui_row)


flet.app(target=main)


#from https://www.cnblogs.com/unm001/p/16721397.html





