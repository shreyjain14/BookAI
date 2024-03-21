import anthropic
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY'),
)

CLAUDE_MODEL = 'claude-3-haiku-20240307'


def claude_outline(title, audience, description):
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1000,
        temperature=0,
        system="You are an expert in book author.\n"
               "you must respond to the questions in JSON and the format would be given."
               "DO NOT ADD ANY \n in the json",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f'write me an outline for a light novel story for the target audience of {audience} \na book titled "{title}" and here is a small description about the book: \n{description} \nYou must reply in the following format: \n\n'
                                '{"title":<insert title here>,"introduction":<insert introduction here>,"chapter<number>":{"title":<insert chapter title here>,"content":<insert a brief about the chapter here>}}'
                    }
                ]
            }
        ]
    )

    reply = ''.join(message.content[0].text.split('\n'))

    rep = json.loads(reply)

    chapters = [('Introduction', rep["introduction"])]

    book = []

    for chapter in rep:
        if chapter != 'title' and chapter != 'introduction':
            chapters.append((rep[chapter]['title'], rep[chapter]['content']))

    cnt = ''

    try:

        for chapter in chapters:
            message = client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=1000,
                temperature=1,
                system="You are an expert in book author.\n"
                       "you must write a whole chapter."
                       "Do not write the book title just the chapter content.",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f'CHAPTER TITLE: {title}, DESCRIPTION: {description} in the following format: <chapter content>'
                            }
                        ]
                    }
                ]
            )

            print(message.content)

            book.append((chapter[0], message.content[0].text))

        for chapter in book:
            cnt += f'''
            <div class="row">
                <h3>{chapter[0]}</h3>
            </div>
            <div class="row">
                <p>{chapter[1]}</p>
            </div>
            '''

    except anthropic.RateLimitError as e:
        print(f'RATE LIMIT: {e}')
        cnt = 'ERROR: RATE LIMIT | Please try again later.'

    return [cnt]
