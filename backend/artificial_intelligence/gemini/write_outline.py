from backend.artificial_intelligence.gemini.new_convo import new_convo


def get_book_outline(title, audience, description):
    prompt = f"""\
    write me an outline for a light novel story for the target audience of {audience} a book titled 
    "{title}"
    and here is a small description about the book:
    
    {description}
    
    You must reply in the following format:
    
    TITLE: <insert title here>
    
    SPLIT
    
    INTRODUCTION: 
    <insert introduction here>
    
    SPLIT
    
    CHAPTER #:<insert chapter title here> 
    <insert a brief about the chapter here>
    
    SPLIT
    """

    convo = new_convo()

    convo.send_message(prompt)

    print(convo.last.text)

    return convo.last.text.split('SPLIT')

