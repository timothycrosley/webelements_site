'''
    The Home Page for %(label)s
'''

import logging as log
from WebBot import Page, PageControls
from WebElements import UITemplate

exampleCode = """
from WebElements import Layout, Document, Buttons

page = Document.Document()
layout = page.addChildElement(Layout.Center()).addChildElement(Layout.Horizontal())
layout += Buttons.Button(text="Use WebElements.", **{'class':'MainAction'})
layout += Buttons.Button(text="Enjoy writing less code.", **{'class':'DeleteAction'})
layout += Buttons.Button(text="100% Python.")

print page.toHTML(formatted=True)
"""

exampleOutput = """
<!DOCTYPE html>
<html>
 <head>
  <title>
  </title>
  <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
  </meta>
 </head>
 <body>
  <div class="WCenter">
   <div class="WOuter">
    <div class="WInner">
     <div class="WClear">
      <input class="WBlock WLeft MainAction" type="button" value="Use WebElements." />
      <input class="WBlock WLeft DeleteAction" type="button" value="Enjoy writing less code." />
      <input class="WBlock WLeft" type="button" value="100% Python." />
     </div>
    </div>
   </div>
  </div>
 </body>
</html>
"""

class Home(Page):
    class ContentControl(PageControls.TemplateControl):
        template = UITemplate.fromFile("Pages/Home/Template.wui")

        def initUI(self, ui, request):
            """
                The initial setup of the interface (such as dynamically adding widgets that are not present in the
                view) should be done here.
            """
            pass

        def setUIData(self, ui, request):
            """
                Any data populating that occurs as a result of the data in the request should be done here.
            """
            ui.exampleCode.code = exampleCode
            ui.exampleOutput.code = exampleOutput

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

