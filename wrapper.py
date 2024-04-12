from reportlab.lib.utils import simpleSplit

def getWrapedText(canvas, text, width, x_position, y_position, font_size, fontFamily="Helvetica"):
    canvas.setFont(fontFamily, font_size)
    max_width = width  # Define the maximum width for the schoolName text
    wrapped_schoolName = simpleSplit(text=text, fontName=fontFamily, fontSize=font_size, maxWidth=max_width)

    if len(wrapped_schoolName) > 1:
        y_position += 10

    for line in wrapped_schoolName:
        canvas.drawCentredString(x_position, y_position, line)
        y_position -= 24  # Move to the next line; adjust the value as needed based on font size