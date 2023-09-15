import streamlit as st
from langchain import PromptTemplate
from langchain.document_loaders import YoutubeLoader
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from huggingface_hub import InferenceClient
from templates import BLOG_TEMPLATE, IMAGE_TEMPLATE

CLIENT = InferenceClient()

# Initialize Streamlit
st.set_page_config(page_title ="📝 Article Generator App")
st.title('📝 Article Generator App')

# Getting the OpenAI API key from the sidebar
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
chat_model = None
if openai_api_key.startswith('sk-'):
    chat_model = ChatOpenAI(model_name='gpt-3.5-turbo-16k', openai_api_key=openai_api_key)
else:
    st.warning('Please enter a valid OpenAI API key!', icon='⚠')

@st.cache_data ()
def generate_blog(yt_url):
    """Generate a blog article from a YouTube URL."""
    loader = YoutubeLoader.from_youtube_url(yt_url, add_video_info=True)
    transcript = loader.load()

    """Create a response schema for structured output."""
    schema = [
        ResponseSchema(name="title", description="Article title"),
        ResponseSchema(name="meta_description", description="Article Meta Description"),
        ResponseSchema(name="content", description="Article content in markdown"),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(schema)
    format_instructions = output_parser.get_format_instructions()
    
    prompt = PromptTemplate(
        input_variables=['transcript'],
        template=BLOG_TEMPLATE,
        partial_variables={"format_instructions": format_instructions}
    )
    prompt_query = prompt.format(transcript=transcript[0].page_content)

    response = chat_model.predict(prompt_query)
    
    return output_parser.parse(response), transcript[0].metadata["thumbnail_url"]

@st.cache_data ()
def generate_image(title):
    """Generate an image based on the title."""
    prompt = PromptTemplate(
        input_variables=['title'],
        template=IMAGE_TEMPLATE,
    )
    prompt_query = prompt.format(title=title)

    stb_prompt = chat_model.predict(prompt_query)

    tags = [
        stb_prompt,
        'award winning',
        'high resolution',
        'photo realistic',
        'intricate details',
        'beautiful',
        '[trending on artstation]'
    ]
    result = ', '.join(tags)
    response = CLIENT.post(json={
        "inputs": result,
        "parameters": { "negative_prompt": 'blurry, artificial, cropped, low quality, ugly'}
    }, model="stabilityai/stable-diffusion-2-1")

    return response

# Creating a form to get the YouTube URL
with st.form('myform'):
    yt_url = st.text_input('Enter youtube url:', '')
    generate_image_option = st.checkbox('Generate Image Instead of Thumbnail')
    submitted = st.form_submit_button('Submit')
    
    if submitted and chat_model and yt_url:
        with st.spinner("Generating blog... This may take a while⏳"):
            blog, thumbnail = generate_blog(yt_url)
            if generate_image_option:
                with st.spinner("Generating image... This may take a while⏳"):
                    image = generate_image(blog['title'])
                    st.image(image)
            else:
                st.image(thumbnail)
            st.markdown(blog['content'])