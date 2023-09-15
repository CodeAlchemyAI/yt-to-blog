BLOG_TEMPLATE = """Act as an expert copywriter specializing in content optimization for SEO. Your task is to take a given YouTube transcript and transform it into a well-structured and engaging article. Your objectives are as follows:

        Content Transformation: Begin by thoroughly reading the provided YouTube transcript. Understand the main ideas, key points, and the overall message conveyed.

        Sentence Structure: While rephrasing the content, pay careful attention to sentence structure. Ensure that the article flows logically and coherently.

        Keyword Identification: Identify the main keyword or phrase from the transcript. It's crucial to determine the primary topic that the YouTube video discusses.

        Keyword Integration: Incorporate the identified keyword naturally throughout the article. Use it in headings, subheadings, and within the body text. However, avoid overuse or keyword stuffing, as this can negatively affect SEO.

        Unique Content: Your goal is to make the article 100% unique. Avoid copying sentences directly from the transcript. Rewrite the content in your own words while retaining the original message and meaning.

        SEO Friendliness: Craft the article with SEO best practices in mind. This includes optimizing meta tags (title and meta description), using header tags appropriately, and maintaining an appropriate keyword density.

        Engaging and Informative: Ensure that the article is engaging and informative for the reader. It should provide value and insight on the topic discussed in the YouTube video.

        Proofreading: Proofread the article for grammar, spelling, and punctuation errors. Ensure it is free of any mistakes that could detract from its quality.

        By following these guidelines, create a well-optimized, unique, and informative article that would rank well in search engine results and engage readers effectively.

        \n{format_instructions}

        Transcript:{transcript}"""


IMAGE_TEMPLATE= """Write a Stable Diffusion prompts using the below formula with the title: {title}
                \n
                Here’s a formula for a Stable Diffusion image prompt: 
                An image of [adjective] [subject] [doing action], [creative lighting style], detailed, realistic, trending on artstation, 
                in style of [famous artist 1], [famous artist 2], [famous artist 3]
                \n
                Output with no introduction, only the prompt
                PROMPT:
                """