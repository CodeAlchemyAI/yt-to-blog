import streamlit as st
from langchain import PromptTemplate
from langchain.document_loaders import YoutubeLoader
from langchain.chat_models import ChatOpenAI

# Setting up the page title and header
st.set_page_config(page_title ="📝 Article Generator App")
st.title('📝 Article Generator App')

# Getting the OpenAI API key from the sidebar
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# A function to generate a blog article from a YouTube URL
def generate_blog(yt_url, openai_api_key):
    # Loading the video transcript
    loader = YoutubeLoader.from_youtube_url(yt_url, add_video_info=True)
    transcript = loader.load()
    
    # Creating an instance of the chat model
    chat_model = ChatOpenAI(model_name='gpt-3.5-turbo-16k', openai_api_key=openai_api_key)
    
    # Creating a prompt template
    template = """Act as an expert copywriter specializing in content optimization for SEO. Your task is to take a given YouTube transcript and transform it into a well-structured and engaging article. Your objectives are as follows:

        Content Transformation: Begin by thoroughly reading the provided YouTube transcript. Understand the main ideas, key points, and the overall message conveyed.

        Sentence Structure: While rephrasing the content, pay careful attention to sentence structure. Ensure that the article flows logically and coherently.

        Keyword Identification: Identify the main keyword or phrase from the transcript. It's crucial to determine the primary topic that the YouTube video discusses.

        Keyword Integration: Incorporate the identified keyword naturally throughout the article. Use it in headings, subheadings, and within the body text. However, avoid overuse or keyword stuffing, as this can negatively affect SEO.

        Unique Content: Your goal is to make the article 100% unique. Avoid copying sentences directly from the transcript. Rewrite the content in your own words while retaining the original message and meaning.

        SEO Friendliness: Craft the article with SEO best practices in mind. This includes optimizing meta tags (title and meta description), using header tags appropriately, and maintaining an appropriate keyword density.

        Engaging and Informative: Ensure that the article is engaging and informative for the reader. It should provide value and insight on the topic discussed in the YouTube video.

        Proofreading: Proofread the article for grammar, spelling, and punctuation errors. Ensure it is free of any mistakes that could detract from its quality.

        By following these guidelines, create a well-optimized, unique, and informative article that would rank well in search engine results and engage readers effectively.

        Transcript:{transcript}"""

    # Creating a prompt instance and formatting it with the transcript
    prompt = PromptTemplate(input_variables=['transcript'], template=template)
    prompt_query = prompt.format(transcript=transcript)
    
    # Getting the response from the chat model
    response = chat_model.predict(prompt_query)
    
    # Returning the response as a markdown formatted text
    return st.markdown(response)

# Creating a form to get the YouTube URL
with st.form('myform'):
    yt_url = st.text_input('Enter youtube url:', '')
    submitted = st.form_submit_button('Submit')
    
    # Validating the OpenAI API key and the YouTube URL before generating the blog
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter a valid OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-') and yt_url:
        with st.spinner("Generating blog... This may take a while⏳"):
            generate_blog(yt_url, openai_api_key)