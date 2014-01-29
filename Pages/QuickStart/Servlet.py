'''
    QuickStart

    Shows quick start guides for common web element actions
'''

import logging as log
from WebBot import Page, PageControls
from WebElements import UITemplate

HELLOWORLD_IN = """
from WebElements import Document, Display

page = Document()
page += Display.Label(text="Hello World!")
print page
"""

HELLOWORLD_OUT = """
<!DOCTYPE html>
<html>
 <head>
  <title>
  </title>
  <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
  </meta>
 </head>
 <body>
  <label>
   Hello World!
  </label>
 </body>
</html>
"""

COMBINE_EXAMPLE = """
from WebElements import Layout, Buttons, Document

page = Document.Document()
layout = page.addChildElement(Layout.Horizontal())
layout += Buttons.Button('button1', text='Button1')
layout += Buttons.Button('button2', text='Button2')

print repr(page)

###--------------------------- Output-------------------- ###

'''
Document()
|---Head()
|  |---Title()
|  |  |---TextNode('')
|  |---HTTPHeader()
|---Body()
|  |---Horizontal()
|  |  |---Button(id='button1', name='button1')
|  |  |---Button(id='button2', name='button2')
'''
"""

XML_TEMPLATE_EXAMPLE = """
<document>
    <horizontal>
        <button accessor="button1" text="Button1" />
        <button accessor="button2" text="Button2" />
    </horizontal>
</document>
"""

SHPAML_TEMPLATE_EXAMPLE = """
document
    horizontal
        > button@button1 text="Button1"
        > button@button2 text="Button2"
"""

LOAD_TEMPLATE_EXAMPLE = """
from WebElements import UITemplate, Base, All

ui = Base.TemplateElement(template=UITemplate.fromFile('example.wui'), factory=All.Factory)
"""

CUSTOM_ELEMENT_EXAMPLE = """
from WebElements import Factory, Layout, Display, Buttons

Factory = Factory.Factory("CustomFactory")


class LabelButton(Layout.Horizontal):
    '''
        Places a label and a button side by side
    '''
    properties = Layout.Horizontal.properties.copy()
    properties['text'] = {'action':'setText'}

    def _create(self, id=None, name=None, parent=None, **kwargs):
        Layout.Horizontal._create(self, id, name, parent, **kwargs)

        self.label = self.addChildElement(Display.Label())
        self.button = self.addChildElement(Buttons.Button())

    def setText(self, text):
        '''
            Sets the text beside the button
        '''
        self.label.setText(text)

Factory.addProduct(LabelButton)

"""

USING_CUSTOM_ELEMENT_EXAMPLE = """
from WebElements import Factory, All, Base
import CustomElements

factory = CompositeFactory((All.Factory, CustomElements.Factory))
ui = Base.TemplateElement(template=UITemplate.fromFile('template.wui'), factory=factory)
"""

ADDING_ROWS_EXAMPLE = """
from WebElements.DataViews import Table

table = Table("myTable")
row = table.addRow()
row.cell('Name').setText('Timothy')
row.cell('Email').setText('timothy.crosley@gmail.com')
row.cell('Phone').setText('(410) 212-7618')

row = table.addRow()
row.cell('Name').setText('James')
row.cell('Email').setText('james@madeupperson.com')
row.cell('Phone').setText('(555) 555-5555')
"""

PASSING_DATA_EXAMPLE = """
from WebElements.DataViews import Table

table = Table("myTable")

data = ((('Name', 'Timothy'),
         ('Email', 'timothy.crosley@gmail.com'),
         ('Phone', '(410) 212-7618')),
        (('Name', 'James'),
         ('Email', 'james@madeupperson.com'),
         ('Phone', '(555) 555-5555')))

table.addRows(data)
"""

CHANGE_ORDER_EXAMPLE = """
table.columns = ('Email', 'Phone', 'Name')
"""

EXAMPLE_TABLE_DATA = ((('Name', 'Timothy'), ('Email', 'timothy.crosley@gmail.com'),
                       ('Phone', '(410) 212-7618')),
                      (('Name', 'James'), ('Email', 'james@madeupperson.com'),
                       ('Phone', '(555) 555-5555')))

class QuickStart(Page):
    class ContentControl(PageControls.TemplateControl):
        template = UITemplate.fromFile("Pages/QuickStart/Template.wui")

        def initUI(self, ui, request):
            """
                The initial setup of the interface (such as dynamically adding widgets that are not present in the
                view) should be done here.
            """
            ui.helloWorldPython.code = HELLOWORLD_IN
            ui.helloWorldHTML.code = HELLOWORLD_OUT
            ui.combineExample.code = COMBINE_EXAMPLE
            ui.xmlTemplateExample.code = XML_TEMPLATE_EXAMPLE
            ui.shpamlTemplateExample.code = SHPAML_TEMPLATE_EXAMPLE
            ui.loadTemplateExample.code = LOAD_TEMPLATE_EXAMPLE
            ui.customElementExample.code = CUSTOM_ELEMENT_EXAMPLE
            ui.usingCustomElementsExample.code = USING_CUSTOM_ELEMENT_EXAMPLE
            ui.addingRowsExample.code = ADDING_ROWS_EXAMPLE
            ui.passingDataExample.code = PASSING_DATA_EXAMPLE
            ui.changeOrderExample.code = CHANGE_ORDER_EXAMPLE

            ui.myTable.addRows(EXAMPLE_TABLE_DATA)
            ui.myTable2.addRows(EXAMPLE_TABLE_DATA)

            ui.myTable2.columns = ('Email', 'Phone', 'Name')

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
