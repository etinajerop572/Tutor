import gradio as gr
from dotenv import load_dotenv

from implementation.answer import answer_question

load_dotenv(override=True)


def format_context(context):
    result = "<h2 style='color: #ff7800;'>Relevant Context</h2>\n\n"
    for doc in context:
        result += f"<span style='color: #ff7800;'>Source: {doc.metadata['source']}</span>\n\n"
        result += doc.page_content + "\n\n"
    return result


def chat(history):
    last_message = history[-1]["content"]
    prior = history[:-1]
    answer, context = answer_question(last_message, prior)
    history.append({"role": "assistant", "content": answer})
    return history, format_context(context)


def main():
    def put_message_in_chatbot(message, history):
        return "", history + [{"role": "user", "content": message}]

    theme = gr.themes.Soft(font=["Inter", "system-ui", "sans-serif"])

    with gr.Blocks(title="Tutor inteligente del curso de Introducción a la programación en el lenguaje C", theme=theme) as ui:
        gr.Markdown("# 🏢 Tutor inteligente\nPregúntame lo que quieras acerca del curso de programación en el lenguaje C!")

        with gr.Row():
            with gr.Column(scale=1):
                chatbot = gr.Chatbot(
                    label="💬 Conversación", height=600, type="messages", show_copy_button=True
                )
                message = gr.Textbox(
                    label="Tu pregunta: ",
                    placeholder="Pregúntame lo que quieras acerca del curso de programación en el lenguaje C...",
                    show_label=False,
                )

            with gr.Column(scale=1):
                context_markdown = gr.Markdown(
                    label="📚 Contexto",
                    value="*El contexto aparece aquí*",
                    container=True,
                    height=600,
                )

        message.submit(
            put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]
        ).then(chat, inputs=chatbot, outputs=[chatbot, context_markdown])

    ui.launch(
        #inbrowser=True
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        debug=False
        )


if __name__ == "__main__":
    main()
