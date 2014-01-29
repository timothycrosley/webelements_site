import WebElements
from DynamicForm.AppEngine import DynamicForm, PageControls
from WebElements import UITemplate, Buttons

PAGES = [('Quick Start Guides', 'QuickStart'), ('API Documentation', 'Documentation'), ('Discuss', 'Discuss')]

class Page(DynamicForm):
    def title(self, request):
        return "WebElements - Python Building Blocks for the Web"

    class MainControl(PageControls.TemplateControl):
        template = UITemplate.fromFile("WebBot/Page.wui")

        def initUI(self, ui, request):
            ui.pageContents.replaceWith(self.contentControl)

            for pageName, page in PAGES:
                newLink = ui.pageLinks.addChildElement(Buttons.Link(href=page))
                button = newLink.addChildElement(Buttons.ToggleButton(page + "Link", text=pageName))
                if page in request.path:
                    button.toggleOn()
                    newLink.setDestination("Home")

        def setUIData(self, ui, request):
            ui.version.setText(WebElements.__version__)
