'''
    Documentation

    Allows users to search through and view WebElement API documentation.
'''

import pydoc

import logging as log
from WebBot import Page, PageControls
from WebElements import UITemplate, ClientSide
import GuiBuilderConfig

ELEMENTS = GuiBuilderConfig.Factory.products.keys()

class Documentation(Page):
    class ContentControl(PageControls.TemplateControl):
        template = UITemplate.fromFile("Pages/Documentation/Template.wui")

        def initUI(self, ui, request):
            ui.results.replaceWith(self.results)
            ui.document.replaceWith(self.document)
            ui.search.clientSide.focus()
            ui.search.clientSide.on("keyup", self.results.clientSide.get(timeout=500))

        def setUIData(self, ui, request):
            """
                Any data populating that occurs as a result of the data in the request should be done here.
            """
            pass

        def processPost(self, ui, request):
            """
                Any unique processing that needs to be done on a post should be done here.
                Note: There is corresponding process(Get|Delete|Put) methods.
            """
            pass

        def validPost(self, ui, request):
            """
                Any validation of post data should occur here: with true being returned only if the data
                is valid.
                Note: There is corresponding valid(Get|Delete|Put) methods.
            """
            return True

    class Document(PageControls.TemplateControl):
        template = UITemplate.fromFile("Pages/Documentation/Document.wui")

        def initUI(self, ui, request):
            openDocument = request.fields.get('load')
            if openDocument:
                ui.display.setVisibleElement(ui.openDocument)
                html = ui.openDocument.addChildElement(self.buildElement('straightHTML'))
                htmlDoc = pydoc.HTMLDoc()
                product = GuiBuilderConfig.Factory.build(openDocument.lower(), "", "")
                if product:
                    html.html = htmlDoc.docclass(product.__class__)
                    html.html = html.html.replace('href="', 'href="Documentation?load=').replace(".html", "")

    class Results(PageControls.TemplateControl):
        template = UITemplate.fromFile("Pages/Documentation/Results.wui")
        grabFields = ('search', )

        def setUIData(self, ui, request):
            search = request.fields.get('search', '')
            if not search:
                usedProducts = []
                for data in GuiBuilderConfig.sections:
                    name = data['Name']
                    numberOfElements = len(data['Factory'].products)
                    elements = data['Factory'].products.iteritems()

                    section = ui.sections.addChildElement(self.buildElement("Accordion", name))
                    section.setLabel(name)
                    section.toggle.attributes['tooltip'] = data['Factory'].__doc__
                    section.style['width'] = "100%"
                    elementsContainer = section.addChildElement(self.buildElement("multiSelect"))
                    elementsContainer.style['height'] = "%dpx" % (numberOfElements * 20)
                    elementsContainer.style['width'] = "100%"
                    elementsContainer.addJavascriptEvent('onchange', self.document.clientSide.get(load=
                                            ClientSide.Script("WebElements.selectedOption(this).value")))

                    for elementName, element in elements:
                        if element in usedProducts:
                            continue
                        else:
                            elementsContainer.addOption(elementName)
                ui.sections[0].addClass("First")
                ui.sections[-1].addClass("Last")
                return

            results = ui.sections.addChildElement(self.buildElement("multiSelect"))
            results.addClass("Results")
            results.style['width'] = "100%"
            results.addOptions([productName for productName in ELEMENTS if search.lower() in productName.lower()])
            results.style['height'] = "%dpx" % (len(results.childElements) * 20)
            results.addJavascriptEvent('onchange', self.document.clientSide.get(load=
                                       ClientSide.Script("WebElements.selectedOption(this).value")))
            return results

