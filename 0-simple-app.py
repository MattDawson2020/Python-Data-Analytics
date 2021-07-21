import justpy as jp

# justpy has JS roots so uses a similar syntax to node with app()
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes ="text-p1 text-center")
    # order of these elements matter, as they are added on the page in that order
    return wp



jp.justpy(app)