import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv

load_dotenv()

genai.configure(api_key=getenv('GOOGLE_API_KEY'))


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def get_ideas(audience, about=None):
    convo = model.start_chat(history=[])

    if about:
        prompt = f"""\
                You must give me 5 new book ideas for the targeted audience of: {audience} 
                in the field of {about}
                in the following format:

                BOOK TITLE: DESCRIPTION
                """

    else:
        prompt = f"""\
        You must give me new 10 book ideas for the targeted audience of: {audience} 
        in the following format:
        
        "TITLE: <BOOK TITLE>:\nDESCRIPTION: <DESCRIPTION>\n"
        
        and do not add any numbering or split the books with a "\n"
        """

    convo.send_message(prompt)

    response = convo.last.text

    books_split = response.split(f'\n\n')

    books = """\
    <table class="table table-striped">
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Description</th>
            <td></td>
        </tr>
    """

    _id = 1

    for book in books_split:
        ns = book.split("\n")

        if ns[0][:2] == ns[0][-2:] == '**':
            ns[0] = ns[0][2:-2]

        books += f"""
        <tr id='{_id}'>
            <td>{_id}</td>
            <td name='title' id='title_{_id}'>{ns[0][7:]}</td>
            <td name='desc' id='desc_{_id}'>{ns[1][13:]}</td>
            <td>
                <button onclick="useIdeas({_id})" class="btn btn-primary">Use This</button>
            </td>
        </tr>
"""
        _id += 1

    books += "</table>"
    return [books]


if __name__ == '__main__':
    get_ideas('middle aged women')
