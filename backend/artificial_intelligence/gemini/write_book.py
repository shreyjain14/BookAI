def writeChapter(convo, title, audience, outline):
    prompt = f"""\
    write me an introduction for a light novel story for the target audience of {audience} a book titled 
    "{title}"
    You must reply in the following format:
    
    
    INTRODUCTION: 
    <insert introduction here>
    
    """

    convo.send_message(prompt)
