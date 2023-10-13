from typing import Dict
import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


class view_fam:
    def __init__(self, page: Page) -> None:
        self.vs: Dict[str, View] = {}
        """ 页页集 """

        vv = [
            ElevatedButton(
                f"页{i}",
                on_click=lambda x: page.go(f"/pg_{x.control.data}"),
                data=i,
            )
            for i in range(10)
        ]
        vv.insert(0, AppBar(title=Text("主页"), bgcolor=colors.SURFACE_VARIANT))

        self.vs["main"] = View("/", vv)  # 主页

        for i in range(10):
            self.vs[f"/pg_{i}"] = View(
                f"/pg_{i}",
                [
                    AppBar(title=Text(f"页{i}"), bgcolor=colors.BLUE_ACCENT_100),
                    ElevatedButton(
                        "上一页",
                        on_click=lambda x: page.go(f"/pg_{x.control.data-1}"),
                        disabled=i <= 0,
                        data=i,
                    ),
                    ElevatedButton("去主页", on_click=lambda _: page.go("/")),
                    ElevatedButton(
                        "下一页",
                        on_click=lambda x: page.go(f"/pg_{x.control.data+1}"),
                        disabled=i >= 9,
                        data=i,
                    ),
                ],
            )


def main(page: Page):
    page.title = "Routes Example"
    vvs = view_fam(page)
    """页面的集合"""

    def route_change(route):
        """
        当收到信号，要改变页面时，用这个来决定具体要加载的页面\n
        实际上，当收到回退信号时，并不能后退到上一个页面，而是直接加载主页
        """
        if page.route == "/":
            if page.views[0].route == "/":
                return
            else:

                page.views.clear()

                page.views.append(vvs.vs["main"])
                page.update()
        else:
            if page.route == page.views[0].route:
                pass
            else:

                v = vvs.vs.get(page.route, None)
                if v is not None:
                    page.views.clear()
                    page.views.append(v)
                    page.update()

    def view_pop(view):

        if len(page.views) == 0:
            page.views.append(vvs.vs["main"])
        elif page.views[0].route == "/":
            pass
        else:
            page.views.clear()
            page.views.append(vvs.vs["main"])

        page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


# flet.app(target=main, view=flet.WEB_BROWSER)
flet.app(target=main)

